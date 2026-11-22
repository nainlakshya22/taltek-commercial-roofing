"""
Generate high-fidelity vector assets for TALTEK Commercial Roofing
"""
import os

images_dir = os.path.join("assets", "images")
os.makedirs(images_dir, exist_ok=True)

# 1. TALTEK LOGO (Primary and Light/Dark variants)
logo_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 64" fill="none" role="img" aria-label="TALTEK Commercial Roofing Logo">
  <defs>
    <linearGradient id="taltekOrange" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E58646" />
      <stop offset="100%" stop-color="#D87535" />
    </linearGradient>
    <linearGradient id="steelGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F5F4F0" />
      <stop offset="100%" stop-color="#A7ADB2" />
    </linearGradient>
  </defs>
  <!-- Architectural Emblem -->
  <g transform="translate(6, 6)">
    <!-- Base industrial angle / structural truss -->
    <path d="M 4 48 L 26 8 L 48 48 Z" stroke="#3A4048" stroke-width="2.5" fill="none" stroke-linejoin="round"/>
    <path d="M 12 48 L 26 22 L 40 48" stroke="#3A4048" stroke-width="1.5" fill="none"/>
    <!-- Precision Copper Peak / Roof Membrane Chevron -->
    <path d="M 16 34 L 26 14 L 36 34" stroke="url(#taltekOrange)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="26" cy="14" r="3" fill="#D87535" />
    <!-- Horizontal datum bar -->
    <line x1="0" y1="48" x2="52" y2="48" stroke="url(#taltekOrange)" stroke-width="2.5" stroke-linecap="square"/>
    <!-- Precision ticks -->
    <line x1="26" y1="48" x2="26" y2="52" stroke="#D87535" stroke-width="2"/>
    <line x1="6" y1="48" x2="6" y2="51" stroke="#A7ADB2" stroke-width="1.5"/>
    <line x1="46" y1="48" x2="46" y2="51" stroke="#A7ADB2" stroke-width="1.5"/>
  </g>
  <!-- Wordmark -->
  <text x="74" y="38" font-family="'Inter', 'Manrope', 'Segoe UI', -apple-system, sans-serif" font-weight="900" font-size="28" letter-spacing="4" fill="#F5F4F0">TALTEK</text>
  <text x="75" y="52" font-family="'Inter', 'Manrope', 'Segoe UI', -apple-system, sans-serif" font-weight="600" font-size="8.5" letter-spacing="3.2" fill="#A7ADB2">COMMERCIAL ROOFING</text>
  <circle cx="258" cy="49" r="1.5" fill="#D87535"/>
  <text x="264" y="52" font-family="'Inter', sans-serif" font-weight="500" font-size="8" letter-spacing="2" fill="#D87535">EST. 2009</text>
