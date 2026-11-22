"""
TALTEK COMMERCIAL ROOFING - COMPANY & CORPORATE PAGES
Generates:
1. about.html
2. team.html (Feature 09: Team Profiles & Verified Accreditations)
3. faq.html
4. careers.html
5. contact.html
"""

from build_site import render_page

def build_about_page():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Enterprise Heritage Since 2009</span>
          <h1 class="section-title">Engineered Commercial Strength</h1>
          <p class="section-desc">
            TALTEK Commercial Roofing was established with a singular mission: to deliver uncompromising engineering precision, structural durability, and professional accountability to commercial and industrial property owners.
          </p>
        </div>

        <div style="display: grid; grid-template-columns: 1.4fr 1fr; gap: var(--space-10); margin-top: var(--space-8); align-items: center;">
          <div>
            <h2 style="font-size: 26px; color: var(--text-primary); margin-bottom: 16px;">Rooted in Goodlettsville, Performing Across 15 States</h2>
            <p style="color: var(--text-secondary); line-height: 1.8; margin-bottom: 16px;">
              From our first commercial roof installation in 2009, TALTEK has grown into an established Southeastern commercial roofing contractor. Headquartered at 1214 S. Dickerson Rd in Goodlettsville, Tennessee, we manage logistics, fabrication, and crew deployments covering healthcare institutions, massive manufacturing plants, and distribution centers across 15 Southeastern states.
            </p>
            <p style="color: var(--text-secondary); line-height: 1.8; margin-bottom: 24px;">
              Over more than a decade of focused operations, we have served more than <strong>10,000 customers</strong> across the Southeastern United States while maintaining an <strong>A+ Better Business Bureau rating</strong> (accredited since 2009). We are not generic residential roofers who occasionally bid on commercial jobs; our entire tooling, crane infrastructure, safety culture, and supply chains are engineered strictly for high-load commercial and industrial assets.
            </p>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; border-top: 1px solid var(--border-subtle); padding-top: 20px;">
              <div>
                <span style="font-family: var(--font-mono); font-size: 11px; color: var(--copper); font-weight: 700; display:block;">ESTABLISHED RECORD</span>
                <strong style="font-size: 24px; color: var(--text-primary); display:block;">EST. 2009</strong>
                <span style="font-size: 13px; color: var(--text-secondary);">BBB Accredited A+ Rating</span>
              </div>
              <div>
                <span style="font-family: var(--font-mono); font-size: 11px; color: var(--copper); font-weight: 700; display:block;">CUSTOMER TRUST</span>
                <strong style="font-size: 24px; color: var(--text-primary); display:block;">10,000+</strong>
                <span style="font-size: 13px; color: var(--text-secondary);">Customers Served</span>
              </div>
            </div>
          </div>

          <div>
            <div style="border: 1px solid var(--border-medium); border-radius: 8px; overflow: hidden; box-shadow: var(--shadow-lg);">
              <picture>
                <source srcset="assets/images/commercial-contractors.webp" type="image/webp">
                <img src="assets/images/commercial-contractors.jpg" alt="TALTEK Certified Commercial Roofing Contractors On Site" width="1000" height="650" style="width: 100%; height: auto; object-fit: cover;">
              </picture>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Core Values Section -->
    <section class="section bg-surface" style="border-top: 1px solid var(--border-subtle);">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Operating Principles</span>
          <h2 class="section-title">The Four Pillars of TALTEK</h2>
        </div>

        <div class="grid grid-cols-4" style="gap: var(--space-6);">
          <div class="industrial-card">
            <div class="card-top-tag">01 // PRECISION</div>
            <h3 class="card-title">Engineering Discipline</h3>
            <p class="card-desc">
              Every detail—from tapered slope calculations to robotic hot-air seam welds—is executed to exact architectural and manufacturer tolerances.
            </p>
          </div>
          <div class="industrial-card">
            <div class="card-top-tag">02 // INTEGRITY</div>
            <h3 class="card-title">Transparent Accounting</h3>
            <p class="card-desc">
              No hidden change orders or vague scopes. We provide forensic core sample verification and detailed line-item specifications before work begins.
            </p>
          </div>
          <div class="industrial-card">
            <div class="card-top-tag">03 // SAFETY</div>
            <h3 class="card-title">OSHA Zero-Incident</h3>
            <p class="card-desc">
              Mandatory OSHA 30-hour supervisor oversight, engineered tie-off lines, and daily safety briefings ensuring zero risk to facility personnel.
            </p>
          </div>
          <div class="industrial-card">
            <div class="card-top-tag">04 // DURABILITY</div>
            <h3 class="card-title">NDL Warranty Options</h3>
            <p class="card-desc">
              Eligible commercial single-ply installations qualify for manufacturer No Dollar Limit (NDL) warranties up to 30 years backed by Johns Manville, GAF, and Elevate.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Accreditation Strip -->
    <section class="section-tight bg-primary" style="border-top: 1px solid var(--border-subtle);">
      <div class="container text-center">
        <h2 style="font-size: 20px; color: var(--text-primary); margin-bottom: 16px;">National Manufacturer Partnerships &amp; Industry Standing</h2>
        <div style="display: flex; justify-content: center; align-items: center; margin-bottom: 24px;">
          <img src="assets/images/certifications.svg" alt="Certified Partners: Johns Manville, GAF, Elevate, CertainTeed, Versico, OSHA 10/30 Safety, BBB A+ Accredited" style="max-height: 80px; width: auto;">
        </div>
        <a href="request-inspection.html" class="btn btn-primary">Schedule a Commercial Roof Consultation</a>
      </div>
    </section>
    """

    render_page(
        "about.html",
        "About TALTEK Commercial Roofing | Goodlettsville, TN Enterprise History",
        "Learn about TALTEK Commercial Roofing: established in 2009, over 10,000 customers served across 15 Southeastern states, headquartered in Goodlettsville, Tennessee.",
        "about",
        content,
        path_depth=0
    )

def build_team_page():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Enterprise Leadership &amp; Safety Officers</span>
          <h1 class="section-title">Leadership &amp; Verified Accreditations</h1>
          <p class="section-desc">
            TALTEK Commercial Roofing operates with verified master manufacturer credentials, OSHA 30 safety compliance, and senior project estimators with decades of single-ply expertise.
          </p>
        </div>

        <!-- Verified Accreditations Display (Feature 09) -->
        <div style="background: var(--bg-card); border: 1px solid var(--border-medium); border-radius: 8px; padding: var(--space-8); margin-bottom: var(--space-12);">
          <div style="text-align: center; margin-bottom: 24px;">
            <span class="eyebrow">Audited Manufacturer Certifications</span>
            <h2 style="font-size: 24px; color: var(--text-primary);">Independent Industry Standing</h2>
            <p style="font-size: 14px; color: var(--text-secondary); max-width: 680px; margin: 8px auto 0;">
              TALTEK has earned top-tier manufacturer contractor designations, entitling our clients to the highest-tier No Dollar Limit (NDL) warranty coverage available in commercial construction.
            </p>
          </div>

          <div class="grid grid-cols-3" style="gap: var(--space-6);">
            <!-- JM -->
            <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); padding: 20px; border-radius: 6px;">
              <span style="font-family: var(--font-mono); font-size: 11px; color: var(--copper); font-weight: 700;">JOHNS MANVILLE</span>
              <h3 style="font-size: 18px; color: var(--text-primary); margin: 6px 0;">Peak Advantage Certified Contractor</h3>
              <p style="font-size: 13px; color: var(--text-secondary);">
                Certified contractor status authorized to install Johns Manville commercial roofing systems with eligible Peak Advantage NDL warranties covering labor and materials.
              </p>
            </div>

            <!-- GAF -->
            <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); padding: 20px; border-radius: 6px;">
              <span style="font-family: var(--font-mono); font-size: 11px; color: var(--copper); font-weight: 700;">GAF COMMERCIAL</span>
              <h3 style="font-size: 18px; color: var(--text-primary); margin: 6px 0;">Certified Commercial Contractor</h3>
              <p style="font-size: 13px; color: var(--text-secondary);">
                Certified commercial roofing installer for GAF EverGuard TPO and single-ply commercial assemblies with manufacturer warranty eligibility.
              </p>
            </div>

            <!-- Elevate -->
            <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); padding: 20px; border-radius: 6px;">
              <span style="font-family: var(--font-mono); font-size: 11px; color: var(--copper); font-weight: 700;">ELEVATE (FIRESTONE)</span>
              <h3 style="font-size: 18px; color: var(--text-primary); margin: 6px 0;">Certified Commercial Applicator</h3>
              <p style="font-size: 13px; color: var(--text-secondary);">
                Certified installer for Elevate RubberGard EPDM, UltraPly TPO, and commercial low-slope single-ply membrane roofing systems.
              </p>
            </div>

            <!-- CertainTeed & Versico -->
            <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); padding: 20px; border-radius: 6px;">
              <span style="font-family: var(--font-mono); font-size: 11px; color: var(--copper); font-weight: 700;">CERTAINTEED &amp; VERSICO</span>
              <h3 style="font-size: 18px; color: var(--text-primary); margin: 6px 0;">Commercial Roofing Partner</h3>
              <p style="font-size: 13px; color: var(--text-secondary);">
                Certified commercial applicator for single-ply and modified commercial roofing systems backed by manufacturer warranty options.
              </p>
            </div>

            <!-- OSHA -->
            <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); padding: 20px; border-radius: 6px;">
              <span style="font-family: var(--font-mono); font-size: 11px; color: var(--status-success); font-weight: 700;">SAFETY LEADERSHIP</span>
              <h3 style="font-size: 18px; color: var(--text-primary); margin: 6px 0;">OSHA 10 &amp; 30 Safety Standard</h3>
              <p style="font-size: 13px; color: var(--text-secondary);">
                Minimum OSHA 10 for all field employees and OSHA 30 for supervisors and management. Weekly safety training and daily job-site Toolbox Talks.
              </p>
            </div>

            <!-- BBB -->
            <div style="background: var(--bg-surface); border: 1px solid var(--border-subtle); padding: 20px; border-radius: 6px;">
              <span style="font-family: var(--font-mono); font-size: 11px; color: var(--copper); font-weight: 700;">BETTER BUSINESS BUREAU</span>
              <h3 style="font-size: 18px; color: var(--text-primary); margin: 6px 0;">BBB Accredited • A+ Rating</h3>
              <p style="font-size: 13px; color: var(--text-secondary);">
                Accredited with the Better Business Bureau since 2009 with continuous A+ rating, reflecting ethical contracting and customer satisfaction.
              </p>
            </div>
          </div>
        </div>

        <!-- Professional Operations Roster -->
        <div class="section-header">
          <span class="eyebrow">Goodlettsville Headquarters</span>
          <h2 class="section-title">Commercial Operations Leadership</h2>
        </div>

        <div class="grid grid-cols-4" style="gap: var(--space-6);">
          <!-- Role 1 -->
          <div class="team-member-card">
            <div class="member-avatar">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            </div>
            <div class="member-info">
              <div class="member-role">DIRECTOR OF OPERATIONS</div>
              <h3 class="member-name">Commercial Operations</h3>
              <p class="member-bio">
                Directs logistics, crane scheduling, and crew deployment across 15 Southeastern states. Over 18 years overseeing complex healthcare and manufacturing projects.
              </p>
              <div class="member-creds">
                <span class="license-tag">OSHA 30</span>
                <span class="license-tag">JM Master</span>
              </div>
            </div>
          </div>

          <!-- Role 2 -->
          <div class="team-member-card">
            <div class="member-avatar">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            </div>
            <div class="member-info">
              <div class="member-role">SENIOR ESTIMATOR</div>
              <h3 class="member-name">Engineering &amp; Estimating</h3>
              <p class="member-bio">
                Specializes in single-ply value engineering, tapered polyiso slope calculations, and structural core sample analysis for national accounts.
              </p>
              <div class="member-creds">
                <span class="license-tag">AutoCAD</span>
                <span class="license-tag">Edge ES-1</span>
              </div>
            </div>
          </div>

          <!-- Role 3 -->
          <div class="team-member-card">
            <div class="member-avatar">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            </div>
            <div class="member-info">
              <div class="member-role">SAFETY &amp; COMPLIANCE</div>
              <h3 class="member-name">Safety Directorate</h3>
              <p class="member-bio">
                Manages TALTEK's Zero-Incident Safety Program, active site tie-off audits, hazardous material mitigation, and annual OSHA employee certifications.
              </p>
              <div class="member-creds">
                <span class="license-tag primary">OSHA 500</span>
                <span class="license-tag">Fall Protection</span>
              </div>
            </div>
          </div>

          <!-- Role 4 -->
          <div class="team-member-card">
            <div class="member-avatar">
              <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            </div>
            <div class="member-info">
              <div class="member-role">QUALITY ASSURANCE</div>
              <h3 class="member-name">Field QA &amp; Inspection</h3>
              <p class="member-bio">
                Performs robotic seam needle probe testing, peel-adhesion tests, and FLIR thermal drone moisture audits prior to manufacturer warranty punch-lists.
              </p>
              <div class="member-creds">
                <span class="license-tag">FLIR Level 1</span>
                <span class="license-tag">FAA Part 107</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    """

    render_page(
        "team.html",
        "Meet Our Team & Verified Certifications | TALTEK Commercial Roofing",
        "Explore TALTEK Commercial Roofing's verified team credentials: Johns Manville Peak Advantage, GAF Master Select, Carlisle ESP, Soprema PMMA, and OSHA 30 certifications.",
        "team",
        content,
        path_depth=0
    )

