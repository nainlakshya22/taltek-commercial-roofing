"""
Test TALTEK Commercial Roofing local server, pages, and API endpoints
"""

import http.client
import subprocess
import time
import json
import sys

def test_site():
    # Start server in background
    proc = subprocess.Popen([sys.executable, "server.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(1.5)

    try:
        conn = http.client.HTTPConnection("127.0.0.1", 8080, timeout=5)
        
        # Test 1: GET /index.html
        conn.request("GET", "/index.html")
        res = conn.getresponse()
        print(f"GET /index.html: Status {res.status}")
        headers = dict(res.getheaders())
        assert res.status == 200, f"Expected 200, got {res.status}"
        assert "Content-Security-Policy" in headers, "Missing CSP header"
        assert "X-Frame-Options" in headers, "Missing X-Frame-Options header"
        assert "X-Content-Type-Options" in headers, "Missing X-Content-Type-Options header"
        body = res.read().decode("utf-8")
        assert "TALTEK Commercial Roofing" in body, "Missing brand in body"
        print("  -> Headers and content verified!")

        # Test 2: GET /services/tpo-roofing.html
        conn.request("GET", "/services/tpo-roofing.html")
        res = conn.getresponse()
        print(f"GET /services/tpo-roofing.html: Status {res.status}")
        assert res.status == 200
        res.read()

        # Test 3: GET /projects/nashville-general-hospital.html
        conn.request("GET", "/projects/nashville-general-hospital.html")
        res = conn.getresponse()
        print(f"GET /projects/nashville-general-hospital.html: Status {res.status}")
        assert res.status == 200
        res.read()

        # Test 4: GET /privacy-policy.html
        conn.request("GET", "/privacy-policy.html")
        res = conn.getresponse()
        print(f"GET /privacy-policy.html: Status {res.status}")
        assert res.status == 200
        res.read()

        # Test 5: GET /sitemap.xml
        conn.request("GET", "/sitemap.xml")
        res = conn.getresponse()
        print(f"GET /sitemap.xml: Status {res.status}")
        assert res.status == 200
        res.read()

        # Test 6: GET /robots.txt
        conn.request("GET", "/robots.txt")
        res = conn.getresponse()
        print(f"GET /robots.txt: Status {res.status}")
        assert res.status == 200
        res.read()

        # Test 7: GET /api/health
        conn.request("GET", "/api/health")
        res = conn.getresponse()
        print(f"GET /api/health: Status {res.status}")
        data = json.loads(res.read().decode("utf-8"))
        assert data.get("status") == "healthy"
        print(f"  -> API Health: {data}")

        # Test 8: POST /api/quote
        quote_payload = json.dumps({
            "building_name": "Test Distribution Center",
            "property_type": "Industrial Warehouse",
            "city": "Goodlettsville",
            "state": "Tennessee",
            "roof_sqft": 45000,
            "full_name": "Test Representative",
            "business_email": "rep@testwarehouse.com",
            "phone": "6155550199"
        })
        conn.request("POST", "/api/quote", body=quote_payload, headers={"Content-Type": "application/json"})
        res = conn.getresponse()
        print(f"POST /api/quote: Status {res.status}")
        q_data = json.loads(res.read().decode("utf-8"))
        assert q_data.get("success") is True
        print(f"  -> Quote reference generated: {q_data.get('reference')}")

        # Test 9: POST /api/privacy-request
        priv_payload = json.dumps({
            "state_of_residence": "Tennessee",
            "request_type": "Right to Know / Access",
            "first_name": "John",
            "last_name": "Doe",
            "email": "jdoe@example.com",
            "phone": "6155550188"
        })
        conn.request("POST", "/api/privacy-request", body=priv_payload, headers={"Content-Type": "application/json"})
        res = conn.getresponse()
        print(f"POST /api/privacy-request: Status {res.status}")
        p_data = json.loads(res.read().decode("utf-8"))
        assert p_data.get("success") is True
        print(f"  -> Privacy tracking code generated: {p_data.get('tracking_code')}")

        conn.close()
        print("\\nALL 9 AUTOMATED SUITE TESTS PASSED PERFECTLY!")

    finally:
        proc.terminate()
        proc.wait()

if __name__ == "__main__":
    test_site()
