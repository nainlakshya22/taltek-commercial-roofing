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
                    print("\\nServer stopped cleanly.")
                return
        except OSError as e:
            if p == ports_to_try[-1]:
                print(f"Failed to bind server to any candidate port: {e}")
                sys.exit(1)
            continue

if __name__ == "__main__":
    run()
'''

with open("server.py", "w", encoding="utf-8") as f:
    f.write(server_py)
print("Generated: server.py")
