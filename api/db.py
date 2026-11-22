"""
TALTEK COMMERCIAL ROOFING - PERSISTENCE & LIFECYCLE MANAGEMENT
Provides secure SQLite persistence, rate limiting, and notification dispatch
for commercial inspection leads and consumer privacy rights requests.
"""

import os
import sqlite3
import json
import time
import hashlib
from datetime import datetime

# Path resolution: use data/taltek_records.db locally; fallback to /tmp on serverless environments if read-only
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "taltek_records.db")

def get_db_connection():
    # If data directory is not writable (e.g. read-only serverless root), fallback to /tmp
    target_path = DB_PATH
    try:
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        # Test write permission
        test_file = os.path.join(os.path.dirname(target_path), ".perm_test")
        with open(test_file, "w") as f:
            f.write("ok")
        os.remove(test_file)
    except Exception:
        target_path = "/tmp/taltek_records.db"

    conn = sqlite3.connect(target_path, timeout=10.0)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()

    # 1. Commercial Leads Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS commercial_leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        reference_id TEXT UNIQUE NOT NULL,
        created_at TEXT NOT NULL,
        property_type TEXT,
        building_name TEXT,
        street_address TEXT,
        city TEXT,
        state TEXT,
        zip_code TEXT,
        service_requirement TEXT,
        roof_sqft INTEGER,
        existing_roof_type TEXT,
        estimated_age TEXT,
        current_condition TEXT,
        project_notes TEXT,
        full_name TEXT NOT NULL,
        company_name TEXT NOT NULL,
        business_email TEXT NOT NULL,
        phone TEXT NOT NULL,
        sms_consent INTEGER DEFAULT 0,
        status TEXT DEFAULT 'NEW',
        assigned_estimator TEXT DEFAULT 'UNASSIGNED',
        delivery_status TEXT DEFAULT 'PENDING_CONFIG',
        ip_hash TEXT
    )
    """)

    # 2. Privacy Rights Requests Table (Full Lifecycle)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS privacy_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tracking_code TEXT UNIQUE NOT NULL,
        created_at TEXT NOT NULL,
        state_of_residence TEXT NOT NULL,
        request_type TEXT NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        details TEXT,
        lifecycle_status TEXT DEFAULT 'SUBMITTED',
        verification_status TEXT DEFAULT 'PENDING_VERIFICATION',
        verified_at TEXT,
        completed_at TEXT,
        officer_notes TEXT,
        statutory_deadline TEXT,
        ip_hash TEXT
    )
    """)

    # 3. Rate Limiting Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS rate_limits (
        ip_hash TEXT,
        action TEXT,
        timestamp INTEGER
    )
    """)

    conn.commit()
    conn.close()

# Auto-initialize database on import
init_db()

def hash_ip(ip_address):
    salt = os.environ.get("IP_SALT", "TALTEK_SECURE_SALT_2026")
    return hashlib.sha256((ip_address + salt).encode("utf-8")).hexdigest()[:16]

def is_rate_limited(ip_hash, action="quote", max_per_minute=5):
    conn = get_db_connection()
    cur = conn.cursor()
    cutoff = int(time.time()) - 60

    # Clean old logs
    cur.execute("DELETE FROM rate_limits WHERE timestamp < ?", (cutoff - 3600,))
    
    cur.execute(
        "SELECT COUNT(*) FROM rate_limits WHERE ip_hash = ? AND action = ? AND timestamp > ?",
        (ip_hash, action, cutoff)
    )
    count = cur.fetchone()[0]

    if count >= max_per_minute:
        conn.close()
        return True

    # Record this hit
    cur.execute(
        "INSERT INTO rate_limits (ip_hash, action, timestamp) VALUES (?, ?, ?)",
        (ip_hash, action, int(time.time()))
    )
    conn.commit()
    conn.close()
    return False

def save_commercial_lead(data, ip_hash="unknown"):
    conn = get_db_connection()
    cur = conn.cursor()
    now_iso = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    # Generate reference ID
    import random
    ref_id = f"TK-{random.randint(100000, 999999)}"

    # Check notification dispatch configuration
    delivery_status = "PENDING_SMTP_CONFIG"
    smtp_host = os.environ.get("SMTP_HOST")
    webhook_url = os.environ.get("TALTEK_WEBHOOK_URL")

    if smtp_host or webhook_url:
        delivery_status = "DELIVERY_QUEUED"

    cur.execute("""
    INSERT INTO commercial_leads (
        reference_id, created_at, property_type, building_name,
        street_address, city, state, zip_code, service_requirement,
        roof_sqft, existing_roof_type, estimated_age, current_condition,
        project_notes, full_name, company_name, business_email, phone,
        sms_consent, status, delivery_status, ip_hash
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        ref_id, now_iso, data.get("property_type", ""),
        data.get("building_name", ""), data.get("street_address", ""),
        data.get("city", ""), data.get("state", ""), data.get("zip_code", ""),
        data.get("service_requirement", "Commercial Inspection"),
        int(data.get("roof_sqft") or 0), data.get("existing_roof_type", ""),
        data.get("estimated_age", ""), data.get("current_condition", ""),
        data.get("project_notes", ""), data.get("full_name", ""),
        data.get("company_name", ""), data.get("business_email", ""),
        data.get("phone", ""), 1 if data.get("sms_consent") == "yes" else 0,
        "NEW", delivery_status, ip_hash
    ))

    conn.commit()
    conn.close()

    # Attempt dispatch if configured
    if smtp_host or webhook_url:
        try_dispatch_lead(ref_id, data)

    return ref_id, delivery_status

