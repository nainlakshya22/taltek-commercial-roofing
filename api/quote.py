"""
Vercel Serverless Function: POST /api/quote
Handles commercial inspection & quote requests with validation, honeypot spam protection,
rate limiting, secure SQLite persistence, and security headers.
"""
from http.server import BaseHTTPRequestHandler
import json
import re
import os
import sys

# Ensure root is on path for api.db import
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from api.db import save_commercial_lead, is_rate_limited, hash_ip
except ImportError:
    from db import save_commercial_lead, is_rate_limited, hash_ip

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. Rate Limiting Check
        client_ip = self.headers.get("x-forwarded-for", self.client_address[0] if self.client_address else "127.0.0.1").split(",")[0].strip()
        ip_hash = hash_ip(client_ip)

        if is_rate_limited(ip_hash, action="quote", max_per_minute=5):
            self.send_response(429)
            self.send_header("Content-Type", "application/json")
            self.send_header("Retry-After", "60")
            self.end_headers()
            self.wfile.write(json.dumps({
                "success": False,
                "error": "Rate limit exceeded. Too many requests. Please wait one minute or call (615) 448-6349 directly."
            }).encode("utf-8"))
            return

        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data.decode("utf-8")) if post_data else {}
        except Exception:
            data = {}

        # 2. Anti-Spam Honeypot Verification
        if data.get("hp_website_title"):
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "success": False,
                "error": "Spam submission rejected by security filter."
            }).encode("utf-8"))
            return

        # 3. Server-Side Validation
        email = data.get("business_email", "").strip()
        phone = data.get("phone", "").strip()
        name = data.get("full_name", "").strip()
        building = data.get("building_name", "").strip()

        errors = []
        if not name:
            errors.append("Contact name is required.")
        if not building:
            errors.append("Building / Facility name is required.")
        if not email or not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            errors.append("A valid business email address is required.")
        if not phone or len(re.sub(r"\D", "", phone)) < 10:
            errors.append("A valid 10-digit telephone number is required.")

        if errors:
            self.send_response(422)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "success": False,
                "errors": errors
            }).encode("utf-8"))
            return

        # 4. Secure Persistence to Database
        ref_id, delivery_status = save_commercial_lead(data, ip_hash=ip_hash)

        response_payload = {
            "success": True,
            "reference": ref_id,
            "delivery_status": delivery_status,
            "message": "Commercial inspection request logged successfully into TALTEK dispatch records. A commercial estimator will review facility details and contact your office within 2 to 4 business hours.",
            "dispatched_to": "Goodlettsville Headquarters Dispatch",
            "support_hotline": "+1 (615) 448-6349"
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.end_headers()
        self.wfile.write(json.dumps(response_payload).encode("utf-8"))

    def do_GET(self):
        self.send_response(405)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"error": "Method not allowed. Use POST."}).encode("utf-8"))
