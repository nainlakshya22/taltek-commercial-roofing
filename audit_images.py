import glob
import re
import os

img_srcs = set()
for html_file in glob.glob("**/*.html", recursive=True):
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
    for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', content):
        img_srcs.add((html_file.replace("\\", "/"), m.group(1)))
    for m in re.finditer(r'url\(["\']?([^"\'\)]+)["\']?\)', content):
        if not m.group(1).startswith("data:"):
            img_srcs.add((html_file.replace("\\", "/"), m.group(1)))

print(f"Total image references found: {len(img_srcs)}")

broken = []
for page, src in sorted(img_srcs):
    # calculate target path
    if src.startswith("http://") or src.startswith("https://") or src.startswith("//"):
        status = "EXTERNAL"
    elif src.startswith("/"):
        local_path = os.path.normpath(os.path.join(".", src.lstrip("/")))
        status = "OK" if os.path.exists(local_path) else "BROKEN"
    else:
        page_dir = os.path.dirname(page)
        local_path = os.path.normpath(os.path.join(page_dir, src))
        status = "OK" if os.path.exists(local_path) else "BROKEN"
    
    if status == "BROKEN":
        broken.append((page, src, local_path))
    print(f"[{status}] {page} -> {src}")

print(f"\nTotal broken images: {len(broken)}")
for page, src, local_path in broken:
    print(f"BROKEN: {page} references '{src}' (resolved to '{local_path}')")
