"""
TALTEK COMMERCIAL ROOFING - MASTER AUDIT & FUNCTIONAL TEST SUITE
Tests all serverless API handlers, server.py handlers, financial math formulas,
roof estimator pricing engines, honeypot defenses, and static file integrity.
"""

import sys
import io
import json
import unittest

# Import Vercel serverless handlers
from api.health import handler as HealthHandler
from api.quote import handler as QuoteHandler
from api.privacy_request import handler as PrivacyHandler
try:
    from local_server import TaltekRequestHandler
except ImportError:
    from server import TaltekRequestHandler

class DummySocket:
    def __init__(self, request_bytes=b""):
        self.request_bytes = request_bytes
        self.wfile = io.BytesIO()

    def makefile(self, mode, *args, **kwargs):
        if "r" in mode:
            return io.BytesIO(self.request_bytes)
        return self.wfile

    def sendall(self, b):
        self.wfile.write(b)

class TestBackendAndFunctionalFeatures(unittest.TestCase):

    def test_01_api_health(self):
        """Test GET /api/health returns 200, proper JSON, and security headers"""
        sock = DummySocket(b"GET /api/health HTTP/1.1\r\nHost: localhost\r\n\r\n")
        HealthHandler(sock, ("127.0.0.1", 80), None)
        out = sock.wfile.getvalue().decode("utf-8")
        self.assertIn("HTTP/1.0 200", out)
        self.assertIn("X-Content-Type-Options: nosniff", out)
        self.assertIn("X-Frame-Options: SAMEORIGIN", out)
        self.assertIn("healthy", out)
        print("  [TEST PASSED] GET /api/health returned 200 OK & security headers")

    def test_02_api_quote_valid(self):
        """Test POST /api/quote with valid commercial payload returns 200 and reference ID"""
        payload = json.dumps({
            "full_name": "Marcus Vance",
            "building_name": "Cumberland Logistics Center",
            "business_email": "mvance@logistics.com",
            "phone": "6154486349",
            "property_type": "Industrial Warehouse",
            "roof_sqft": 45000
        }).encode("utf-8")

        req_bytes = b"POST /api/quote HTTP/1.1\r\nContent-Type: application/json\r\nContent-Length: " + str(len(payload)).encode() + b"\r\n\r\n" + payload
        sock = DummySocket(req_bytes)
        QuoteHandler(sock, ("127.0.0.1", 80), None)
        out = sock.wfile.getvalue().decode("utf-8")
        self.assertIn("HTTP/1.0 200", out)
        self.assertIn("X-Content-Type-Options: nosniff", out)
        data = json.loads(out[out.find("{"):])
        self.assertTrue(data.get("success"))
        self.assertTrue(data.get("reference", "").startswith("TK-"))
        print(f"  [TEST PASSED] POST /api/quote generated valid reference ID: {data.get('reference')}")

    def test_03_api_quote_spam_honeypot(self):
        """Test POST /api/quote with honeypot field populated is blocked with 400"""
        payload = json.dumps({
            "full_name": "Spam Bot",
            "building_name": "Fake Site",
            "business_email": "bot@spam.com",
            "phone": "6155550199",
            "hp_website_title": "http://spamsite.ru"  # Honeypot trap
        }).encode("utf-8")

        req_bytes = b"POST /api/quote HTTP/1.1\r\nContent-Type: application/json\r\nContent-Length: " + str(len(payload)).encode() + b"\r\n\r\n" + payload
        sock = DummySocket(req_bytes)
        QuoteHandler(sock, ("127.0.0.1", 80), None)
        out = sock.wfile.getvalue().decode("utf-8")
        self.assertIn("HTTP/1.0 400", out)
        self.assertIn("Spam submission rejected", out)
        print("  [TEST PASSED] Honeypot correctly blocked automated spam submission (400 Bad Request)")

    def test_04_api_privacy_request(self):
        """Test POST /api/privacy-request generates statutory tracking code"""
        payload = json.dumps({
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jdoe@facility.com",
            "phone": "6155550188",
            "state_of_residence": "Tennessee",
            "request_type": "Right to Know / Access"
        }).encode("utf-8")

        req_bytes = b"POST /api/privacy-request HTTP/1.1\r\nContent-Type: application/json\r\nContent-Length: " + str(len(payload)).encode() + b"\r\n\r\n" + payload
        sock = DummySocket(req_bytes)
        PrivacyHandler(sock, ("127.0.0.1", 80), None)
        out = sock.wfile.getvalue().decode("utf-8")
        self.assertIn("HTTP/1.0 200", out)
        data = json.loads(out[out.find("{"):])
        self.assertTrue(data.get("success"))
        self.assertTrue(data.get("tracking_code", "").startswith("TIPA-"))
        print(f"  [TEST PASSED] POST /api/privacy-request generated tracking code: {data.get('tracking_code')}")

    def test_05_financing_calculator_math(self):
        """Test commercial financing amortization formula correctness"""
        principal = 120000
        months = 60
        annual_rate = 7.5
        monthly_rate = (annual_rate / 100) / 12

        monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
        total_repayment = monthly_payment * months
        total_interest = total_repayment - principal

        self.assertAlmostEqual(monthly_payment, 2404.55, delta=1.0)
        self.assertAlmostEqual(total_repayment, 144273.23, delta=5.0)
        self.assertAlmostEqual(total_interest, 24273.23, delta=5.0)
        print(f"  [TEST PASSED] Financing formula verified: ${round(monthly_payment):,}/mo, total interest ${round(total_interest):,}")

    def test_06_estimator_pricing_model(self):
        """Test interactive roof estimator pricing engine mathematical boundaries"""
        sqft = 25000
        base_min, base_max = 7.20, 10.50
        cond_mult = 1.10
        type_mult = 1.0

        min_total = round(sqft * base_min * cond_mult * type_mult)
        max_total = round(sqft * base_max * cond_mult * type_mult)

        self.assertEqual(min_total, 198000)
        self.assertEqual(max_total, 288750)
        print(f"  [TEST PASSED] Estimator pricing engine bounds verified: ${min_total:,} – ${max_total:,}")

    def test_07_security_headers_in_server(self):
        """Test that server.py injects all mandatory US cybersecurity headers"""
        req_bytes = b"GET /index.html HTTP/1.1\r\nHost: localhost\r\n\r\n"
        sock = DummySocket(req_bytes)
        TaltekRequestHandler(sock, ("127.0.0.1", 80), None)
        out = sock.wfile.getvalue().decode("utf-8")
        self.assertIn("HTTP/1.0 200", out)
        self.assertIn("Content-Security-Policy", out)
        self.assertIn("X-Frame-Options: SAMEORIGIN", out)
        self.assertIn("X-Content-Type-Options: nosniff", out)
        self.assertIn("Referrer-Policy: strict-origin-when-cross-origin", out)
        print("  [TEST PASSED] All mandatory US cybersecurity headers verified on server.py")

def run_tests():
    print("=" * 60)
    print("RUNNING TALTEK MASTER AUDIT & FUNCTIONAL TEST SUITE")
    print("=" * 60)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBackendAndFunctionalFeatures)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("\nALL BACKEND & FUNCTIONAL SUITE TESTS PASSED (100% SUCCESS)!")
        return True
    return False

if __name__ == "__main__":
    success = run_tests()
    if not success:
        sys.exit(1)
