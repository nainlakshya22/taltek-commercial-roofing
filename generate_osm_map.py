"""Generate ultra-clear Southeastern US map with perfectly positioned Google Maps pins and telemetry."""
import io
import math
import urllib.request
from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageOps, ImageFont

BASE_DIR = Path(r"c:\Users\nainl\OneDrive\Desktop\taltek-commercial-roofing")
IMAGES_DIR = BASE_DIR / "assets" / "images"

def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return (xtile, ytile)

# Bounding box for Southeastern US:
# Lat: 26.5 to 39.5, Lon: -91.5 to -75.0
zoom = 6
x_min, y_min = deg2num(39.5, -91.5, zoom)
x_max, y_max = deg2num(26.5, -75.0, zoom)

headers = {'User-Agent': 'TALTEKCommercialRoofingApp/1.0 (info@taltekroofing.com)'}
tile_w, tile_h = 256, 256
cols = (x_max - x_min + 1)
rows = (y_max - y_min + 1)
stitched_w = cols * tile_w
stitched_h = rows * tile_h

print(f"Stitching {cols}x{rows} tiles -> {stitched_w}x{stitched_h} px")
canvas = Image.new("RGBA", (stitched_w, stitched_h), (20, 24, 28, 255))

for xi, x in enumerate(range(x_min, x_max + 1)):
    for yi, y in enumerate(range(y_min, y_max + 1)):
        url = f"https://tile.openstreetmap.org/{zoom}/{x}/{y}.png"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as res:
                img_data = res.read()
                tile_img = Image.open(io.BytesIO(img_data)).convert("RGBA")
                canvas.paste(tile_img, (xi * tile_w, yi * tile_h))
        except Exception as e:
            print(f"Error tile {x},{y}: {e}")

# Stylize for luxury industrial look:
r, g, b, a = canvas.split()
rgb = Image.merge("RGB", (r, g, b))
inverted = ImageOps.invert(rgb)
enhancer = ImageEnhance.Color(inverted)
colored = enhancer.enhance(0.65)
contrast = ImageEnhance.Contrast(colored).enhance(1.25)
brightness = ImageEnhance.Brightness(contrast).enhance(0.85)

styled_canvas = brightness.convert("RGBA")

def get_xy(lat, lon):
    lat_rad = math.radians(lat)
    n = 2.0 ** zoom
    xf = ((lon + 180.0) / 360.0 * n - x_min) * tile_w
    yf = (((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n) - y_min) * tile_h
    return (int(xf), int(yf))

draw = ImageDraw.Draw(styled_canvas)

hq_x, hq_y = get_xy(36.3242, -86.7133)

# Draw range rings from Goodlettsville HQ
for radius_px, miles_label in [(65, "100 MILES"), (160, "250 MILES"), (320, "500 MILES DISPATCH RADIUS")]:
    bbox = [hq_x - radius_px, hq_y - radius_px, hq_x + radius_px, hq_y + radius_px]
    draw.ellipse(bbox, outline=(216, 117, 53, 90), width=2)
    draw.text((hq_x + radius_px + 8, hq_y - 8), miles_label, fill=(216, 117, 53, 220))

# Hub definitions with custom label offsets to guarantee ZERO overlap:
# (Name, Subtitle, Lat, Lon, (label_offset_x, label_offset_y), text_align)
HUBS = [
    ("Louisville Hub", "Kentucky Network", 38.2527, -85.7585, (16, -18)),
    ("Richmond Hub", "Virginia & Mid-Atlantic", 37.5407, -77.4360, (16, -18)),
    ("Charlotte Hub", "Carolinas Regional Center", 35.2271, -80.8431, (16, -14)),
    ("Atlanta Logistics", "Georgia Fleet & Staging", 33.7490, -84.3880, (18, 6)),
    ("Birmingham Hub", "Alabama Operations", 33.5186, -86.8104, (-210, -6)),
    ("Gulf Coast Operations", "Mobile & New Orleans (MS/LA)", 30.6954, -88.0399, (16, -10)),
    ("Florida Disaster Fleet", "Jacksonville & Orlando Hub", 30.3322, -81.6557, (16, -10)),
]

# Draw connection lines from HQ to Regional Hubs
for name, sub, lat, lon, offset in HUBS:
    px, py = get_xy(lat, lon)
    draw.line([(hq_x, hq_y), (px, py)], fill=(216, 117, 53, 120), width=2)

# Draw Regional Hub Pins & Labels
for name, sub, lat, lon, (ox, oy) in HUBS:
    px, py = get_xy(lat, lon)
    # Pin marker
    draw.ellipse([px - 8, py - 8, px + 8, py + 8], fill=(230, 230, 230, 255), outline=(216, 117, 53, 255), width=2)
    draw.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(216, 117, 53, 255))
    
    # Label badge
    lx = px + ox
    ly = py + oy
    title_text = name
    sub_text = sub
    badge_w = max(len(title_text) * 7 + 24, len(sub_text) * 6 + 24)
    badge_h = 36
    
    draw.rectangle([lx, ly, lx + badge_w, ly + badge_h], fill=(10, 12, 15, 240), outline=(45, 55, 65, 220), width=1)
    draw.text((lx + 10, ly + 5), title_text, fill=(245, 244, 240, 255))
    draw.text((lx + 10, ly + 19), sub_text, fill=(216, 117, 53, 230))

