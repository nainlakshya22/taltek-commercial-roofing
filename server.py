"""
TALTEK COMMERCIAL ROOFING - DEVELOPMENT & API SERVER
Lightweight, pure-Python server with security headers and mock REST API handlers.
"""

import http.server
import socketserver
import json
import os
import sys
import random
from urllib.parse import urlparse, parse_qs

PORT = int(os.environ.get("PORT", 8080))
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class TaltekRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # US Cybersecurity & Privacy Headers
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("X-XSS-Protection", "1; mode=block")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        self.send_header("Content-Security-Policy", "default-src 'self' 'unsafe-inline' data: https:; img-src 'self' data: https:; font-src 'self' https: data:;")
        super().end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "healthy", "service": "TALTEK Commercial Roofing API"}).encode("utf-8"))
            return
        
        # Route directory root to index.html if needed
        super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        try:
            payload = json.loads(body.decode("utf-8")) if body else {}
        except Exception:
            payload = {}

        # 1. Commercial Quote / Inspection Submission
        if parsed.path == "/api/quote":
            # Check honeypot
            if payload.get("hp_website_title"):
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Spam detected."}).encode("utf-8"))
                return

            ref_id = f"TK-{random.randint(100000, 999999)}"
            response_data = {
                "success": True,
                "reference": ref_id,
                "message": "Commercial inspection request transmitted to Goodlettsville dispatch.",
                "timestamp": payload.get("timestamp") or "now"
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode("utf-8"))
            return

        # 2. Consumer Privacy Rights Request
        elif parsed.path == "/api/privacy-request":
            if payload.get("hp_privacy_verification"):
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Spam detected."}).encode("utf-8"))
                return

            tracking_code = f"TIPA-{random.randint(1000, 9999)}"
            response_data = {
                "success": True,
                "tracking_code": tracking_code,
                "message": "Privacy rights request recorded into compliance register."
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode("utf-8"))
            return

        # Fallback for unrecognized endpoints
        self.send_response(404)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode("utf-8"))

def run():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), TaltekRequestHandler) as httpd:
        print(f"TALTEK Commercial Roofing server running on http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped cleanly.")

if __name__ == "__main__":
    run()
