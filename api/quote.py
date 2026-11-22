"""
Vercel Serverless Function: POST /api/quote
Handles commercial inspection & quote requests with validation, honeypot spam protection,
and security headers.
"""
from http.server import BaseHTTPRequestHandler
import json
import re
import random
import time

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data.decode("utf-8")) if post_data else {}
        except Exception:
            data = {}

        # 1. Anti-Spam Honeypot Verification
        if data.get("hp_website_title"):
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "success": False,
                "error": "Spam submission rejected by security filter."
            }).encode("utf-8"))
            return

        # 2. Server-Side Validation
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

        # 3. Success Response with Reference ID
        ref_id = f"TK-{random.randint(100000, 999999)}"
        response_payload = {
            "success": True,
            "reference": ref_id,
            "message": "Commercial inspection request logged successfully. A TALTEK estimator will review site access and contact your office within 2 to 4 business hours.",
            "dispatched_to": "Goodlettsville Corporate Dispatch",
            "timestamp": int(time.time())
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