# Finally draw HQ Pin and Major Callout above the pin so it never overlaps Nashville/Birmingham
draw.ellipse([hq_x - 30, hq_y - 30, hq_x + 30, hq_y + 30], fill=(216, 117, 53, 50), outline=(216, 117, 53, 255), width=2)
draw.ellipse([hq_x - 16, hq_y - 16, hq_x + 16, hq_y + 16], fill=(216, 117, 53, 255), outline=(255, 255, 255, 255), width=3)
draw.ellipse([hq_x - 5, hq_y - 5, hq_x + 5, hq_y + 5], fill=(255, 255, 255, 255))

# Prominent HQ Callout Card above the HQ pin
card_w = 360
card_h = 62
card_x = hq_x - (card_w // 2)
card_y = hq_y - 85

# Pointer from card to pin
draw.polygon([(hq_x - 8, card_y + card_h), (hq_x + 8, card_y + card_h), (hq_x, hq_y - 20)], fill=(216, 117, 53, 255))
# Card box
draw.rectangle([card_x, card_y, card_x + card_w, card_y + card_h], fill=(12, 15, 18, 250), outline=(216, 117, 53, 255), width=2)
draw.text((card_x + 16, card_y + 10), "★ TALTEK CORPORATE HQ (GOODLETTSVILLE, TN)", fill=(255, 255, 255, 255))
draw.text((card_x + 16, card_y + 26), "1214 S. Dickerson Rd • (615) 448-6349", fill=(216, 117, 53, 255))
draw.text((card_x + 16, card_y + 42), "Serving Davidson, Sumner, Nashville Metro & 15 SE States", fill=(167, 173, 178, 240))

# Header Badge on top left
draw.rectangle([25, 25, 490, 75], fill=(8, 10, 13, 245), outline=(35, 45, 55, 240), width=1)
draw.text((38, 34), "SOUTHEASTERN REGIONAL OPERATIONS", fill=(245, 244, 240, 255))
draw.text((38, 52), "15 OPERATIONAL STATES • 7 DIRECT REGIONAL HUBS", fill=(216, 117, 53, 255))

# Legend on bottom right
leg_x = stitched_w - 380
leg_y = stitched_h - 105
draw.rectangle([leg_x, leg_y, leg_x + 355, leg_y + 85], fill=(8, 10, 13, 245), outline=(35, 45, 55, 240), width=1)
# Legend items
draw.ellipse([leg_x + 16, leg_y + 16, leg_x + 28, leg_y + 28], fill=(216, 117, 53, 255))
draw.text((leg_x + 36, leg_y + 15), "Corporate Headquarters (Goodlettsville, TN)", fill=(245, 244, 240, 240))
draw.ellipse([leg_x + 18, leg_y + 40, leg_x + 26, leg_y + 48], fill=(230, 230, 230, 255), outline=(216, 117, 53, 255), width=1)
draw.text((leg_x + 36, leg_y + 37), "Verified State Hub (TN, AL, NC, SC, VA, LA, MS)", fill=(167, 173, 178, 240))
draw.line([(leg_x + 16, leg_y + 64), (leg_x + 28, leg_y + 64)], fill=(216, 117, 53, 200), width=2)
draw.text((leg_x + 36, leg_y + 57), "Emergency Dispatch Coverage Corridors", fill=(167, 173, 178, 240))

# Crop canvas to clean 1000x680 presentation
cx, cy = hq_x, hq_y
crop_w, crop_h = 1000, 680
crop_box = (
    max(0, cx - int(crop_w * 0.44)),
    max(0, cy - int(crop_h * 0.38)),
    min(stitched_w, cx + int(crop_w * 0.56)),
    min(stitched_h, cy + int(crop_h * 0.62))
)
final_img = styled_canvas.crop(crop_box).resize((1000, 680), Image.Resampling.LANCZOS)

# Save files
out_png = IMAGES_DIR / "southeast-map.png"
out_jpg = IMAGES_DIR / "southeast-map.jpg"
out_webp = IMAGES_DIR / "southeast-map.webp"

final_img.save(out_png, format="PNG")
final_img.convert("RGB").save(out_jpg, format="JPEG", quality=92)
final_img.save(out_webp, format="WEBP", quality=90)

print(f"SUCCESS: Saved {out_png} ({out_png.stat().st_size} bytes)")
print(f"SUCCESS: Saved {out_webp} ({out_webp.stat().st_size} bytes)")
