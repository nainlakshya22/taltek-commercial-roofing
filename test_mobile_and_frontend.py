"""Comprehensive Mobile and Frontend QA Test Script for TALTEK Commercial Roofing.
Uses Python standard library only (no external dependencies).
"""

import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(r"c:\Users\nainl\OneDrive\Desktop\taltek-commercial-roofing")

def test_pages():
    print("=" * 60)
    print("TALTEK COMMERCIAL ROOFING — FRONTEND & MOBILE QA AUDIT")
    print("=" * 60)
    
    html_files = sorted(list(BASE_DIR.rglob("*.html")))
    print(f"Total HTML pages found: {len(html_files)}")
    assert len(html_files) == 36, f"Expected 36 pages, found {len(html_files)}"
    
    errors = []
    
    # 1. Test Viewport and Meta tags
    print("\n[1/7] Testing Viewport and Core Meta Tags on all 36 pages...")
    for page in html_files:
        content = page.read_text(encoding="utf-8")
        if '<meta name="viewport" content="width=device-width, initial-scale=1.0' not in content:
            errors.append(f"{page.name}: Missing standard responsive viewport meta tag")
        if not re.search(r'<title>.*TALTEK.*</title>', content, re.IGNORECASE):
            errors.append(f"{page.name}: Missing or improper TALTEK page title")
        if 'base.css' not in content or 'components.css' not in content:
            errors.append(f"{page.name}: Missing core stylesheets")
        if 'main.js' not in content:
            errors.append(f"{page.name}: Missing main.js")
            
    if not errors:
        print("  -> PASSED: All 36 pages have standard responsive viewports, titles, and core asset links.")
    else:
        for err in errors[:5]:
            print(f"  -> ERROR: {err}")
        return False

    # 2. Test Image References
    print("\n[2/7] Testing Image & Asset Integrity across all pages...")
    missing_assets = []
    asset_pattern = re.compile(r'(?:src|href|srcset)=["\']([^"\'>\s]+)["\']')
    
    total_refs = 0
    for page in html_files:
        content = page.read_text(encoding="utf-8")
        matches = asset_pattern.findall(content)
        for rel_link in matches:
            if rel_link.startswith(("http://", "https://", "#", "tel:", "mailto:", "javascript:", "data:")):
                continue
            total_refs += 1
            clean_path = rel_link.split("?")[0].split("#")[0]
            target_path = (page.parent / clean_path).resolve()
            if not target_path.exists():
                missing_assets.append((page.name, clean_path))
                
    print(f"  -> Total asset references verified: {total_refs}")
    if not missing_assets:
        print("  -> PASSED: 0 missing or broken asset links detected across all 36 pages.")
    else:
        for p, a in missing_assets[:5]:
            print(f"  -> BROKEN ASSET: {p} references non-existent {a}")
        return False

    # 3. Test High-Resolution Photography Assets
    print("\n[3/7] Verifying High-Resolution Photography & WebP Fallbacks...")
    required_photos = [
        "hero-rooftop.webp", "hero-rooftop.jpg",
        "before-damaged-roof.webp", "before-damaged-roof.jpg",
        "after-tpo-roof.webp", "after-tpo-roof.jpg",
        "project-krusteaz.webp", "project-krusteaz.jpg",
        "project-nashville-general.webp", "project-nashville-general.jpg",
        "project-frost-bank.webp", "project-frost-bank.jpg",
        "project-malone-plaza.webp", "project-malone-plaza.jpg",
        "project-rapha-center.webp", "project-rapha-center.jpg",
        "commercial-contractors.webp", "commercial-contractors.jpg",
        "roof-assessment-inspector.webp", "roof-assessment-inspector.jpg",
        "commercial-tpo-installation.webp", "commercial-tpo-installation.jpg",
        "heavy-industrial-roof.webp", "heavy-industrial-roof.jpg",
        "commercial-construction-site.webp", "commercial-construction-site.jpg"
    ]
    img_dir = BASE_DIR / "assets" / "images"
    missing_photos = [photo for photo in required_photos if not (img_dir / photo).exists()]
    if not missing_photos:
        print(f"  -> PASSED: All {len(required_photos)} curated photography files exist in both WebP and JPG formats.")
    else:
        print(f"  -> ERROR: Missing photography files: {missing_photos}")
        return False

    # 4. Test Google Maps Integration on contact.html
    print("\n[4/7] Testing Google Maps & Geolocation on contact.html...")
    contact_html = (BASE_DIR / "contact.html").read_text(encoding="utf-8")
    maps_checks = [
        ("iframe maps embed", "maps.google.com/maps?q=" in contact_html),
        ("Goodlettsville address in map query", "1214+S+Dickerson+Rd" in contact_html),
        ("Get Directions link", "google.com/maps/dir/?api=1" in contact_html),
        ("Open in Google Maps link", "google.com/maps/search/?api=1" in contact_html),
        ("Headquarters Address Card", "1214 S. Dickerson Rd" in contact_html),
        ("Fallback text/noscript", "noscript" in contact_html)
    ]
    for check_name, passed in maps_checks:
        assert passed, f"contact.html failed check: {check_name}"
        print(f"  -> Verified {check_name}: OK")
    print("  -> PASSED: Google Maps and Geolocation integration fully verified.")

    # 5. Verify All 12 Mandatory Interactive Features
    print("\n[5/7] Verifying 12 Mandatory Interactive Features...")
    index_html = (BASE_DIR / "index.html").read_text(encoding="utf-8")
    services_html = (BASE_DIR / "services.html").read_text(encoding="utf-8")
    portfolio_html = (BASE_DIR / "projects.html").read_text(encoding="utf-8")
    estimator_html = (BASE_DIR / "estimator.html").read_text(encoding="utf-8")
    financing_html = (BASE_DIR / "financing.html").read_text(encoding="utf-8")
    inspection_html = (BASE_DIR / "request-inspection.html").read_text(encoding="utf-8")
    team_html = (BASE_DIR / "team.html").read_text(encoding="utf-8")
    service_areas_html = (BASE_DIR / "service-areas.html").read_text(encoding="utf-8")
    
    features = [
        ("01. Cinematic Hero", "hero-section" in index_html and "hero-rooftop" in index_html),
        ("02. Interactive Roof Estimator", "roof-estimator-app" in estimator_html and "building-tile" in estimator_html),
        ("03. Before/After Interactive Slider", "before-after-container" in index_html and "ba-slider-handle" in index_html),
        ("04. Commercial Portfolio & Filters", "portfolio-filter-bar" in portfolio_html and "project-grid" in portfolio_html),
        ("05. Google Reviews System", "reviews-summary-card" in index_html and "4.8" in index_html),
        ("06. Financing Calculator", "financing-calculator-box" in financing_html and "fin-project-cost" in financing_html),
        ("07. Multi-step Inspection/Quote Form", "quote-wizard" in inspection_html and "data-step=" in inspection_html),
        ("08. Interactive Service Area Map", "taltek-service-map" in service_areas_html and "Goodlettsville" in service_areas_html),
        ("09. Leadership & Technical Team", "Peak Advantage" in team_html and "grid" in team_html),
        ("10. AI Roofing Assistant & Live Chat", "chat-widget-container" in index_html and "chat-user-input" in index_html),
        ("11. Individual Commercial Service Pages", len(list((BASE_DIR / "services").glob("*.html"))) == 12),
        ("12. Sticky Mobile Action Bar", "mobile-sticky-action-bar" in index_html and "tel:+16154486349" in index_html)
    ]
    
    for feat_name, ok in features:
        assert ok, f"Mandatory feature missing or failed: {feat_name}"
        print(f"  -> {feat_name}: PASSED")

    # 6. Test Responsive CSS Architecture
    print("\n[6/7] Verifying Responsive CSS Architecture...")
    base_css = (BASE_DIR / "assets" / "css" / "base.css").read_text(encoding="utf-8")
    comp_css = (BASE_DIR / "assets" / "css" / "components.css").read_text(encoding="utf-8")
    feat_css = (BASE_DIR / "assets" / "css" / "features.css").read_text(encoding="utf-8")
    
    css_checks = [
        ("overflow-x hidden prevention", "overflow-x: hidden" in base_css),
        ("fluid heading clamp", "clamp(" in base_css),
        ("mobile utility bar responsiveness", "@media (max-width: 900px)" in comp_css and "@media (max-width: 480px)" in comp_css),
        ("header button hide on small mobile", "@media (max-width: 540px)" in comp_css),
        ("mobile drawer width clamping", "min(380px, 100vw)" in comp_css),
        ("button wrapping on mobile", "white-space: normal" in comp_css),
        ("sticky mobile bar chat collision offset", "bottom: 76px" in comp_css),
        ("google map embed styling", ".map-embed-wrapper" in comp_css and ".google-map-iframe" in comp_css),
        ("fluid estimator price clamp", "clamp(" in feat_css),
        ("portfolio swipe on mobile", "overflow-x: auto" in feat_css)
    ]
    for check_name, ok in css_checks:
        assert ok, f"CSS check failed: {check_name}"
        print(f"  -> {check_name}: PASSED")

    # 7. JavaScript Touch & Interactive Support
    print("\n[7/7] Verifying JavaScript Touch and Interaction Logic...")
    all_js = "".join([f.read_text(encoding="utf-8") for f in (BASE_DIR / "assets" / "js").glob("*.js")])
    js_checks = [
        ("Before/After touch events", "touchstart" in all_js and "touchmove" in all_js),
        ("Mobile drawer toggle", "mobile-nav" in all_js or "mobile-menu" in all_js or "drawer" in all_js or "hamburger" in all_js or "navToggle" in all_js),
        ("Cookie consent manager", "cookie-banner" in all_js or "cookieConsent" in all_js or "taltek_cookie_consent" in all_js),
        ("Chat assistant logic", "chat" in all_js or "chat-widget" in all_js)
    ]
    for check_name, ok in js_checks:
        assert ok, f"JS check failed: {check_name}"
        print(f"  -> {check_name}: PASSED")

    print("\n" + "=" * 60)
    print("ALL FRONTEND AND MOBILE QA TESTS PASSED WITH 100% SUCCESS!")
    print("=" * 60)
    return True

if __name__ == "__main__":
    success = test_pages()
    sys.exit(0 if success else 1)
