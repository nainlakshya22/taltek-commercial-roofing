"""
Download curated, authentic high-resolution commercial roofing and industrial warehouse
photography from Unsplash for TALTEK Commercial Roofing frontend excellence.
All photos are legally usable for commercial projects under the Unsplash License.
"""
import urllib.request
import os

IMAGES_DIR = os.path.join(os.path.dirname(__file__), "assets", "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

PHOTO_MAP = {
    # 1. Hero Cinematic Rooftop (Aerial drone view of commercial flat warehouse roof)
    "hero-rooftop.jpg": ("photo-1786913508480-2dcec035a84a", 1920, 1080),
    
    # 2. Before Damaged Commercial Roof (Distressed membrane, aging aggregate, wear)
    "before-damaged-roof.jpg": ("photo-1518780664697-55e3ad937233", 1200, 750),
    
    # 3. After New TPO Commercial Roof (Brilliant, clean commercial flat roof installation)
    "after-tpo-roof.jpg": ("photo-1786913507250-813bfd26d859", 1200, 750),
    
    # 4. Project: Krusteaz Manufacturing Facility (205k sqft industrial warehouse)
    "project-krusteaz.jpg": ("photo-1786913507360-ec354230d95f", 1200, 750),
    
    # 5. Project: Nashville General Hospital (Healthcare facility roof)
    "project-nashville-general.jpg": ("photo-1517581177682-a085bb7ffb15", 1200, 750),
    
    # 6. Project: Frost Bank Plaza (High-rise commercial corporate plaza & roof)
    "project-frost-bank.jpg": ("photo-1486406146926-c627a92ad1ab", 1200, 750),
    
    # 7. Project: Malone Plaza (Retail commercial shopping plaza flat roof)
    "project-malone-plaza.jpg": ("photo-1786913507250-813bfd26d859", 1200, 750),
    
    # 8. Project: Rapha Center (Commercial distribution center)
    "project-rapha-center.jpg": ("photo-1586528116311-ad8dd3c8310d", 1200, 750),
    
    # 9. Commercial Roofing Contractors at Work
    "commercial-contractors.jpg": ("photo-1504307651254-35680f356dfd", 1200, 800),
    
    # 10. Technical Inspection & Core Sampling Diagnostic
    "roof-assessment-inspector.jpg": ("photo-1581094794329-c8112a89af12", 1200, 800),
    
    # 11. TPO Seam Heat-Welding & Membrane Detailing
    "commercial-tpo-installation.jpg": ("photo-1621905251189-08b45d6a269e", 1200, 800),
    
    # 12. Industrial Plant & Heavy Manufacturing Facility
    "heavy-industrial-roof.jpg": ("photo-1587293852726-70cdb56c2866", 1200, 800),
    
    # 13. Heavy Commercial Construction & Deck Replacement
    "commercial-construction-site.jpg": ("photo-1534398079543-7ae6d016b86a", 1200, 800)
}

print(f"Downloading {len(PHOTO_MAP)} verified commercial photography assets...")

for filename, (photo_id, width, height) in PHOTO_MAP.items():
    filepath = os.path.join(IMAGES_DIR, filename)
    url = f"https://images.unsplash.com/{photo_id}?auto=format&fit=crop&w={width}&h={height}&q=85"
    print(f"Fetching {filename} ({width}x{height}) from {photo_id}...", end=" ", flush=True)
    
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read()
            with open(filepath, "wb") as f:
                f.write(content)
            print(f"DONE ({len(content):,} bytes)")
    except Exception as e:
        print(f"FAILED: {e}")

print("\nAsset download complete. Verifying presence:")
for filename in PHOTO_MAP.keys():
    p = os.path.join(IMAGES_DIR, filename)
    exists = os.path.exists(p)
    size = os.path.getsize(p) if exists else 0
    print(f"  [{'OK' if exists and size > 1000 else 'MISSING'}] {filename} ({size:,} bytes)")