</svg>"""

with open(os.path.join(images_dir, "taltek-logo.svg"), "w", encoding="utf-8") as f:
    f.write(logo_svg)

# 2. Hero Background SVG Graphic (High-impact industrial architectural rooftop at twilight)
hero_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Commercial industrial rooftop infrastructure">
  <defs>
    <linearGradient id="skyGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#080A0C" />
      <stop offset="45%" stop-color="#14181D" />
      <stop offset="75%" stop-color="#241E1C" />
      <stop offset="100%" stop-color="#3A2418" />
    </linearGradient>
    <linearGradient id="horizonGlow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#D87535" stop-opacity="0.1" />
      <stop offset="50%" stop-color="#D87535" stop-opacity="0.45" />
      <stop offset="100%" stop-color="#D87535" stop-opacity="0.1" />
    </linearGradient>
    <linearGradient id="roofGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E2328" />
      <stop offset="50%" stop-color="#16191D" />
      <stop offset="100%" stop-color="#0C0E10" />
    </linearGradient>
    <linearGradient id="membraneHighlight" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#A7ADB2" stop-opacity="0.25" />
      <stop offset="100%" stop-color="#1E2328" stop-opacity="0.05" />
    </linearGradient>
    <pattern id="gridPattern" width="60" height="60" patternUnits="userSpaceOnUse">
      <path d="M 60 0 L 0 0 0 60" fill="none" stroke="#252A30" stroke-width="0.75" stroke-opacity="0.5"/>
    </pattern>
    <pattern id="isoGrid" width="120" height="70" patternUnits="userSpaceOnUse">
      <path d="M 0 35 L 60 0 L 120 35 L 60 70 Z" fill="none" stroke="#2A313A" stroke-width="0.8" stroke-opacity="0.4"/>
    </pattern>
  </defs>

  <!-- Sky & Atmosphere -->
  <rect width="1920" height="1080" fill="url(#skyGrad)"/>
  
  <!-- Subtle Horizon Glow -->
  <ellipse cx="960" cy="520" rx="900" ry="220" fill="url(#horizonGlow)" />

  <!-- Distant Industrial Skyline / Crane Silhouettes -->
  <g opacity="0.35" fill="#13171B">
    <!-- Building silhouettes -->
    <rect x="140" y="440" width="160" height="180" />
    <rect x="220" y="410" width="120" height="210" />
    <rect x="420" y="460" width="180" height="160" />
    <rect x="780" y="430" width="220" height="190" />
    <rect x="1100" y="450" width="140" height="170" />
    <rect x="1320" y="420" width="190" height="200" />
    <rect x="1600" y="440" width="220" height="180" />
    <!-- Tower Crane lines -->
    <path d="M 340 540 L 340 320 L 460 300 M 340 320 L 290 330" stroke="#485058" stroke-width="2"/>
    <path d="M 1240 550 L 1240 300 L 1380 280 M 1240 300 L 1190 310" stroke="#485058" stroke-width="2"/>
  </g>

  <!-- Commercial Flat Roof Structure in Perspective -->
  <!-- Parapet wall top edge -->
  <polygon points="0,520 1920,480 1920,535 0,580" fill="#20252B" stroke="#363E46" stroke-width="1.5"/>
  <!-- Copper coping flashing cap -->
  <polygon points="0,520 1920,480 1920,488 0,528" fill="#D87535" opacity="0.85"/>

  <!-- Vast Commercial TPO/EPDM Roof Deck -->
  <polygon points="0,580 1920,535 1920,1080 0,1080" fill="url(#roofGrad)"/>
  
  <!-- Architectural Coordinate Grid Overlay across roof -->
  <polygon points="0,580 1920,535 1920,1080 0,1080" fill="url(#isoGrid)"/>

  <!-- Precision Heat-Welded Membrane Seam Lines in Perspective -->
  <g stroke="#3A434C" stroke-width="1.2" opacity="0.65">
    <line x1="200" y1="575" x2="100" y2="1080" />
    <line x1="450" y1="568" x2="380" y2="1080" />
    <line x1="720" y1="562" x2="700" y2="1080" stroke="#D87535" stroke-width="1.5" opacity="0.5"/>
    <line x1="1020" y1="556" x2="1080" y2="1080" />
    <line x1="1320" y1="549" x2="1460" y2="1080" />
    <line x1="1620" y1="542" x2="1820" y2="1080" />
  </g>

  <!-- Rooftop HVAC / Industrial Infrastructure Elements with dimension marks -->
  <g opacity="0.85">
    <!-- Unit 1 -->
    <rect x="300" y="660" width="220" height="120" fill="#1C2025" stroke="#373F47" stroke-width="1.5" rx="4"/>
    <rect x="320" y="680" width="80" height="70" fill="#121518" stroke="#2B3239"/>
    <circle cx="460" cy="715" r="32" fill="#14181B" stroke="#D87535" stroke-width="1.5" stroke-dasharray="6,4"/>
    <text x="320" y="650" font-family="'Inter', monospace" font-size="11" fill="#A7ADB2" letter-spacing="1.5">HVAC-RTU 01 // VIBRATION ISOLATED</text>
    
    <!-- Unit 2 (Distant) -->
    <rect x="1200" y="590" width="160" height="90" fill="#191D21" stroke="#323A42" stroke-width="1.5" rx="3"/>
    <circle cx="1310" cy="635" r="24" fill="#111417" stroke="#3D454E"/>
    <text x="1200" y="582" font-family="'Inter', monospace" font-size="9" fill="#757D85" letter-spacing="1">CONDENSER-R3 // CURB MOUNTED</text>

    <!-- Commercial Skylights / Smoke Vents -->
    <polygon points="760,720 900,720 940,780 720,780" fill="#1E2328" stroke="#3A434C" stroke-width="1.2"/>
    <polygon points="775,730 885,730 920,770 740,770" fill="#2A333C" opacity="0.7"/>
    <line x1="720" y1="780" x2="940" y2="780" stroke="#D87535" stroke-width="2"/>
    <text x="730" y="805" font-family="'Inter', monospace" font-size="10" fill="#A7ADB2" letter-spacing="1.5">ROOFLIGHT TRANSLUCENT BAY // FALL PROTECTION INTEGRATED</text>
  </g>

  <!-- Technical Telemetry & Engineering HUD overlay -->
  <g font-family="'Inter', monospace" font-size="11" fill="#A7ADB2" opacity="0.8">
    <text x="60" y="80" fill="#D87535" font-weight="700" letter-spacing="2">SYS://TALTEK-AERIAL-MONITOR</text>
    <text x="60" y="105" letter-spacing="1">COORD: 36.3134° N, 86.7136° W</text>
    <text x="60" y="125" letter-spacing="1">HEADQUARTERS: GOODLETTSVILLE, TN</text>
    <text x="60" y="145" letter-spacing="1">MEMBRANE SPEC: 60-MIL TPO / CLASS A RATED</text>
    
    <!-- Top Right Telemetry -->
    <text x="1600" y="80" text-anchor="end" fill="#F5F4F0" font-weight="600" letter-spacing="2">NDL WARRANTY VERIFICATION</text>
    <text x="1600" y="105" text-anchor="end" letter-spacing="1">WIND SPEED DESIGN: 120 MPH</text>
    <text x="1600" y="125" text-anchor="end" fill="#D87535" letter-spacing="1">CLIENT BASE: 10,000+ PROJECTS</text>
  </g>

  <!-- Crosshair and calibration marks -->
  <g stroke="#D87535" stroke-width="1" opacity="0.5">
    <line x1="960" y1="460" x2="960" y2="480" />
    <line x1="960" y1="520" x2="960" y2="540" />
    <line x1="930" y1="500" x2="950" y2="500" />
    <line x1="970" y1="500" x2="990" y2="500" />
    <circle cx="960" cy="500" r="16" fill="none" stroke-dasharray="2,2"/>
  </g>
</svg>"""

