"""
TALTEK COMMERCIAL ROOFING - SERVICE PAGES GENERATOR
Generates services.html and all 12 individual service pages (Feature 11).
"""

from build_site import render_page

def build_services_overview():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Enterprise Solutions</span>
          <h1 class="section-title">Commercial &amp; Industrial Roofing Services</h1>
          <p class="section-desc">
            Engineered single-ply membranes, capital replacements, preventive maintenance, and 24/7 disaster response across 15 Southeastern states. Certified Master Contractor with Johns Manville, GAF, Carlisle, and Soprema.
          </p>
        </div>

        <div class="grid grid-cols-3" style="gap: var(--space-8); margin-top: var(--space-10);">
          <!-- 1. Commercial Installation -->
          <div class="industrial-card">
            <div class="card-top-tag">SERVICE 01 // NEW CONSTRUCTION</div>
            <h2 class="card-title"><a href="services/commercial-roofing.html">Commercial Roof Installation</a></h2>
            <p class="card-desc">
              Precision single-ply TPO, EPDM, and PVC roof installations engineered for new commercial developments, distribution warehouses, retail complexes, and office buildings.
            </p>
            <ul style="font-size: 13px; color: var(--text-secondary); margin-bottom: 20px; line-height: 1.8;">
              <li>• ASTM D6878 single-ply membranes</li>
              <li>• Tapered polyisocyanurate insulation</li>
              <li>• 20 to 30-Year NDL manufacturer warranties</li>
            </ul>
            <a href="services/commercial-roofing.html" class="btn btn-outline btn-sm">Explore Installation &rarr;</a>
          </div>

          <!-- 2. Industrial Roofing -->
          <div class="industrial-card">
            <div class="card-top-tag">SERVICE 02 // MANUFACTURING</div>
            <h2 class="card-title"><a href="services/industrial-roofing.html">Industrial Roofing Systems</a></h2>
            <p class="card-desc">
              Heavy-duty roofing solutions for manufacturing plants, chemical processing facilities, cold storage warehouses, and aerospace infrastructure requiring zero operational downtime.
            </p>
            <ul style="font-size: 13px; color: var(--text-secondary); margin-bottom: 20px; line-height: 1.8;">
              <li>• High-load vibration isolation curbs</li>
              <li>• Chemical &amp; grease resistant PVC formulations</li>
              <li>• National account project execution</li>
            </ul>
            <a href="services/industrial-roofing.html" class="btn btn-outline btn-sm">Explore Industrial &rarr;</a>
          </div>

          <!-- 3. Roof Replacement -->
          <div class="industrial-card">
            <div class="card-top-tag">SERVICE 03 // RE-ROOFING</div>
            <h2 class="card-title"><a href="services/roof-replacement.html">Commercial Roof Replacement</a></h2>
            <p class="card-desc">
              Full tear-off and re-cover engineering for deteriorating ballast, built-up, and metal roofs. Sloped tapered insulation design eliminating chronic ponding water.
            </p>
            <ul style="font-size: 13px; color: var(--text-secondary); margin-bottom: 20px; line-height: 1.8;">
              <li>• Full insulation moisture inspection</li>
              <li>• Flute-fill metal retrofit solutions</li>
              <li>• Fast-track completion timelines</li>
            </ul>
            <a href="services/roof-replacement.html" class="btn btn-outline btn-sm">Explore Replacement &rarr;</a>
          </div>

          <!-- 4. Roof Repair -->
          <div class="industrial-card">
            <div class="card-top-tag">SERVICE 04 // LEAK MITIGATION</div>
            <h2 class="card-title"><a href="services/roof-repair.html">Commercial Roof Repair</a></h2>
            <p class="card-desc">
              Diagnostic leak detection and precision seam re-welding. Thermal infrared imaging to identify hidden subsurface moisture before catastrophic deck decay occurs.
            </p>
            <ul style="font-size: 13px; color: var(--text-secondary); margin-bottom: 20px; line-height: 1.8;">
              <li>• Hot-air robotic seam reinforcement</li>
              <li>• Perimeter flashing renewal &amp; termination bars</li>
              <li>• Documented photo repair reports</li>
            </ul>
            <a href="services/roof-repair.html" class="btn btn-outline btn-sm">Explore Repair &rarr;</a>
          </div>

          <!-- 5. Emergency Services -->
          <div class="industrial-card featured">
            <div class="card-top-tag" style="color: var(--copper);">SERVICE 05 // 24/7 RAPID DISPATCH</div>
            <h2 class="card-title"><a href="services/emergency-services.html">Emergency Roofing Services</a></h2>
            <p class="card-desc">
              Round-the-clock emergency mobilization for active storm penetrations, hail impacts, tornado wind blow-offs, and sudden membrane tears across Tennessee and neighboring states.
            </p>
            <ul style="font-size: 13px; color: var(--text-secondary); margin-bottom: 20px; line-height: 1.8;">
              <li>• Immediate 2-4 hour crew dispatch</li>
              <li>• Temporary tarping &amp; mechanical stabilization</li>
              <li>• Direct commercial insurance coordination</li>
            </ul>
            <a href="services/emergency-services.html" class="btn btn-primary btn-sm">Call Emergency Hotline &rarr;</a>
          </div>

          <!-- 6. Preventative Maintenance -->
          <div class="industrial-card">
            <div class="card-top-tag">SERVICE 06 // ASSET CARE</div>
            <h2 class="card-title"><a href="services/preventative-maintenance.html">Preventative Maintenance</a></h2>
            <p class="card-desc">
              Scheduled asset longevity programs. Biannual physical inspections, roof drain clearing, expansion joint servicing, and documented compliance with warranty upkeep rules.
            </p>
            <ul style="font-size: 13px; color: var(--text-secondary); margin-bottom: 20px; line-height: 1.8;">
              <li>• Biannual photographic condition audits</li>
              <li>• Debris clearing &amp; scupper desilting</li>
              <li>• Extended manufacturer warranty protection</li>
            </ul>
            <a href="services/preventative-maintenance.html" class="btn btn-outline btn-sm">Explore Maintenance &rarr;</a>
          </div>

          <!-- 7. TPO Roofing -->
          <div class="industrial-card">
            <div class="card-top-tag">SERVICE 07 // COOL ROOF</div>
            <h2 class="card-title"><a href="services/tpo-roofing.html">TPO Roofing Systems</a></h2>
            <p class="card-desc">
              Energy Star rated Thermoplastic Polyolefin single-ply systems. High solar albedo cooling, puncture resistance, and seamless hot-air welded bonds.
            </p>
            <ul style="font-size: 13px; color: var(--text-secondary); margin-bottom: 20px; line-height: 1.8;">
              <li>• 60-mil and 80-mil JM &amp; GAF systems</li>
              <li>• Class A fire ratings &amp; FM 1-90 wind uplift</li>
              <li>• Significant HVAC cooling cost reduction</li>
            </ul>
            <a href="services/tpo-roofing.html" class="btn btn-outline btn-sm">Explore TPO &rarr;</a>
          </div>

          <!-- 8. EPDM Rubber -->
          <div class="industrial-card">
            <div class="card-top-tag">SERVICE 08 // SYNTHETIC RUBBER</div>
            <h2 class="card-title"><a href="services/epdm-roofing.html">EPDM Rubber Roofing</a></h2>
            <p class="card-desc">
              Time-tested ethylene propylene diene monomer rubber membranes offering superior 300% thermal expansion flexibility and resistance to extreme freeze-thaw cycles.
            </p>
            <ul style="font-size: 13px; color: var(--text-secondary); margin-bottom: 20px; line-height: 1.8;">
              <li>• Ballasted and mechanically fastened systems</li>
              <li>• 30+ year real-world performance record</li>
              <li>• Ideal for logistics and distribution parks</li>
            </ul>
            <a href="services/epdm-roofing.html" class="btn btn-outline btn-sm">Explore EPDM &rarr;</a>
          </div>

          <!-- 9. PVC Roofing -->
          <div class="industrial-card">
            <div class="card-top-tag">SERVICE 09 // CHEMICAL DEFENSE</div>
            <h2 class="card-title"><a href="services/pvc-roofing.html">PVC Chemical Resistant</a></h2>
            <p class="card-desc">
              Elvaloy KEE fortified polyvinyl chloride membranes designed specifically for food processing plants, restaurant rooftops, and facilities with grease or acidic emissions.
            </p>
            <ul style="font-size: 13px; color: var(--text-secondary); margin-bottom: 20px; line-height: 1.8;">
              <li>• Animal fat &amp; hydrocarbon grease proof</li>
              <li>• Hot-air molecularly fused seams</li>
              <li>• Highest fire retardant ratings in single-ply</li>
            </ul>
            <a href="services/pvc-roofing.html" class="btn btn-outline btn-sm">Explore PVC &rarr;</a>
          </div>

          <!-- 10. Storm Protection -->
          <div class="industrial-card">
            <div class="card-top-tag">SERVICE 10 // HARDENING</div>
            <h2 class="card-title"><a href="services/storm-protection.html">Storm &amp; Wind Protection</a></h2>
            <p class="card-desc">
              High-wind uplift reinforcement, impact-resistant DensDeck gypsum coverboards, engineered coping caps, and FM Global rated fastening layouts for hurricane and tornado zones.
            </p>
            <ul style="font-size: 13px; color: var(--text-secondary); margin-bottom: 20px; line-height: 1.8;">
              <li>• UL 2218 Class 4 hail resistance</li>
              <li>• Up to 150 MPH wind design pressures</li>
              <li>• Heavy-gauge perimeter coping metal</li>
            </ul>
            <a href="services/storm-protection.html" class="btn btn-outline btn-sm">Explore Storm Protection &rarr;</a>
          </div>

          <!-- 11. Roof Assessment -->
          <div class="industrial-card">
            <div class="card-top-tag">SERVICE 11 // DUE DILIGENCE</div>
            <h2 class="card-title"><a href="services/roof-assessment.html">Commercial Roof Assessment</a></h2>
            <p class="card-desc">
              Pre-purchase real estate due diligence, non-destructive FLIR radiometric drone thermal imaging, physical core sampling, and 10-year capital expenditure forecasts.
            </p>
            <ul style="font-size: 13px; color: var(--text-secondary); margin-bottom: 20px; line-height: 1.8;">
              <li>• Non-destructive thermal moisture scans</li>
              <li>• Structural deck integrity laboratory tests</li>
              <li>• Comprehensive architectural reports</li>
            </ul>
            <a href="services/roof-assessment.html" class="btn btn-outline btn-sm">Explore Assessment &rarr;</a>
          </div>

          <!-- 12. Gutter & Drainage -->
          <div class="industrial-card">
            <div class="card-top-tag">SERVICE 12 // WATER RUNOFF</div>
            <h2 class="card-title"><a href="services/gutter-services.html">Commercial Gutters &amp; Drainage</a></h2>
            <p class="card-desc">
              Heavy-gauge seamless box gutters, custom industrial downspouts, scupper boxes, collector heads, and interior roof drain bowl installations engineered for 100-year storm rainfalls.
            </p>
            <ul style="font-size: 13px; color: var(--text-secondary); margin-bottom: 20px; line-height: 1.8;">
              <li>• 24-gauge Galvalume &amp; aluminum fabrication</li>
              <li>• High-volume overflow scupper design</li>
              <li>• Siphonic and gravity drainage upgrades</li>
            </ul>
            <a href="services/gutter-services.html" class="btn btn-outline btn-sm">Explore Drainage &rarr;</a>
          </div>
        </div>
      </div>
    </section>

    <!-- CALL TO ACTION BANNER -->
    <section class="section-tight bg-elevated" style="border-top: 1px solid var(--border-medium);">
      <div class="container text-center">
        <h2 style="font-size: 28px; margin-bottom: 12px;">Need a Tailored Commercial Roofing Proposal?</h2>
        <p style="color: var(--text-secondary); max-width: 650px; margin: 0 auto 24px;">
          TALTEK engineers will evaluate your building blueprints, perform on-site core sampling, and engineer an optimized single-ply solution backed by a 20-30 year NDL warranty.
        </p>
        <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
          <a href="request-inspection.html" class="btn btn-primary">Schedule On-Site Roof Inspection</a>
          <a href="estimator.html" class="btn btn-secondary">Use Interactive Estimator</a>
        </div>
      </div>
    </section>
    """

    render_page(
        "services.html",
        "Commercial Roofing Services | Industrial Single-Ply Systems — TALTEK",
        "Comprehensive commercial and industrial roofing services: TPO, EPDM, PVC, capital roof replacement, 24/7 emergency dispatch, and preventative maintenance across 15 Southeastern states.",
        "services",
        content,
        path_depth=0
    )

def build_individual_services():
    services_data = [
        {
            "slug": "commercial-roofing",
            "title": "Commercial Roof Installation",
            "eyebrow": "ENGINEERED NEW CONSTRUCTION & RETROFIT",
            "desc": "Precision commercial flat roof installations engineered for business continuity, maximum energy efficiency, and 20 to 30-year No Dollar Limit manufacturer protection.",
            "hero_img": "assets/images/hero-rooftop.svg",
            "diagram": "assets/images/tpo-system-diagram.svg",
            "body": """
              <h2>Commercial Flat Roofing Built to Perform</h2>
              <p>
                At TALTEK Commercial Roofing, commercial roof installation is approached as a structural engineering discipline. Headquartered in Goodlettsville, Tennessee, we deploy certified installation crews across 15 Southeastern states, specializing in single-ply thermoplastic and thermoset membrane assemblies.
              </p>
              <p>
                A commercial roof represents one of the largest capital investments in any facility. Substandard installation or improper thermal fastening causes premature seam failure, saturated insulation, and catastrophic interior inventory damage. We eliminate these risks through Johns Manville Peak Advantage and GAF Master Select master contractor protocols, ensuring every square foot meets rigorous FM Global wind uplift standards and ASTM technical guidelines.
              </p>
              <h3>Integrated Multi-Layer Roofing System Assembly</h3>
              <p>
                Our commercial installations are built with multi-layer resilience: heavy-gauge steel or concrete structural decking, a continuous self-adhering air/vapor retarder, staggered layers of high-R closed-cell polyisocyanurate insulation, impact-resistant DensDeck gypsum coverboards, and factory-certified single-ply membranes.
              </p>
            """,
            "specs": [
              ("Membrane Options", "60-mil / 80-mil TPO, 60-mil EPDM, 60-mil PVC"),
              ("Insulation", "Continuous Tapered Polyisocyanurate (R-30+ ASHRAE 90.1)"),
              ("Fastening Method", "Fully Adhered or Mechanically Fastened w/ Stress Plates"),
              ("Manufacturer Warranties", "20-Year, 25-Year, and 30-Year No Dollar Limit (NDL)"),
              ("Contractor Warranty", "TALTEK 2-Year Comprehensive Workmanship Guarantee"),
              ("Fire & Uplift Ratings", "UL Class A Fire Rated • FM 1-90 to FM 1-150 Wind Approved")
            ]
        },
        {
            "slug": "industrial-roofing",
            "title": "Industrial Roofing Systems",
            "eyebrow": "MANUFACTURING, WAREHOUSING & LOGISTICS",
            "desc": "Heavy-duty industrial roofing engineered for large-scale distribution centers, chemical processing plants, and manufacturing facilities across the Southeastern USA.",
            "hero_img": "assets/images/project-krusteaz.svg",
            "diagram": "assets/images/tpo-system-diagram.svg",
            "body": """
              <h2>Industrial-Scale Roofing Infrastructure</h2>
              <p>
                Industrial facilities present extreme structural demands: continuous heavy vibration from rooftop HVAC and exhaust units, chemical discharge, massive roof square footage exceeding 200,000 sq. ft., and the non-negotiable requirement of uninterrupted manufacturing operations below.
              </p>
              <p>
                TALTEK Commercial Roofing has documented proven success on massive industrial assets. At the Krusteaz Manufacturing Facility in Hopkinsville, Kentucky, our crews executed a complete 205,869 sq. ft. tear-off and replacement down to the steel deck with zero operational interruption to the active food production plant below.
              </p>
              <h3>Vibration-Isolated Curbs &amp; Expansion Detailing</h3>
              <p>
                Industrial installations require specialized perimeter flashing, curb isolation, and heavy-gauge coping metals designed to flex with industrial equipment vibrations without cracking welds or separating membrane adhesives.
              </p>
            """,
            "specs": [
              ("Facility Specializations", "Manufacturing Plants, Cold Storage, Distribution Hubs"),
              ("Scale Capability", "20,000 to 500,000+ Square Feet Single-Structure"),
              ("Operations Protocol", "Zero Internal Dust/Downtime Industrial Phasing"),
              ("NDL Warranties", "Johns Manville 20-Year Labor and Materials NDL"),
              ("Safety Certification", "OSHA 30-Hour Supervisor Oversight & Zero-Incident Protocols")
            ]
        },
        {
            "slug": "roof-replacement",
            "title": "Commercial Roof Replacement",
            "eyebrow": "COMPLETE TEAR-OFF & RE-ROOFING",
            "desc": "Turnkey commercial roof tear-off and replacement services eliminating saturated insulation, chronic ponding water, and recurring maintenance overhead.",
            "hero_img": "assets/images/after-tpo-roof.svg",
            "diagram": "assets/images/tpo-system-diagram.svg",
            "body": """
              <h2>Decisive Capital Investment Protection</h2>
              <p>
                When a commercial roof reaches the end of its useful design life, repeated localized patching becomes a financial drain. Saturated insulation compromises building thermal performance, escalating HVAC power demands while covertly rusting steel roof decking from the underside.
              </p>
              <p>
                TALTEK's roof replacement methodology begins with non-destructive FLIR infrared radiometric moisture scanning. By mapping exact saturation boundaries, we determine whether a complete deck tear-off or a code-compliant single-ply re-cover is the most cost-effective path.
              </p>
              <h3>Engineered Tapered Polyisocyanurate Slopes</h3>
              <p>
                Ponding water is the leading catalyst of premature commercial membrane failure. During replacement, our engineers calculate custom tapered insulation crickets (1/8\" to 1/4\" per foot slope), ensuring positive gravity drainage into internal drains and perimeter scuppers.
              </p>
            """,
            "specs": [
              ("Diagnostic Protocol", "FLIR Thermal Radiometric Drone Scan + Core Sampling"),
              ("Slope Engineering", "Custom Tapered Polyiso Drainage Crickets"),
              ("Deck Restoration", "Damaged 22-Gauge Fluted Steel Deck Replacement"),
              ("National Portfolio", "Projects Executed in TN, KY, NY, TX, AL, and Across SE"),
              ("Warranty", "20-Year NDL Labor and Materials Guarantee")
            ]
        },
        {
            "slug": "roof-repair",
            "title": "Commercial Roof Repair",
            "eyebrow": "SURGICAL LEAK REPAIR & PREVENTATIVE RESTORATION",
            "desc": "Precision commercial leak detection, seam re-welding, and perimeter flashing repair by certified single-ply master technicians.",
            "hero_img": "assets/images/before-damaged-roof.svg",
            "diagram": "assets/images/tpo-system-diagram.svg",
            "body": """
              <h2>Surgical Leak Detection &amp; Seam Welding</h2>
              <p>
                A roof leak rarely originates directly above where water drips inside the building. Water enters through a compromised perimeter coping joint, mechanical pipe curb, or unseated seam, traveling horizontally along steel deck flutes before penetrating into the tenant space.
              </p>
              <p>
                TALTEK's repair technicians are trained in forensic moisture tracing. We don't apply temporary caulk or generic tar that cracks within 90 days. We clean the existing membrane, probe seam integrity with specialized testing needles, and hot-air weld factory-certified membrane patches and target details.
              </p>
              <h3>Documented Commercial Repair Records</h3>
              <p>
                Every commercial repair is documented with high-resolution before, during, and after photography. Property managers receive a detailed technical report explaining the failure mechanism, work performed, and recommendations for warranty preservation.
              </p>
            """,
            "specs": [
              ("Diagnostic Method", "Electronic Moisture Meter & Seam Probe Auditing"),
              ("Repair Technology", "Robotic Hot-Air Welding & PMMA Liquid Flashing"),
              ("Documentation", "Full Photographic Commercial Closeout Report"),
              ("Response Time", "Standard Service within 24-48 Hours")
            ]
        },
        {
            "slug": "emergency-services",
            "title": "24/7 Emergency Roofing Services",
            "eyebrow": "RAPID STORM RESPONSE & DISASTER MITIGATION",
            "desc": "Immediate commercial emergency response dispatch for active water intrusions, tornado wind blow-offs, and severe storm damage across Tennessee and the Southeast.",
            "hero_img": "assets/images/hero-rooftop.svg",
            "diagram": "assets/images/tpo-system-diagram.svg",
            "body": """
              <h2>Round-the-Clock Commercial Emergency Dispatch</h2>
              <p>
                When severe weather strikes—whether hail punctures, high-wind membrane uplift, or structural HVAC curb displacement—every minute of water intrusion damages tenant inventories, delicate computer hardware, and structural building integrity.
              </p>
              <p>
                TALTEK maintains dedicated emergency crews on 24/7/365 standby. By calling our Goodlettsville dispatch center at <strong>+1 (615) 448-6349</strong>, facility managers secure rapid on-site mobilization across Middle Tennessee and regional Southeastern hubs.
              </p>
              <h3>Stabilization &amp; Insurance Coordination</h3>
              <p>
                Our priority on site is immediate weatherproofing: securing loose membranes, installing heavy-gauge weighted water-diverting tarps, and repairing ruptured flashings. We then assist property owners with photographic documentation and detailed forensic estimates formatted for commercial insurance carriers.
              </p>
            """,
            "specs": [
              ("Dispatch Hotline", "+1 (615) 448-6349 (24 Hours / 7 Days)"),
              ("Deployment Speed", "2 to 4 Hour On-Site Priority Window"),
              ("Service Territory", "Tennessee, Alabama, Mississippi, Louisiana, NC, SC, VA"),
              ("Capabilities", "Emergency Membrane Welds, Water Diversion, Deck Shoring")
            ]
        },
        {
            "slug": "preventative-maintenance",
            "title": "Preventative Maintenance",
            "eyebrow": "COMMERCIAL ASSET PRESERVATION PROGRAMS",
            "desc": "Scheduled commercial maintenance programs engineered to extend single-ply roof longevity, prevent unbudgeted capital expenditures, and uphold manufacturer warranty requirements.",
            "hero_img": "assets/images/after-tpo-roof.svg",
            "diagram": "assets/images/commercial-drone-scan.svg",
            "body": """
              <h2>Proactive Roof Asset Lifecycle Management</h2>
              <p>
                Major single-ply roofing manufacturers—including Johns Manville, GAF, and Carlisle—explicitly mandate regular maintenance inspections in their warranty terms. Neglecting annual drain clearing or failing to document foreign debris damage can void otherwise valuable 20-year No Dollar Limit policies.
              </p>
              <p>
                TALTEK's Preventative Maintenance Agreements provide commercial property managers and real estate investment trusts (REITs) with proactive asset care. Our certified inspectors conduct thorough spring and autumn audits, clearing drainage paths, resealing expansion joints, and repairing minor punctures before they turn into building-wide crises.
              </p>
              <h3>Capital Reserve Planning &amp; Drone Thermography</h3>
              <p>
                Our clients receive detailed digital portals featuring annual condition indexes, life expectancy projections, and 5-year capital expenditure forecasts, transforming unpredictable roof repairs into planned, budgeted investments.
              </p>
            """,
            "specs": [
              ("Inspection Cadence", "Semi-Annual (Spring & Fall Post-Storm Audits)"),
              ("Core Tasks", "Drain & Scupper Cleaning, Seam Probing, Flashing Inspection"),
              ("Deliverable", "Comprehensive Digital Condition Index & Photo Portal"),
              ("Warranty Benefit", "Guaranteed Compliance with Manufacturer NDL Mandates")
            ]
        },
        {
            "slug": "tpo-roofing",
            "title": "TPO Roofing Systems",
            "eyebrow": "HIGH-ALBEDO SINGLE-PLY MEMBRANE",
            "desc": "Energy Star compliant white Thermoplastic Polyolefin (TPO) roofing with hot-air welded seams, superior solar reflectance, and manufacturer NDL warranties up to 30 years.",
            "hero_img": "assets/images/project-nashville-general.svg",
            "diagram": "assets/images/tpo-system-diagram.svg",
            "body": """
              <h2>The Industry Benchmark in Cool Commercial Roofing</h2>
              <p>
                Thermoplastic Polyolefin (TPO) is the fastest-growing commercial single-ply roofing system in the United States, and TALTEK's core specialty since our founding in 2009. Combining the weather-resistance of EPDM with the heat-welded seam integrity of PVC, TPO provides unmatched commercial value.
              </p>
              <p>
                Our white TPO installations reflect over 78% of incoming solar radiation (Solar Reflectance Index SRI 95+), dramatically reducing rooftop surface temperatures from 160&deg;F down to ambient levels. This lowers interior cooling loads on warehouse and office air conditioning systems by up to 25%.
              </p>
              <h3>Robotic Heat-Welded Molecular Bonds</h3>
              <p>
                Unlike glued or taped systems that weaken under prolonged ponding water, TPO seams are fused using robotic hot-air welders operating at over 1,000&deg;F. The molecular bond created is three times stronger than the membrane itself, guaranteeing watertight security across thousands of feet of field seams.
              </p>
            """,
            "specs": [
              ("Membrane Thickness", "60-Mil (Standard Commercial) or 80-Mil (Extreme Spec)"),
              ("Solar Reflectance", "SRI 95+ (ENERGY STAR &amp; CRRC Certified)"),
              ("Seam Fusion", "Robotic Hot-Air Molecular Weld (ASTM D6878)"),
              ("Manufacturer Partners", "Johns Manville Peak Advantage, GAF Commercial, Carlisle"),
              ("Warranty Options", "20-Year, 25-Year, and 30-Year NDL Labor and Materials")
            ]
        },
        {
            "slug": "epdm-roofing",
            "title": "EPDM Synthetic Rubber Roofing",
            "eyebrow": "ELASTOMERIC MEMBRANE FOR COLD & CYCLIC CLIMATES",
            "desc": "Durable Ethylene Propylene Diene Monomer synthetic rubber roofing offering 300% elongation, puncture resistance, and unmatched 30+ year real-world durability.",
            "hero_img": "assets/images/project-malone-plaza.svg",
            "diagram": "assets/images/epdm-system-diagram.svg",
            "body": """
              <h2>Unmatched Flexibility &amp; Freeze-Thaw Resilience</h2>
              <p>
                EPDM (Ethylene Propylene Diene Monomer) synthetic rubber has established a 50-year track record of commercial reliability. Highly valued for its remarkable 300% elasticity, EPDM effortlessly accommodates significant building thermal expansion and contraction without cracking or splitting.
              </p>
              <p>
                At Malone Plaza in Rochester, New York, TALTEK executed a complex 100,000 sq. ft. national account project consisting of a 60,000 sq. ft. ballast swap-out and 40,000 sq. ft. of mechanically attached EPDM with R-40 insulation, delivering the completed project in under 60 calendar days.
              </p>
              <h3>Ballasted, Mechanically Attached &amp; Fully Adhered</h3>
              <p>
                TALTEK installs EPDM systems in all configurations: mechanically fastened for wind uplift economy, fully adhered with low-VOC bonding adhesives, or ballasted with washed river stone for high thermal mass.
              </p>
            """,
            "specs": [
              ("Membrane Spec", "60-Mil Non-Reinforced or 75-Mil Reinforced Synthetic Rubber"),
              ("Elongation", "300% Elastic Recovery (Resists Severe Thermal Shock)"),
              ("Application Styles", "Fully Adhered, Mechanically Attached, Ballasted"),
              ("Warranties", "20-Year to 30-Year Manufacturer Warranties Available")
            ]
        },
        {
            "slug": "pvc-roofing",
            "title": "PVC Chemical Resistant Roofing",
            "eyebrow": "INDUSTRIAL CHEMICAL, ACID & GREASE DEFENSE",
            "desc": "Polyvinyl Chloride single-ply membrane engineered with Elvaloy KEE for restaurant exhaust hoods, manufacturing plants, and chemical processing facilities.",
            "hero_img": "assets/images/project-krusteaz.svg",
            "diagram": "assets/images/pvc-system-diagram.svg",
            "body": """
              <h2>Engineered for Harsh Industrial &amp; Grease Environments</h2>
              <p>
                Standard TPO or EPDM membranes break down rapidly when exposed to animal fats, cooking oils, jet fuel, or industrial chemical exhausts. The petroleum oils soften the membrane, leading to blistering, swelling, and eventual rupture.
              </p>
              <p>
                For facilities with rooftop grease exhausts—such as food processing facilities, restaurant centers, and industrial manufacturers—TALTEK installs high-performance PVC single-ply membranes fortified with DuPont Elvaloy KEE (Ketone Ethylene Ester) permanent plasticizers.
              </p>
              <h3>Permanent Fire &amp; Chemical Resistance</h3>
              <p>
                PVC membranes are inherently fire retardant and will self-extinguish when flames are removed, holding the highest Class A fire ratings available in commercial construction.
              </p>
            """,
            "specs": [
              ("Chemical Defense", "ASTM D4434 Type III & Type IV Resistant to Fats & Hydrocarbons"),
              ("Fire Rating", "UL Class A Flame Spread Self-Extinguishing"),
              ("Plasticizer Spec", "Elvaloy KEE Non-Migrating Solid Phase Formulations"),
              ("Seam Integrity", "Hot-Air Welded Molecular Bond")
            ]
        },
        {
            "slug": "storm-protection",
            "title": "Storm & High-Wind Protection",
            "eyebrow": "COMMERCIAL ROOF HARDENING & DISASTER PREVENTION",
            "desc": "Engineered high-wind uplift fastening, impact-resistant coverboards, and heavy-gauge perimeter metal systems designed to withstand Southeastern storms.",
            "hero_img": "assets/images/hero-rooftop.svg",
            "diagram": "assets/images/tpo-system-diagram.svg",
            "body": """
              <h2>Commercial Roof Hardening for Southeastern Storms</h2>
              <p>
                The Southeastern United States faces severe weather patterns: tornadic straight-line winds, heavy hailstorms, and tropical storm wind shear. Over 70% of storm-related commercial roof failures begin at the perimeter coping or corner eaves where wind vortex pressures are triple the field pressure.
              </p>
              <p>
                TALTEK hardens commercial roof assemblies using FM Global 1-90 and 1-120 wind uplift guidelines. We install high-density fiberglass mat DensDeck gypsum coverboards directly beneath the membrane, shielding polyiso insulation from hail impacts up to 2 inches in diameter.
              </p>
              <h3>Heavy-Gauge ANSI/SPRI ES-1 Perimeter Coping</h3>
              <p>
                We fabricate and install ANSI/SPRI ES-1 certified perimeter edge metals and coping caps in our dedicated sheet metal shop, ensuring the outer edges of your roof stay mechanically locked down during 120+ MPH wind events.
              </p>
            """,
            "specs": [
              ("Hail Resistance", "UL 2218 Class 4 Severe Impact Certified Assemblies"),
              ("Wind Design", "Calculated to ASCE 7-22 Standards (Up to 150 MPH)"),
              ("Edge Metal Spec", "ANSI/SPRI ES-1 Tested 24-Gauge Galvalume / Kynar 500"),
              ("Substrate Shield", "1/2\" High-Density Gypsum Coverboard Layer")
            ]
        },
        {
            "slug": "roof-assessment",
            "title": "Commercial Roof Assessment",
            "eyebrow": "INFRARED THERMOGRAPHY & PRE-PURCHASE DUE DILIGENCE",
            "desc": "Comprehensive non-destructive moisture scans, core sampling, and 10-year capital expenditure forecast reports for commercial property owners and REITs.",
            "hero_img": "assets/images/commercial-drone-scan.svg",
            "diagram": "assets/images/commercial-drone-scan.svg",
            "body": """
              <h2>Data-Driven Commercial Roof Due Diligence</h2>
              <p>
                Purchasing or managing a commercial property without an objective, certified roof assessment is a high-stakes gamble. Hidden water saturation inside insulation can silently destroy structural decking and cost hundreds of thousands in unbudgeted replacements.
              </p>
              <p>
                TALTEK's diagnostic assessment team utilizes FLIR radiometric thermal cameras mounted on FAA Part 107 licensed inspection drones. By scanning roofs immediately after sunset, our thermographers exploit the thermal mass differential: wet insulation retains solar heat longer than dry insulation, revealing exact subsurface moisture boundaries on our high-resolution heat map.
              </p>
              <h3>Physical Core Sampling &amp; Deck Testing</h3>
              <p>
                We corroborate infrared findings with physical core sampling, checking deck integrity, existing fastener pullout resistance, and vapor barrier conditions. Property owners receive a comprehensive bound engineering report with projected lifespan and budget plans.
              </p>
            """,
            "specs": [
              ("Drone Inspection", "FAA Part 107 Commercial Flight Operations w/ Radiometric FLIR"),
              ("Diagnostic Accuracy", "Pinpoints Sub-Membrane Saturation Down to the Square Foot"),
              ("Physical Verification", "Calibrated Core Extraction & Immediate Watertight Patch"),
              ("Deliverable", "Comprehensive Capital Budgeting & Executive Due Diligence Report")
            ]
        },
        {
            "slug": "gutter-services",
            "title": "Commercial Gutters & Drainage",
            "eyebrow": "HIGH-CAPACITY BOX GUTTERS & RUNOFF MANAGEMENT",
            "desc": "Heavy-gauge industrial box gutters, collector heads, and interior roof drain installations engineered for 100-year storm event water volumes.",
            "hero_img": "assets/images/hero-rooftop.svg",
            "diagram": "assets/images/tpo-system-diagram.svg",
            "body": """
              <h2>Engineered Commercial Drainage Systems</h2>
              <p>
                Even the most robust single-ply membrane will fail prematurely if water cannot rapidly escape the roof deck. A commercial flat roof spanning 50,000 square feet collects over 31,000 gallons of water during a single 1-inch rainfall event.
              </p>
              <p>
                TALTEK designs and installs complete commercial water management systems. In our metal fabrication shop, we custom-form heavy-gauge (24-gauge Galvalume or 0.040\" Kynar 500 aluminum) seamless box gutters up to 8 inches in width, engineered to handle intense cloudbursts without overflowing into wall cavities.
              </p>
              <h3>Internal Roof Drains &amp; Emergency Overflow Scuppers</h3>
              <p>
                For facilities with interior drainage, we install cast-iron drain bowls with integrated gravel stops and clamping rings, complemented by secondary emergency overflow scuppers that prevent catastrophic structural ponding if primary lines become obstructed.
              </p>
            """,
            "specs": [
              ("Gutter Profiles", "7-Inch & 8-Inch Commercial Box Gutters"),
              ("Material Gauges", "24-Gauge Galvalume, 22-Gauge Steel, or 0.040\" Aluminum"),
              ("Drainage Standard", "Engineered to 100-Year Rainfall Frequency Tables"),
              ("Components", "Scuppers, Downspouts, Cast-Iron Drains, Sump Pans")
            ]
        }
    ]

    service_photos = {
        "commercial-roofing": "assets/images/commercial-tpo-installation.jpg",
        "industrial-roofing": "assets/images/heavy-industrial-roof.jpg",
        "roof-replacement": "assets/images/commercial-construction-site.jpg",
        "roof-repair": "assets/images/commercial-contractors.jpg",
        "emergency-services": "assets/images/heavy-industrial-roof.jpg",
        "preventative-maintenance": "assets/images/roof-assessment-inspector.jpg",
        "tpo-roofing": "assets/images/commercial-tpo-installation.jpg",
        "epdm-roofing": "assets/images/heavy-industrial-roof.jpg",
        "pvc-roofing": "assets/images/heavy-industrial-roof.jpg",
        "storm-protection": "assets/images/commercial-construction-site.jpg",
        "roof-assessment": "assets/images/roof-assessment-inspector.jpg",
        "gutter-services": "assets/images/commercial-contractors.jpg"
    }

    for s in services_data:
        photo_url = service_photos.get(s["slug"], "assets/images/commercial-contractors.jpg")
        specs_rows = "".join([f"""
          <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--border-subtle); padding: 10px 0; font-size: 13px;">
            <strong style="color: var(--text-primary);">{k}:</strong>
            <span style="color: var(--text-secondary); text-align: right; max-width: 60%;">{v}</span>
          </div>
        """ for k, v in s["specs"]])

        content = f"""
        <!-- Hero Section -->
        <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
          <div class="container">
            <div style="max-width: 900px;">
              <span class="eyebrow">{s["eyebrow"]}</span>
              <h1 class="section-title" style="font-size: clamp(2.25rem, 5vw, 3.75rem);">{s["title"]}</h1>
              <p class="section-desc">{s["desc"]}</p>
              <div style="display: flex; gap: 16px; margin-top: 24px; flex-wrap: wrap;">
                <a href="../request-inspection.html" class="btn btn-primary">Schedule {s["title"]} Inspection</a>
                <a href="tel:+16154486349" class="btn btn-secondary">Call HQ: (615) 448-6349</a>
              </div>
            </div>
          </div>
        </section>

        <!-- Main Editorial Content & Technical Specs -->
        <section class="section bg-surface" style="border-top: 1px solid var(--border-subtle);">
          <div class="container">
            <div class="editorial-grid">
              <!-- Left: Editorial Text & Diagrams -->
              <div>
                <!-- Primary Service Field Photo -->
                <div style="margin-bottom: 32px; border: 1px solid var(--border-medium); border-radius: 8px; overflow: hidden; box-shadow: var(--shadow-md);">
                  <img src="../{photo_url}" alt="{s["title"]} Field Implementation" width="800" height="450" style="width: 100%; height: auto; max-height: 420px; object-fit: cover;">
                </div>

                <div class="editorial-body" style="color: var(--text-secondary); font-size: 15px; line-height: 1.8;">
                  {s["body"]}
                </div>

                <div style="margin: 40px 0;">
                  <h3 style="font-size: 20px; color: var(--text-primary); margin-bottom: 16px;">System Assembly Cross-Section</h3>
                  <img src="../{s["diagram"]}" alt="{s["title"]} Technical Cross-Section Diagram" width="600" height="360" style="width: 100%; height: auto; border: 1px solid var(--border-medium); border-radius: 6px;">
                </div>

                <!-- Case Study Reference -->
                <div style="background: var(--bg-card); border-left: 3px solid var(--copper); padding: 20px; border-radius: 4px; margin-top: 32px;">
                  <h4 style="font-size: 16px; color: var(--text-primary); margin-bottom: 8px;">Documented Field Proof</h4>
                  <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 12px;">
                    Review how TALTEK implemented these exact technical protocols on verified commercial facilities such as the <strong>Nashville General Hospital</strong> (18,235 sq ft TPO) and the <strong>Krusteaz Manufacturing Facility</strong> (205,869 sq ft industrial replacement).
                  </p>
                  <a href="../projects.html" class="btn btn-outline btn-sm">Explore Project Case Studies &rarr;</a>
                </div>
              </div>

              <!-- Right: Specifications Sidebar -->
              <div>
                <div style="background: var(--bg-card); border: 1px solid var(--border-medium); border-radius: 6px; padding: 24px; position: sticky; top: 100px;">
                  <div style="font-family: var(--font-mono); font-size: 11px; color: var(--copper); font-weight: 700; margin-bottom: 8px;">[ ENGINEERING SPECIFICATION ]</div>
                  <h3 style="font-size: 18px; color: var(--text-primary); margin-bottom: 16px;">Technical Standards</h3>
                  
                  <div style="display: flex; flex-direction: column;">
                    {specs_rows}
                  </div>

                  <div style="margin-top: 24px; padding-top: 20px; border-top: 1px solid var(--border-subtle);">
                    <a href="../request-inspection.html" class="btn btn-primary" style="width: 100%; margin-bottom: 10px;">Request Scope Inspection</a>
                    <a href="../estimator.html" class="btn btn-outline btn-sm" style="width: 100%;">Calculate Preliminary Cost</a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- FAQ Strip -->
        <section class="section bg-primary" style="border-top: 1px solid var(--border-subtle);">
          <div class="container" style="max-width: 880px;">
            <div class="section-header text-center">
              <span class="eyebrow">Technical Questions</span>
              <h2 class="section-title">Frequently Asked Questions</h2>
            </div>
            
            <div style="display: flex; flex-direction: column; gap: 16px;">
              <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 6px; padding: 20px;">
                <h4 style="font-size: 16px; color: var(--text-primary); margin-bottom: 8px;">How long does this installation or replacement typically take?</h4>
                <p style="font-size: 14px; color: var(--text-secondary);">Timeline depends on building square footage and deck complexity. A standard 25,000 sq ft single-ply replacement is typically executed in 10 to 14 working days, fully phased so tenant activities remain completely uninterrupted.</p>
              </div>
              <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 6px; padding: 20px;">
                <h4 style="font-size: 16px; color: var(--text-primary); margin-bottom: 8px;">What warranties are included with this system?</h4>
                <p style="font-size: 14px; color: var(--text-secondary);">TALTEK provides direct Manufacturer No Dollar Limit (NDL) Warranties for 20, 25, or 30 years backed by Johns Manville, GAF, Carlisle, or Soprema covering 100% of labor and materials, accompanied by TALTEK's 2-Year Contractor Workmanship Warranty.</p>
              </div>
              <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 6px; padding: 20px;">
                <h4 style="font-size: 16px; color: var(--text-primary); margin-bottom: 8px;">Do you handle commercial insurance claims for storm damage?</h4>
                <p style="font-size: 14px; color: var(--text-secondary);">Yes. Our staff provides complete forensic photographic damage packages, thermal scans, and Xactimate-compliant commercial line-item estimates to streamline commercial insurance carrier reviews.</p>
              </div>
            </div>
          </div>
        </section>
        """

        render_page(
            f"services/{s['slug']}.html",
            f"{s['title']} | TALTEK Commercial Roofing",
            s["desc"],
            f"services/{s['slug']}",
            content,
            path_depth=1
        )

if __name__ == "__main__":
    build_services_overview()
    build_individual_services()
    print("All service pages generated successfully!")
