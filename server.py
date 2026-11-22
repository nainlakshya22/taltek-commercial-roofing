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

PORT = int(os.environ.get("PORT", 8000))

class TaltekRequestHandler(http.server.SimpleHTTPRequestHandler):
    extensions_map = http.server.SimpleHTTPRequestHandler.extensions_map.copy()
    extensions_map.update({
        ".webp": "image/webp",
        ".avif": "image/avif",
        ".svg": "image/svg+xml",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".css": "text/css; charset=utf-8",
        ".js": "application/javascript; charset=utf-8",
        ".json": "application/json; charset=utf-8",
        ".html": "text/html; charset=utf-8",
    })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # US Cybersecurity & Privacy Headers
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("X-XSS-Protection", "1; mode=block")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
        self.send_header("Content-Security-Policy", "default-src 'self' 'unsafe-inline' data: https:; img-src 'self' data: https:; font-src 'self' https: data:; script-src 'self' 'unsafe-inline' https:; connect-src 'self' https:; frame-src 'self' https://maps.google.com https://www.google.com;")
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
    ports_to_try = [PORT]
    for alt in [8000, 8080, 8081]:
        if alt not in ports_to_try:
            ports_to_try.append(alt)

    for p in ports_to_try:
        try:
            with socketserver.TCPServer(("", p), TaltekRequestHandler) as httpd:
                print(f"TALTEK Commercial Roofing local server running on http://localhost:{p}")
                sys.stdout.flush()
                try:
                    httpd.serve_forever()
                except KeyboardInterrupt:
                    print("\nServer stopped cleanly.")
                return
        except OSError as e:
            if p == ports_to_try[-1]:
                print(f"Failed to bind server to any candidate port: {e}")
                sys.exit(1)
            continue

if __name__ == "__main__":
    run()
