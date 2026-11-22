"""
Generate Southeast Map SVG and additional service diagrams
"""
import os

images_dir = os.path.join("assets", "images")

# 1. SOUTHEAST INTERACTIVE MAP SVG
# Shows US Southeastern states with Goodlettsville HQ marked with pulsing beacon,
# verified states styled with distinct fills, interactive data attributes, and regional coordinates.
map_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 680" fill="none" class="taltek-service-map" role="img" aria-label="TALTEK 15-State Southeastern Commercial Roofing Coverage Map">
  <defs>
    <linearGradient id="licensedStateGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2C3540"/>
      <stop offset="100%" stop-color="#1E252D"/>
    </linearGradient>
    <linearGradient id="primaryHqGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#D87535"/>
      <stop offset="100%" stop-color="#9E4D1B"/>
    </linearGradient>
    <filter id="glowEffect" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Background Radar / Grid Map Texture -->
  <rect width="1000" height="680" fill="#0C0E11" rx="8"/>
  <g stroke="#1A2129" stroke-width="0.8" opacity="0.6">
    <line x1="0" y1="100" x2="1000" y2="100"/>
    <line x1="0" y1="200" x2="1000" y2="200"/>
    <line x1="0" y1="300" x2="1000" y2="300"/>
    <line x1="0" y1="400" x2="1000" y2="400"/>
    <line x1="0" y1="500" x2="1000" y2="500"/>
    <line x1="0" y1="600" x2="1000" y2="600"/>
    <line x1="200" y1="0" x2="200" y2="680"/>
    <line x1="400" y1="0" x2="400" y2="680"/>
    <line x1="600" y1="0" x2="600" y2="680"/>
    <line x1="800" y1="0" x2="800" y2="680"/>
  </g>

  <!-- Map Title and Coordinates Legend -->
  <g font-family="'Inter', sans-serif" transform="translate(40, 45)">
    <text font-weight="900" font-size="16" fill="#F5F4F0" letter-spacing="1">SOUTHEASTERN REGIONAL OPERATIONS</text>
    <text y="24" font-family="'Inter', monospace" font-size="11" fill="#D87535">15 STATES OPERATIONAL • 7 DIRECTLY LICENSED HUBS</text>
  </g>

  <!-- Interactive States Group -->
  <g class="states-layer" stroke="#3A4654" stroke-width="1.5">

    <!-- TENNESSEE (HQ State) -->
    <path id="state-tn" class="state-path state-hq" data-state="Tennessee" data-status="Headquarters &amp; Primary Hub" data-license="Fully Licensed &amp; Insured" data-projects="5,200+ Projects Completed"
      d="M 370 270 L 610 235 L 630 250 L 590 285 L 340 310 L 330 275 Z"
      fill="#28323D" />

    <!-- ALABAMA (Verified Licensed) -->
    <path id="state-al" class="state-path state-licensed" data-state="Alabama" data-status="Verified Licensed State" data-license="Licensed Commercial Contractor" data-projects="840+ Projects"
      d="M 400 310 L 485 300 L 500 440 L 440 450 L 440 430 L 410 430 Z"
      fill="url(#licensedStateGrad)" />

    <!-- MISSISSIPPI (Verified Licensed) -->
    <path id="state-ms" class="state-path state-licensed" data-state="Mississippi" data-status="Verified Licensed State" data-license="Commercial Roofing License" data-projects="620+ Projects"
      d="M 340 310 L 400 310 L 410 430 L 380 435 L 360 415 L 325 390 Z"
      fill="url(#licensedStateGrad)" />

    <!-- LOUISIANA (Verified Licensed) -->
    <path id="state-la" class="state-path state-licensed" data-state="Louisiana" data-status="Verified Licensed State" data-license="State Licensed Commercial Contractor" data-projects="510+ Projects"
      d="M 280 390 L 345 390 L 340 430 L 390 440 L 390 470 L 340 470 L 300 450 Z"
      fill="url(#licensedStateGrad)" />

    <!-- NORTH CAROLINA (Verified Licensed) -->
    <path id="state-nc" class="state-path state-licensed" data-state="North Carolina" data-status="Verified Licensed State" data-license="General Commercial Roofing Contractor" data-projects="920+ Projects"
      d="M 590 240 L 760 210 L 810 245 L 750 280 L 620 275 Z"
      fill="url(#licensedStateGrad)" />

    <!-- SOUTH CAROLINA (Verified Licensed) -->
    <path id="state-sc" class="state-path state-licensed" data-state="South Carolina" data-status="Verified Licensed State" data-license="Commercial Specialty Roofing License" data-projects="710+ Projects"
      d="M 590 285 L 680 275 L 750 280 L 700 350 L 610 330 Z"
      fill="url(#licensedStateGrad)" />

    <!-- VIRGINIA (Verified Licensed) -->
    <path id="state-va" class="state-path state-licensed" data-state="Virginia" data-status="Verified Licensed State" data-license="Class A Commercial Contractor" data-projects="830+ Projects"
      d="M 570 195 L 730 150 L 775 190 L 740 215 L 590 235 Z"
      fill="url(#licensedStateGrad)" />

    <!-- GEORGIA (Operational Southeast) -->
    <path id="state-ga" class="state-path state-operational" data-state="Georgia" data-status="Operational Regional Territory" data-license="Commercial Support Coverage" data-projects="890+ Projects"
      d="M 485 300 L 590 285 L 610 330 L 630 420 L 520 440 L 500 370 Z"
      fill="#1A2027" />

    <!-- FLORIDA (Operational Southeast) -->
    <path id="state-fl" class="state-path state-operational" data-state="Florida" data-status="Operational Regional Territory" data-license="Commercial Emergency &amp; Logistics" data-projects="650+ Projects"
      d="M 440 450 L 630 420 L 680 480 L 690 560 L 630 610 L 610 520 L 520 450 Z"
      fill="#1A2027" />

    <!-- KENTUCKY (Operational Southeast) -->
    <path id="state-ky" class="state-path state-operational" data-state="Kentucky" data-status="Operational Regional Territory (Krusteaz Facility)" data-license="Commercial Deployment Ready" data-projects="440+ Projects"
      d="M 370 220 L 540 180 L 570 200 L 510 240 L 370 270 Z"
      fill="#1A2027" />

    <!-- ARKANSAS (Operational Southeast) -->
    <path id="state-ar" class="state-path state-operational" data-state="Arkansas" data-status="Operational Regional Territory" data-license="Commercial Deployment Ready" data-projects="260+ Projects"
      d="M 270 300 L 340 300 L 325 390 L 260 380 Z"
      fill="#1A2027" />
  </g>

  <!-- HEADQUARTERS PIN (Goodlettsville, TN) -->
  <g class="hq-marker" transform="translate(420, 275)" filter="url(#glowEffect)">
    <!-- Pulse wave rings -->
    <circle cx="0" cy="0" r="18" fill="none" stroke="#D87535" stroke-width="1.5" opacity="0.4">
      <animate attributeName="r" values="8;24;36" dur="3s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;0.3;0" dur="3s" repeatCount="indefinite"/>
    </circle>
    <!-- Solid core beacon -->
    <circle cx="0" cy="0" r="7" fill="#D87535" stroke="#FFFFFF" stroke-width="2"/>
    <text x="14" y="4" font-family="'Inter', sans-serif" font-weight="900" font-size="12" fill="#F5F4F0">HQ: GOODLETTSVILLE, TN</text>
    <text x="14" y="18" font-family="'Inter', monospace" font-size="9.5" fill="#D87535">1214 S. DICKERSON RD</text>
  </g>

  <!-- Regional Hub Markers -->
  <!-- Birmingham, AL -->
  <circle cx="455" cy="365" r="4" fill="#A7ADB2" stroke="#14181D" stroke-width="1.5"/>
  <text x="465" y="370" font-family="'Inter', sans-serif" font-size="9" fill="#A7ADB2">Birmingham Hub</text>

  <!-- Charlotte, NC -->
  <circle cx="680" cy="270" r="4" fill="#A7ADB2" stroke="#14181D" stroke-width="1.5"/>
  <text x="690" y="274" font-family="'Inter', sans-serif" font-size="9" fill="#A7ADB2">Charlotte Hub</text>

  <!-- Richmond, VA -->
  <circle cx="720" cy="190" r="4" fill="#A7ADB2" stroke="#14181D" stroke-width="1.5"/>
  <text x="730" y="194" font-family="'Inter', sans-serif" font-size="9" fill="#A7ADB2">Richmond Hub</text>

  <!-- New Orleans, LA -->
  <circle cx="370" cy="455" r="4" fill="#A7ADB2" stroke="#14181D" stroke-width="1.5"/>
  <text x="320" y="480" font-family="'Inter', sans-serif" font-size="9" fill="#A7ADB2">Gulf Operations</text>

  <!-- Interactive State Tooltip Container (Dynamic JS Updates) -->
  <g id="map-tooltip" transform="translate(40, 480)" style="pointer-events: none;">
    <rect width="320" height="150" rx="6" fill="#14181E" stroke="#D87535" stroke-width="1.5" opacity="0.95"/>
    <text id="tt-state-name" x="20" y="32" font-family="'Inter', sans-serif" font-weight="900" font-size="15" fill="#F5F4F0">TENNESSEE (HEADQUARTERS)</text>
    <text id="tt-status" x="20" y="58" font-family="'Inter', sans-serif" font-weight="700" font-size="11" fill="#D87535">OPERATIONAL HQ &amp; DISPATCH</text>
    <text id="tt-license" x="20" y="80" font-family="'Inter', sans-serif" font-size="10.5" fill="#A7ADB2">License: Fully Licensed, Bonded &amp; Insured</text>
    <text id="tt-projects" x="20" y="100" font-family="'Inter', sans-serif" font-size="10.5" fill="#A7ADB2">Completed: 5,200+ Roof Installations</text>
    <text x="20" y="128" font-family="'Inter', monospace" font-size="9" fill="#F5F4F0" letter-spacing="1">CLICK STATE OR CALL (615) 448-6349</text>
  </g>

  <!-- Legend Bottom Right -->
  <g transform="translate(680, 530)">
    <rect width="280" height="110" rx="6" fill="#111519" stroke="#252D37" stroke-width="1"/>
    <circle cx="20" cy="25" r="5" fill="#D87535"/>
    <text x="35" y="29" font-family="'Inter', sans-serif" font-size="10" fill="#F5F4F0" font-weight="600">TALTEK Corporate HQ (Goodlettsville)</text>

    <rect x="15" y="45" width="12" height="10" fill="url(#licensedStateGrad)" stroke="#3A4654"/>
    <text x="35" y="54" font-family="'Inter', sans-serif" font-size="10" fill="#A7ADB2">Verified State License (TN, AL, LA, MS, NC, SC, VA)</text>

    <rect x="15" y="70" width="12" height="10" fill="#1A2027" stroke="#3A4654"/>
    <text x="35" y="79" font-family="'Inter', sans-serif" font-size="10" fill="#757D85">Southeastern Operations Network</text>
  </g>
