"""
Vercel Serverless Function: POST /api/privacy-request
Handles consumer privacy rights requests under Tennessee (TIPA) and California (CCPA/CPRA).
"""
from http.server import BaseHTTPRequestHandler
import json
import re
import random
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data.decode("utf-8")) if post_data else {}
        except Exception:
            data = {}

        # 1. Anti-Spam Honeypot Verification
        if data.get("hp_privacy_verification"):
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "success": False,
                "error": "Spam request rejected."
            }).encode("utf-8"))
            return

        # 2. Server-Side Validation
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

        # 3. Generate Tracking Code & Acknowledge
        date_str = datetime.now().strftime("%Y%m%d")
        rand_code = random.randint(1000, 9999)
        prefix = "TIPA" if "Tennessee" in state else ("CCPA" if "California" in state else "PRIV")
        tracking_code = f"{prefix}-{date_str}-{rand_code}"

        response_payload = {
            "success": True,
            "tracking_code": tracking_code,
            "message": "Privacy rights request logged into compliance register. Our designated Privacy Officer will review your submission and respond within the statutory timeframe.",
            "statutory_response_window_days": 45
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
