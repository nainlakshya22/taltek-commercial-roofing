"""
TALTEK COMMERCIAL ROOFING - DEDICATED FUNCTIONAL TOOL PAGES
Generates:
1. estimator.html (Feature 02: Interactive Commercial Roof Estimator)
2. request-inspection.html (Feature 07: Multi-Step Quote & Inspection Wizard)
3. financing.html (Feature 06: Commercial Financing Calculator)
4. service-areas.html (Feature 08: Interactive Service Area Map)
"""

from build_site import render_page

def build_estimator_page():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Capital Planning &amp; Engineering</span>
          <h1 class="section-title">Commercial Roof Estimator</h1>
          <p class="section-desc">
            Calculate preliminary commercial roof replacement, new installation, and repair cost ranges based on real industrial benchmarks across the Southeastern United States.
          </p>
        </div>

        <div class="estimator-container" id="roof-estimator-app">
          <!-- Form Inputs -->
          <div class="estimator-form-pane">
            <!-- 1. Building Type -->
            <div class="form-group">
              <label class="form-label">
                <span>1. Building Profile</span>
                <span class="form-hint">Select facility type</span>
              </label>
              <div class="option-selector-grid">
                <button type="button" class="selector-tile building-tile active" data-value="warehouse">
                  <span class="tile-icon">&#9638;</span>
                  <span class="tile-label">Industrial Warehouse</span>
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
                  <span class="tile-label">Healthcare Facility</span>
                </button>
                <button type="button" class="selector-tile building-tile" data-value="multifamily">
                  <span class="tile-icon">&#9636;</span>
                  <span class="tile-label">Multi-Family Complex</span>
                </button>
              </div>
            </div>

            <!-- 2. Square Footage -->
            <div class="form-group">
              <div class="form-label">
                <span>2. Approximate Roof Area</span>
                <span id="est-area-badge" style="color: var(--copper); font-family: var(--font-mono); font-weight: 700;">25,000 SQ FT</span>
              </div>
              <div class="slider-wrapper">
                <input type="range" id="est-roof-area" class="range-input" min="5000" max="300000" step="2500" value="25000" aria-label="Roof area slider in square feet">
                <div class="range-val-display">
                  <span>5,000 sq ft</span>
                  <span>150,000 sq ft</span>
                  <span>300,000+ sq ft</span>
                </div>
              </div>
              <div style="margin-top: 14px; display: flex; align-items: center; gap: 8px;">
                <label for="est-area-number" style="font-size: 13px; color: var(--text-secondary);">Exact square feet:</label>
                <input type="number" id="est-area-number" class="form-control" style="width: 140px; padding: 6px 12px; font-size: 14px;" value="25000" min="1000" max="500000">
              </div>
            </div>

            <!-- 3. Desired System -->
            <div class="form-group">
              <label class="form-label">3. Desired Roofing System</label>
              <div class="option-selector-grid">
                <button type="button" class="selector-tile system-tile active" data-value="jm-tpo-60">
                  <span class="tile-label">JM 60-Mil TPO</span>
                  <span style="font-size: 10px; color: var(--text-muted);">20-Yr NDL System</span>
                </button>
                <button type="button" class="selector-tile system-tile" data-value="jm-tpo-80">
                  <span class="tile-label">JM 80-Mil Extreme TPO</span>
                  <span style="font-size: 10px; color: var(--text-muted);">30-Yr NDL Severe Spec</span>
                </button>
                <button type="button" class="selector-tile system-tile" data-value="carlisle-epdm">
                  <span class="tile-label">Carlisle EPDM Rubber</span>
                  <span style="font-size: 10px; color: var(--text-muted);">300% Elongation Flex</span>
                </button>
                <button type="button" class="selector-tile system-tile" data-value="pvc-chemical">
                  <span class="tile-label">PVC Chemical/Grease</span>
                  <span style="font-size: 10px; color: var(--text-muted);">Elvaloy KEE Formula</span>
                </button>
                <button type="button" class="selector-tile system-tile" data-value="soprema-pmma">
                  <span class="tile-label">Soprema PMMA</span>
                  <span style="font-size: 10px; color: var(--text-muted);">Liquid Waterproofing</span>
                </button>
              </div>
            </div>

            <!-- 4. Project Scope -->
            <div class="form-group">
              <label class="form-label">4. Project Scope</label>
              <div style="display: flex; gap: 12px;">
                <button type="button" class="selector-tile project-type-tile active" data-value="replacement" style="flex: 1;">
                  <span class="tile-label">Full Tear-Off &amp; Replacement</span>
                  <span style="font-size: 10px; color: var(--text-muted);">Complete Deck Tear-Off + Tapered Polyiso</span>
                </button>
                <button type="button" class="selector-tile project-type-tile" data-value="repair" style="flex: 1;">
                  <span class="tile-label">Targeted Seam Repair / Restoration</span>
                  <span style="font-size: 10px; color: var(--text-muted);">Localized Membrane Welds &amp; Flashing</span>
                </button>
              </div>
            </div>

            <!-- 5. Existing Condition -->
            <div class="form-group">
              <label class="form-label">5. Current Substrate Condition</label>
              <div class="option-selector-grid">
                <button type="button" class="selector-tile condition-tile" data-value="good">
                  <span class="tile-label">Good / Minor Wear</span>
                </button>
                <button type="button" class="selector-tile condition-tile active" data-value="fair">
                  <span class="tile-label">Fair / Ponding Water</span>
                </button>
                <button type="button" class="selector-tile condition-tile" data-value="deteriorated">
                  <span class="tile-label">Active Interior Leaks</span>
                </button>
                <button type="button" class="selector-tile condition-tile" data-value="severe">
                  <span class="tile-label">Severe Saturation / Decay</span>
                </button>
              </div>
            </div>
          </div>

          <!-- Summary & Live Output -->
          <div class="estimator-summary-pane">
            <div>
              <div class="card-top-tag">[ PRELIMINARY ESTIMATION SUMMARY ]</div>
              <h2 style="font-size: 20px; color: var(--text-primary); margin-bottom: 12px;">Budgetary Range</h2>
              
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
                  <span>Selected System:</span>
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
              <a id="est-transfer-quote-btn" href="request-inspection.html?sqft=25000&system=jm-tpo-60" class="btn btn-primary" style="width: 100%; margin-bottom: 10px;">
                Lock In Core Sample Inspection &rarr;
              </a>
              <div class="estimator-disclaimer-box">
                <strong>LEGAL DISCLAIMER:</strong> This commercial estimator tool provides an automated preliminary mathematical projection for capital budgeting purposes only. It does NOT constitute a formal binding bid, warranty commitment, or guaranteed contract price. Commercial roofing systems require on-site physical core extraction, moisture scanning, and structural deck evaluation by an authorized TALTEK roofing engineer.
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    """

    extra_scripts = """
  <script src="assets/js/estimator.js"></script>
    """

    render_page(
        "estimator.html",
        "Commercial Roof Estimator | Preliminary Project Calculator — TALTEK",
        "Interactive commercial roof cost estimator. Calculate preliminary budget ranges for TPO, EPDM, and PVC roof installations and replacements across the Southeastern USA.",
        "estimator",
        content,
        path_depth=0,
        extra_scripts=extra_scripts
    )

def build_quote_page():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container" style="max-width: 980px;">
        <div class="section-header text-center">
          <span class="eyebrow">Enterprise Dispatch &amp; Estimation</span>
          <h1 class="section-title">Schedule a Commercial Roof Inspection</h1>
          <p class="section-desc">
            Complete our 5-step commercial inspection wizard. Our engineering team in Goodlettsville, TN will review your facility specifications and dispatch a certified inspector for core sampling, moisture scans, and proposal preparation.
          </p>
        </div>

        <!-- FEATURE 07: MULTI-STEP WIZARD -->
        <div class="quote-wizard" id="commercial-quote-wizard">
          <!-- Wizard Steps Progress Bar -->
          <div class="wizard-progress-bar" role="tablist">
            <div class="wizard-step-tab active" data-step="1">1. Property</div>
            <div class="wizard-step-tab" data-step="2">2. Scope</div>
            <div class="wizard-step-tab" data-step="3">3. Roof Specs</div>
            <div class="wizard-step-tab" data-step="4">4. Contact</div>
            <div class="wizard-step-tab" data-step="5">5. Confirmation</div>
          </div>

          <form id="commercial-quote-form" class="wizard-content" novalidate>
            <!-- Error Alert Banner -->
            <div id="quote-error-banner" style="display:none; background: rgba(239, 68, 68, 0.15); border: 1px solid var(--status-danger); color: #FCA5A5; padding: 16px; border-radius: 4px; margin-bottom: 20px; font-size: 13px;">
              <strong>DISPATCH CONNECTION NOTICE:</strong> Unable to connect to the TALTEK dispatch servers. Your request was NOT transmitted. To secure immediate priority scheduling or report an emergency, please contact our 24/7 direct line at <a href="tel:+16154486349" style="color: #FFFFFF; text-decoration: underline; font-weight: 700;">+1 (615) 448-6349</a> or email <a href="mailto:sales@taltekroofing.com" style="color: #FFFFFF; text-decoration: underline;">sales@taltekroofing.com</a>.
            </div>

            <!-- Honeypot anti-spam trap (hidden from users, bot trap) -->
            <input type="text" name="hp_website_title" style="display:none !important;" tabindex="-1" autocomplete="off" aria-hidden="true">

            <!-- STEP 1: PROPERTY INFORMATION -->
            <div class="wizard-step-pane active" data-step="1">
              <h2 style="font-size: 20px; color: var(--text-primary); margin-bottom: 8px;">Step 1: Property Information</h2>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 24px;">Identify the commercial building type and physical location.</p>

              <div class="form-group">
                <label class="form-label">Property Classification *</label>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px;">
                  <label class="custom-radio">
                    <input type="radio" name="property_type" value="Commercial Office" checked>
                    <span>Commercial Office</span>
                  </label>
                  <label class="custom-radio">
                    <input type="radio" name="property_type" value="Industrial Warehouse">
                    <span>Industrial Warehouse</span>
                  </label>
                  <label class="custom-radio">
                    <input type="radio" name="property_type" value="Manufacturing Plant">
                    <span>Manufacturing Plant</span>
                  </label>
                  <label class="custom-radio">
                    <input type="radio" name="property_type" value="Retail Plaza">
                    <span>Retail Plaza / Mall</span>
                  </label>
                  <label class="custom-radio">
                    <input type="radio" name="property_type" value="Healthcare Facility">
                    <span>Healthcare / Hospital</span>
                  </label>
                  <label class="custom-radio">
                    <input type="radio" name="property_type" value="Multi-Family">
                    <span>Multi-Family Complex</span>
                  </label>
                </div>
              </div>

              <div class="form-group">
                <label for="building_name" class="form-label">Building / Facility Name *</label>
                <input type="text" id="building_name" name="building_name" class="form-control" placeholder="e.g. Cumberland Distribution Center" required>
                <span class="form-error-msg">Building name is required.</span>
              </div>

              <div class="grid grid-cols-2" style="gap: 16px;">
                <div class="form-group">
                  <label for="street_address" class="form-label">Physical Street Address *</label>
                  <input type="text" id="street_address" name="street_address" class="form-control" placeholder="123 Industrial Blvd" required>
                  <span class="form-error-msg">Address is required.</span>
                </div>
                <div class="form-group">
                  <label for="city" class="form-label">City *</label>
                  <input type="text" id="city" name="city" class="form-control" placeholder="e.g. Nashville" required>
                  <span class="form-error-msg">City is required.</span>
                </div>
              </div>

              <div class="grid grid-cols-2" style="gap: 16px;">
                <div class="form-group">
                  <label for="state_select" class="form-label">State *</label>
                  <select id="state_select" name="state" class="form-control" required>
                    <option value="Tennessee" selected>Tennessee (Headquarters)</option>
                    <option value="Alabama">Alabama</option>
                    <option value="Mississippi">Mississippi</option>
                    <option value="Louisiana">Louisiana</option>
                    <option value="North Carolina">North Carolina</option>
                    <option value="South Carolina">South Carolina</option>
                    <option value="Virginia">Virginia</option>
                    <option value="Kentucky">Kentucky</option>
                    <option value="Georgia">Georgia</option>
                    <option value="Florida">Florida</option>
                    <option value="Arkansas">Arkansas</option>
                    <option value="Other SE State">Other Southeastern State</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="zip_code" class="form-label">ZIP Code *</label>
                  <input type="text" id="zip_code" name="zip_code" class="form-control" placeholder="e.g. 37072" required>
                  <span class="form-error-msg">Valid ZIP code required.</span>
                </div>
              </div>
            </div>

            <!-- STEP 2: ROOFING REQUIREMENTS -->
            <div class="wizard-step-pane" data-step="2">
              <h2 style="font-size: 20px; color: var(--text-primary); margin-bottom: 8px;">Step 2: Roofing Requirements</h2>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 24px;">Specify the urgency and primary objective of this inspection.</p>

              <div class="form-group">
                <label class="form-label">Primary Service Requirement *</label>
                <div style="display: grid; gap: 12px;">
                  <label class="custom-radio" style="background: var(--bg-card); padding: 12px; border: 1px solid var(--border-medium); border-radius: 4px;">
                    <input type="radio" name="service_requirement" value="Complete Roof Replacement" checked>
                    <div>
                      <strong style="color: var(--text-primary); display: block;">Complete Roof Replacement / Re-Cover</strong>
                      <span style="font-size: 12px; color: var(--text-secondary);">End-of-life membrane, chronic leaks, upgrading to 20-30 yr NDL single-ply.</span>
                    </div>
                  </label>
                  <label class="custom-radio" style="background: var(--bg-card); padding: 12px; border: 1px solid var(--border-medium); border-radius: 4px;">
                    <input type="radio" name="service_requirement" value="Leak Repair / Active Infiltration">
                    <div>
                      <strong style="color: var(--text-primary); display: block;">Active Leak Repair &amp; Diagnostic Tracing</strong>
                      <span style="font-size: 12px; color: var(--text-secondary);">Water currently penetrating interior, seam failure, curb leak.</span>
                    </div>
                  </label>
                  <label class="custom-radio" style="background: var(--bg-card); padding: 12px; border: 1px solid var(--border-medium); border-radius: 4px;">
                    <input type="radio" name="service_requirement" value="Emergency Storm Damage Dispatch">
                    <div>
                      <strong style="color: var(--copper); display: block;">Emergency Storm / Hail / Tornado Dispatch</strong>
                      <span style="font-size: 12px; color: var(--text-secondary);">Immediate 24/7 priority emergency response.</span>
                    </div>
                  </label>
                  <label class="custom-radio" style="background: var(--bg-card); padding: 12px; border: 1px solid var(--border-medium); border-radius: 4px;">
                    <input type="radio" name="service_requirement" value="Preventative Maintenance Audit">
                    <div>
                      <strong style="color: var(--text-primary); display: block;">Preventative Maintenance &amp; Asset Longevity Plan</strong>
                      <span style="font-size: 12px; color: var(--text-secondary);">Scheduled semi-annual drain clearing, warranty preservation.</span>
                    </div>
                  </label>
                  <label class="custom-radio" style="background: var(--bg-card); padding: 12px; border: 1px solid var(--border-medium); border-radius: 4px;">
                    <input type="radio" name="service_requirement" value="Pre-Purchase Due Diligence / Drone Scan">
                    <div>
                      <strong style="color: var(--text-primary); display: block;">Pre-Purchase Due Diligence / Infrared Thermal Scan</strong>
                      <span style="font-size: 12px; color: var(--text-secondary);">FLIR radiometric drone scan, core extraction, 10-year CapEx budget.</span>
                    </div>
                  </label>
                </div>
              </div>
            </div>

            <!-- STEP 3: ROOF INFORMATION -->
            <div class="wizard-step-pane" data-step="3">
              <h2 style="font-size: 20px; color: var(--text-primary); margin-bottom: 8px;">Step 3: Roof Technical Information</h2>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 24px;">Provide approximate dimensions and existing material information.</p>

              <div class="grid grid-cols-2" style="gap: 16px;">
                <div class="form-group">
                  <label for="roof_sqft" class="form-label">Approximate Roof Area (Sq. Ft.) *</label>
                  <input type="number" id="roof_sqft" name="roof_sqft" class="form-control" placeholder="e.g. 25000" min="500" max="1000000" required>
                  <span class="form-error-msg">Approximate square footage is required.</span>
                </div>
                <div class="form-group">
                  <label for="existing_roof_type" class="form-label">Current Roofing Material</label>
                  <select id="existing_roof_type" name="existing_roof_type" class="form-control">
                    <option value="Single-Ply TPO" selected>Single-Ply TPO</option>
                    <option value="Single-Ply EPDM Rubber">Single-Ply EPDM (Rubber)</option>
                    <option value="Single-Ply PVC">Single-Ply PVC</option>
                    <option value="Built-Up / Tar &amp; Gravel">Built-Up Roof (BUR) / Tar &amp; Gravel</option>
                    <option value="Modified Bitumen">Modified Bitumen</option>
                    <option value="Standing Seam Metal">Standing Seam Metal</option>
                    <option value="Ballasted Membrane">Ballasted Stone Membrane</option>
                    <option value="Unknown">Unknown / Needs Core Extraction</option>
                  </select>
                </div>
              </div>

              <div class="grid grid-cols-2" style="gap: 16px;">
                <div class="form-group">
                  <label for="estimated_age" class="form-label">Estimated Roof Age (Years)</label>
                  <select id="estimated_age" name="estimated_age" class="form-control">
                    <option value="Under 5 Years">Under 5 Years</option>
                    <option value="5-10 Years">5 to 10 Years</option>
                    <option value="11-15 Years">11 to 15 Years</option>
                    <option value="16-20 Years" selected>16 to 20 Years</option>
                    <option value="20+ Years">20+ Years (End of Life)</option>
                    <option value="Unknown">Unknown</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="current_condition" class="form-label">Observed Condition</label>
                  <select id="current_condition" name="current_condition" class="form-control">
                    <option value="Active Leaks in Multiple Areas">Active Leaks in Multiple Areas</option>
                    <option value="Isolated Single Leak">Isolated Single Leak</option>
                    <option value="Severe Ponding Water">Severe Ponding Water / Poor Drainage</option>
                    <option value="Storm / Wind Damage">Recent Hail or Wind Damage</option>
                    <option value="Aging but Currently Dry">Aging but Currently Watertight</option>
                  </select>
                </div>
              </div>

              <div class="form-group">
                <label for="project_notes" class="form-label">Project Details / Specific Access Requirements</label>
                <textarea id="project_notes" name="project_notes" class="form-control" placeholder="Note tenant schedule constraints, roof hatch access location, or insurance carrier deadlines..."></textarea>
              </div>
            </div>

            <!-- STEP 4: CONTACT INFORMATION -->
            <div class="wizard-step-pane" data-step="4">
              <h2 style="font-size: 20px; color: var(--text-primary); margin-bottom: 8px;">Step 4: Contact &amp; Company Details</h2>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 24px;">Enter your commercial facility contact details for engineer dispatch.</p>

              <div class="grid grid-cols-2" style="gap: 16px;">
                <div class="form-group">
                  <label for="full_name" class="form-label">Full Name *</label>
                  <input type="text" id="full_name" name="full_name" class="form-control" placeholder="John Doe" required>
                  <span class="form-error-msg">Full name is required.</span>
                </div>
                <div class="form-group">
                  <label for="company_name" class="form-label">Company / Organization Name *</label>
                  <input type="text" id="company_name" name="company_name" class="form-control" placeholder="Acme Logistics LLC" required>
                  <span class="form-error-msg">Company name is required.</span>
                </div>
              </div>

              <div class="grid grid-cols-2" style="gap: 16px;">
                <div class="form-group">
                  <label for="business_email" class="form-label">Business Email Address *</label>
                  <input type="email" id="business_email" name="business_email" class="form-control" placeholder="jdoe@company.com" required>
                  <span class="form-error-msg">Valid business email required.</span>
                </div>
                <div class="form-group">
                  <label for="phone" class="form-label">Direct Telephone Number *</label>
                  <input type="tel" id="phone" name="phone" class="form-control" placeholder="(615) 555-0199" required>
                  <span class="form-error-msg">Valid 10-digit phone number required.</span>
                </div>
              </div>

              <!-- SMS & Communications Consent (US TCPA / CAN-SPAM Compliant, UNCHECKED BY DEFAULT) -->
              <div style="background: var(--bg-card); border: 1px solid var(--border-medium); padding: 16px; border-radius: 4px; margin: 20px 0;">
                <label class="custom-checkbox">
                  <input type="checkbox" id="sms_consent" name="sms_consent" value="yes">
                  <span style="font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
                    [Optional] I agree to receive text (SMS) notifications regarding my inspection schedule and dispatch updates from TALTEK Commercial Roofing at the mobile number provided above. Message and data rates may apply. Reply STOP to cancel at any time. Review our <a href="sms-terms.html" target="_blank" style="color: var(--copper); text-decoration: underline;">SMS Terms</a> and <a href="privacy-policy.html" target="_blank" style="color: var(--copper); text-decoration: underline;">Privacy Policy</a>. (Consent is not a condition of purchase).
                  </span>
                </label>
              </div>

              <!-- Summary Review Box populated before submit -->
              <div>
                <h3 style="font-size: 15px; color: var(--text-primary); margin-bottom: 8px;">Inspection Request Summary</h3>
                <div id="wizard-summary-review"></div>
              </div>
            </div>

            <!-- STEP 5: CONFIRMATION PANE -->
            <div class="wizard-step-pane" data-step="5">
              <div style="text-align: center; padding: clamp(2rem, 5vw, 4rem) 1rem;">
                <div style="width: 64px; height: 64px; background: rgba(16, 185, 129, 0.15); border: 2px solid var(--status-success); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; color: var(--status-success); font-size: 32px;">
                  &check;
                </div>
                <h2 style="font-size: 28px; color: var(--text-primary); margin-bottom: 8px;">Inspection Request Recorded</h2>
                <div style="font-family: var(--font-mono); font-size: 14px; color: var(--copper); margin-bottom: 16px;">
                  REFERENCE TRACKING ID: <span id="confirmation-ref-code">TK-894721</span>
                </div>
                <p id="confirmation-dispatch-msg" style="color: var(--text-secondary); max-width: 600px; margin: 0 auto 24px; line-height: 1.7;">
                  Thank you. Your commercial roofing assessment request has been recorded into the TALTEK dispatch register. A certified commercial roofing estimator will review facility specifications and contact your office to confirm site access details.
                </p>
                <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap;">
                  <a href="tel:+16154486349" class="btn btn-secondary">Direct Dispatch: (615) 448-6349</a>
                  <a href="index.html" class="btn btn-outline">Return to Homepage</a>
                </div>
              </div>
            </div>

            <!-- Wizard Bottom Action Buttons -->
            <div class="wizard-actions">
              <button type="button" class="btn btn-secondary wizard-btn-prev" style="display: none;">&larr; Back</button>
              <div style="margin-left: auto; display: flex; gap: 12px;">
                <button type="button" class="btn btn-primary wizard-btn-next">Next Step &rarr;</button>
                <button type="submit" class="btn btn-primary wizard-btn-submit" style="display: none;">Submit Inspection Request</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </section>
    """

    extra_scripts = """
  <script src="assets/js/quote-form.js"></script>
    """

    render_page(
        "request-inspection.html",
        "Request a Commercial Roof Inspection | Multi-Step Wizard — TALTEK",
        "Schedule a comprehensive commercial roof inspection with TALTEK Commercial Roofing. Core moisture scans, deck evaluations, and single-ply proposals across Tennessee and 15 Southeastern states.",
        "request-inspection",
        content,
        path_depth=0,
        extra_scripts=extra_scripts
    )