with open(os.path.join(images_dir, "hero-rooftop.svg"), "w", encoding="utf-8") as f:
    f.write(hero_svg)

# 3. BEFORE / AFTER COMPARISON IMAGES
# Before: Aging damaged membrane with blisters, standing water, failed seams, open cracks
before_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 650" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Damaged commercial roof prior to TALTEK replacement">
  <defs>
    <radialGradient id="pondGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#121815" stop-opacity="0.95"/>
      <stop offset="60%" stop-color="#1A221E" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#2D332F" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="agedDeck" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3D3A37"/>
      <stop offset="50%" stop-color="#32302D"/>
      <stop offset="100%" stop-color="#262422"/>
    </linearGradient>
  </defs>
  <rect width="1000" height="650" fill="url(#agedDeck)"/>
  
  <!-- Texture & Weathering lines -->
  <g stroke="#1F1D1B" stroke-width="1.5" opacity="0.7">
    <!-- Severe alligatoring and surface cracks -->
    <path d="M 50 120 Q 150 140 220 110 T 380 160 T 520 120 T 700 170 T 890 130" fill="none" stroke-width="2.5"/>
    <path d="M 80 240 Q 200 280 320 230 T 490 290 T 680 240 T 920 280" fill="none" stroke-width="2"/>
    <path d="M 40 400 Q 180 380 310 430 T 510 390 T 730 450 T 950 410" fill="none" stroke-width="2.2"/>
    <path d="M 90 530 Q 240 570 380 520 T 590 580 T 820 540" fill="none" stroke-width="2"/>
  </g>

  <!-- Blisters and punctures -->
  <ellipse cx="280" cy="190" rx="45" ry="25" fill="#201E1C" stroke="#161413" stroke-width="2"/>
  <ellipse cx="640" cy="340" rx="60" ry="32" fill="#1C1A18" stroke="#141211" stroke-width="2.5"/>
  <ellipse cx="420" cy="480" rx="35" ry="20" fill="#22201E" stroke="#181615" stroke-width="2"/>

  <!-- Ponding Water with rust deposits -->
  <ellipse cx="500" cy="310" rx="260" ry="110" fill="url(#pondGrad)"/>
  <path d="M 320 290 Q 500 260 680 300 Q 640 370 470 360 Q 340 350 320 290 Z" fill="#222623" opacity="0.8" stroke="#3D3425" stroke-width="3"/>
  <!-- Rust staining -->
  <path d="M 680 280 C 730 310 750 350 720 370" stroke="#7A3D1E" stroke-width="8" stroke-linecap="round" opacity="0.6"/>
  <path d="M 330 270 C 310 320 320 360 360 380" stroke="#683419" stroke-width="6" stroke-linecap="round" opacity="0.55"/>

  <!-- Failed flashing around curb -->
  <rect x="740" y="100" width="180" height="130" fill="#292623" stroke="#181614" stroke-width="2"/>
  <path d="M 740 230 L 920 230" stroke="#A83232" stroke-width="4" stroke-dasharray="8,6"/>
  <text x="745" y="255" font-family="'Inter', sans-serif" font-size="12" fill="#E66767" font-weight="700">FAILED PERIMETER FLASHING</text>

  <!-- Identification Overlay -->
  <rect x="30" y="30" width="280" height="48" fill="#0A0C0E" rx="4" opacity="0.85"/>
  <text x="45" y="60" font-family="'Inter', sans-serif" font-weight="800" font-size="14" fill="#EF4444" letter-spacing="1.5">BEFORE: SEVERE DEGRADATION</text>
  <text x="45" y="95" font-family="'Inter', monospace" font-size="11" fill="#A7ADB2">Saturated insulation &amp; seam failure</text>