</svg>"""

with open(os.path.join(images_dir, "southeast-map.svg"), "w", encoding="utf-8") as f:
    f.write(map_svg)

# 2. EPDM ROOFING SYSTEM DIAGRAM
epdm_diag = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 360" fill="none" role="img" aria-label="EPDM Rubber Roofing System Assembly Diagram">
  <rect width="600" height="360" rx="12" fill="#12161A" stroke="#29313A" stroke-width="1.5"/>
  <text x="30" y="40" font-family="'Inter', sans-serif" font-weight="800" font-size="16" fill="#F5F4F0">EPDM RUBBER MEMBRANE // CROSS-SECTION</text>
  <text x="30" y="60" font-family="'Inter', monospace" font-size="11" fill="#D87535">SYNTHETIC ETHYLENE PROPYLENE DIENE MONOMER</text>
  
  <!-- Layer 1: EPDM Membrane -->
  <rect x="30" y="90" width="540" height="26" fill="#1F2328" stroke="#48515C" stroke-width="1.5" rx="3"/>
  <text x="45" y="107" font-family="'Inter', sans-serif" font-weight="700" font-size="11" fill="#F5F4F0">1. 60-MIL NON-REINFORCED OR 75-MIL REINFORCED EPDM RUBBER</text>
  
  <!-- Layer 2: Primer & Factory Seam Tape -->
  <rect x="30" y="122" width="540" height="18" fill="#D87535" opacity="0.9" rx="2"/>
  <text x="45" y="135" font-family="'Inter', sans-serif" font-weight="700" font-size="9" fill="#F5F4F0">2. SECURETAPE FACTORY-APPLIED DOUBLE SEAM WATERPROOF BOND</text>

  <!-- Layer 3: High Density Polyiso Cover Board -->
  <rect x="30" y="146" width="540" height="30" fill="#4B5663" rx="3"/>
  <text x="45" y="165" font-family="'Inter', sans-serif" font-weight="600" font-size="10" fill="#F5F4F0">3. 1/2" HIGH-DENSITY ISO COVER BOARD (PUNCTURE SHIELD)</text>

  <!-- Layer 4: Base Insulation -->
  <rect x="30" y="182" width="540" height="55" fill="#2E3742" stroke="#414D5C" rx="3"/>
  <text x="45" y="208" font-family="'Inter', sans-serif" font-weight="700" font-size="11" fill="#F5F4F0">4. TWO LAYERS TAPERED POLYISOCYANURATE (THERMAL BARRIER)</text>
  <text x="45" y="226" font-family="'Inter', monospace" font-size="10" fill="#D87535">THERMAL EXPANSION FLEXIBILITY: 300% ELONGATION CAPABILITY</text>

  <!-- Layer 5: Concrete/Metal Deck -->
  <rect x="30" y="243" width="540" height="40" fill="#1A2027" stroke="#37414E" rx="3"/>
  <text x="45" y="268" font-family="'Inter', sans-serif" font-weight="600" font-size="10" fill="#A7ADB2">5. STRUCTURAL ROOF SUBSTRATE (CONCRETE SLAB OR STEEL)</text>

  <!-- Legend Bottom -->
  <text x="30" y="320" font-family="'Inter', monospace" font-size="10" fill="#A7ADB2">SPECIFICATION: ASTM D4637 // 30+ YEAR DESIGN LIFE // THERMAL CYCLING RESISTANT</text>
</svg>"""

