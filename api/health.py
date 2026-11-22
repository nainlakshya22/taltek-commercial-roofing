"""
Vercel Serverless Function: GET /api/health
"""
from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.end_headers()
        
        response = {
            "status": "healthy",
            "service": "TALTEK Commercial Roofing API",
            "runtime": "Vercel Serverless Python",
            "headquarters": "Goodlettsville, TN 37072",
            "phone": "+1-615-448-6349"
        }
        self.wfile.write(json.dumps(response).encode("utf-8"))