def build_faq_page():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container" style="max-width: 900px;">
        <div class="section-header text-center">
          <span class="eyebrow">Expert Technical Guidance</span>
          <h1 class="section-title">Frequently Asked Questions</h1>
          <p class="section-desc">
            Technical, operational, and warranty answers for commercial property owners, facility directors, and asset managers evaluating roofing systems.
          </p>
        </div>

        <div style="display: flex; flex-direction: column; gap: 20px; margin-top: var(--space-8);">
          <!-- Q1 -->
          <div style="background: var(--bg-card); border: 1px solid var(--border-medium); border-radius: 6px; padding: 24px;">
            <h2 style="font-size: 18px; color: var(--text-primary); margin-bottom: 10px;">What is a No Dollar Limit (NDL) Manufacturer Warranty?</h2>
            <p style="color: var(--text-secondary); line-height: 1.7; font-size: 14.5px;">
              A No Dollar Limit (NDL) warranty is the gold standard in commercial roofing protection. Issued directly by major manufacturers such as Johns Manville, GAF, or Carlisle, an NDL warranty covers 100% of both labor and material replacement costs required to correct leak defects for a 20, 25, or 30-year term, with zero financial ceiling or pro-rated depreciation. TALTEK is an authorized Master Contractor certified to provide these verified warranties.
            </p>
          </div>

          <!-- Q2 -->
          <div style="background: var(--bg-card); border: 1px solid var(--border-medium); border-radius: 6px; padding: 24px;">
            <h2 style="font-size: 18px; color: var(--text-primary); margin-bottom: 10px;">What is the primary difference between TPO, EPDM, and PVC?</h2>
            <p style="color: var(--text-secondary); line-height: 1.7; font-size: 14.5px;">
              <strong>TPO (Thermoplastic Polyolefin)</strong> is a white, heat-reflective cool roof membrane featuring robotic heat-welded seams; it excels in reducing HVAC cooling costs and is the most popular commercial single-ply system.<br><br>
              <strong>EPDM (Ethylene Propylene Diene Monomer)</strong> is a synthetic black or white rubber membrane with 300% elongation, ideal for cold or cyclic freeze-thaw climates.<br><br>
              <strong>PVC (Polyvinyl Chloride)</strong> with Elvaloy KEE formulations is engineered specifically to resist chemical fumes, animal fats, and restaurant grease exhausts that would degrade TPO or EPDM.
            </p>
          </div>

          <!-- Q3 -->
          <div style="background: var(--bg-card); border: 1px solid var(--border-medium); border-radius: 6px; padding: 24px;">
            <h2 style="font-size: 18px; color: var(--text-primary); margin-bottom: 10px;">Can my facility remain open and operational during a roof replacement?</h2>
            <p style="color: var(--text-secondary); line-height: 1.7; font-size: 14.5px;">
              Yes. The vast majority of our commercial and industrial replacements are completed while tenant businesses, hospitals, and manufacturing lines remain 100% operational. For example, during our 205,869 sq. ft. tear-off at the Krusteaz food manufacturing plant in Kentucky, internal production continued uninterrupted. We implement low-odor adhesives, HEPA dust mitigation, and designated external debris staging chutes.
            </p>
          </div>

          <!-- Q4 -->
          <div style="background: var(--bg-card); border: 1px solid var(--border-medium); border-radius: 6px; padding: 24px;">
            <h2 style="font-size: 18px; color: var(--text-primary); margin-bottom: 10px;">Which states are you licensed to perform commercial roofing in?</h2>
            <p style="color: var(--text-secondary); line-height: 1.7; font-size: 14.5px;">
              TALTEK is headquartered in Goodlettsville, Tennessee, and maintains verified contractor licenses in Tennessee (#CMC-C Commercial), Alabama, Louisiana, Mississippi, North Carolina, South Carolina, and Virginia, with operational logistics and emergency support across 15 Southeastern states.
            </p>
          </div>

          <!-- Q5 -->
          <div style="background: var(--bg-card); border: 1px solid var(--border-medium); border-radius: 6px; padding: 24px;">
            <h2 style="font-size: 18px; color: var(--text-primary); margin-bottom: 10px;">How quickly can you dispatch for an active emergency leak?</h2>
            <p style="color: var(--text-secondary); line-height: 1.7; font-size: 14.5px;">
              We operate a 24/7/365 Emergency Dispatch Service reached directly at <strong>+1 (615) 448-6349</strong>. Priority commercial emergency crews are typically mobilized within 2 to 4 hours across Middle Tennessee and neighboring regional operating hubs.
            </p>
          </div>

          <!-- Q6 -->
          <div style="background: var(--bg-card); border: 1px solid var(--border-medium); border-radius: 6px; padding: 24px;">
            <h2 style="font-size: 18px; color: var(--text-primary); margin-bottom: 10px;">What is included in a TALTEK commercial roof inspection?</h2>
            <p style="color: var(--text-secondary); line-height: 1.7; font-size: 14.5px;">
              Our comprehensive commercial roof inspection includes non-destructive FLIR radiometric thermal imaging (to detect trapped moisture within insulation), physical core extraction (to verify deck and substrate composition), seam probe integrity testing, perimeter flashing audit, and a formal engineering report with remaining lifespan projections and capital budgeting estimates.
            </p>
          </div>
        </div>

        <div style="text-align: center; margin-top: var(--space-10);">
          <h2 style="font-size: 22px; color: var(--text-primary); margin-bottom: 12px;">Have a Question Not Listed Here?</h2>
          <p style="color: var(--text-secondary); margin-bottom: 20px;">Our commercial engineering staff is available to answer any technical specification query.</p>
          <a href="contact.html" class="btn btn-primary">Contact Engineering Staff</a>
        </div>
      </div>
    </section>
    """

    render_page(
        "faq.html",
        "Commercial Roofing FAQ | Warranties, Materials & Process — TALTEK",
        "Frequently asked questions regarding commercial flat roofing: TPO vs EPDM vs PVC, Johns Manville NDL warranties, 15-state licensing, and emergency leak dispatch.",
        "faq",
        content,
        path_depth=0
    )

def build_careers_page():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container" style="max-width: 900px;">
        <div class="section-header text-center">
          <span class="eyebrow">Enterprise Craftsmanship</span>
          <h1 class="section-title">Build Your Career at TALTEK</h1>
          <p class="section-desc">
            Join one of the Southeast's fastest-growing commercial and industrial roofing contractors. We offer industry-leading compensation, OSHA 30 certifications, and a culture of engineering excellence.
          </p>
        </div>

        <div style="background: var(--bg-card); border: 1px solid var(--border-medium); border-radius: 8px; padding: var(--space-8); margin: var(--space-8) 0;">
          <h2 style="font-size: 22px; color: var(--text-primary); margin-bottom: 12px;">Why Work at TALTEK Commercial Roofing?</h2>
          <div class="grid grid-cols-3" style="gap: 16px; margin-top: 20px;">
            <div style="background: var(--bg-surface); padding: 16px; border-radius: 4px;">
              <strong style="color: var(--copper); display: block; margin-bottom: 4px;">Competitive Compensation</strong>
              <span style="font-size: 13px; color: var(--text-secondary);">Top hourly rates and salaried management positions with comprehensive medical, dental, and retirement benefits.</span>
            </div>
            <div style="background: var(--bg-surface); padding: 16px; border-radius: 4px;">
              <strong style="color: var(--copper); display: block; margin-bottom: 4px;">Safety-First Operations</strong>
              <span style="font-size: 13px; color: var(--text-secondary);">Company-funded OSHA 10 and OSHA 30 certifications with modern safety equipment and tie-off gear.</span>
            </div>
            <div style="background: var(--bg-surface); padding: 16px; border-radius: 4px;">
              <strong style="color: var(--copper); display: block; margin-bottom: 4px;">Advanced Tooling</strong>
              <span style="font-size: 13px; color: var(--text-secondary);">Work with robotic Leister hot-air welders, FLIR thermal radiometric drones, and modern crane logistics.</span>
            </div>
          </div>
        </div>

        <div class="section-header" style="margin-top: var(--space-10);">
          <span class="eyebrow">Active Employment Openings</span>
          <h2 class="section-title">Current Opportunities</h2>
        </div>

        <div style="display: flex; flex-direction: column; gap: 16px;">
          <!-- Job 1 -->
          <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 6px; padding: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
            <div>
              <span class="license-tag primary">FULL-TIME // FIELD</span>
              <h3 style="font-size: 18px; color: var(--text-primary); margin: 6px 0;">Commercial Single-Ply Roofing Foreman</h3>
              <p style="font-size: 13px; color: var(--text-secondary);">Goodlettsville, TN (Travel across Southeastern sites) • 5+ years TPO/EPDM experience</p>
            </div>
            <a href="contact.html?inquiry=careers-foreman" class="btn btn-outline btn-sm">Apply via Contact Desk &rarr;</a>
          </div>

          <!-- Job 2 -->
          <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 6px; padding: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
            <div>
              <span class="license-tag primary">FULL-TIME // ESTIMATING</span>
              <h3 style="font-size: 18px; color: var(--text-primary); margin: 6px 0;">Commercial Roofing Project Estimator</h3>
              <p style="font-size: 13px; color: var(--text-secondary);">Headquarters (Goodlettsville, TN) • Bluebeam, The EDGE, single-ply takeoff expertise</p>
            </div>
            <a href="contact.html?inquiry=careers-estimator" class="btn btn-outline btn-sm">Apply via Contact Desk &rarr;</a>
          </div>

          <!-- Job 3 -->
          <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 6px; padding: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px;">
            <div>
              <span class="license-tag primary">FULL-TIME // APPRENTICESHIP</span>
              <h3 style="font-size: 18px; color: var(--text-primary); margin: 6px 0;">Commercial Roofing Technician Apprentice</h3>
              <p style="font-size: 13px; color: var(--text-secondary);">Goodlettsville, TN • Paid training, tool stipend, OSHA certification</p>
            </div>
            <a href="contact.html?inquiry=careers-apprentice" class="btn btn-outline btn-sm">Apply via Contact Desk &rarr;</a>
          </div>
        </div>

        <div style="text-align: center; margin-top: var(--space-8); padding-top: 24px; border-top: 1px solid var(--border-subtle);">
          <p style="color: var(--text-secondary); font-size: 14px;">To submit a general resume, email our HR department directly at <a href="mailto:sales@taltekroofing.com" style="color: var(--copper); font-weight: 700;">sales@taltekroofing.com</a> with subject line "Commercial Career Application".</p>
        </div>
      </div>
    </section>
    """

    render_page(
        "careers.html",
        "Careers & Commercial Roofing Apprenticeships | TALTEK",
        "Explore commercial and industrial roofing careers at TALTEK: single-ply foremen, commercial estimators, and certified technicians in Goodlettsville, TN.",
        "careers",
        content,
        path_depth=0
    )

def build_contact_page():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Direct Corporate Communications</span>
          <h1 class="section-title">Contact TALTEK Commercial Roofing</h1>
          <p class="section-desc">
            Headquartered in Goodlettsville, Tennessee. Contact our commercial estimating desk, dispatch center, or project managers directly.
          </p>
        </div>

        <div style="display: grid; grid-template-columns: 1.2fr 1.8fr; gap: var(--space-10); margin-top: var(--space-8);">
          <!-- Contact Info Column -->
          <div>
            <div style="background: var(--bg-card); border: 1px solid var(--border-medium); border-radius: 8px; padding: 28px; margin-bottom: 24px;">
              <div class="card-top-tag">[ HEADQUARTERS DIRECTORY ]</div>
              <h2 style="font-size: 20px; color: var(--text-primary); margin-bottom: 16px;">Corporate Office</h2>

              <div style="display: flex; flex-direction: column; gap: 16px; font-size: 14px;">
                <div style="display: flex; gap: 12px;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--copper); flex-shrink: 0;"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                  <div>
                    <strong style="color: var(--text-primary); display:block;">Physical Address:</strong>
                    <span style="color: var(--text-secondary);">1214 S. Dickerson Rd<br>Goodlettsville, TN 37072, USA</span>
                  </div>
                </div>

                <div style="display: flex; gap: 12px;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--copper); flex-shrink: 0;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                  <div>
                    <strong style="color: var(--text-primary); display:block;">Main Dispatch Telephone:</strong>
                    <a href="tel:+16154486349" style="color: var(--copper); font-weight: 700;">+1 (615) 448-6349</a>
                  </div>
                </div>

                <div style="display: flex; gap: 12px;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--copper); flex-shrink: 0;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                  <div>
                    <strong style="color: var(--text-primary); display:block;">Official Email:</strong>
                    <a href="mailto:sales@taltekroofing.com" style="color: var(--text-primary);">sales@taltekroofing.com</a>
                  </div>
                </div>

                <div style="display: flex; gap: 12px;">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="color: var(--copper); flex-shrink: 0;"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                  <div>
                    <strong style="color: var(--text-primary); display:block;">Operating Hours:</strong>
                    <span style="color: var(--text-secondary);">Office: Mon&ndash;Fri 7:00 AM &ndash; 6:00 PM CT<br>Emergency Dispatch: 24 Hours / 7 Days</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Emergency Box -->
            <div style="background: rgba(216,117,53,0.1); border: 1px solid var(--copper); border-radius: 8px; padding: 20px;">
              <h3 style="font-size: 16px; color: var(--copper); margin-bottom: 6px;">24/7 Rapid Emergency Response</h3>
              <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 12px;">
                For active commercial leaks or storm damage across our 15 Southeastern operating states, call our direct emergency line immediately.
              </p>
              <a href="tel:+16154486349" class="btn btn-primary btn-sm" style="width: 100%;">Call Emergency Line: (615) 448-6349</a>
            </div>
          </div>

          <!-- Contact Form Column -->
          <div style="background: var(--bg-surface); border: 1px solid var(--border-medium); border-radius: 8px; padding: clamp(1.5rem, 4vw, 2.5rem);">
            <h2 style="font-size: 20px; color: var(--text-primary); margin-bottom: 8px;">Transmit Commercial Message</h2>
            <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 24px;">Complete the form below. An engineering representative will respond promptly.</p>

            <form id="general-contact-form">
              <!-- Honeypot -->
              <input type="text" name="hp_contact_check" style="display:none !important;" tabindex="-1" autocomplete="off" aria-hidden="true">

              <div class="grid grid-cols-2" style="gap: 16px;">
                <div class="form-group">
                  <label for="contact_name" class="form-label">Full Name *</label>
                  <input type="text" id="contact_name" name="contact_name" class="form-control" placeholder="Jane Smith" required>
                </div>
                <div class="form-group">
                  <label for="contact_company" class="form-label">Company / Entity *</label>
                  <input type="text" id="contact_company" name="contact_company" class="form-control" placeholder="Tennessee Logistics LLC" required>
                </div>
              </div>

              <div class="grid grid-cols-2" style="gap: 16px;">
                <div class="form-group">
                  <label for="contact_email" class="form-label">Business Email *</label>
                  <input type="email" id="contact_email" name="contact_email" class="form-control" placeholder="jsmith@company.com" required>
                </div>
                <div class="form-group">
                  <label for="contact_phone" class="form-label">Direct Phone *</label>
                  <input type="tel" id="contact_phone" name="contact_phone" class="form-control" placeholder="(615) 448-6349" required>
                </div>
              </div>

              <div class="form-group">
                <label for="contact_subject" class="form-label">Department / Inquiry Type</label>
                <select id="contact_subject" name="contact_subject" class="form-control">
                  <option value="New Roof Proposal" selected>New Roof Proposal / Plan Review</option>
                  <option value="Emergency Leak Service">Emergency Leak Service</option>
                  <option value="Warranty Administration">Warranty Administration / NDL Inquiries</option>
                  <option value="General Commercial Inquiry">General Commercial Inquiry</option>
                  <option value="Career Application">Employment / Career Application</option>
                </select>
              </div>

              <div class="form-group">
                <label for="contact_message" class="form-label">Message / Project Summary *</label>
                <textarea id="contact_message" name="contact_message" class="form-control" placeholder="Please outline your facility location, square footage, and project timeline..." required></textarea>
              </div>

              <button type="submit" class="btn btn-primary" style="width: 100%;">Transmit Commercial Message</button>
              
              <div id="contact-success-msg" style="display:none; background: rgba(16, 185, 129, 0.12); border: 1px solid var(--status-success); color: var(--text-primary); padding: 18px; border-radius: 6px; margin-top: 16px; font-size: 13.5px; text-align: left;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                  <span style="color: var(--status-success); font-weight: 700; font-size: 16px;">&check;</span>
                  <strong style="color: var(--status-success);">Inquiry Formatted For Dispatch</strong>
                </div>
                <p style="color: var(--text-secondary); margin-bottom: 12px; line-height: 1.5;">
                  Your message has been pre-formatted for direct transmission to TALTEK commercial estimating. Click below to send via your email client or contact our Goodlettsville dispatch desk directly:
                </p>
                <div style="display: flex; gap: 10px; flex-wrap: wrap;">
                  <a id="contact-mailto-link" href="mailto:sales@taltekroofing.com" class="btn btn-primary btn-sm">Transmit Via Email Client &rarr;</a>
                  <a href="tel:+16154486349" class="btn btn-secondary btn-sm">Direct Phone: (615) 448-6349</a>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>

    <!-- PHASE 3: GOOGLE MAPS & BUSINESS LOCATION SECTION -->
    <section class="section bg-surface" id="location-map" aria-label="TALTEK Headquarters Google Maps Location" style="border-top: 1px solid var(--border-subtle);">
      <div class="container">
        <div class="section-header text-center">
          <span class="eyebrow">Goodlettsville Headquarters &amp; Operations Center</span>
          <h2 class="section-title">Visit Our Headquarters</h2>
          <p class="section-desc">
            Conveniently situated in Goodlettsville, Tennessee, providing central logistics dispatch for commercial roofing crews and emergency response units throughout the Southeast.
          </p>
        </div>

        <div class="map-location-card">
          <!-- Location Details & Action Strip -->
          <div class="map-info-bar">
            <div class="map-address-block">
              <div class="card-top-tag">[ CORPORATE GEOLOCATION ]</div>
              <h3 style="font-size: 18px; color: var(--text-primary); margin: 6px 0;">1214 S. Dickerson Rd, Goodlettsville, TN 37072</h3>
              <p style="font-size: 13px; color: var(--text-secondary); margin: 0;">
                Serving Davidson, Sumner, Robertson, Wilson, Williamson, and 15 Southeastern States.
              </p>
            </div>
            <div class="map-actions-group">
              <a href="https://www.google.com/maps/dir/?api=1&destination=1214+S+Dickerson+Rd+Goodlettsville+TN+37072+USA" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="3 11 22 2 13 21 11 13 3 11"></polygon></svg>
                Get Directions
              </a>
              <a href="https://www.google.com/maps/search/?api=1&query=1214+S+Dickerson+Rd+Goodlettsville+TN+37072+USA" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>
                Open in Google Maps
              </a>
            </div>
          </div>

          <!-- Responsive Google Maps Embed with Fallback -->
          <div class="map-embed-wrapper">
            <iframe 
              src="https://maps.google.com/maps?q=1214+S+Dickerson+Rd,+Goodlettsville,+TN+37072&amp;t=&amp;z=15&amp;ie=UTF8&amp;iwloc=&amp;output=embed" 
              class="google-map-iframe" 
              loading="lazy" 
              title="TALTEK Commercial Roofing Headquarters Map Location" 
              aria-label="Interactive Google Map showing TALTEK Commercial Roofing headquarters in Goodlettsville, TN"
              referrerpolicy="no-referrer-when-downgrade">
            </iframe>
            <!-- Offline / No-Script Fallback -->
            <noscript>
              <div class="map-fallback-box">
                <p><strong>TALTEK Commercial Roofing Headquarters</strong></p>
                <p>1214 S. Dickerson Rd, Goodlettsville, TN 37072, USA</p>
                <a href="https://www.google.com/maps/search/?api=1&query=1214+S+Dickerson+Rd+Goodlettsville+TN+37072+USA" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm">
                  View on Google Maps &rarr;
                </a>
              </div>
            </noscript>
          </div>
        </div>
      </div>
    </section>
    """

    extra_scripts = """
  <script>
    document.getElementById('general-contact-form')?.addEventListener('submit', function(e) {
      e.preventDefault();
      const hp = this.querySelector('input[name="hp_contact_check"]');
      if (hp && hp.value) return;

      const name = this.querySelector('#contact_name')?.value || '';
      const email = this.querySelector('#contact_email')?.value || '';
      const phone = this.querySelector('#contact_phone')?.value || '';
      const subject = this.querySelector('#contact_subject')?.value || 'Commercial Roofing Inquiry';
      const message = this.querySelector('#contact_message')?.value || '';

      const mailtoBody = `Name: ${name}%0D%0APhone: ${phone}%0D%0AEmail: ${email}%0D%0ADepartment: ${subject}%0D%0A%0D%0AProject Message:%0D%0A${encodeURIComponent(message)}`;
      const mailtoHref = `mailto:sales@taltekroofing.com?subject=${encodeURIComponent('TALTEK Commercial Inquiry: ' + subject)}&body=${mailtoBody}`;

      const mailtoBtn = document.getElementById('contact-mailto-link');
      if (mailtoBtn) mailtoBtn.href = mailtoHref;

      const successMsg = document.getElementById('contact-success-msg');
      if (successMsg) {
        successMsg.style.display = 'block';
        successMsg.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    });
  </script>
    """

    render_page(
        "contact.html",
        "Contact TALTEK Commercial Roofing | Goodlettsville, TN Headquarters",
        "Contact TALTEK Commercial Roofing: 1214 S. Dickerson Rd, Goodlettsville, TN 37072. Phone: +1 (615) 448-6349. Email: sales@taltekroofing.com. Serving 15 Southeastern states.",
        "contact",
        content,
        path_depth=0,
        extra_scripts=extra_scripts
    )

if __name__ == "__main__":
    build_about_page()
    build_team_page()
    build_faq_page()
    build_careers_page()
    build_contact_page()
    print("All corporate company pages generated successfully!")