</svg>"""

with open(os.path.join(images_dir, "before-damaged-roof.svg"), "w", encoding="utf-8") as f:
    f.write(before_svg)

# After: Flawless Johns Manville White TPO, heat-welded seams, crisp perimeter flashing, perfect drainage
after_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 650" preserveAspectRatio="xMidYMid slice" role="img" aria-label="TALTEK newly installed premium Johns Manville TPO commercial roof">
  <defs>
    <linearGradient id="cleanTPO" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E8ECEF"/>
      <stop offset="50%" stop-color="#D9DFE4"/>
      <stop offset="100%" stop-color="#CBD2D8"/>
    </linearGradient>
    <linearGradient id="sunReflection" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.5"/>
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.3"/>
    </linearGradient>
  </defs>
  <!-- Flawless Cool Roof Reflective Membrane -->
  <rect width="1000" height="650" fill="url(#cleanTPO)"/>

  <!-- High-albedo solar reflectivity wash -->
  <polygon points="100,0 600,0 450,650 0,650" fill="url(#sunReflection)" opacity="0.25"/>

  <!-- Precision Robotic Hot-Air Welded Seams -->
  <g stroke="#9BA3AB" stroke-width="3" opacity="0.85">
    <line x1="220" y1="0" x2="220" y2="650"/>
    <line x1="480" y1="0" x2="480" y2="650"/>
    <line x1="740" y1="0" x2="740" y2="650"/>
  </g>
  <!-- Seam Weld Indicators (Robotic testing markings) -->
  <g stroke="#D87535" stroke-width="1" stroke-dasharray="2,6" opacity="0.7">
    <line x1="223" y1="0" x2="223" y2="650"/>
    <line x1="483" y1="0" x2="483" y2="650"/>
    <line x1="743" y1="0" x2="743" y2="650"/>
  </g>

  <!-- Newly sealed equipment curb with Johns Manville membrane corners & copper details -->
  <rect x="740" y="100" width="180" height="130" fill="#E2E7EC" stroke="#8E97A0" stroke-width="2"/>
  <rect x="735" y="95" width="190" height="14" fill="#D87535"/>
  <rect x="755" y="125" width="150" height="85" fill="#31373E" rx="3"/>
  <!-- Target curb flashing fillet -->
  <path d="M 720 245 L 940 245" stroke="#10B981" stroke-width="3"/>
  <text x="735" y="270" font-family="'Inter', sans-serif" font-size="11" fill="#059669" font-weight="700">CERTIFIED FACTORY FLASHING</text>

  <!-- Walkway Safety Pads (Textured Yellow/Grey) -->
  <g fill="#A1A9B0" stroke="#7E878F" stroke-width="1.5">
    <rect x="300" y="520" width="70" height="90" rx="3"/>
    <rect x="390" y="520" width="70" height="90" rx="3"/>
    <rect x="480" y="520" width="70" height="90" rx="3"/>
    <rect x="570" y="520" width="70" height="90" rx="3"/>
    <rect x="660" y="520" width="70" height="90" rx="3"/>
  </g>
  <text x="300" y="505" font-family="'Inter', monospace" font-size="10" fill="#6B7280" letter-spacing="1">DESIGNATED WALKWAY PADS // OSHA ACCESSIBLE</text>

  <!-- Identification Overlay -->
  <rect x="30" y="30" width="340" height="48" fill="#0A0C0E" rx="4" opacity="0.9"/>
  <text x="45" y="60" font-family="'Inter', sans-serif" font-weight="800" font-size="14" fill="#10B981" letter-spacing="1.5">AFTER: 60-MIL JOHNS MANVILLE TPO</text>
  <text x="45" y="95" font-family="'Inter', monospace" font-size="11" fill="#10B981">20-Year NDL Warranty // 100% Watertight</text>
</svg>"""

with open(os.path.join(images_dir, "after-tpo-roof.svg"), "w", encoding="utf-8") as f:
    f.write(after_svg)

# 4. FIVE VERIFIED REAL CASE STUDY PROJECTS
# Project 1: Nashville General Hospital
proj1_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Nashville General Hospital Commercial Roofing Project">
  <defs>
    <linearGradient id="p1Sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#14181E"/><stop offset="100%" stop-color="#222B36"/>
    </linearGradient>
    <linearGradient id="p1Roof" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E2E7EC"/><stop offset="100%" stop-color="#BAC3CC"/>
    </linearGradient>
  </defs>
  <rect width="800" height="500" fill="url(#p1Sky)"/>
  <!-- Hospital Facade -->
  <rect x="60" y="220" width="680" height="280" fill="#1A1E24" stroke="#2C3440" stroke-width="2"/>
  <g fill="#2A3340" stroke="#3A4656" stroke-width="1">
    <!-- Hospital Windows -->
    <rect x="100" y="260" width="50" height="40"/><rect x="180" y="260" width="50" height="40"/>
    <rect x="260" y="260" width="50" height="40"/><rect x="340" y="260" width="50" height="40"/>
    <rect x="420" y="260" width="50" height="40"/><rect x="500" y="260" width="50" height="40"/>
    <rect x="580" y="260" width="50" height="40"/><rect x="660" y="260" width="50" height="40"/>
    <rect x="100" y="330" width="50" height="40"/><rect x="180" y="330" width="50" height="40"/>
    <rect x="260" y="330" width="50" height="40"/><rect x="340" y="330" width="50" height="40"/>
    <rect x="420" y="330" width="50" height="40"/><rect x="500" y="330" width="50" height="40"/>
    <rect x="580" y="330" width="50" height="40"/><rect x="660" y="330" width="50" height="40"/>
  </g>
  <!-- Johns Manville TPO Rooftop with tapered insulation pitch -->
  <polygon points="40,220 760,220 720,130 80,130" fill="url(#p1Roof)" stroke="#D87535" stroke-width="2"/>
  <!-- Welded seams -->
  <line x1="220" y1="130" x2="200" y2="220" stroke="#8E99A4" stroke-width="1.8"/>
  <line x1="400" y1="130" x2="400" y2="220" stroke="#8E99A4" stroke-width="1.8"/>
  <line x1="580" y1="130" x2="600" y2="220" stroke="#8E99A4" stroke-width="1.8"/>
  <!-- Drainage crickets -->
  <polygon points="340,160 460,160 400,200" fill="#9BA7B4" opacity="0.6"/>
  <!-- Badge -->
  <rect x="40" y="30" width="310" height="58" fill="#0A0C0E" rx="4" stroke="#D87535" stroke-width="1.5"/>
  <text x="56" y="54" font-family="'Inter', sans-serif" font-weight="800" font-size="13" fill="#F5F4F0" letter-spacing="1">NASHVILLE GENERAL HOSPITAL</text>
  <text x="56" y="73" font-family="'Inter', sans-serif" font-size="11" fill="#D87535">18,235 SQ FT • 20-YR NDL JM TPO</text>
