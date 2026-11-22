"""Generate Southeast Map SVG and additional service diagrams with embedded real geographic map."""
import os
import base64

images_dir = os.path.join("assets", "images")
webp_path = os.path.join(images_dir, "southeast-map.webp")

if os.path.exists(webp_path):
    with open(webp_path, "rb") as f:
        map_b64 = base64.b64encode(f.read()).decode("ascii")
    bg_image_tag = f'<image href="data:image/webp;base64,{map_b64}" width="1000" height="680" preserveAspectRatio="xMidYMid slice"/>'
else:
    bg_image_tag = '<rect width="1000" height="680" fill="#0C0E11" rx="8"/>'

map_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 680" fill="none" class="taltek-service-map" role="img" aria-label="TALTEK 15-State Southeastern Commercial Roofing Coverage Map">
  <defs>
    <filter id="glowEffect" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
    <style>
      .state-path {{
        fill: transparent;
        transition: fill 0.25s ease, stroke 0.25s ease;
        cursor: pointer;
      }}
      .state-path:hover {{
        fill: rgba(216, 117, 53, 0.28);
        stroke: #D87535;
        stroke-width: 2.5;
        filter: url(#glowEffect);
      }}
      .state-hq:hover {{
        fill: rgba(216, 117, 53, 0.4);
      }}
    </style>
  </defs>

  <!-- Clear Realistic Geographic Map Layer -->
  {bg_image_tag}

  <!-- Interactive States Group with Transparent Clickable Hit-Areas -->
  <g class="states-layer" stroke="rgba(216, 117, 53, 0.4)" stroke-width="1.2">

    <!-- TENNESSEE (HQ State) -->
    <path id="state-tn" class="state-path state-hq" data-state="Tennessee" data-status="Headquarters &amp; Primary Hub" data-license="Fully Licensed &amp; Insured" data-projects="5,200+ Projects Completed"
      d="M 370 270 L 610 235 L 630 250 L 590 285 L 340 310 L 330 275 Z" />

    <!-- ALABAMA (Verified Licensed) -->
    <path id="state-al" class="state-path state-licensed" data-state="Alabama" data-status="Verified Licensed State" data-license="Licensed Commercial Contractor" data-projects="840+ Projects"
      d="M 400 310 L 485 300 L 500 440 L 440 450 L 440 430 L 410 430 Z" />

    <!-- MISSISSIPPI (Verified Licensed) -->
    <path id="state-ms" class="state-path state-licensed" data-state="Mississippi" data-status="Verified Licensed State" data-license="Commercial Roofing License" data-projects="620+ Projects"
      d="M 340 310 L 400 310 L 410 430 L 380 435 L 360 415 L 325 390 Z" />

    <!-- LOUISIANA (Verified Licensed) -->
    <path id="state-la" class="state-path state-licensed" data-state="Louisiana" data-status="Verified Licensed State" data-license="State Licensed Commercial Contractor" data-projects="510+ Projects"
      d="M 280 390 L 345 390 L 340 430 L 390 440 L 390 470 L 340 470 L 300 450 Z" />

    <!-- NORTH CAROLINA (Verified Licensed) -->
    <path id="state-nc" class="state-path state-licensed" data-state="North Carolina" data-status="Verified Licensed State" data-license="General Commercial Roofing Contractor" data-projects="920+ Projects"
      d="M 590 240 L 760 210 L 810 245 L 750 280 L 620 275 Z" />

    <!-- SOUTH CAROLINA (Verified Licensed) -->
    <path id="state-sc" class="state-path state-licensed" data-state="South Carolina" data-status="Verified Licensed State" data-license="Commercial Specialty Roofing License" data-projects="710+ Projects"
      d="M 590 285 L 680 275 L 750 280 L 700 350 L 610 330 Z" />

    <!-- VIRGINIA (Verified Licensed) -->
    <path id="state-va" class="state-path state-licensed" data-state="Virginia" data-status="Verified Licensed State" data-license="Class A Commercial Contractor" data-projects="830+ Projects"
      d="M 570 195 L 730 150 L 775 190 L 740 215 L 590 235 Z" />

    <!-- GEORGIA (Operational Southeast) -->
    <path id="state-ga" class="state-path state-operational" data-state="Georgia" data-status="Operational Regional Territory" data-license="Commercial Support Coverage" data-projects="890+ Projects"
      d="M 485 300 L 590 285 L 610 330 L 630 420 L 520 440 L 500 370 Z" />

    <!-- FLORIDA (Operational Southeast) -->
    <path id="state-fl" class="state-path state-operational" data-state="Florida" data-status="Operational Regional Territory" data-license="Commercial Emergency &amp; Logistics" data-projects="650+ Projects"
      d="M 440 450 L 630 420 L 680 480 L 690 560 L 630 610 L 610 520 L 520 450 Z" />

    <!-- KENTUCKY (Operational Southeast) -->
    <path id="state-ky" class="state-path state-operational" data-state="Kentucky" data-status="Operational Regional Territory (Krusteaz Facility)" data-license="Commercial Deployment Ready" data-projects="440+ Projects"
      d="M 370 220 L 540 180 L 570 200 L 510 240 L 370 270 Z" />
  </g>
</svg>
"""

with open(os.path.join(images_dir, "southeast-map.svg"), "w", encoding="utf-8") as f:
    f.write(map_svg)

print("SUCCESS: Updated southeast-map.svg with clear realistic map image.")