with open(os.path.join(images_dir, "epdm-system-diagram.svg"), "w", encoding="utf-8") as f:
    f.write(epdm_diag)

# 3. PVC ROOFING SYSTEM DIAGRAM
pvc_diag = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 360" fill="none" role="img" aria-label="PVC Commercial Roofing System Chemical Resistance Diagram">
  <rect width="600" height="360" rx="12" fill="#12161A" stroke="#29313A" stroke-width="1.5"/>
  <text x="30" y="40" font-family="'Inter', sans-serif" font-weight="800" font-size="16" fill="#F5F4F0">PVC ROOFING MEMBRANE // CHEMICAL DEFENSE</text>
  <text x="30" y="60" font-family="'Inter', monospace" font-size="11" fill="#D87535">POLYVINYL CHLORIDE RESTAURANT &amp; INDUSTRIAL SPEC</text>
  
  <!-- Layer 1: PVC Chemical Resistant Cap -->
  <rect x="30" y="90" width="540" height="28" fill="#F0F4F8" stroke="#8E9AA7" stroke-width="1.5" rx="3"/>
  <text x="45" y="108" font-family="'Inter', sans-serif" font-weight="700" font-size="11" fill="#111315">1. 60 OR 80-MIL PVC MEMBRANE WITH ELVALOY KEE MOLECULAR PLASTICIZER</text>
  
  <!-- Layer 2: Chemical & Grease Barrier -->
  <rect x="30" y="124" width="540" height="24" fill="#10B981" opacity="0.85" rx="3"/>
  <text x="45" y="140" font-family="'Inter', sans-serif" font-weight="700" font-size="9.5" fill="#FFFFFF">2. ANIMAL FATS, JET FUEL &amp; INDUSTRIAL CHEMICAL BARRIER</text>

  <!-- Layer 3: Gypsum Cover Board -->
  <rect x="30" y="154" width="540" height="26" fill="#5A6673" rx="3"/>
  <text x="45" y="171" font-family="'Inter', sans-serif" font-weight="600" font-size="10" fill="#F5F4F0">3. DENSDECK PRIME WATER-RESISTANT FIBERGLASS MAT BOARD</text>

  <!-- Layer 4: Polyiso Insulation -->
  <rect x="30" y="186" width="540" height="52" fill="#2E3742" stroke="#414D5C" rx="3"/>
  <text x="45" y="210" font-family="'Inter', sans-serif" font-weight="700" font-size="11" fill="#F5F4F0">4. CONTINUOUS CLOSED-CELL POLYISOCYANURATE BOARD</text>
  <text x="45" y="226" font-family="'Inter', monospace" font-size="10" fill="#D87535">FIRE RETARDANT UL CLASS A // ASTM D4434 TYPE III</text>

  <!-- Layer 5: Deck -->
  <rect x="30" y="244" width="540" height="38" fill="#1F252D" stroke="#37414E" rx="3"/>
  <text x="45" y="268" font-family="'Inter', sans-serif" font-weight="600" font-size="10" fill="#A7ADB2">5. STRUCTURAL PRECAST CONCRETE OR FLUTED STEEL DECK</text>

  <!-- Legend Bottom -->
  <text x="30" y="320" font-family="'Inter', monospace" font-size="10" fill="#A7ADB2">ROOFTOP GREASE EXHAUST RESISTANCE // MANUFACTURING &amp; PROCESSING FACILITIES</text>
