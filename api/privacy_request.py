"""
Vercel Serverless Function: POST /api/privacy-request
Handles consumer privacy rights requests under Tennessee (TIPA) and California (CCPA/CPRA)
with validation, rate limiting, and full lifecycle persistence.
"""
from http.server import BaseHTTPRequestHandler
import json
import re
import os
import sys

# Ensure root is on path for api.db import
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from api.db import save_privacy_request, is_rate_limited, hash_ip
except ImportError:
    from db import save_privacy_request, is_rate_limited, hash_ip

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. Rate Limiting Check
        client_ip = self.headers.get("x-forwarded-for", self.client_address[0] if self.client_address else "127.0.0.1").split(",")[0].strip()
        ip_hash = hash_ip(client_ip)

        if is_rate_limited(ip_hash, action="privacy", max_per_minute=3):
            self.send_response(429)
            self.send_header("Content-Type", "application/json")
            self.send_header("Retry-After", "60")
            self.end_headers()
            self.wfile.write(json.dumps({
                "success": False,
                "error": "Rate limit exceeded. Please wait one minute before submitting another request."
            }).encode("utf-8"))
            return

        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data.decode("utf-8")) if post_data else {}
        except Exception:
            data = {}

        # 2. Anti-Spam Honeypot Verification
        if data.get("hp_privacy_verification"):
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "success": False,
                "error": "Spam request rejected."
            }).encode("utf-8"))
            return

        # 3. Server-Side Validation
        email = data.get("email", "").strip()
        first_name = data.get("first_name", "").strip()
        last_name = data.get("last_name", "").strip()
        req_type = data.get("request_type", "").strip()
        state = data.get("state_of_residence", "").strip()

        errors = []
        if not first_name or not last_name:
            errors.append("First and last names are required for identity verification.")
        if not email or not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            errors.append("A valid email address is required to transmit confirmation.")
        if not req_type:
            errors.append("Request type must be specified.")
        if not state:
            errors.append("State of residence is required to determine applicable privacy framework.")

        if errors:
            self.send_response(422)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "success": False,
                "errors": errors
            }).encode("utf-8"))
            return

        # 4. Save to Persistent Store
        tracking_code, deadline_iso = save_privacy_request(data, ip_hash=ip_hash)

        response_payload = {
            "success": True,
            "tracking_code": tracking_code,
            "lifecycle_status": "SUBMITTED",
            "statutory_deadline": deadline_iso,
            "statutory_window_days": 45,
            "message": "Privacy rights request logged into TALTEK compliance register. Our designated Privacy Officer will review your submission and respond within the statutory timeframe."
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