</svg>"""

with open(os.path.join(images_dir, "project-nashville-general.svg"), "w", encoding="utf-8") as f:
    f.write(proj1_svg)

# Project 2: Frost Bank Plaza (Corpus Christi, TX) - Soprema PMMA Waterproofing
proj2_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Frost Bank Plaza Commercial Roofing Project">
  <defs>
    <linearGradient id="p2Sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0E1720"/><stop offset="100%" stop-color="#1C2F42"/>
    </linearGradient>
    <linearGradient id="pmmaCoat" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2D3A47"/><stop offset="100%" stop-color="#1D2630"/>
    </linearGradient>
  </defs>
  <rect width="800" height="500" fill="url(#p2Sky)"/>
  <!-- High Rise Tower Outline -->
  <rect x="220" y="100" width="360" height="400" fill="#131920" stroke="#253240" stroke-width="2"/>
  <!-- Glazing Grid -->
  <g stroke="#1F2A38" stroke-width="1" opacity="0.7">
    <line x1="220" y1="160" x2="580" y2="160"/><line x1="220" y1="220" x2="580" y2="220"/>
    <line x1="220" y1="280" x2="580" y2="280"/><line x1="220" y1="340" x2="580" y2="340"/>
    <line x1="220" y1="400" x2="580" y2="400"/>
    <line x1="310" y1="100" x2="310" y2="500"/><line x1="400" y1="100" x2="400" y2="500"/>
    <line x1="490" y1="100" x2="490" y2="500"/>
  </g>
  <!-- Plaza Rooftop Terrace / Soprema PMMA Waterproofed Deck -->
  <polygon points="160,350 640,350 690,460 110,460" fill="url(#pmmaCoat)" stroke="#3E4F61" stroke-width="2"/>
  <!-- Liquid applied fleece reinforcement lines -->
  <g stroke="#D87535" stroke-width="1.2" opacity="0.6">
    <line x1="240" y1="365" x2="200" y2="450"/>
    <line x1="360" y1="365" x2="340" y2="450"/>
    <line x1="480" y1="365" x2="480" y2="450"/>
    <line x1="580" y1="365" x2="600" y2="450"/>
  </g>
  <!-- Coping restoration and lightning rods -->
  <polygon points="160,345 640,345 640,352 160,352" fill="#D87535"/>
  <line x1="180" y1="345" x2="180" y2="315" stroke="#F5F4F0" stroke-width="2"/>
  <line x1="620" y1="345" x2="620" y2="315" stroke="#F5F4F0" stroke-width="2"/>
  <!-- Badge -->
  <rect x="40" y="30" width="310" height="58" fill="#0A0C0E" rx="4" stroke="#D87535" stroke-width="1.5"/>
  <text x="56" y="54" font-family="'Inter', sans-serif" font-weight="800" font-size="13" fill="#F5F4F0" letter-spacing="1">FROST BANK PLAZA</text>
  <text x="56" y="73" font-family="'Inter', sans-serif" font-size="11" fill="#D87535">22,000 SQ FT • SOPREMA PMMA • CORPUS CHRISTI</text>
</svg>"""

with open(os.path.join(images_dir, "project-frost-bank.svg"), "w", encoding="utf-8") as f:
    f.write(proj2_svg)

# Project 3: Krusteaz Manufacturing Facility (205,869 sq ft)
proj3_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Krusteaz Manufacturing Facility Commercial Roofing Project">
  <defs>
    <linearGradient id="p3Sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#111317"/><stop offset="100%" stop-color="#222730"/>
    </linearGradient>
    <linearGradient id="megaRoof" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#EEF2F6"/><stop offset="100%" stop-color="#BAC4CE"/>
    </linearGradient>
  </defs>
  <rect width="800" height="500" fill="url(#p3Sky)"/>
  <!-- Industrial Plant Structure -->
  <polygon points="30,260 770,260 770,480 30,480" fill="#181C22" stroke="#2E3540" stroke-width="2"/>
  <!-- Massive Warehouse Roof in Deep Perspective -->
  <polygon points="30,260 770,260 680,100 120,100" fill="url(#megaRoof)" stroke="#8FA0B2" stroke-width="2"/>
  <!-- Grid of repetitive industrial vents and skylights -->
  <g fill="#404A58" opacity="0.7">
    <rect x="200" y="130" width="25" height="15" rx="2"/><rect x="300" y="130" width="25" height="15" rx="2"/>
    <rect x="400" y="130" width="25" height="15" rx="2"/><rect x="500" y="130" width="25" height="15" rx="2"/>
    <rect x="600" y="130" width="25" height="15" rx="2"/>
    <rect x="180" y="180" width="35" height="20" rx="2"/><rect x="300" y="180" width="35" height="20" rx="2"/>
    <rect x="420" y="180" width="35" height="20" rx="2"/><rect x="540" y="180" width="35" height="20" rx="2"/>
  </g>
  <!-- Longitude Seams across 205k sqft -->
  <g stroke="#7F8E9E" stroke-width="1.5">
    <line x1="250" y1="100" x2="200" y2="260"/>
    <line x1="400" y1="100" x2="400" y2="260" stroke="#D87535" stroke-width="2"/>
    <line x1="550" y1="100" x2="600" y2="260"/>
  </g>
  <!-- Badge -->
  <rect x="40" y="30" width="340" height="58" fill="#0A0C0E" rx="4" stroke="#D87535" stroke-width="1.5"/>
  <text x="56" y="54" font-family="'Inter', sans-serif" font-weight="800" font-size="13" fill="#F5F4F0" letter-spacing="1">KRUSTEAZ MANUFACTURING</text>
  <text x="56" y="73" font-family="'Inter', sans-serif" font-size="11" fill="#D87535">205,869 SQ FT • JM TPO SYSTEM • HOPKINSVILLE, KY</text>
