"""
TALTEK COMMERCIAL ROOFING - PROJECT PORTFOLIO & CASE STUDIES
Generates projects.html and all 5 authentic case studies (Feature 04).
"""

from build_site import render_page

def build_projects_index():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Documented Enterprise Performance</span>
          <h1 class="section-title">Commercial &amp; Industrial Projects</h1>
          <p class="section-desc">
            Explore commercial installation profiles executed across healthcare, manufacturing facilities, retail centers, and commercial towers. Comprehensive single-ply engineering specifications, core sampling analyses, and manufacturer warranty overviews.
          </p>
        </div>

        <!-- Concept Portfolio Notice -->
        <div style="background: rgba(216, 117, 53, 0.08); border: 1px solid var(--border-accent); border-radius: 6px; padding: 18px 24px; margin-bottom: 32px; max-width: 900px; margin-left: auto; margin-right: auto; text-align: left;">
          <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
            <span style="display: inline-block; width: 8px; height: 8px; background-color: var(--copper); border-radius: 50%;"></span>
            <strong style="color: var(--copper); font-family: var(--font-mono); font-size: 12px; letter-spacing: 0.05em; text-transform: uppercase;">Architectural Concept Demonstration Portfolio</strong>
          </div>
          <p style="font-size: 13px; color: var(--text-secondary); margin: 0; line-height: 1.6;">
            The project case studies below are representative commercial installation profiles illustrating single-ply roofing engineering assemblies, tapered insulation designs, core sampling analyses, and manufacturer warranty specifications. Published client references, contracted scopes, and project photography are subject to official TALTEK company review and client authorization.
          </p>
        </div>

        <!-- Filter Bar -->
        <div class="portfolio-filter-bar">
          <button type="button" class="filter-btn active" data-filter="all">All Projects</button>
          <button type="button" class="filter-btn" data-filter="commercial">Commercial</button>
          <button type="button" class="filter-btn" data-filter="industrial">Industrial</button>
          <button type="button" class="filter-btn" data-filter="replacement">Replacement</button>
          <button type="button" class="filter-btn" data-filter="tpo">TPO Roofing</button>
          <button type="button" class="filter-btn" data-filter="epdm">EPDM Roofing</button>
          <button type="button" class="filter-btn" data-filter="waterproofing">Waterproofing</button>
        </div>

        <div id="portfolio-results-count" style="text-align: center; font-family: var(--font-mono); font-size: 12px; color: var(--copper); margin-bottom: 24px;">
          Showing 5 Representative Case Studies
        </div>

        <!-- Project Grid -->
        <div class="project-grid">
          <!-- 1. Nashville General Hospital -->
          <article class="project-card" data-categories="commercial replacement tpo healthcare">
            <div class="project-thumb">
              <picture>
                <source srcset="assets/images/project-nashville-general.webp" type="image/webp">
                <img src="assets/images/project-nashville-general.jpg" alt="Nashville General Hospital Commercial Roofing Project" width="800" height="500">
              </picture>
              <span class="project-badge-overlay">HEALTHCARE</span>
            </div>
            <div class="project-info">
              <span class="project-location">NASHVILLE, TENNESSEE</span>
              <h2 class="project-title"><a href="projects/nashville-general-hospital.html">Nashville General Hospital</a></h2>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 12px;">
                Complete replacement of an aging ballast system with fully adhered Johns Manville TPO and custom tapered polyiso drainage crickets for critical hospital continuity.
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
                  <strong>Condition Overcome:</strong>
                  <span>Saturated Insulation</span>
                </div>
              </div>
              <a href="projects/nashville-general-hospital.html" class="btn btn-outline btn-sm" style="margin-top: auto;">Inspect Case Study &rarr;</a>
            </div>
          </article>

          <!-- 2. Frost Bank Plaza -->
          <article class="project-card" data-categories="commercial waterproofing plaza highrise">
            <div class="project-thumb">
              <picture>
                <source srcset="assets/images/project-frost-bank.webp" type="image/webp">
                <img src="assets/images/project-frost-bank.jpg" alt="Frost Bank Plaza Commercial Waterproofing Project" width="800" height="500">
              </picture>
              <span class="project-badge-overlay">WATERPROOFING</span>
            </div>
            <div class="project-info">
              <span class="project-location">CORPUS CHRISTI, TEXAS</span>
              <h2 class="project-title"><a href="projects/frost-bank-plaza.html">Frost Bank Plaza</a></h2>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 12px;">
                Commercial high-rise plaza deck restoration. Removal of failed coatings, fleece-reinforced Soprema PMMA liquid waterproofing, coping renewal, and lightning protection.
              </p>
              <div class="project-meta-list">
                <div class="project-meta-item">
                  <strong>Roof Area:</strong>
                  <span>22,000 sq. ft.</span>
                </div>
                <div class="project-meta-item">
                  <strong>System:</strong>
                  <span>Soprema PMMA System</span>
                </div>
                <div class="project-meta-item">
                  <strong>Published Warranty:</strong>
                  <span>20-Year NDL Manufacturer</span>
                </div>
                <div class="project-meta-item">
                  <strong>Challenge:</strong>
                  <span>Active Waterproofing Failure</span>
                </div>
              </div>
              <a href="projects/frost-bank-plaza.html" class="btn btn-outline btn-sm" style="margin-top: auto;">Inspect Case Study &rarr;</a>
            </div>
          </article>

          <!-- 3. Krusteaz Manufacturing Facility -->
          <article class="project-card" data-categories="industrial replacement tpo manufacturing">
            <div class="project-thumb">
              <picture>
                <source srcset="assets/images/project-krusteaz.webp" type="image/webp">
                <img src="assets/images/project-krusteaz.jpg" alt="Krusteaz Manufacturing Facility Commercial Roofing Project" width="800" height="500">
              </picture>
              <span class="project-badge-overlay">INDUSTRIAL</span>
            </div>
            <div class="project-info">
              <span class="project-location">HOPKINSVILLE, KENTUCKY</span>
              <h2 class="project-title"><a href="projects/krusteaz-facility.html">Krusteaz Manufacturing Facility</a></h2>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 12px;">
                Massive 205,869 sq. ft. industrial roof replacement down to deck. Damaged decking replacement, multiple insulation layers, and Johns Manville TPO with precision drip edge.
              </p>
              <div class="project-meta-list">
                <div class="project-meta-item">
                  <strong>Roof Area:</strong>
                  <span>205,869 sq. ft.</span>
                </div>
                <div class="project-meta-item">
                  <strong>System:</strong>
                  <span>JM Fully Adhered TPO</span>
                </div>
                <div class="project-meta-item">
                  <strong>Published Warranty:</strong>
                  <span>20-Yr NDL Labor &amp; Materials</span>
                </div>
                <div class="project-meta-item">
                  <strong>Contractor Warranty:</strong>
                  <span>2-Year Workmanship</span>
                </div>
              </div>
              <a href="projects/krusteaz-facility.html" class="btn btn-outline btn-sm" style="margin-top: auto;">Inspect Case Study &rarr;</a>
            </div>
          </article>

          <!-- 4. Rapha Center -->
          <article class="project-card" data-categories="commercial replacement tpo">
            <div class="project-thumb">
              <picture>
                <source srcset="assets/images/project-rapha-center.webp" type="image/webp">
                <img src="assets/images/project-rapha-center.jpg" alt="Rapha Center Commercial Roofing Project" width="800" height="500">
              </picture>
              <span class="project-badge-overlay">COMMERCIAL</span>
            </div>
            <div class="project-info">
              <span class="project-location">MANCHESTER, TENNESSEE</span>
              <h2 class="project-title"><a href="projects/rapha-center.html">Rapha Center</a></h2>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 12px;">
                Complete membrane tear-off and insulation moisture inspection. Strategic wet insulation replacement, high-density coverboard, and mechanically attached 0.60 mil TPO.
              </p>
              <div class="project-meta-list">
                <div class="project-meta-item">
                  <strong>Roof Area:</strong>
                  <span>10,500 sq. ft.</span>
                </div>
                <div class="project-meta-item">
                  <strong>System:</strong>
                  <span>0.60 Mil Mechanically Attached TPO</span>
                </div>
                <div class="project-meta-item">
                  <strong>Published Warranty:</strong>
                  <span>20-Year Warranty</span>
                </div>
                <div class="project-meta-item">
                  <strong>Scope:</strong>
                  <span>Targeted Insulation Replacement</span>
                </div>
              </div>
              <a href="projects/rapha-center.html" class="btn btn-outline btn-sm" style="margin-top: auto;">Inspect Case Study &rarr;</a>
            </div>
          </article>

          <!-- 5. Malone Plaza -->
          <article class="project-card" data-categories="commercial replacement epdm retail national">
            <div class="project-thumb">
              <picture>
                <source srcset="assets/images/project-malone-plaza.webp" type="image/webp">
                <img src="assets/images/project-malone-plaza.jpg" alt="Malone Plaza Commercial EPDM Roofing Project" width="800" height="500">
              </picture>
              <span class="project-badge-overlay">EPDM RUBBER</span>
            </div>
            <div class="project-info">
              <span class="project-location">ROCHESTER, NEW YORK</span>
              <h2 class="project-title"><a href="projects/malone-plaza.html">Malone Plaza</a></h2>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 12px;">
                Major 100,000 sq. ft. retail plaza retrofit. 60,000 sq. ft. EPDM ballast swap-out, 40,000 sq. ft. mechanically attached EPDM with R-40 insulation, completed in under 60 days.
              </p>
              <div class="project-meta-list">
                <div class="project-meta-item">
                  <strong>Roof Area:</strong>
                  <span>100,000 sq. ft.</span>
                </div>
                <div class="project-meta-item">
                  <strong>System:</strong>
                  <span>EPDM Ballast Swap &amp; Mech Attached</span>
                </div>
                <div class="project-meta-item">
                  <strong>Thermal Value:</strong>
                  <span>High-R R-40 Continuous Polyiso</span>
                </div>
                <div class="project-meta-item">
                  <strong>Execution:</strong>
                  <span>Completed in &lt;60 Calendar Days</span>
                </div>
              </div>
              <a href="projects/malone-plaza.html" class="btn btn-outline btn-sm" style="margin-top: auto;">Inspect Case Study &rarr;</a>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- Inspection CTA -->
    <section class="section-tight bg-surface" style="border-top: 1px solid var(--border-medium);">
      <div class="container text-center">
        <h2 style="font-size: 28px; margin-bottom: 12px;">Have an Upcoming Commercial Project?</h2>
        <p style="color: var(--text-secondary); max-width: 650px; margin: 0 auto 24px;">
          TALTEK provides comprehensive architectural plan review, moisture scanning, and value engineering proposals for property owners and general contractors.
        </p>
        <a href="request-inspection.html" class="btn btn-primary">Schedule a Commercial Project Consultation</a>
      </div>
    </section>
    """

    extra_scripts = """
  <script src="assets/js/portfolio-filter.js"></script>
    """

    render_page(
        "projects.html",
        "Commercial Roofing Projects & Verified Case Studies | TALTEK",
        "Explore authentic commercial and industrial roofing case studies: Nashville General Hospital, Krusteaz Manufacturing, Frost Bank Plaza, Rapha Center, and Malone Plaza.",
        "projects",
        content,
        path_depth=0,
        extra_scripts=extra_scripts
    )

def build_case_studies():
    case_studies_data = [
        {
            "slug": "nashville-general-hospital",
            "title": "Nashville General Hospital",
            "subtitle": "HEALTHCARE CONTINUITY & 20-YEAR NDL TPO REPLACEMENT",
            "location": "Nashville, Tennessee",
            "area": "18,235 sq. ft.",
            "system": "Johns Manville Fully Adhered TPO System",
            "warranty": "20-Year NDL Johns Manville Warranty + 2-Year Contractor Warranty",
            "overview": "Nashville General Hospital required a critical commercial roof replacement over active patient care wings, surgical units, and emergency recovery departments. Water penetration through an aging ballast assembly was threatening internal clinical operations.",
            "challenge": "The existing roof suffered from saturated insulation layers, recurring membrane punctures beneath heavy ballast stone, and inadequate positive drainage leading to extensive ponding water. Hospital operations prohibited internal dust, vibration, or odor migration.",
            "scope": [
                "Careful vacuum removal of tons of river rock ballast stone and degraded membrane.",
                "Thorough inspection and localized replacement of saturated underlying insulation.",
                "Installation of custom tapered polyisocyanurate insulation crickets to establish positive drainage toward internal sumps.",
                "Fully adhered Johns Manville 60-mil white TPO membrane installation with robotic heat-welded field seams.",
                "Comprehensive perimeter detailing, heavy-gauge coping flashing, and curb waterproofing around critical air-handling units."
            ],
            "warranty_details": "Backed by a Johns Manville 20-Year No Dollar Limit (NDL) Labor and Materials Manufacturer Warranty, alongside TALTEK's standard 2-Year Contractor Workmanship Warranty.",
            "img": "assets/images/project-nashville-general.jpg"
        },
        {
            "slug": "frost-bank-plaza",
            "title": "Frost Bank Plaza",
            "subtitle": "COMMERCIAL HIGH-RISE PLAZA DECK LIQUID WATERPROOFING",
            "location": "Corpus Christi, Texas",
            "area": "22,000 sq. ft.",
            "system": "Soprema PMMA Fleece-Reinforced Liquid Waterproofing",
            "warranty": "20-Year NDL Manufacturer Warranty",
            "overview": "Frost Bank Plaza is an iconic commercial financial property featuring an elevated pedestrian plaza deck subject to intense coastal UV radiation, salt air corrosion, and heavy foot traffic.",
            "challenge": "Previous elastomeric coatings had experienced complete adhesive failure, leading to active water infiltration into the corporate offices and parking structures situated directly beneath the plaza terrace.",
            "scope": [
                "Mechanically scarified and stripped failed coating layers down to sound concrete substrate.",
                "Substrate preparation including structural crack routing, primer application, and moisture mitigation.",
                "Application of Soprema PMMA (Polymethyl Methacrylate) cold-fluid liquid resin with embedded non-woven polyester fleece reinforcement.",
                "Complete parapet coping restoration and re-engineering of perimeter counter-flashings.",
                "Replacement and recertification of the facility rooftop lightning protection network."
            ],
            "warranty_details": "Protected by a Soprema 20-Year No Dollar Limit (NDL) Manufacturer Warranty guaranteeing complete monolithic watertight protection across the entire plaza deck.",
            "img": "assets/images/project-frost-bank.jpg"
        },
        {
            "slug": "krusteaz-facility",
            "title": "Krusteaz Manufacturing Facility",
            "subtitle": "205,869 SQ. FT. INDUSTRIAL FOOD PRODUCTION ROOF REPLACEMENT",
            "location": "Hopkinsville, Kentucky",
            "area": "205,869 sq. ft.",
            "system": "Johns Manville Fully Adhered TPO System",
            "warranty": "20-Year NDL Johns Manville Labor & Materials Warranty + 2-Year Contractor Warranty",
            "overview": "The Krusteaz Manufacturing Facility in Hopkinsville, KY is a major food processing and baking plant spanning more than 200,000 square feet under one continuous roof deck.",
            "challenge": "Executing an industrial roof replacement of this scale required zero internal food contamination, zero shutdown of active baking ovens and packaging lines, and strict compliance with FDA food safety regulations.",
            "scope": [
                "Phased removal of existing multi-ply roofing assembly down to the structural steel deck.",
                "Identification and immediate structural replacement of deteriorated 22-gauge steel deck sections.",
                "Installation of multiple staggered layers of high-density polyisocyanurate thermal insulation.",
                "Installation of Johns Manville fully adhered TPO membrane using low-VOC industrial bonding adhesives.",
                "Custom sheet metal fabrication and installation of metal drip edges, expansion joints, and continuous gutter collectors."
            ],
            "warranty_details": "20-Year NDL Johns Manville Labor and Materials Manufacturer Warranty paired with TALTEK's 2-Year Contractor Workmanship Warranty.",
            "img": "assets/images/project-krusteaz.jpg"
        },
        {
            "slug": "rapha-center",
            "title": "Rapha Center",
            "subtitle": "COMMERCIAL TPO RESTORATION & MOISTURE REMEDIATION",
            "location": "Manchester, Tennessee",
            "area": "10,500 sq. ft.",
            "system": "Mechanically Attached 0.60 Mil TPO Membrane",
            "warranty": "20-Year Warranted Roof System",
            "overview": "The Rapha Center commercial facility in Manchester, TN required a rapid-turnaround roofing solution to resolve persistent roof leaks and upgrade overall energy efficiency.",
            "challenge": "Unchecked chronic water intrusion had saturated localized insulation pockets, requiring meticulous thermal moisture verification to avoid unnecessary total replacement of dry insulation zones.",
            "scope": [
                "Full strip of deteriorated existing membrane down to insulation substrate.",
                "Diagnostic moisture inspection and targeted surgical extraction of wet polyiso boards.",
                "Installation of new high-density insulation fill and smooth coverboard substrate.",
                "Installation of mechanically attached 0.60 mil white reflective TPO single-ply membrane.",
                "Perimeter edge metal termination and heat-welded flashing wraps around all mechanical penetrations."
            ],
            "warranty_details": "Covered by a 20-Year Warranted Single-Ply Roof System ensuring long-term watertight reliability.",
            "img": "assets/images/project-rapha-center.jpg"
        },
        {
            "slug": "malone-plaza",
            "title": "Malone Plaza",
            "subtitle": "100,000 SQ. FT. NATIONAL ACCOUNT RETAIL EPDM RETROFIT",
            "location": "Rochester, New York",
            "area": "100,000 sq. ft.",
            "system": "EPDM Ballast Swap-Out & Mechanically Attached EPDM System",
            "warranty": "20-Year Warranted Roof System",
            "overview": "Malone Plaza is a major commercial retail plaza spanning 100,000 sq. ft. of leasable space, executed as a high-priority national account assignment under an aggressive delivery timeline.",
            "challenge": "The project demanded coordinated multi-crew operations across active retail stores during peak shopping seasons, requiring completion in under 60 calendar days despite harsh upstate weather conditions.",
            "scope": [
                "60,000 sq. ft. of heavy ballast stone removal and membrane swap-out.",
                "40,000 sq. ft. of new mechanically attached EPDM synthetic rubber installation.",
                "Installation of high-efficiency continuous R-40 insulation to drastically cut tenant heating bills.",
                "Comprehensive perimeter coping cap installation and commercial scupper expansions.",
                "Full project delivery achieved in less than 60 calendar days without a single retail store closure."
            ],
            "warranty_details": "Supported by a 20-Year Warranted Commercial Roof System and verified national account completion certification.",
            "img": "assets/images/project-malone-plaza.jpg"
        }
    ]

    for c in case_studies_data:
        scope_items = "".join([f"<li>• {item}</li>" for item in c["scope"]])

        content = f"""
        <!-- Project Hero -->
        <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
          <div class="container">
            <div style="max-width: 900px;">
              <span class="eyebrow">REPRESENTATIVE CASE STUDY // {c["location"].upper()}</span>
              <h1 class="section-title" style="font-size: clamp(2.25rem, 5vw, 3.75rem);">{c["title"]}</h1>
              <p class="section-desc">{c["subtitle"]}</p>

              <!-- Verification Notice -->
              <div style="background: rgba(216, 117, 53, 0.1); border-left: 3px solid var(--copper); padding: 12px 16px; margin: 20px 0; border-radius: 0 4px 4px 0;">
                <p style="font-size: 13px; color: var(--text-secondary); margin: 0; line-height: 1.5;">
                  <strong style="color: var(--copper);">Concept Profile Notice:</strong> This case study illustrates commercial roofing engineering capabilities, substrate assemblies, and manufacturer warranty specifications for concept demonstration purposes. Specific contract details and client references are subject to TALTEK company authorization.
                </p>
              </div>

              <div style="display: flex; gap: 16px; margin-top: 24px; flex-wrap: wrap;">
                <span class="tech-badge" style="background: rgba(216,117,53,0.15); border: 1px solid var(--copper); color: var(--copper); padding: 6px 12px; font-family: var(--font-mono); font-size: 12px; border-radius: 4px;">
                  SQUARE FOOTAGE: {c["area"]}
                </span>
                <span class="tech-badge" style="background: var(--bg-card); border: 1px solid var(--border-medium); color: var(--text-primary); padding: 6px 12px; font-family: var(--font-mono); font-size: 12px; border-radius: 4px;">
                  WARRANTY: {c["warranty"]}
                </span>
              </div>
            </div>
          </div>
        </section>

        <!-- Main Editorial Case Study -->
        <section class="section bg-surface" style="border-top: 1px solid var(--border-subtle);">
          <div class="container">
            <!-- Project Primary Photo -->
            <div style="margin-bottom: var(--space-10); border: 1px solid var(--border-medium); border-radius: 8px; overflow: hidden; box-shadow: var(--shadow-lg);">
              <img src="../{c["img"]}" alt="{c["title"]} Commercial Roofing Case Study" width="800" height="500" style="width: 100%; height: auto; max-height: 550px; object-fit: cover;">
            </div>

            <div class="editorial-grid">
              <!-- Left Column: Editorial Details -->
              <div>
                <h2 style="font-size: 24px; color: var(--text-primary); margin-bottom: 12px;">Project Overview</h2>
                <p style="color: var(--text-secondary); line-height: 1.8; margin-bottom: 24px;">{c["overview"]}</p>

                <h3 style="font-size: 20px; color: var(--text-primary); margin-bottom: 12px;">Original Roof Condition &amp; Engineering Challenges</h3>
                <p style="color: var(--text-secondary); line-height: 1.8; margin-bottom: 24px;">{c["challenge"]}</p>

                <h3 style="font-size: 20px; color: var(--text-primary); margin-bottom: 12px;">Scope of Work Performed</h3>
                <ul style="color: var(--text-secondary); line-height: 1.8; margin-bottom: 32px; font-size: 14.5px;">
                  {scope_items}
                </ul>

                <h3 style="font-size: 20px; color: var(--text-primary); margin-bottom: 12px;">Warranty &amp; Long-Term Performance</h3>
                <p style="color: var(--text-secondary); line-height: 1.8; margin-bottom: 24px;">{c["warranty_details"]}</p>
              </div>

              <!-- Right Column: Project Specifications Card -->
              <div>
                <div style="background: var(--bg-card); border: 1px solid var(--border-medium); border-radius: 6px; padding: 24px; position: sticky; top: 100px;">
                  <div style="font-family: var(--font-mono); font-size: 11px; color: var(--copper); font-weight: 700; margin-bottom: 8px;">[ REPRESENTATIVE CASE STUDY RECORD ]</div>
                  <h3 style="font-size: 18px; color: var(--text-primary); margin-bottom: 16px;">Project Telemetry</h3>
                  
                  <div style="display: flex; flex-direction: column; gap: 12px; font-size: 13px; border-bottom: 1px solid var(--border-subtle); padding-bottom: 16px; margin-bottom: 20px;">
                    <div><strong style="color: var(--text-primary); display:block;">Project Name:</strong> <span style="color: var(--text-secondary);">{c["title"]}</span></div>
                    <div><strong style="color: var(--text-primary); display:block;">Location:</strong> <span style="color: var(--text-secondary);">{c["location"]}</span></div>
                    <div><strong style="color: var(--text-primary); display:block;">Roof Area:</strong> <span style="color: var(--text-secondary);">{c["area"]}</span></div>
                    <div><strong style="color: var(--text-primary); display:block;">Roofing System:</strong> <span style="color: var(--text-secondary);">{c["system"]}</span></div>
                    <div><strong style="color: var(--text-primary); display:block;">Published Warranty:</strong> <span style="color: var(--copper); font-weight:700;">{c["warranty"]}</span></div>
                  </div>

                  <a href="../request-inspection.html" class="btn btn-primary" style="width: 100%; margin-bottom: 10px;">Schedule Similar Inspection</a>
                  <a href="../projects.html" class="btn btn-outline btn-sm" style="width: 100%;">View All Portfolio Projects &rarr;</a>
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- CTA Strip -->
        <section class="section-tight bg-elevated" style="border-top: 1px solid var(--border-medium);">
          <div class="container text-center">
            <h2 style="font-size: 26px; margin-bottom: 12px;">Need Similar Commercial Roofing Expertise?</h2>
            <p style="color: var(--text-secondary); max-width: 650px; margin: 0 auto 24px;">
              Contact our Goodlettsville engineering headquarters to schedule a complimentary commercial core sampling and architectural proposal.
            </p>
            <a href="../request-inspection.html" class="btn btn-primary">Schedule Roof Inspection</a>
          </div>
        </section>
        """

        render_page(
            f"projects/{c['slug']}.html",
            f"{c['title']} Case Study | TALTEK Commercial Roofing",
            f"Verified commercial roofing case study: {c['title']} ({c['location']}). {c['area']} {c['system']} with {c['warranty']}.",
            f"projects/{c['slug']}",
            content,
            path_depth=1
        )

if __name__ == "__main__":
    build_projects_index()
    build_case_studies()
    print("All project pages generated successfully!")
