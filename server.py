"""
TALTEK COMMERCIAL ROOFING - DEVELOPMENT & LOCAL API SERVER
Serves static pages with US cybersecurity headers and routes REST API endpoints
through the production database and validation handlers.
"""

import http.server
import socketserver
import json
import os
import sys

DIRECTORY = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, DIRECTORY)

from api.quote import handler as QuoteHandler
from api.privacy_request import handler as PrivacyHandler
from api.health import handler as HealthHandler

PORT = int(os.environ.get("PORT", 8080))

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
        self.send_header("Content-Security-Policy", "default-src 'self' 'unsafe-inline' data: https:; img-src 'self' data: https:; font-src 'self' https: data:; script-src 'self' 'unsafe-inline' https:; connect-src 'self' https:;")
        super().end_headers()

    def do_GET(self):
        if self.path == "/api/health":
            HealthHandler.do_GET(self)
            return
        super().do_GET()

    def do_POST(self):
        if self.path == "/api/quote":
            QuoteHandler.do_POST(self)
            return
        elif self.path in ["/api/privacy-request", "/api/privacy_request"]:
            PrivacyHandler.do_POST(self)
            return

        self.send_response(404)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode("utf-8"))

def run():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), TaltekRequestHandler) as httpd:
        print(f"TALTEK Commercial Roofing local server running on http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped cleanly.")

if __name__ == "__main__":
    run()