def save_privacy_request(data, ip_hash="unknown"):
    conn = get_db_connection()
    cur = conn.cursor()
    now_iso = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    # Statutory deadline: 45 days per TIPA and CCPA
    deadline_ts = int(time.time()) + (45 * 86400)
    deadline_iso = datetime.fromtimestamp(deadline_ts).strftime("%Y-%m-%d")

    import random
    state = data.get("state_of_residence", "Tennessee")
    prefix = "TIPA" if "Tennessee" in state else ("CCPA" if "California" in state else "PRIV")
    date_code = datetime.now().strftime("%Y%m%d")
    tracking_code = f"{prefix}-{date_code}-{random.randint(1000, 9999)}"

    cur.execute("""
    INSERT INTO privacy_requests (
        tracking_code, created_at, state_of_residence, request_type,
        first_name, last_name, email, phone, details,
        lifecycle_status, verification_status, statutory_deadline, ip_hash
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        tracking_code, now_iso, state, data.get("request_type", ""),
        data.get("first_name", ""), data.get("last_name", ""),
        data.get("email", ""), data.get("phone", ""), data.get("details", ""),
        "SUBMITTED", "PENDING_IDENTITY_MATCH", deadline_iso, ip_hash
    ))

    conn.commit()
    conn.close()

    return tracking_code, deadline_iso

def try_dispatch_lead(ref_id, data):
    """
    Safely dispatches lead notification to TALTEK recipients if environment credentials exist.
    Never crashes or discards data if unconfigured.
    """
    webhook_url = os.environ.get("TALTEK_WEBHOOK_URL")
    if webhook_url:
        try:
            import urllib.request
            payload = json.dumps({
                "text": f"New TALTEK Commercial Lead: {data.get('full_name')} ({data.get('company_name')}) - Ref: {ref_id}",
                "lead": data
            }).encode("utf-8")
            req = urllib.request.Request(webhook_url, data=payload, headers={"Content-Type": "application/json"})
            urllib.request.urlopen(req, timeout=5)
            # Update delivery status
            conn = get_db_connection()
            conn.execute("UPDATE commercial_leads SET delivery_status = 'DELIVERED_WEBHOOK' WHERE reference_id = ?", (ref_id,))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Webhook dispatch failed: {e}")
