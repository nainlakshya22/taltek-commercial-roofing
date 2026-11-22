"""
TALTEK COMMERCIAL ROOFING - ADMINISTRATIVE RECORD & LIFECYCLE CLI
Used by authorized compliance and dispatch officers to view, export, and
update commercial leads and consumer privacy requests.
"""

import sys
import os
import argparse
from datetime import datetime

# Add root directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from api.db import get_db_connection

def list_leads():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT reference_id, created_at, full_name, company_name, phone, business_email, status, delivery_status FROM commercial_leads ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()

    print("\n" + "=" * 90)
    print(f"TALTEK COMMERCIAL LEADS REGISTER ({len(rows)} TOTAL)")
    print("=" * 90)
    if not rows:
        print("No leads recorded yet.")
        return

    print(f"{'REFERENCE':<12} {'CREATED':<20} {'NAME':<20} {'COMPANY':<22} {'STATUS':<12}")
    print("-" * 90)
    for r in rows:
        print(f"{r['reference_id']:<12} {r['created_at']:<20} {r['full_name'][:18]:<20} {r['company_name'][:20]:<22} {r['status']:<12}")
    print("=" * 90)

def view_lead(ref_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM commercial_leads WHERE reference_id = ?", (ref_id,))
    row = cur.fetchone()
    conn.close()

    if not row:
        print(f"Error: Lead reference {ref_id} not found.")
        return

    print("\n" + "=" * 60)
    print(f"COMMERCIAL LEAD DETAIL: {row['reference_id']}")
    print("=" * 60)
    for k in row.keys():
        print(f"{k.replace('_', ' ').title():<22}: {row[k]}")
    print("=" * 60)

def list_privacy():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT tracking_code, created_at, state_of_residence, request_type, first_name, last_name, email, lifecycle_status, statutory_deadline FROM privacy_requests ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()

    print("\n" + "=" * 100)
    print(f"TALTEK CONSUMER PRIVACY RIGHTS REGISTER ({len(rows)} TOTAL)")
    print("=" * 100)
    if not rows:
        print("No privacy requests recorded.")
        return

    print(f"{'TRACKING CODE':<22} {'STATE':<14} {'REQUEST TYPE':<26} {'STATUS':<16} {'DEADLINE':<12}")
    print("-" * 100)
    for r in rows:
        print(f"{r['tracking_code']:<22} {r['state_of_residence'][:12]:<14} {r['request_type'][:24]:<26} {r['lifecycle_status']:<16} {r['statutory_deadline']:<12}")
    print("=" * 100)

def view_privacy(code):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM privacy_requests WHERE tracking_code = ?", (code,))
    row = cur.fetchone()
    conn.close()

    if not row:
        print(f"Error: Privacy tracking code {code} not found.")
        return

    print("\n" + "=" * 60)
    print(f"PRIVACY REQUEST RECORD: {row['tracking_code']}")
    print("=" * 60)
    for k in row.keys():
        print(f"{k.replace('_', ' ').title():<22}: {row[k]}")
    print("=" * 60)

def update_privacy(code, status, notes=""):
    conn = get_db_connection()
    now_iso = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    completed_at = now_iso if status in ["COMPLETED", "REJECTED"] else None

    conn.execute("""
    UPDATE privacy_requests
    SET lifecycle_status = ?, officer_notes = ?, completed_at = COALESCE(?, completed_at)
    WHERE tracking_code = ?
    """, (status, notes, completed_at, code))
    
    if conn.total_changes == 0:
        print(f"Error: Request {code} not found.")
    else:
        conn.commit()
        print(f"Successfully updated privacy request {code} to '{status}'.")
    conn.close()

def main():
    parser = argparse.ArgumentParser(description="TALTEK Records Management CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Leads
    subparsers.add_parser("list-leads")
    view_lead_p = subparsers.add_parser("view-lead")
    view_lead_p.add_argument("ref_id", help="Lead Reference ID (e.g. TK-123456)")

    # Privacy
    subparsers.add_parser("list-privacy")
    view_priv_p = subparsers.add_parser("view-privacy")
    view_priv_p.add_argument("tracking_code", help="Privacy Tracking Code (e.g. TIPA-20261122-1234)")
    
    update_priv_p = subparsers.add_parser("update-privacy")
    update_priv_p.add_argument("tracking_code", help="Privacy Tracking Code")
    update_priv_p.add_argument("--status", required=True, choices=["SUBMITTED", "IDENTITY_VERIFIED", "IN_REVIEW", "COMPLETED", "REJECTED", "APPEALED"])
    update_priv_p.add_argument("--notes", default="", help="Compliance officer review notes")

    args = parser.parse_args()

    if args.command == "list-leads":
        list_leads()
    elif args.command == "view-lead":
        view_lead(args.ref_id)
    elif args.command == "list-privacy":
        list_privacy()
    elif args.command == "view-privacy":
        view_privacy(args.tracking_code)
    elif args.command == "update-privacy":
        update_privacy(args.tracking_code, args.status, args.notes)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
