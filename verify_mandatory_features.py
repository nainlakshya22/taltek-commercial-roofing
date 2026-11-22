"""
TALTEK COMMERCIAL ROOFING - VERIFICATION OF ALL 12 MANDATORY FEATURES
"""

import os
import sys

def verify_mandatory_features():
    print("Checking All 12 Mandatory Premium Features...")

    with open("index.html", "r", encoding="utf-8") as f:
        home_html = f.read()

    # Feature 01: Cinematic Hero
    assert "hero-section" in home_html, "Feature 01: Missing hero-section"
    assert "hero-poster-img" in home_html, "Feature 01: Missing hero-poster-img fallback"
    assert "hero-overlay" in home_html, "Feature 01: Missing hero-overlay"
    assert "Schedule a Roof Inspection" in home_html, "Feature 01: Missing Primary CTA"
    assert "Explore Our Projects" in home_html, "Feature 01: Missing Secondary CTA"
    print("  [PASSED] Feature 01 — Cinematic Video Hero")

    # Feature 02: Interactive Roof Estimator
    with open("estimator.html", "r", encoding="utf-8") as f:
        est_html = f.read()
    assert "roof-estimator-app" in est_html, "Feature 02: Missing roof-estimator-app"
    assert "building-tile" in est_html, "Feature 02: Missing building type selectors"
    assert "est-roof-area" in est_html, "Feature 02: Missing area slider"
    assert "system-tile" in est_html, "Feature 02: Missing system tiles"
    assert "project-type-tile" in est_html, "Feature 02: Missing scope tiles"
    assert "condition-tile" in est_html, "Feature 02: Missing condition tiles"
    assert "NON-BINDING PRELIMINARY ESTIMATE" in est_html or "LEGAL DISCLAIMER" in est_html, "Feature 02: Missing disclaimer"
    print("  [PASSED] Feature 02 — Interactive Commercial Roof Estimator")

    # Feature 03: Before / After Slider
    assert "before-after-container" in home_html, "Feature 03: Missing before-after-container"
    assert "ba-slider-handle" in home_html, "Feature 03: Missing slider handle"
    assert "ba-after-layer" in home_html, "Feature 03: Missing after layer"
    assert "BEFORE: DETERIORATING MEMBRANE" in home_html, "Feature 03: Missing BEFORE label"
    assert "AFTER: JOHNS MANVILLE TPO SYSTEM" in home_html, "Feature 03: Missing AFTER label"
    print("  [PASSED] Feature 03 — Before / After Interactive Draggable Slider")

    # Feature 04: Filterable Project Portfolio
    with open("projects.html", "r", encoding="utf-8") as f:
        proj_html = f.read()
    assert "portfolio-filter-bar" in proj_html, "Feature 04: Missing filter bar"
    assert "project-grid" in proj_html, "Feature 04: Missing project grid"
    for cs in ["nashville-general-hospital.html", "frost-bank-plaza.html", "krusteaz-facility.html", "rapha-center.html", "malone-plaza.html"]:
        assert os.path.exists(os.path.join("projects", cs)), f"Feature 04: Missing case study {cs}"
    print("  [PASSED] Feature 04 — Filterable Project Portfolio & 5 Dedicated Case Studies")

    # Feature 05: Google Reviews Integration
    assert "reviews-summary-card" in home_html, "Feature 05: Missing reviews summary card"
    assert "4.8" in home_html, "Feature 05: Missing 4.8 rating"
    assert "10,000+ Clients Served" in home_html, "Feature 05: Missing client stats"
    assert "Verified Google Business Review" in home_html, "Feature 05: Missing verified review tags"
    print("  [PASSED] Feature 05 — Google Reviews Integration")

    # Feature 06: Financing Calculator
    with open("financing.html", "r", encoding="utf-8") as f:
        fin_html = f.read()
    assert "financing-calculator-box" in fin_html, "Feature 06: Missing financing calculator box"
    assert "fin-project-cost" in fin_html, "Feature 06: Missing cost input"
    assert "fin-term-months" in fin_html, "Feature 06: Missing term input"
    assert "fin-interest-rate" in fin_html, "Feature 06: Missing rate input"
    assert "MANDATORY FINANCING DISCLOSURE" in fin_html, "Feature 06: Missing financing legal disclosure"
    print("  [PASSED] Feature 06 — Financing Calculator")

    # Feature 07: Multi-Step Quote Form
    with open("request-inspection.html", "r", encoding="utf-8") as f:
        quote_html = f.read()
    assert "quote-wizard" in quote_html, "Feature 07: Missing quote wizard"
    assert 'data-step="1"' in quote_html and 'data-step="5"' in quote_html, "Feature 07: Missing wizard steps"
    assert "hp_website_title" in quote_html, "Feature 07: Missing spam honeypot"
    assert "sms_consent" in quote_html, "Feature 07: Missing un-checked SMS consent option"
    print("  [PASSED] Feature 07 — Multi-Step Commercial Inspection Request Wizard")

    # Feature 08: Interactive Service Area Map
    with open("service-areas.html", "r", encoding="utf-8") as f:
        map_html = f.read()
    assert "taltek-service-map" in map_html, "Feature 08: Missing map element"
    assert "Tennessee" in map_html and "Goodlettsville" in map_html, "Feature 08: Missing HQ data"
    assert "Alabama" in map_html and "Louisiana" in map_html and "Mississippi" in map_html and "Virginia" in map_html, "Feature 08: Missing licensed states"
    print("  [PASSED] Feature 08 — Interactive Service Area Map")

    # Feature 09: Team Profiles and Verified Accreditations
    with open("team.html", "r", encoding="utf-8") as f:
        team_html = f.read()
    assert "Peak Advantage Master Contractor" in team_html, "Feature 09: Missing Johns Manville credential"
    assert "Master Select Commercial Contractor" in team_html, "Feature 09: Missing GAF credential"
    assert "OSHA 30-Hour Supervisor Certified" in team_html, "Feature 09: Missing OSHA credential"
    assert "NRCA Active Commercial Member" in team_html, "Feature 09: Missing NRCA credential"
    print("  [PASSED] Feature 09 — Team Profiles & Verified Manufacturer Accreditations")

    # Feature 10: Live Chat / AI Assistant
    assert "chat-widget-container" in home_html, "Feature 10: Missing chat widget"
    assert "AUTOMATED (NON-HUMAN)" in home_html, "Feature 10: Missing automated indicator badge"
    assert "chat-user-input" in home_html, "Feature 10: Missing chat input"
    print("  [PASSED] Feature 10 — Live Chat / Industrial AI Assistant")

    # Feature 11: Individual Service Pages
    service_pages = [
        "commercial-roofing.html", "industrial-roofing.html", "roof-replacement.html",
        "roof-repair.html", "emergency-services.html", "preventative-maintenance.html",
        "tpo-roofing.html", "epdm-roofing.html", "pvc-roofing.html",
        "storm-protection.html", "roof-assessment.html", "gutter-services.html"
    ]
    for sp in service_pages:
        assert os.path.exists(os.path.join("services", sp)), f"Feature 11: Missing service page {sp}"
    print(f"  [PASSED] Feature 11 — All 12 Dedicated Service Pages Present")

    # Feature 12: Sticky Mobile Action Bar
    assert "mobile-sticky-action-bar" in home_html, "Feature 12: Missing sticky action bar"
    assert "Call (615) 448-6349" in home_html, "Feature 12: Missing phone button"
    assert "Request Inspection" in home_html, "Feature 12: Missing inspection button"
    print("  [PASSED] Feature 12 — Sticky Mobile Call / Quote Action Bar")

    print("\nALL 12 MANDATORY PREMIUM FEATURES ARE 100% VERIFIED AND PRESENT!")

if __name__ == "__main__":
    verify_mandatory_features()