def build_financing_page():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container" style="max-width: 980px;">
        <div class="section-header text-center">
          <span class="eyebrow">Capital Expenditure Optimization</span>
          <h1 class="section-title">Commercial Roofing Financing Calculator</h1>
          <p class="section-desc">
            Model structured capital expenditure financing, monthly repayment schedules, and interest projections for major commercial and industrial roof replacement projects.
          </p>
        </div>

        <!-- FEATURE 06: FINANCING CALCULATOR -->
        <div class="financing-calculator-box" id="financing-calc-form">
          <div class="financing-grid" style="display: grid; grid-template-columns: 1.4fr 1fr; gap: var(--space-8);">
            <!-- Left: Inputs -->
            <div>
              <div class="form-group">
                <label for="fin-project-cost" class="form-label">
                  <span>Estimated Total Project Cost ($)</span>
                  <span style="font-family: var(--font-mono); color: var(--copper); font-weight:700;">$150,000</span>
                </label>
                <input type="number" id="fin-project-cost" class="form-control" value="150000" min="10000" max="2500000" step="5000">
                <div class="slider-wrapper" style="margin-top: 10px;">
                  <input type="range" id="fin-cost-slider" class="range-input" min="10000" max="1000000" step="10000" value="150000" aria-label="Financing cost slider">
                  <div class="range-val-display">
                    <span>$10,000</span>
                    <span>$500,000</span>
                    <span>$1,000,000+</span>
                  </div>
                </div>
              </div>

              <div class="form-group">
                <label for="fin-down-payment" class="form-label">Initial Down Payment ($)</label>
                <input type="number" id="fin-down-payment" class="form-control" value="30000" min="0" max="1000000" step="5000">
                <span class="form-hint">Typical commercial down payments range from 10% to 25%.</span>
              </div>

              <div class="grid grid-cols-2" style="gap: 16px;">
                <div class="form-group">
                  <label for="fin-term-months" class="form-label">Financing Term</label>
                  <select id="fin-term-months" class="form-control">
                    <option value="24">24 Months (2 Years)</option>
                    <option value="36">36 Months (3 Years)</option>
                    <option value="48">48 Months (4 Years)</option>
                    <option value="60" selected>60 Months (5 Years)</option>
                    <option value="84">84 Months (7 Years)</option>
                  </select>
                </div>
                <div class="form-group">
                  <label for="fin-interest-rate" class="form-label">Estimated APR Rate (%)</label>
                  <input type="number" id="fin-interest-rate" class="form-control" value="7.5" min="1.0" max="25.0" step="0.25">
                </div>
              </div>
            </div>

            <!-- Right: Dynamic Payment Box -->
            <div style="display: flex; flex-direction: column; justify-content: space-between;">
              <div class="calc-output-card">
                <span style="font-size: 12px; color: var(--text-muted); text-transform: uppercase; font-family: var(--font-mono);">Estimated Monthly Repayment</span>
                <div id="fin-output-monthly" class="calc-monthly-payment">$2,405</div>
                <div style="font-size: 11px; color: var(--text-secondary);">Fixed monthly capital amortization</div>

                <div style="margin-top: 24px; padding-top: 16px; border-top: 1px solid var(--border-subtle); display: flex; flex-direction: column; gap: 8px; font-size: 13px; text-align: left;">
                  <div style="display: flex; justify-content: space-between;">
                    <span style="color: var(--text-secondary);">Financed Principal:</span>
                    <strong id="fin-output-financed-amount" style="color: var(--text-primary);">$120,000</strong>
                  </div>
                  <div style="display: flex; justify-content: space-between;">
                    <span style="color: var(--text-secondary);">Total Finance Charges:</span>
                    <strong id="fin-output-interest" style="color: var(--copper);">$24,288</strong>
                  </div>
                  <div style="display: flex; justify-content: space-between;">
                    <span style="color: var(--text-secondary);">Total Repayment:</span>
                    <strong id="fin-output-total" style="color: var(--text-primary);">$144,288</strong>
                  </div>
                </div>
              </div>

              <div style="margin-top: 20px;">
                <a href="request-inspection.html" class="btn btn-primary" style="width: 100%; margin-bottom: 10px;">Apply Financed Quote to Inspection</a>
                <a href="estimator.html" class="btn btn-outline btn-sm" style="width: 100%;">Calculate Detailed Sq Ft Pricing</a>
              </div>
            </div>
          </div>

          <!-- Financing Legal Disclaimers -->
          <div class="estimator-disclaimer-box" style="margin-top: 24px;">
            <strong>MANDATORY FINANCING DISCLOSURE:</strong> The calculations provided above are hypothetical illustrations generated for budgeting and preliminary planning purposes only. TALTEK Commercial Roofing is an independent licensed roofing contractor and does not directly issue loans, originate commercial credit, or guarantee financing rates or eligibility. Commercial project financing, leasing arrangements, and terms are provided solely through verified third-party commercial lending partners and are subject to independent credit approval, underwriting criteria, and binding contract execution.
          </div>
        </div>
      </div>
    </section>
    """

    extra_scripts = """
  <script src="assets/js/financing-calc.js"></script>
    """

    render_page(
        "financing.html",
        "Commercial Roofing Financing Calculator | Capital Equipment Leasing — TALTEK",
        "Model commercial roof replacement financing, monthly repayments, and interest rates for industrial facilities across Tennessee and the Southeastern USA.",
        "financing",
        content,
        path_depth=0,
        extra_scripts=extra_scripts
    )

def build_service_areas_page():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Regional Infrastructure</span>
          <h1 class="section-title">Verified Southeastern Service Areas</h1>
          <p class="section-desc">
            Headquartered in Goodlettsville, Tennessee, TALTEK deploys certified commercial roofing crews and rapid-response disaster teams across 15 Southeastern states.
          </p>
        </div>

        <!-- FEATURE 08: MAP & REGIONAL HUB DIRECTORY -->
        <div class="map-grid" style="display: grid; grid-template-columns: 1.8fr 1.2fr; gap: var(--space-8); margin-bottom: var(--space-12);">
          <div class="service-map-wrapper">
            <img src="assets/images/southeast-map.svg" alt="Interactive vector map of TALTEK 15 Southeastern operating states" class="taltek-service-map" width="1000" height="680" style="width: 100%; height: auto;">
          </div>

          <div id="state-detail-panel">
            <div class="state-selected-card" style="background: var(--bg-card); border: 1px solid var(--border-accent); border-radius: 6px; padding: 24px;">
              <div style="font-family: var(--font-mono); font-size: 11px; color: var(--copper); font-weight: 700; margin-bottom: 6px;">[ SERVICE REGION SPECIFICATION ]</div>
              <h2 style="font-size: 22px; color: var(--text-primary); margin-bottom: 8px;">Tennessee (Headquarters)</h2>
              <p style="color: var(--text-secondary); font-size: 14px; margin-bottom: 16px;">Corporate Operations, Warehousing &amp; Primary Rapid Dispatch</p>
              <div style="display: grid; gap: 8px; font-size: 13px; margin-bottom: 20px; border-top: 1px solid var(--border-subtle); padding-top: 12px;">
                <div><strong style="color: var(--text-primary);">Licensing:</strong> <span style="color: var(--text-secondary);">Tennessee Board for Licensing Contractors (#CMC-C Commercial)</span></div>
                <div><strong style="color: var(--text-primary);">Headquarters:</strong> <span style="color: var(--text-secondary);">1214 S. Dickerson Rd, Goodlettsville, TN 37072</span></div>
                <div><strong style="color: var(--text-primary);">Phone:</strong> <span style="color: var(--copper); font-weight:700;">+1 (615) 448-6349</span></div>
                <div><strong style="color: var(--text-primary);">Track Record:</strong> <span style="color: var(--text-secondary);">5,200+ Roof Installations Completed</span></div>
                <div><strong style="color: var(--text-primary);">Key Projects:</strong> <span style="color: var(--text-secondary);">Nashville General Hospital, Rapha Center</span></div>
              </div>
              <a href="request-inspection.html?state=Tennessee" class="btn btn-primary btn-sm">Request Tennessee Inspection</a>
            </div>
          </div>
        </div>

        <!-- Verified State Licensing Directory -->
        <div style="margin-top: var(--space-8);">
          <div class="section-header">
            <span class="eyebrow">Legal Licensing Verification</span>
            <h2 class="section-title">Verified Contractor Licensing By State</h2>
            <p class="section-desc">
              TALTEK complies strictly with statutory contractor licensing, bonded requirements, and commercial general liability minimums across all Southeastern jurisdictions.
            </p>
          </div>

          <div class="grid grid-cols-2" style="gap: var(--space-6);">
            <!-- TN -->
            <div class="industrial-card">
              <div class="card-top-tag">STATE 01 // CORPORATE HEADQUARTERS</div>
              <h3 class="card-title">Tennessee</h3>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 8px;">
                <strong>Licensing Board:</strong> Tennessee Board for Licensing Contractors<br>
                <strong>Classification:</strong> CMC-C Commercial Roofing / Full Commercial Authorization<br>
                <strong>Operational Facility:</strong> 1214 S. Dickerson Rd, Goodlettsville, TN 37072<br>
                <strong>Dispatched Hubs:</strong> Nashville, Memphis, Knoxville, Chattanooga, Clarksville
              </p>
            </div>

            <!-- AL -->
            <div class="industrial-card">
              <div class="card-top-tag">STATE 02 // VERIFIED LICENSED</div>
              <h3 class="card-title">Alabama</h3>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 8px;">
                <strong>Licensing Board:</strong> Alabama State Licensing Board for General Contractors<br>
                <strong>Classification:</strong> Commercial Roofing &amp; Sheet Metal Contractor<br>
                <strong>Regional Operations Hub:</strong> Birmingham Regional Hub<br>
                <strong>Service Areas:</strong> Birmingham, Huntsville, Mobile, Montgomery, Tuscaloosa
              </p>
            </div>

            <!-- LA -->
            <div class="industrial-card">
              <div class="card-top-tag">STATE 03 // VERIFIED LICENSED</div>
              <h3 class="card-title">Louisiana</h3>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 8px;">
                <strong>Licensing Board:</strong> Louisiana State Licensing Board for Contractors<br>
                <strong>Classification:</strong> Commercial Building Construction &amp; Specialty Roofing<br>
                <strong>Specialization:</strong> Chemical Resistant PVC &amp; High-Wind Coastal Assemblies<br>
                <strong>Service Areas:</strong> New Orleans, Baton Rouge, Shreveport, Lafayette
              </p>
            </div>

            <!-- MS -->
            <div class="industrial-card">
              <div class="card-top-tag">STATE 04 // VERIFIED LICENSED</div>
              <h3 class="card-title">Mississippi</h3>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 8px;">
                <strong>Licensing Board:</strong> Mississippi State Board of Contractors<br>
                <strong>Classification:</strong> Commercial Roofing Specialist License<br>
                <strong>Specialization:</strong> Rapid Storm Disaster Recovery &amp; Distribution Roofing<br>
                <strong>Service Areas:</strong> Jackson, Gulfport, Southaven, Biloxi, Hattiesburg
              </p>
            </div>

            <!-- NC -->
            <div class="industrial-card">
              <div class="card-top-tag">STATE 05 // VERIFIED LICENSED</div>
              <h3 class="card-title">North Carolina</h3>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 8px;">
                <strong>Licensing Board:</strong> North Carolina Licensing Board for General Contractors<br>
                <strong>Classification:</strong> Commercial Specialty Building Contractor<br>
                <strong>Regional Operations Hub:</strong> Charlotte Regional Hub<br>
                <strong>Service Areas:</strong> Charlotte, Raleigh, Greensboro, Durham, Winston-Salem
              </p>
            </div>

            <!-- SC -->
            <div class="industrial-card">
              <div class="card-top-tag">STATE 06 // VERIFIED LICENSED</div>
              <h3 class="card-title">South Carolina</h3>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 8px;">
                <strong>Licensing Board:</strong> South Carolina Contractor's Licensing Board<br>
                <strong>Classification:</strong> Specialty Commercial Roofing License<br>
                <strong>Specialization:</strong> Coastal Hurricane Uplift Hardening (FM 1-120 Standards)<br>
                <strong>Service Areas:</strong> Charleston, Columbia, Greenville, Spartanburg, Myrtle Beach
              </p>
            </div>

            <!-- VA -->
            <div class="industrial-card">
              <div class="card-top-tag">STATE 07 // VERIFIED LICENSED</div>
              <h3 class="card-title">Virginia</h3>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 8px;">
                <strong>Licensing Board:</strong> Virginia Board for Contractors (DPOR)<br>
                <strong>Classification:</strong> Class A Commercial Contractor License<br>
                <strong>Regional Operations Hub:</strong> Richmond Hub<br>
                <strong>Service Areas:</strong> Richmond, Virginia Beach, Norfolk, Roanoke, Alexandria
              </p>
            </div>

            <!-- Additional Operational States -->
            <div class="industrial-card">
              <div class="card-top-tag">REGIONAL LOGISTICS // 15 STATES TOTAL</div>
              <h3 class="card-title">Southeastern Operations Network</h3>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 8px;">
                <strong>Active Territories:</strong> Kentucky (Hopkinsville Krusteaz Plant), Georgia, Florida, Arkansas, West Virginia, and national account assignments across the United States.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
    """

    extra_scripts = """
  <script src="assets/js/service-map.js"></script>
    """

    render_page(
        "service-areas.html",
        "Southeastern Service Areas & Verified Licensing | TALTEK Commercial Roofing",
        "Interactive coverage map and verified contractor licensing across Tennessee, Alabama, Louisiana, Mississippi, North Carolina, South Carolina, Virginia, and the Southeastern US.",
        "service-areas",
        content,
        path_depth=0,
        extra_scripts=extra_scripts
    )

if __name__ == "__main__":
    build_estimator_page()
    build_quote_page()
    build_financing_page()
    build_service_areas_page()
    print("All functional tool pages generated successfully!")
