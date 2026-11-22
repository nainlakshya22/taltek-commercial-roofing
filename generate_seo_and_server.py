"""
TALTEK COMMERCIAL ROOFING - SEO METADATA & PYTHON DEVELOPMENT SERVER
Generates:
1. robots.txt
2. sitemap.xml
3. server.py (Production-ready local HTTP & REST API server with security headers)
"""

import os
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")

# 1. robots.txt
robots_txt = f"""# TALTEK Commercial Roofing - Robots Exclusion Protocol
# https://taltekroofing.com/

User-agent: *
Allow: /
Disallow: /api/
Disallow: /scratch/
Disallow: /brain/

# Sitemap Location
Sitemap: https://taltekroofing.com/sitemap.xml
"""

with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_txt)
print("Generated: robots.txt")

# 2. sitemap.xml
all_pages = [
    ("index.html", "1.0", "weekly"),
    ("about.html", "0.8", "monthly"),
    ("services.html", "0.9", "weekly"),
    ("services/commercial-roofing.html", "0.9", "monthly"),
    ("services/industrial-roofing.html", "0.9", "monthly"),
    ("services/roof-replacement.html", "0.9", "monthly"),
    ("services/roof-repair.html", "0.9", "monthly"),
    ("services/emergency-services.html", "0.9", "monthly"),
    ("services/preventative-maintenance.html", "0.8", "monthly"),
    ("services/tpo-roofing.html", "0.9", "monthly"),
    ("services/epdm-roofing.html", "0.8", "monthly"),
    ("services/pvc-roofing.html", "0.8", "monthly"),
    ("services/storm-protection.html", "0.8", "monthly"),
    ("services/roof-assessment.html", "0.8", "monthly"),
    ("services/gutter-services.html", "0.8", "monthly"),
    ("projects.html", "0.9", "weekly"),
    ("projects/nashville-general-hospital.html", "0.8", "monthly"),
    ("projects/frost-bank-plaza.html", "0.8", "monthly"),
    ("projects/krusteaz-facility.html", "0.8", "monthly"),
    ("projects/rapha-center.html", "0.8", "monthly"),
    ("projects/malone-plaza.html", "0.8", "monthly"),
    ("team.html", "0.7", "monthly"),
    ("service-areas.html", "0.9", "monthly"),
    ("estimator.html", "0.9", "weekly"),
    ("request-inspection.html", "1.0", "weekly"),
    ("financing.html", "0.8", "monthly"),
    ("faq.html", "0.7", "monthly"),
    ("careers.html", "0.7", "monthly"),
    ("contact.html", "0.9", "monthly"),
    ("privacy-policy.html", "0.5", "monthly"),
    ("cookie-policy.html", "0.5", "monthly"),
    ("terms.html", "0.5", "monthly"),
    ("accessibility.html", "0.6", "monthly"),
    ("california-privacy-rights.html", "0.5", "monthly"),
    ("privacy-request.html", "0.6", "monthly"),
    ("sms-terms.html", "0.5", "monthly")
]

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

for url, priority, freq in all_pages:
    sitemap_xml += f"""  <url>
    <loc>https://taltekroofing.com/{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{priority}</priority>
  </url>
"""

sitemap_xml += "</urlset>\n"

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
print("Generated: sitemap.xml")

# 3. server.py
server_py = '''"""
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
            print("\\nServer stopped cleanly.")

if __name__ == "__main__":
    run()
'''

with open("server.py", "w", encoding="utf-8") as f:
    f.write(server_py)
print("Generated: server.py")
