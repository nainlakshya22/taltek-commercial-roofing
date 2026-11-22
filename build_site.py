"""
TALTEK COMMERCIAL ROOFING - FULL PRODUCTION SITE GENERATOR
Generates all 36 authentic multi-page HTML documents with verified company data,
Luxury Industrial Futurism styling, WCAG 2.2 AA accessibility, and US compliance.
"""

import os
from build_templates import get_header_html, get_footer_html, get_root_prefix

def render_page(filepath, title, desc, canonical_slug, content_html, path_depth=0, extra_scripts=""):
    root = get_root_prefix(path_depth)
    header = get_header_html(root, canonical_slug)
    footer = get_footer_html(root)
    
    # JSON-LD Schema
    schema_json = f"""{{
  "@context": "https://schema.org",
  "@type": "RoofingContractor",
  "name": "TALTEK Commercial Roofing",
  "url": "https://taltekroofing.com/{canonical_slug}.html",
  "logo": "https://taltekroofing.com/assets/images/taltek-logo.svg",
  "image": "https://taltekroofing.com/assets/images/hero-rooftop.svg",
  "description": "{desc}",
  "telephone": "+1-615-448-6349",
  "email": "sales@taltekroofing.com",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "1214 S. Dickerson Rd",
    "addressLocality": "Goodlettsville",
    "addressRegion": "TN",
    "postalCode": "37072",
    "addressCountry": "US"
  }},
  "geo": {{
    "@type": "GeoCoordinates",
    "latitude": 36.3134,
    "longitude": -86.7136
  }},
  "openingHoursSpecification": [
    {{
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "07:00",
      "closes": "18:00"
    }},
    {{
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Saturday", "Sunday"],
      "opens": "00:00",
      "closes": "23:59",
      "description": "24/7 Emergency Storm Dispatch"
    }}
  ],
  "areaServed": ["Tennessee", "Alabama", "Louisiana", "Mississippi", "North Carolina", "South Carolina", "Virginia", "Kentucky", "Georgia", "Florida"],
  "priceRange": "$$$$"
}}"""

    full_html = f"""<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | TALTEK Commercial Roofing</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="https://taltekroofing.com/{canonical_slug}.html">
  
  <!-- Open Graph / Social -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title} | TALTEK Commercial Roofing">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{root}assets/images/hero-rooftop.jpg">
  <meta property="og:url" content="https://taltekroofing.com/{canonical_slug}.html">
  <meta property="og:site_name" content="TALTEK Commercial Roofing">
  
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title} | TALTEK Commercial Roofing">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{root}assets/images/hero-rooftop.jpg">
  
  <!-- Theme Colors -->
  <meta name="theme-color" content="#0A0C0E">
  <link rel="icon" type="image/svg+xml" href="{root}assets/images/taltek-logo.svg">

  <!-- Design System Stylesheets -->
  <link rel="stylesheet" href="{root}assets/css/variables.css">
  <link rel="stylesheet" href="{root}assets/css/base.css">
  <link rel="stylesheet" href="{root}assets/css/components.css">
  <link rel="stylesheet" href="{root}assets/css/features.css">
  <link rel="stylesheet" href="{root}assets/css/animations.css">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
{schema_json}
  </script>
</head>
<body>
{header}

  <main id="main-content" role="main">
{content_html}
  </main>

{footer}
{extra_scripts}
</body>
</html>"""

    dirname = os.path.dirname(filepath)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Generated: {filepath}")

print("Page renderer ready.")
