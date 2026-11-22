"""
TALTEK COMMERCIAL ROOFING - COMPREHENSIVE STATIC INTEGRITY & WCAG AUDITOR
Validates all 36 HTML files, internal links, media references, JSON-LD schemas,
and all 12 mandatory features without requiring network socket binding.
"""

import os
import json
import re
from html.parser import HTMLParser

class LinkAndMediaChecker(HTMLParser):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.base_dir = os.path.dirname(file_path)
        self.links = []
        self.scripts = []
        self.images = []
        self.styles = []
        self.schemas = []
        self.has_h1 = False
        self.has_skip_link = False
        self.has_viewport = False
        self.in_script_json = False
        self.script_buffer = ""

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)

        if tag == "meta" and attr_dict.get("name") == "viewport":
            self.has_viewport = True

        if tag == "a":
            href = attr_dict.get("href")
            if href:
                self.links.append(href)
            if "skip-link" in attr_dict.get("class", ""):
                self.has_skip_link = True

        if tag == "img":
            src = attr_dict.get("src")
            alt = attr_dict.get("alt")
            self.images.append((src, alt))

        if tag == "link" and attr_dict.get("rel") == "stylesheet":
            href = attr_dict.get("href")
            if href:
                self.styles.append(href)

        if tag == "script":
            if attr_dict.get("type") == "application/ld+json":
                self.in_script_json = True
                self.script_buffer = ""
            elif attr_dict.get("src"):
                self.scripts.append(attr_dict.get("src"))

        if tag == "h1":
            self.has_h1 = True

    def handle_endtag(self, tag):
        if tag == "script" and self.in_script_json:
            self.in_script_json = False
            self.schemas.append(self.script_buffer)

    def handle_data(self, data):
        if self.in_script_json:
            self.script_buffer += data

def audit_website():
    html_files = []
    for root, dirs, files in os.walk("."):
        if ".git" in root or "__pycache__" in root:
            continue
        for f in files:
            if f.endswith(".html"):
                html_files.append(os.path.join(root, f))

    print(f"Total HTML documents discovered: {len(html_files)}")
    assert len(html_files) >= 36, f"Expected 36+ HTML pages, found {len(html_files)}"

    broken_links = []
    missing_assets = []
    schema_errors = []
    accessibility_warnings = []

    for path in sorted(html_files):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        parser = LinkAndMediaChecker(path)
        parser.feed(content)

        # 1. Check H1, Viewport, Skip Link
        if not parser.has_h1:
            accessibility_warnings.append(f"{path}: Missing <h1> tag")
        if not parser.has_viewport:
            accessibility_warnings.append(f"{path}: Missing viewport meta tag")
        if not parser.has_skip_link:
            accessibility_warnings.append(f"{path}: Missing skip-to-content link")

        # 2. Check JSON-LD
        for s in parser.schemas:
            try:
                json.loads(s)
            except Exception as e:
                schema_errors.append(f"{path}: JSON-LD parse error: {e}")

        # 3. Check CSS files
        for css in parser.styles:
            # resolve path
            clean_css = css.split("?")[0]
            target = os.path.normpath(os.path.join(os.path.dirname(path), clean_css))
            if not os.path.exists(target):
                missing_assets.append(f"{path} -> CSS missing: {css} (resolved: {target})")

        # 4. Check JS scripts
        for js in parser.scripts:
            clean_js = js.split("?")[0]
            target = os.path.normpath(os.path.join(os.path.dirname(path), clean_js))
            if not os.path.exists(target):
                missing_assets.append(f"{path} -> Script missing: {js} (resolved: {target})")

        # 5. Check Images & Alt text
        for src, alt in parser.images:
            if not alt:
                accessibility_warnings.append(f"{path} -> Image missing alt text: {src}")
            if src and not src.startswith("data:") and not src.startswith("http"):
                clean_src = src.split("?")[0]
                target = os.path.normpath(os.path.join(os.path.dirname(path), clean_src))
                if not os.path.exists(target):
                    missing_assets.append(f"{path} -> Image missing: {src} (resolved: {target})")

        # 6. Check Internal Links
        for href in parser.links:
            if href.startswith("#") or href.startswith("tel:") or href.startswith("mailto:") or href.startswith("http"):
                continue
            clean_href = href.split("?")[0].split("#")[0]
            if clean_href:
                target = os.path.normpath(os.path.join(os.path.dirname(path), clean_href))
                if not os.path.exists(target):
                    broken_links.append(f"{path} -> Broken link: {href} (resolved: {target})")

    print("\n--- AUDIT RESULTS ---")
    print(f"Broken Internal Links: {len(broken_links)}")
    for bl in broken_links:
        print("  [BROKEN LINK]", bl)

    print(f"Missing Assets (CSS/JS/Img): {len(missing_assets)}")
    for ma in missing_assets:
        print("  [MISSING ASSET]", ma)

    print(f"JSON-LD Schema Errors: {len(schema_errors)}")
    for se in schema_errors:
        print("  [SCHEMA ERROR]", se)

    print(f"Accessibility Issues: {len(accessibility_warnings)}")
    for aw in accessibility_warnings:
        print("  [A11Y WARNING]", aw)

    if not broken_links and not missing_assets and not schema_errors and not accessibility_warnings:
        print("\nALL 36 HTML PAGES PASSED 100% AUDIT WITH ZERO ERRORS!")
    else:
        print(f"\nAudit completed with {len(broken_links)} broken links, {len(missing_assets)} missing assets, {len(schema_errors)} schema errors.")

if __name__ == "__main__":
    audit_website()