</svg>"""

with open(os.path.join(images_dir, "pvc-system-diagram.svg"), "w", encoding="utf-8") as f:
    f.write(pvc_diag)

# 4. THERMAL INFRARED DRONE SCAN DIAGRAM
scan_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 360" fill="none" role="img" aria-label="Thermal Infrared Commercial Roof Moisture Scan Inspection Diagram">
  <defs>
    <radialGradient id="heatPocket" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#EF4444" stop-opacity="0.9"/>
      <stop offset="45%" stop-color="#F59E0B" stop-opacity="0.7"/>
      <stop offset="85%" stop-color="#10B981" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#1E293B" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="600" height="360" rx="12" fill="#0A0E13" stroke="#25303D" stroke-width="1.5"/>
  <!-- Thermal Palette Background -->
  <rect x="20" y="20" width="560" height="280" fill="#131C26" rx="6"/>
  <!-- Grid Matrix -->
  <g stroke="#1F2E3E" stroke-width="1">
    <line x1="20" y1="80" x2="580" y2="80"/><line x1="20" y1="140" x2="580" y2="140"/><line x1="20" y1="200" x2="580" y2="200"/><line x1="20" y1="260" x2="580" y2="260"/>
    <line x1="120" y1="20" x2="120" y2="300"/><line x1="220" y1="20" x2="220" y2="300"/><line x1="320" y1="20" x2="320" y2="300"/><line x1="420" y1="20" x2="420" y2="300"/><line x1="520" y1="20" x2="520" y2="300"/>
  </g>
  <!-- Moisture Heat Signatures -->
  <ellipse cx="260" cy="130" rx="90" ry="55" fill="url(#heatPocket)"/>
  <ellipse cx="440" cy="210" rx="65" ry="40" fill="url(#heatPocket)"/>

  <!-- Drone Flight Reticle -->
  <g stroke="#D87535" stroke-width="1.5">
    <circle cx="260" cy="130" r="30" fill="none" stroke-dasharray="6,4"/>
    <line x1="260" y1="90" x2="260" y2="105"/>
    <line x1="260" y1="155" x2="260" y2="170"/>
    <line x1="220" y1="130" x2="235" y2="130"/>
    <line x1="285" y1="130" x2="300" y2="130"/>
  </g>
  <rect x="210" y="60" width="100" height="22" fill="#0A0C0E" rx="3"/>
  <text x="260" y="75" font-family="'Inter', monospace" font-size="9" fill="#EF4444" font-weight="700" text-anchor="middle">MOISTURE +8.4°F</text>

  <!-- Telemetry Overlay -->
  <g font-family="'Inter', monospace" font-size="10" fill="#A7ADB2">
    <text x="35" y="45" fill="#D87535" font-weight="700">FLIR INFRARED RADIOMETRIC SCAN</text>
    <text x="35" y="62">ALTITUDE: 120 FT AGL • AMBIENT: 64°F</text>
    <text x="35" y="285" fill="#10B981">DRY ZONE: 94.2%</text>
    <text x="160" y="285" fill="#EF4444">MOISTURE INTRUSION: 5.8%</text>
  </g>

  <!-- Legend Bottom -->
  <text x="30" y="335" font-family="'Inter', sans-serif" font-size="11" fill="#F5F4F0">NON-DESTRUCTIVE CORE SAMPLE VERIFICATION // PRE-PURCHASE DUE DILIGENCE</text>
</svg>"""

with open(os.path.join(images_dir, "commercial-drone-scan.svg"), "w", encoding="utf-8") as f:
    f.write(scan_svg)

print("Generated Southeast map & service diagrams successfully!")