</svg>"""

with open(os.path.join(images_dir, "project-krusteaz.svg"), "w", encoding="utf-8") as f:
    f.write(proj3_svg)

# Project 4: Rapha Center (Manchester, TN) - 10,500 sq ft 0.60 mil TPO
proj4_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Rapha Center Commercial Roofing Project">
  <defs>
    <linearGradient id="p4Sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#101419"/><stop offset="100%" stop-color="#242C36"/>
    </linearGradient>
    <linearGradient id="p4Roof" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E5EAEF"/><stop offset="100%" stop-color="#C2CCD6"/>
    </linearGradient>
  </defs>
  <rect width="800" height="500" fill="url(#p4Sky)"/>
  <!-- Commercial Center Facade -->
  <rect x="80" y="240" width="640" height="240" fill="#1A2027" stroke="#2E3846" stroke-width="2"/>
  <!-- TPO Roof with mechanical fastener layout -->
  <polygon points="60,240 740,240 680,120 120,120" fill="url(#p4Roof)" stroke="#7D8D9E" stroke-width="2"/>
  <!-- Fastener plates simulation -->
  <g fill="#D87535" opacity="0.7">
    <circle cx="200" cy="180" r="3"/><circle cx="280" cy="180" r="3"/><circle cx="360" cy="180" r="3"/>
    <circle cx="440" cy="180" r="3"/><circle cx="520" cy="180" r="3"/><circle cx="600" cy="180" r="3"/>
  </g>
  <!-- Seam Lines -->
  <line x1="260" y1="120" x2="240" y2="240" stroke="#8594A3" stroke-width="1.8"/>
  <line x1="420" y1="120" x2="420" y2="240" stroke="#8594A3" stroke-width="1.8"/>
  <line x1="580" y1="120" x2="600" y2="240" stroke="#8594A3" stroke-width="1.8"/>
  <!-- Badge -->
  <rect x="40" y="30" width="310" height="58" fill="#0A0C0E" rx="4" stroke="#D87535" stroke-width="1.5"/>
  <text x="56" y="54" font-family="'Inter', sans-serif" font-weight="800" font-size="13" fill="#F5F4F0" letter-spacing="1">RAPHA CENTER</text>
  <text x="56" y="73" font-family="'Inter', sans-serif" font-size="11" fill="#D87535">10,500 SQ FT • 60-MIL TPO • MANCHESTER, TN</text>
</svg>"""

with open(os.path.join(images_dir, "project-rapha-center.svg"), "w", encoding="utf-8") as f:
    f.write(proj4_svg)

# Project 5: Malone Plaza (Rochester, NY) - 100,000 sq ft EPDM system
proj5_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Malone Plaza Commercial Roofing Project">
  <defs>
    <linearGradient id="p5Sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0E1217"/><stop offset="100%" stop-color="#1F2631"/>
    </linearGradient>
    <linearGradient id="epdmDeck" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#23272C"/><stop offset="100%" stop-color="#14171A"/>
    </linearGradient>
  </defs>
  <rect width="800" height="500" fill="url(#p5Sky)"/>
  <!-- Retail Commercial Center Structure -->
  <polygon points="50,230 750,230 750,470 50,470" fill="#181D24" stroke="#2B3441" stroke-width="2"/>
  <!-- Black EPDM Rubber Membrane Surface -->
  <polygon points="50,230 750,230 670,90 130,90" fill="url(#epdmDeck)" stroke="#394452" stroke-width="2"/>
  <!-- Ballast to Mechanically Attached Transition Line -->
  <line x1="420" y1="90" x2="420" y2="230" stroke="#D87535" stroke-width="2.5" stroke-dasharray="6,4"/>
  <text x="210" y="160" font-family="'Inter', monospace" font-size="10" fill="#A7ADB2" letter-spacing="1">60,000 SQ FT BALLAST SWAP-OUT</text>
  <text x="460" y="160" font-family="'Inter', monospace" font-size="10" fill="#D87535" letter-spacing="1">40,000 SQ FT NEW MECH. ATTACHED EPDM</text>
  <!-- Badge -->
  <rect x="40" y="30" width="340" height="58" fill="#0A0C0E" rx="4" stroke="#D87535" stroke-width="1.5"/>
  <text x="56" y="54" font-family="'Inter', sans-serif" font-weight="800" font-size="13" fill="#F5F4F0" letter-spacing="1">MALONE PLAZA</text>
  <text x="56" y="73" font-family="'Inter', sans-serif" font-size="11" fill="#D87535">100,000 SQ FT • EPDM R-40 SYSTEM • COMPLETED &lt;60 DAYS</text>
