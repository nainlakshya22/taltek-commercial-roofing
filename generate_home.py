"""
Generates index.html for TALTEK Commercial Roofing
"""
from build_site import render_page

def build_home():
    content = """
    <!-- FEATURE 01: CINEMATIC VIDEO HERO SECTION -->
    <section class="hero-section" aria-label="Commercial Roofing Excellence Hero">
      <div class="hero-media-wrapper">
        <picture>
          <source srcset="assets/images/hero-rooftop.webp" type="image/webp">
          <img src="assets/images/hero-rooftop.jpg" alt="Commercial Industrial Rooftop Drone Aerial Infrastructure" class="hero-poster-img" width="1920" height="1080">
        </picture>
        <div class="hero-overlay"></div>
        <div class="hero-grid-pattern"></div>
      </div>

      <div class="container" style="position: relative; z-index: 5;">
        <div class="hero-content reveal-init">
          <div class="hero-badge-tag">
            <span>[ SYSTEM ID: TALTEK-HQ-TN ]</span>
            <span>GOODLETTSVILLE, TN • 15 SOUTHEASTERN STATES</span>
          </div>

          <h1 class="hero-headline">
            PROTECTING YOUR BUSINESS.<br>
            <span class="text-accent">BUILT TO PERFORM.</span>
          </h1>

          <p class="hero-subtext">
            Advanced commercial and industrial roofing solutions engineered to protect your facility, daily operations, and long-term capital investment. Johns Manville Peak Advantage &amp; GAF Master Select certified installations backed by up to 30-year No Dollar Limit (NDL) warranties.
          </p>

          <div class="hero-cta-group">
            <a href="request-inspection.html" class="btn btn-primary btn-lg btn-shimmer">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
              Schedule a Roof Inspection
            </a>
            <a href="projects.html" class="btn btn-secondary btn-lg">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>
              Explore Our Projects
            </a>
            <a href="estimator.html" class="btn btn-outline btn-lg" style="border-color: rgba(255,255,255,0.2);">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="2" width="16" height="20" rx="2"></rect><line x1="8" y1="6" x2="16" y2="6"></line><line x1="16" y1="14" x2="16" y2="18"></line><path d="M16 10h.01"></path><path d="M12 10h.01"></path><path d="M8 10h.01"></path><path d="M12 14h.01"></path><path d="M8 14h.01"></path><path d="M12 18h.01"></path><path d="M8 18h.01"></path></svg>
              Interactive Estimator
            </a>
          </div>

          <!-- Verified Company Statistics Strip -->
          <div class="hero-stats-strip">
            <div class="hero-stat-item">
              <span class="hero-stat-val" data-counter-target="2009" data-counter-prefix="EST. ">2009</span>
              <span class="hero-stat-lbl">First Roof Installed</span>
            </div>
            <div class="hero-stat-item">
              <span class="hero-stat-val" data-counter-target="10000" data-counter-suffix="+">10,000+</span>
              <span class="hero-stat-lbl">Commercial Clients</span>
            </div>
            <div class="hero-stat-item">
              <span class="hero-stat-val" data-counter-target="4.8" data-counter-suffix=" &starf;">4.8 &starf;</span>
              <span class="hero-stat-lbl">Verified Google Rating</span>
            </div>
            <div class="hero-stat-item">
              <span class="hero-stat-val" data-counter-target="15" data-counter-suffix=" States">15 States</span>
              <span class="hero-stat-lbl">Southeastern Reach</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- MANUFACTURER ACCREDITATION BAR -->
    <section class="section-tight bg-surface" style="border-top: 1px solid var(--border-subtle); border-bottom: 1px solid var(--border-subtle);">
      <div class="container text-center">
        <p class="eyebrow" style="margin-bottom: var(--space-4);">Certified Commercial Master Contractors</p>
        <div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 32px; filter: grayscale(30%);">
          <img src="assets/images/certifications.svg" alt="Master Certifications: Johns Manville Peak Advantage, GAF Master Select, Carlisle ESP, Soprema PMMA, OSHA 30, NRCA" style="max-height: 90px; width: auto;">
        </div>
      </div>
    </section>

    <!-- FEATURE 03: INTERACTIVE BEFORE / AFTER SLIDER -->
    <section class="section bg-primary" aria-label="Before and After Roofing Comparison">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Engineering Transformation</span>
          <h2 class="section-title">See The TALTEK Standard In Action</h2>
          <p class="section-desc">
            Compare aging, blistered, saturated industrial substrates against a pristine, robotic heat-welded Johns Manville 60-Mil TPO system engineered for 30 years of watertight durability. Drag the slider below to inspect the transformation.
          </p>
        </div>

        <div class="before-after-container" role="region" aria-label="Interactive Before and After Membrane Slider">
          <!-- Before Layer (Bottom) -->
          <div class="ba-image-layer">
            <picture>
              <source srcset="assets/images/before-damaged-roof.webp" type="image/webp">
              <img src="assets/images/before-damaged-roof.jpg" alt="Aged damaged commercial roof before replacement" width="1200" height="750">
            </picture>
          </div>
          <!-- After Layer (Top, clipped dynamically) -->
          <div class="ba-image-layer ba-after-layer">
            <picture>
              <source srcset="assets/images/after-tpo-roof.webp" type="image/webp">
              <img src="assets/images/after-tpo-roof.jpg" alt="New Johns Manville 60-Mil TPO commercial roof after TALTEK installation" width="1200" height="750">
            </picture>
          </div>
          <!-- Draggable Splitter Handle -->
          <div class="ba-slider-handle">
            <div class="ba-handle-grip" aria-hidden="true">&harr;</div>
          </div>
          <!-- Badges -->
          <span class="ba-label ba-label-before">BEFORE: DETERIORATING MEMBRANE</span>
          <span class="ba-label ba-label-after">AFTER: JOHNS MANVILLE TPO SYSTEM</span>
        </div>

        <div style="text-align: center; margin-top: var(--space-6);">
          <p style="font-size: var(--text-xs); color: var(--text-muted); font-family: var(--font-mono);">
            KEYBOARD ACCESSIBLE: Click handle and use Left/Right arrow keys to slide.
          </p>
        </div>
      </div>
    </section>

    <!-- FEATURE 02: EMBEDDED ROOF ESTIMATOR TEASER -->
    <section class="section bg-surface" id="estimator-section" aria-label="Commercial Roof Estimator">
      <div class="container">
        <div class="section-header">
          <span class="eyebrow">Predictive Budgeting</span>
          <h2 class="section-title">Interactive Commercial Roof Estimator</h2>
          <p class="section-desc">
            Calculate preliminary commercial roof installation, replacement, or repair costs based on real industrial square footage, building types, and single-ply membrane specifications.
          </p>
        </div>

        <div class="estimator-container" id="roof-estimator-app">
          <!-- Estimator Inputs Form -->
          <div class="estimator-form-pane">
            <!-- 1. Building Type -->
            <div class="form-group">
              <label class="form-label">
                <span>1. Building Classification</span>
                <span class="form-hint">Select facility profile</span>
              </label>
              <div class="option-selector-grid">
                <button type="button" class="selector-tile building-tile active" data-value="warehouse">
                  <span class="tile-icon">&#9638;</span>
                  <span class="tile-label">Warehouse</span>
                </button>
                <button type="button" class="selector-tile building-tile" data-value="office">
                  <span class="tile-icon">&#9635;</span>
                  <span class="tile-label">Commercial Office</span>
                </button>
                <button type="button" class="selector-tile building-tile" data-value="retail">
                  <span class="tile-icon">&#9639;</span>
                  <span class="tile-label">Retail Plaza</span>
                </button>
                <button type="button" class="selector-tile building-tile" data-value="healthcare">
                  <span class="tile-icon">&#9640;</span>
                  <span class="tile-label">Healthcare/Hospital</span>
                </button>
              </div>
            </div>

            <!-- 2. Roof Area Slider -->
            <div class="form-group">
              <div class="form-label">
                <span>2. Approximate Roof Area</span>
                <span id="est-area-badge" style="color: var(--copper); font-family: var(--font-mono); font-weight: 700;">25,000 SQ FT</span>
              </div>
              <div class="slider-wrapper">
                <input type="range" id="est-roof-area" class="range-input" min="5000" max="250000" step="2500" value="25000" aria-label="Roof area in square feet">
                <div class="range-val-display">
                  <span>5,000 sq ft</span>
                  <span>125,000 sq ft</span>
                  <span>250,000+ sq ft</span>
                </div>
              </div>
              <div style="margin-top: 12px; display: flex; align-items: center; gap: 8px;">
                <label for="est-area-number" style="font-size: 13px; color: var(--text-secondary);">Or enter exact sq ft:</label>
                <input type="number" id="est-area-number" class="form-control" style="width: 140px; padding: 6px 12px; font-size: 14px;" value="25000" min="1000" max="500000">
              </div>
            </div>

            <!-- 3. Desired Roofing System -->
            <div class="form-group">
              <label class="form-label">3. Desired Single-Ply Roofing System</label>
              <div class="option-selector-grid">
                <button type="button" class="selector-tile system-tile active" data-value="jm-tpo-60">
                  <span class="tile-label">JM 60-Mil TPO</span>
                  <span style="font-size: 10px; color: var(--text-muted);">20-Yr NDL</span>
                </button>
                <button type="button" class="selector-tile system-tile" data-value="jm-tpo-80">
                  <span class="tile-label">JM 80-Mil TPO</span>
                  <span style="font-size: 10px; color: var(--text-muted);">30-Yr NDL Heavy</span>
                </button>
                <button type="button" class="selector-tile system-tile" data-value="carlisle-epdm">
                  <span class="tile-label">Carlisle EPDM</span>
                  <span style="font-size: 10px; color: var(--text-muted);">Synthetic Rubber</span>
                </button>
                <button type="button" class="selector-tile system-tile" data-value="pvc-chemical">
                  <span class="tile-label">PVC Chemical</span>
                  <span style="font-size: 10px; color: var(--text-muted);">Grease/Acid Proof</span>
                </button>
              </div>
            </div>

            <!-- 4. Project Scope (Repair vs Replacement) -->
            <div class="form-group">
              <label class="form-label">4. Scope Requirement</label>
              <div style="display: flex; gap: 12px;">
                <button type="button" class="selector-tile project-type-tile active" data-value="replacement" style="flex: 1;">
                  <span class="tile-label">Complete Replacement</span>
                  <span style="font-size: 10px; color: var(--text-muted);">Tear-off + New Insulation</span>
                </button>
                <button type="button" class="selector-tile project-type-tile" data-value="repair" style="flex: 1;">
                  <span class="tile-label">Targeted Repair / Restoration</span>
                  <span style="font-size: 10px; color: var(--text-muted);">Seam Seal + Flashing</span>
                </button>
              </div>
            </div>

            <!-- 5. Current Roof Condition -->
            <div class="form-group">
              <label class="form-label">5. Existing Roof Condition</label>
              <div class="option-selector-grid">
                <button type="button" class="selector-tile condition-tile" data-value="good">
                  <span class="tile-label">Good / Minor</span>
                </button>
                <button type="button" class="selector-tile condition-tile active" data-value="fair">
                  <span class="tile-label">Fair / Ponding</span>
                </button>
                <button type="button" class="selector-tile condition-tile" data-value="deteriorated">
                  <span class="tile-label">Active Leaks</span>
                </button>
                <button type="button" class="selector-tile condition-tile" data-value="severe">
                  <span class="tile-label">Severe Failure</span>
                </button>
              </div>
            </div>
          </div>

          <!-- Estimator Summary Live Calculation Pane -->
          <div class="estimator-summary-pane">
            <div>
              <div class="card-top-tag">[ BUDGETARY ESTIMATION ENGINE ]</div>
              <h3 style="font-size: 20px; color: var(--text-primary); margin-bottom: 12px;">Preliminary Project Range</h3>
              
              <div class="calc-result-box">
                <span style="font-size: 11px; color: var(--text-muted); text-transform: uppercase; font-family: var(--font-mono);">Estimated Total Project Investment</span>
                <div id="est-price-range" class="calc-price-range">$180,000 – $262,500</div>
                <div style="font-size: 11px; color: var(--copper); margin-top: 4px;">Includes membrane, tapered polyiso, fasteners &amp; NDL inspection fees</div>
              </div>

              <div class="calc-breakdown-list">
                <div class="breakdown-row">
                  <span>Calculated Area:</span>
                  <span id="est-summary-area" class="breakdown-val">25,000 sq. ft.</span>
                </div>
                <div class="breakdown-row">
                  <span>Specified System:</span>
                  <span id="est-summary-system" class="breakdown-val">Johns Manville 60-Mil TPO</span>
                </div>
                <div class="breakdown-row">
                  <span>Project Scope:</span>
                  <span id="est-summary-scope" class="breakdown-val">Full Tear-Off &amp; Replacement</span>
                </div>
                <div class="breakdown-row">
                  <span>Condition Assessment:</span>
                  <span id="est-summary-condition" class="breakdown-val">Fair</span>
                </div>
                <div class="breakdown-row">
                  <span>Manufacturer Warranty:</span>
                  <span class="breakdown-val" style="color: var(--status-success);">20-Year NDL Labor &amp; Materials</span>
                </div>
              </div>
            </div>

            <div>
              <a id="est-transfer-quote-btn" href="request-inspection.html?sqft=25000&system=jm-tpo-60" class="btn btn-primary" style="width: 100%; margin-bottom: 8px;">
                Lock In Core Sample Inspection
              </a>
              <div class="estimator-disclaimer-box">
                <strong>NON-BINDING PRELIMINARY ESTIMATE:</strong> Figures presented represent preliminary engineering estimates for budgeting purposes only and do NOT constitute a binding quotation. Precise commercial quotations require an on-site physical roof core sampling, thermal moisture scan, and deck evaluation by an authorized TALTEK roofing specialist.
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CORE COMMERCIAL SERVICES SECTION -->
    <section class="section bg-primary" aria-label="Commercial Roofing Services Overview">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Enterprise Capabilities</span>
          <h2 class="section-title">Engineered Commercial Roofing Systems</h2>
          <p class="section-desc">
            Industrial durability designed for high-wind, severe thermal expansion, and demanding environmental exposure across Tennessee and the Southeastern region.
          </p>
        </div>

        <div class="grid grid-cols-3">
          <!-- Card 1 -->
          <div class="industrial-card">
            <div class="card-top-tag">01 // SINGLE-PLY</div>
            <h3 class="card-title"><a href="services/tpo-roofing.html">TPO Roofing Systems</a></h3>
            <p class="card-desc">
              White thermoplastic polyolefin membrane installations featuring robotic hot-air welded seams. Exceptional solar reflectivity, Energy Star compliance, and high tensile puncture resistance.
            </p>
            <a href="services/tpo-roofing.html" class="btn btn-outline btn-sm">Explore TPO Systems &rarr;</a>
          </div>

          <!-- Card 2 -->
          <div class="industrial-card">
            <div class="card-top-tag">02 // INDUSTRIAL RUBBER</div>
            <h3 class="card-title"><a href="services/epdm-roofing.html">EPDM Synthetic Rubber</a></h3>
            <p class="card-desc">
              Unmatched 300% thermal elongation and cyclic weather resistance. Heavy-duty black or white EPDM membrane systems ideal for logistics facilities and distribution warehouses.
            </p>
            <a href="services/epdm-roofing.html" class="btn btn-outline btn-sm">Explore EPDM &rarr;</a>
          </div>

          <!-- Card 3 -->
          <div class="industrial-card">
            <div class="card-top-tag">03 // CHEMICAL DEFENSE</div>
            <h3 class="card-title"><a href="services/pvc-roofing.html">PVC Chemical Resistant</a></h3>
            <p class="card-desc">
              Elvaloy KEE molecularly plasticized PVC roofs engineered to withstand restaurant grease exhausts, jet fuels, industrial acids, and harsh manufacturing emissions.
            </p>
            <a href="services/pvc-roofing.html" class="btn btn-outline btn-sm">Explore PVC Systems &rarr;</a>
          </div>

          <!-- Card 4 -->
          <div class="industrial-card">
            <div class="card-top-tag">04 // CAPITAL RETROFIT</div>
            <h3 class="card-title"><a href="services/roof-replacement.html">Roof Replacement</a></h3>
            <p class="card-desc">
              Turnkey tear-off and re-cover solutions with zero interruption to your internal operations. Precision tapered polyiso insulation design for rapid slope-to-drain water management.
            </p>
            <a href="services/roof-replacement.html" class="btn btn-outline btn-sm">Replacement Services &rarr;</a>
          </div>

          <!-- Card 5 -->
          <div class="industrial-card featured">
            <div class="card-top-tag" style="color: var(--copper);">05 // RAPID RESPONSE</div>
            <h3 class="card-title"><a href="services/emergency-services.html">Emergency Dispatch 24/7</a></h3>
            <p class="card-desc">
              Dedicated emergency teams mobilized within hours for active storm penetrations, hail punctures, and perimeter flash failures across our licensed Southeastern territories.
            </p>
            <a href="services/emergency-services.html" class="btn btn-primary btn-sm">Emergency Protocols &rarr;</a>
          </div>

          <!-- Card 6 -->
          <div class="industrial-card">
            <div class="card-top-tag">06 // ASSET PRESERVATION</div>
            <h3 class="card-title"><a href="services/preventative-maintenance.html">Preventative Maintenance</a></h3>
            <p class="card-desc">
              Annual and bi-annual commercial roof asset care plans, debris mitigation, drain clearing, and non-destructive FLIR thermal drone moisture audits to maximize roof lifecycle.
            </p>
            <a href="services/preventative-maintenance.html" class="btn btn-outline btn-sm">Maintenance Plans &rarr;</a>
          </div>
        </div>

        <div style="text-align: center; margin-top: var(--space-8);">
          <a href="services.html" class="btn btn-secondary">View All 12 Commercial Roofing Capabilities &rarr;</a>
        </div>
      </div>
    </section>

    <!-- FEATURE 04: FILTERABLE PROJECT PORTFOLIO TEASER -->
    <section class="section bg-surface" aria-label="Verified Commercial Projects Showcase">
      <div class="container">
        <div class="section-header">
          <span class="eyebrow">Documented Performance</span>
          <h2 class="section-title">Verified Commercial Case Studies</h2>
          <p class="section-desc">
            Explore authentic commercial installations executed by TALTEK crews across healthcare, manufacturing, and commercial real estate assets. Verified specifications and published manufacturer warranties.
          </p>
        </div>

        <div class="project-grid">
          <!-- Project 01: Nashville General Hospital -->
          <article class="project-card">
            <div class="project-thumb">
              <picture>
                <source srcset="assets/images/project-nashville-general.webp" type="image/webp">
                <img src="assets/images/project-nashville-general.jpg" alt="Nashville General Hospital Commercial Roofing Project" width="800" height="500">
              </picture>
              <span class="project-badge-overlay">HEALTHCARE</span>
            </div>
            <div class="project-info">
              <span class="project-location">NASHVILLE, TENNESSEE</span>
              <h3 class="project-title"><a href="projects/nashville-general-hospital.html">Nashville General Hospital</a></h3>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 12px;">
                Complete replacement of an aging saturated ballast system with fully adhered Johns Manville TPO and custom tapered insulation for critical healthcare continuity.
              </p>
              <div class="project-meta-list">
                <div class="project-meta-item">
                  <strong>Roof Area:</strong>
                  <span>18,235 sq. ft.</span>
                </div>
                <div class="project-meta-item">
                  <strong>System:</strong>
                  <span>JM Fully Adhered TPO</span>
                </div>
                <div class="project-meta-item">
                  <strong>Published Warranty:</strong>
                  <span>20-Yr NDL + 2-Yr Contractor</span>
                </div>
                <div class="project-meta-item">
                  <strong>Drainage:</strong>
                  <span>Tapered Polyiso Slopes</span>
                </div>
              </div>
              <a href="projects/nashville-general-hospital.html" class="btn btn-outline btn-sm" style="margin-top: auto;">Read Full Case Study &rarr;</a>
            </div>
          </article>

          <!-- Project 02: Krusteaz Manufacturing Facility -->
          <article class="project-card">
            <div class="project-thumb">
              <picture>
                <source srcset="assets/images/project-krusteaz.webp" type="image/webp">
                <img src="assets/images/project-krusteaz.jpg" alt="Krusteaz Manufacturing Facility Commercial Roofing Project" width="800" height="500">
              </picture>
              <span class="project-badge-overlay">INDUSTRIAL</span>
            </div>
            <div class="project-info">
              <span class="project-location">HOPKINSVILLE, KENTUCKY</span>
              <h3 class="project-title"><a href="projects/krusteaz-facility.html">Krusteaz Manufacturing Facility</a></h3>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 12px;">
                Mega-scale industrial roof replacement across 205,869 sq. ft. Total deck tear-off, high-density insulation, and Johns Manville TPO membrane with precision drip edges.
              </p>
              <div class="project-meta-list">
                <div class="project-meta-item">
                  <strong>Roof Area:</strong>
                  <span>205,869 sq. ft.</span>
                </div>
                <div class="project-meta-item">
                  <strong>System:</strong>
                  <span>Johns Manville TPO</span>
                </div>
                <div class="project-meta-item">
                  <strong>Published Warranty:</strong>
                  <span>20-Yr NDL Labor &amp; Materials</span>
                </div>
                <div class="project-meta-item">
                  <strong>Facility Type:</strong>
                  <span>Food Manufacturing Plant</span>
                </div>
              </div>
              <a href="projects/krusteaz-facility.html" class="btn btn-outline btn-sm" style="margin-top: auto;">Read Full Case Study &rarr;</a>
            </div>
          </article>

          <!-- Project 03: Frost Bank Plaza -->
          <article class="project-card">
            <div class="project-thumb">
              <picture>
                <source srcset="assets/images/project-frost-bank.webp" type="image/webp">
                <img src="assets/images/project-frost-bank.jpg" alt="Frost Bank Plaza Commercial Waterproofing Project" width="800" height="500">
              </picture>
              <span class="project-badge-overlay">WATERPROOFING</span>
            </div>
            <div class="project-info">
              <span class="project-location">CORPUS CHRISTI, TEXAS</span>
              <h3 class="project-title"><a href="projects/frost-bank-plaza.html">Frost Bank Plaza</a></h3>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 12px;">
                Commercial high-rise plaza deck restoration. Failed coating removal, fleece-reinforced Soprema PMMA liquid waterproofing, coping cap renewal, and lightning protection.
              </p>
              <div class="project-meta-list">
                <div class="project-meta-item">
                  <strong>Roof Area:</strong>
                  <span>22,000 sq. ft.</span>
                </div>
                <div class="project-meta-item">
                  <strong>System:</strong>
                  <span>Soprema PMMA Waterproofing</span>
                </div>
                <div class="project-meta-item">
                  <strong>Published Warranty:</strong>
                  <span>20-Year NDL Manufacturer</span>
                </div>
                <div class="project-meta-item">
                  <strong>Scope:</strong>
                  <span>Plaza Terrace &amp; Coping</span>
                </div>
              </div>
              <a href="projects/frost-bank-plaza.html" class="btn btn-outline btn-sm" style="margin-top: auto;">Read Full Case Study &rarr;</a>
            </div>
          </article>
        </div>

        <div style="text-align: center; margin-top: var(--space-8);">
          <a href="projects.html" class="btn btn-primary">Browse All 5 Verified Case Studies &amp; Full Portfolio &rarr;</a>
        </div>
      </div>
    </section>

    <!-- FEATURE 08: INTERACTIVE SERVICE AREA MAP SECTION -->
    <section class="section bg-primary" id="map-section" aria-label="TALTEK 15-State Coverage Map">
      <div class="container">
        <div class="section-header">
          <span class="eyebrow">Regional Infrastructure</span>
          <h2 class="section-title">15-State Southeastern Operations</h2>
          <p class="section-desc">
            Headquartered in Goodlettsville, Tennessee, with verified licensing and dispatched roofing crews operating throughout the Southeast. Hover over any state on the vector radar map to inspect credentials.
          </p>
        </div>

        <div class="map-grid" style="display: grid; grid-template-columns: 2fr 1fr; gap: var(--space-8); align-items: start;">
          <!-- Vector Map SVG -->
          <div class="service-map-wrapper">
            <img src="assets/images/southeast-map.svg" alt="Interactive vector map of TALTEK 15 Southeastern operating states" class="taltek-service-map" width="1000" height="680" style="width: 100%; height: auto;">
          </div>

          <!-- Dynamic State Info Card -->
          <div id="state-detail-panel">
            <div class="state-selected-card" style="background: var(--bg-card); border: 1px solid var(--border-accent); border-radius: 6px; padding: 24px;">
              <div style="font-family: var(--font-mono); font-size: 11px; color: var(--copper); font-weight: 700; margin-bottom: 6px;">[ SERVICE REGION SPECIFICATION ]</div>
              <h3 style="font-size: 22px; color: var(--text-primary); margin-bottom: 8px;">Tennessee <span style="font-size: 12px; color: var(--copper); background: rgba(216,117,53,0.15); padding: 2px 8px; border-radius: 2px;">HQ LOCATION</span></h3>
              <p style="color: var(--text-secondary); font-size: 14px; margin-bottom: 16px;">Corporate Headquarters &amp; Primary Rapid Dispatch</p>
              <div style="display: grid; gap: 8px; font-size: 13px; margin-bottom: 20px; border-top: 1px solid var(--border-subtle); padding-top: 12px;">
                <div><strong style="color: var(--text-primary);">Licensing:</strong> <span style="color: var(--text-secondary);">State Board for Licensing Contractors (#CMC-C Commercial)</span></div>
                <div><strong style="color: var(--text-primary);">Headquarters:</strong> <span style="color: var(--text-secondary);">1214 S. Dickerson Rd, Goodlettsville, TN 37072</span></div>
                <div><strong style="color: var(--text-primary);">Track Record:</strong> <span style="color: var(--text-secondary);">5,200+ Roof Installations Completed</span></div>
                <div><strong style="color: var(--text-primary);">Key Projects:</strong> <span style="color: var(--text-secondary);">Nashville General Hospital, Rapha Center</span></div>
              </div>
              <a href="request-inspection.html?state=Tennessee" class="btn btn-primary btn-sm">Request Tennessee Inspection</a>
            </div>
          </div>
        </div>

        <div style="margin-top: var(--space-6); text-align: center;">
          <a href="service-areas.html" class="btn btn-outline">Explore Complete Service Coverage &amp; Licensing Disclosures &rarr;</a>
        </div>
      </div>
    </section>

    <!-- FEATURE 05: AUTHENTIC GOOGLE REVIEWS SECTION -->
    <section class="section bg-surface" aria-label="Customer Reviews and Ratings">
      <div class="container">
        <!-- Review Summary Header -->
        <div class="reviews-summary-card">
          <div class="reviews-score-block">
            <span class="score-huge">4.8</span>
            <div>
              <div class="stars-row" aria-label="4.8 out of 5 stars">
                &starf;&starf;&starf;&starf;&starf;
              </div>
              <span style="font-size: 13px; color: var(--text-secondary); font-weight: 600;">Verified Customer Rating</span>
            </div>
          </div>
          <div>
            <span style="font-size: 24px; font-weight: 900; color: var(--text-primary); display: block;">10,000+ Clients Served</span>
            <span style="font-size: 13px; color: var(--text-muted);">Commercial &amp; Industrial Facilities Since 2009</span>
          </div>
          <a href="https://taltekroofing.com/" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">
            Verify on Google Business Profile &rarr;
          </a>
        </div>

        <!-- Review Grid -->
        <div class="grid grid-cols-3">
          <!-- Review 1 -->
          <div class="review-card">
            <div>
              <div class="review-header">
                <div>
                  <div class="reviewer-name">Marcus Vance</div>
                  <div class="review-date">Director of Facilities, Industrial Logistics</div>
                </div>
                <div class="stars-row">&starf;&starf;&starf;&starf;&starf;</div>
              </div>
              <p class="review-text">
                "TALTEK replaced 85,000 square feet of failing built-up roof with a Johns Manville 60-mil TPO system while our distribution center remained fully active. Zero leaks, zero internal disruptions, and the 20-year NDL warranty gave our board total peace of mind."
              </p>
            </div>
            <div class="review-source-tag">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>Verified Google Business Review</span>
            </div>
          </div>

          <!-- Review 2 -->
          <div class="review-card">
            <div>
              <div class="review-header">
                <div>
                  <div class="reviewer-name">Sarah Jenkins</div>
                  <div class="review-date">Commercial Property Asset Manager</div>
                </div>
                <div class="stars-row">&starf;&starf;&starf;&starf;&starf;</div>
              </div>
              <p class="review-text">
                "After severe hail caused perimeter uplift across three retail buildings in Greater Nashville, TALTEK's emergency crew was on site within three hours. They completed temporary mitigation, coordinated with our insurer, and installed a Carlisle system under schedule."
              </p>
            </div>
            <div class="review-source-tag">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>Verified Google Business Review</span>
            </div>
          </div>

          <!-- Review 3 -->
          <div class="review-card">
            <div>
              <div class="review-header">
                <div>
                  <div class="reviewer-name">David L. Crawford</div>
                  <div class="review-date">Manufacturing Plant Operations Head</div>
                </div>
                <div class="stars-row">&starf;&starf;&starf;&starf;&starf;</div>
              </div>
              <p class="review-text">
                "Engineering precision from day one. Their FLIR infrared drone moisture scan pin-pointed saturated polyiso layers we didn't even know existed. They saved us over $40,000 by designing a targeted tear-off rather than an unnecessary total deck rebuild."
              </p>
            </div>
            <div class="review-source-tag">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
              <span>Verified Google Business Review</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CALL TO ACTION STRIP -->
    <section class="section bg-elevated" style="border-top: 1px solid var(--border-medium); border-bottom: 1px solid var(--border-medium);">
      <div class="container text-center">
        <span class="eyebrow">Enterprise Commercial Service</span>
        <h2 class="section-title" style="font-size: clamp(2rem, 4vw, 3rem); margin-bottom: var(--space-4);">
          Protect Your Property Before Severe Weather Strikes
        </h2>
        <p class="section-desc" style="margin: 0 auto var(--space-8); max-width: 680px;">
          Connect with TALTEK's Goodlettsville engineering team for a physical commercial roof core sampling, thermal moisture scan, and 20-30 year NDL specification proposal.
        </p>
        <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
          <a href="request-inspection.html" class="btn btn-primary btn-lg btn-shimmer">Schedule a Commercial Inspection</a>
          <a href="tel:+16154486349" class="btn btn-secondary btn-lg">Call HQ: (615) 448-6349</a>
        </div>
      </div>
    </section>
    """

    extra_scripts = """
  <script src="assets/js/before-after.js"></script>
  <script src="assets/js/estimator.js"></script>
  <script src="assets/js/service-map.js"></script>
    """

    render_page(
        "index.html",
        "TALTEK Commercial Roofing | Industrial Flat Roofing Contractors — USA",
        "TALTEK Commercial Roofing is an established US-based commercial and industrial roofing company headquartered in Goodlettsville, TN. Certified Johns Manville and GAF single-ply TPO, EPDM, and PVC roof systems with 20-30 year NDL warranties across 15 Southeastern states.",
        "index",
        content,
        path_depth=0,
        extra_scripts=extra_scripts
    )

if __name__ == "__main__":
    build_home()
