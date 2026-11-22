"""Capture QA Screenshots across required viewports using headless Chrome."""
import os
import subprocess
import time
from pathlib import Path

BASE_DIR = Path(r"c:\Users\nainl\OneDrive\Desktop\taltek-commercial-roofing")
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SCREENSHOT_DIR = BASE_DIR / "screenshots_qa"
SCREENSHOT_DIR.mkdir(exist_ok=True)

VIEWPORTS = [
    ("320px", 320, 640),
    ("375px", 375, 812),
    ("390px", 390, 844),
    ("430px", 430, 932),
    ("768px", 768, 1024),
    ("1024px", 1024, 768),
    ("1440px", 1440, 900),
]

TEST_PAGES = [
    ("index.html", "home"),
    ("estimator.html", "estimator"),
    ("contact.html", "contact"),
    ("projects.html", "projects"),
    ("financing.html", "financing"),
    ("request-inspection.html", "inspection"),
    ("service-areas.html", "service_areas"),
    ("services/tpo-roofing.html", "service_tpo")
]

def make_harness(page_rel_path, width, height):
    # Set cookie consent in iframe on load
    harness_content = f"""<!DOCTYPE html>
<html>
<head>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ background: #07080A; display: flex; justify-content: center; align-items: flex-start; overflow: hidden; }}
    iframe {{
      border: 1px solid #202428;
      width: {width}px;
      height: {height}px;
      background: #111315;
    }}
  </style>
</head>
<body>
  <iframe id="test-frame" src="{page_rel_path}"></iframe>
  <script>
    const iframe = document.getElementById('test-frame');
    iframe.onload = () => {{
      try {{
        iframe.contentWindow.localStorage.setItem('taltek_cookie_consent', JSON.stringify({{
          necessary: true,
          analytics: false,
          marketing: false,
          timestamp: new Date().toISOString()
        }}));
        const banner = iframe.contentDocument.getElementById('cookie-banner');
        if (banner) banner.style.display = 'none';
      }} catch(e) {{}}
    }};
  </script>
</body>
</html>
"""
    harness_path = BASE_DIR / "temp_harness.html"
    harness_path.write_text(harness_content, encoding="utf-8")
    return harness_path

def run_capture():
    print("=" * 60)
    print("STARTING REAL BROWSER SCREENSHOT QA SUITE")
    print("=" * 60)
    
    total = len(VIEWPORTS)
    # We will test index.html across all 7 viewports
    for name, w, h in VIEWPORTS:
        harness_path = make_harness("index.html", w, h)
        out_file = SCREENSHOT_DIR / f"home_{name}.png"
        window_w = max(w + 40, 500)
        window_h = max(h + 40, 600)
        
        url = "file:///" + str(harness_path.resolve()).replace("\\", "/")
        cmd = [
            CHROME_PATH,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--allow-file-access-from-files",
            f"--screenshot={out_file}",
            f"--window-size={window_w},{window_h}",
            url
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if out_file.exists():
            print(f"  [PASSED] Captured index.html at {name} ({w}x{h}) -> {out_file.name} ({out_file.stat().st_size} bytes)")
        else:
            print(f"  [FAILED] Could not capture {name}: {res.stderr}")

    # Also capture other key pages at 375px (mobile standard) and 1440px (desktop standard)
    for rel_path, tag in TEST_PAGES[1:]:
        for name, w, h in [("375px", 375, 812), ("1440px", 1440, 900)]:
            harness_path = make_harness(rel_path, w, h)
            out_file = SCREENSHOT_DIR / f"{tag}_{name}.png"
            window_w = max(w + 40, 500)
            window_h = max(h + 40, 600)
            url = "file:///" + str(harness_path.resolve()).replace("\\", "/")
            cmd = [
                CHROME_PATH,
                "--headless=new",
                "--disable-gpu",
                "--no-sandbox",
                "--allow-file-access-from-files",
                f"--screenshot={out_file}",
                f"--window-size={window_w},{window_h}",
                url
            ]
            subprocess.run(cmd, capture_output=True, text=True)
            if out_file.exists():
                print(f"  [PASSED] Captured {rel_path} at {name} -> {out_file.name}")
            else:
                print(f"  [FAILED] Could not capture {rel_path} at {name}")

    # Clean up temporary harness
    temp = BASE_DIR / "temp_harness.html"
    if temp.exists():
        temp.unlink()
        
    print("\nSCREENSHOT QA SUITE COMPLETED!")

if __name__ == "__main__":
    run_capture()