</svg>"""

with open(os.path.join(images_dir, "project-malone-plaza.svg"), "w", encoding="utf-8") as f:
    f.write(proj5_svg)

# 5. MANUFACTURER & SAFETY CERTIFICATIONS
# Johns Manville, GAF, Carlisle, Soprema, OSHA, NRCA
cert_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 240" fill="none" role="img" aria-label="Manufacturer and Safety Accreditations">
  <!-- Johns Manville Peak Advantage -->
  <g transform="translate(40, 40)">
    <rect width="160" height="150" rx="8" fill="#14181D" stroke="#29303A" stroke-width="1.5"/>
    <text x="80" y="45" font-family="'Inter', sans-serif" font-weight="900" font-size="20" fill="#F5F4F0" text-anchor="middle">JM</text>
    <text x="80" y="70" font-family="'Inter', sans-serif" font-weight="700" font-size="12" fill="#D87535" text-anchor="middle">PEAK ADVANTAGE</text>
    <text x="80" y="90" font-family="'Inter', sans-serif" font-size="10" fill="#A7ADB2" text-anchor="middle">Master Contractor</text>
    <line x1="40" y1="105" x2="120" y2="105" stroke="#29303A"/>
    <text x="80" y="125" font-family="'Inter', sans-serif" font-weight="600" font-size="9" fill="#F5F4F0" text-anchor="middle">20-30 YR NDL</text>
  </g>

  <!-- GAF Master Select -->
  <g transform="translate(240, 40)">
    <rect width="160" height="150" rx="8" fill="#14181D" stroke="#29303A" stroke-width="1.5"/>
    <text x="80" y="45" font-family="'Inter', sans-serif" font-weight="900" font-size="20" fill="#F5F4F0" text-anchor="middle">GAF</text>
    <text x="80" y="70" font-family="'Inter', sans-serif" font-weight="700" font-size="12" fill="#D87535" text-anchor="middle">MASTER SELECT</text>
    <text x="80" y="90" font-family="'Inter', sans-serif" font-size="10" fill="#A7ADB2" text-anchor="middle">Commercial Contractor</text>
    <line x1="40" y1="105" x2="120" y2="105" stroke="#29303A"/>
    <text x="80" y="125" font-family="'Inter', sans-serif" font-weight="600" font-size="9" fill="#F5F4F0" text-anchor="middle">TOP 1% IN USA</text>
  </g>

  <!-- Carlisle SynTec ESP -->
  <g transform="translate(440, 40)">
    <rect width="160" height="150" rx="8" fill="#14181D" stroke="#29303A" stroke-width="1.5"/>
    <text x="80" y="45" font-family="'Inter', sans-serif" font-weight="900" font-size="20" fill="#F5F4F0" text-anchor="middle">CARLISLE</text>
    <text x="80" y="70" font-family="'Inter', sans-serif" font-weight="700" font-size="12" fill="#D87535" text-anchor="middle">ESP APPLICATOR</text>
    <text x="80" y="90" font-family="'Inter', sans-serif" font-size="10" fill="#A7ADB2" text-anchor="middle">Excellence in Single-Ply</text>
    <line x1="40" y1="105" x2="120" y2="105" stroke="#29303A"/>
    <text x="80" y="125" font-family="'Inter', sans-serif" font-weight="600" font-size="9" fill="#F5F4F0" text-anchor="middle">CERTIFIED INSTALLER</text>
  </g>

  <!-- Soprema Certified -->
  <g transform="translate(640, 40)">
    <rect width="160" height="150" rx="8" fill="#14181D" stroke="#29303A" stroke-width="1.5"/>
    <text x="80" y="45" font-family="'Inter', sans-serif" font-weight="900" font-size="18" fill="#F5F4F0" text-anchor="middle">SOPREMA</text>
    <text x="80" y="70" font-family="'Inter', sans-serif" font-weight="700" font-size="12" fill="#D87535" text-anchor="middle">PMMA CERTIFIED</text>
    <text x="80" y="90" font-family="'Inter', sans-serif" font-size="10" fill="#A7ADB2" text-anchor="middle">Liquid Waterproofing</text>
    <line x1="40" y1="105" x2="120" y2="105" stroke="#29303A"/>
    <text x="80" y="125" font-family="'Inter', sans-serif" font-weight="600" font-size="9" fill="#F5F4F0" text-anchor="middle">PLAZA SPECIALIST</text>
  </g>

  <!-- OSHA 30 & Zero Incident -->
  <g transform="translate(840, 40)">
    <rect width="160" height="150" rx="8" fill="#14181D" stroke="#29303A" stroke-width="1.5"/>
    <text x="80" y="45" font-family="'Inter', sans-serif" font-weight="900" font-size="20" fill="#10B981" text-anchor="middle">OSHA 30</text>
    <text x="80" y="70" font-family="'Inter', sans-serif" font-weight="700" font-size="12" fill="#F5F4F0" text-anchor="middle">ZERO-INCIDENT</text>
    <text x="80" y="90" font-family="'Inter', sans-serif" font-size="10" fill="#A7ADB2" text-anchor="middle">Safety Culture</text>
    <line x1="40" y1="105" x2="120" y2="105" stroke="#29303A"/>
    <text x="80" y="125" font-family="'Inter', sans-serif" font-weight="600" font-size="9" fill="#10B981" text-anchor="middle">100% COMPLIANT</text>
  </g>

  <!-- NRCA Member -->
  <g transform="translate(1040, 40)">
    <rect width="140" height="150" rx="8" fill="#14181D" stroke="#29303A" stroke-width="1.5"/>
    <text x="70" y="45" font-family="'Inter', sans-serif" font-weight="900" font-size="20" fill="#F5F4F0" text-anchor="middle">NRCA</text>
    <text x="70" y="70" font-family="'Inter', sans-serif" font-weight="700" font-size="11" fill="#D87535" text-anchor="middle">MEMBER</text>
    <text x="70" y="90" font-family="'Inter', sans-serif" font-size="9.5" fill="#A7ADB2" text-anchor="middle">National Association</text>
    <line x1="30" y1="105" x2="110" y2="105" stroke="#29303A"/>
    <text x="70" y="125" font-family="'Inter', sans-serif" font-weight="600" font-size="9" fill="#F5F4F0" text-anchor="middle">COMMERCIAL</text>
  </g>
</svg>"""

with open(os.path.join(images_dir, "certifications.svg"), "w", encoding="utf-8") as f:
    f.write(cert_svg)

# 6. Service System Diagrams (TPO, EPDM, PVC System Cross Sections)
tpo_diag = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 360" fill="none" role="img" aria-label="TPO Single-Ply Roofing System Cross Section Layer Diagram">
  <rect width="600" height="360" rx="12" fill="#12161A" stroke="#29313A" stroke-width="1.5"/>
  <text x="30" y="40" font-family="'Inter', sans-serif" font-weight="800" font-size="16" fill="#F5F4F0">TPO ROOFING SYSTEM // MULTI-LAYER ASSEMBLY</text>
  <text x="30" y="60" font-family="'Inter', monospace" font-size="11" fill="#D87535">THERMOPLASTIC POLYOLEFIN CLASS 1 RATED</text>
  
  <!-- Layer 1: Reflective TPO Membrane (Top) -->
  <rect x="30" y="90" width="540" height="28" fill="#E2E7EC" stroke="#A7ADB2" stroke-width="1.5" rx="3"/>
  <text x="45" y="108" font-family="'Inter', sans-serif" font-weight="700" font-size="11" fill="#111315">1. 60-MIL OR 80-MIL WHITE TPO MEMBRANE (HEAT-WELDED SEAMS)</text>
  
  <!-- Layer 2: High Density Cover Board -->
  <rect x="30" y="124" width="540" height="24" fill="#697480" rx="3"/>
  <text x="45" y="140" font-family="'Inter', sans-serif" font-weight="600" font-size="10" fill="#F5F4F0">2. HIGH-DENSITY GYPSUM COVER BOARD (HAIL &amp; PUNCTURE RESISTANT)</text>

  <!-- Layer 3: Polyisocyanurate Insulation (R-30+) -->
  <rect x="30" y="154" width="540" height="60" fill="#2E3742" stroke="#414D5C" rx="3"/>
  <text x="45" y="180" font-family="'Inter', sans-serif" font-weight="700" font-size="11" fill="#F5F4F0">3. TAPERED POLYISO INSULATION LAYERS (STAGGERED JOINTS)</text>
  <text x="45" y="198" font-family="'Inter', monospace" font-size="10" fill="#D87535">CONTINUOUS R-VALUE: R-30.0 TO R-35.0 // ASHRAE 90.1 COMPLIANT</text>

  <!-- Layer 4: Vapor Retarder / Air Barrier -->
  <rect x="30" y="220" width="540" height="18" fill="#D87535" opacity="0.85" rx="2"/>
  <text x="45" y="233" font-family="'Inter', sans-serif" font-weight="700" font-size="9" fill="#F5F4F0">4. SELF-ADHERING VAPOR BARRIER // HUMIDITY DEFENSE</text>

  <!-- Layer 5: Heavy Gauge Steel or Concrete Structural Deck -->
  <rect x="30" y="244" width="540" height="38" fill="#1F252D" stroke="#37414E" rx="3"/>
  <!-- Corrugation pattern -->
  <path d="M 40 265 L 70 265 L 85 278 L 115 278 L 130 265 L 160 265 L 175 278 L 205 278 L 220 265 L 250 265 L 265 278 L 295 278 L 310 265 L 340 265 L 355 278 L 385 278 L 400 265 L 430 265 L 445 278 L 475 278 L 490 265 L 520 265 L 535 278 L 560 278" stroke="#525E6E" stroke-width="2" fill="none"/>
  <text x="45" y="260" font-family="'Inter', sans-serif" font-weight="600" font-size="10" fill="#A7ADB2">5. STRUCTURAL STEEL ROOF DECK (22-GAUGE TYPE B)</text>

  <!-- Mechanical Fasteners Graphic -->
  <line x1="280" y1="90" x2="280" y2="265" stroke="#F5F4F0" stroke-width="1.5" stroke-dasharray="4,3"/>
  <circle cx="280" cy="90" r="4" fill="#D87535"/>

  <!-- Legend Bottom -->
  <text x="30" y="320" font-family="'Inter', monospace" font-size="10" fill="#A7ADB2">SPECIFICATION: ASTM D6878 // UL CLASS A FIRE RATING // FM 1-90 APPROVED</text>
</svg>"""

with open(os.path.join(images_dir, "tpo-system-diagram.svg"), "w", encoding="utf-8") as f:
    f.write(tpo_diag)

print("Generated core SVG visuals successfully!")
