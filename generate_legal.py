"""
TALTEK COMMERCIAL ROOFING - LEGAL & PRIVACY COMPLIANCE SUITE
Generates all 7 US legal, privacy, and accessibility pages:
1. privacy-policy.html
2. cookie-policy.html
3. terms.html
4. accessibility.html
5. california-privacy-rights.html
6. privacy-request.html
7. sms-terms.html
"""

from build_site import render_page

def build_privacy_policy():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container" style="max-width: 920px;">
        <span class="eyebrow">US Legal &amp; Regulatory Compliance</span>
        <h1 class="section-title">Privacy Policy</h1>
        <p style="color: var(--text-muted); font-family: var(--font-mono); font-size: 13px; margin-bottom: 24px;">
          EFFECTIVE DATE: NOVEMBER 2026 • LAST REVIEWED: NOVEMBER 2026 • HEADQUARTERS: GOODLETTSVILLE, TN
        </p>

        <div class="editorial-body" style="color: var(--text-secondary); line-height: 1.8; font-size: 15px;">
          <p>
            TALTEK Commercial Roofing ("TALTEK", "we", "us", or "our") is a commercial and industrial roofing enterprise headquartered at <strong>1214 S. Dickerson Rd, Goodlettsville, TN 37072, USA</strong>. We respect your personal privacy and are committed to transparent, lawful data processing practices in compliance with applicable United States federal laws and comprehensive state privacy statutes, including the <strong>Tennessee Information Protection Act (TIPA)</strong> and the <strong>California Consumer Privacy Act (CCPA/CPRA)</strong>.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">1. Information We Collect</h2>
          <p>We collect information directly from you when you request a commercial roof inspection, submit a proposal inquiry, use our interactive estimator, or communicate with our engineering desk. The categories of personal information collected include:</p>
          <ul style="margin: 12px 0 16px 20px;">
            <li><strong>Identifiers:</strong> Full name, business email address, direct telephone number, company or facility name.</li>
            <li><strong>Commercial Property Details:</strong> Physical building address, square footage estimates, existing roof material specifications, leak observations.</li>
            <li><strong>Internet &amp; Network Activity:</strong> IP address, browser type, device telemetry, pages viewed, and session metrics (subject to cookie consent choices).</li>
            <li><strong>Communications Data:</strong> Records of inquiries, customer service chat interactions, and correspondence notes.</li>
          </ul>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">2. Purpose &amp; Use of Personal Information</h2>
          <p>We use your personal information solely for legitimate commercial business purposes:</p>
          <ul style="margin: 12px 0 16px 20px;">
            <li>To dispatch roofing engineers and schedule on-site physical core sampling and moisture inspections.</li>
            <li>To calculate and deliver formal commercial roofing proposals, estimates, and NDL warranty specifications.</li>
            <li>To fulfill contractual obligations and provide customer support.</li>
            <li>To comply with state contractor licensing boards, insurance carrier verifications, and safety compliance records.</li>
            <li>To analyze and optimize website technical performance and security.</li>
          </ul>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">3. Information Sharing &amp; Third Parties</h2>
          <p>
            <strong>TALTEK does not sell or rent personal information to third parties.</strong> We only disclose necessary information to trusted third-party service providers who assist us in operating our business under strict confidentiality agreements:
          </p>
          <ul style="margin: 12px 0 16px 20px;">
            <li>Certified roofing manufacturers (e.g. Johns Manville, GAF, Carlisle, Soprema) solely for issuing authorized NDL warranties.</li>
            <li>Secure cloud hosting, form management, and database infrastructure providers.</li>
            <li>Analytics and mapping providers, only when authorized under your active cookie preferences.</li>
            <li>Law enforcement or regulatory bodies when required by legal process or state licensing audits.</li>
          </ul>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">4. Tennessee Information Protection Act (TIPA) Rights</h2>
          <p>
            Under the Tennessee Information Protection Act (TIPA), Tennessee residents have specific legal rights regarding their personal information:
          </p>
          <ul style="margin: 12px 0 16px 20px;">
            <li><strong>Right to Confirm &amp; Access:</strong> Confirm whether TALTEK is processing your personal information and access such data.</li>
            <li><strong>Right to Correct:</strong> Correct inaccuracies in your personal information.</li>
            <li><strong>Right to Delete:</strong> Request deletion of personal information provided by or obtained about you.</li>
            <li><strong>Right to Obtain Copy:</strong> Obtain a portable copy of personal information previously provided.</li>
            <li><strong>Right to Opt Out:</strong> Opt out of processing for targeted advertising, sale of personal information, or significant profiling.</li>
            <li><strong>Right to Appeal:</strong> If TALTEK declines to take action on a request, you have the right to appeal our decision within a reasonable time.</li>
          </ul>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">5. Global Privacy Control (GPC) &amp; Cookie Consent</h2>
          <p>
            Our website implements automated detection of <strong>Global Privacy Control (GPC)</strong> signals. If your browser transmits a GPC signal, optional tracking and analytics categories are pre-set to opted-out. You may also modify granular cookie preferences anytime using our persistent <button type="button" data-cookie-action="open-preferences" style="background:none; border:none; color:var(--copper); text-decoration:underline; cursor:pointer;">[ Cookie Preferences ]</button> tool.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">6. Data Retention &amp; Security Measures</h2>
          <p>
            We implement industry-standard administrative, physical, and technical safeguards including HTTPS TLS 1.3 encryption, secure database access controls, input sanitization, and automated rate limiting. We retain commercial inquiry data only as long as necessary to fulfill the commercial proposal, maintain warranty and licensing records, or satisfy statutory record-keeping periods.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">7. Submitting a Privacy Rights Request</h2>
          <p>
            To exercise your privacy rights under TIPA, CCPA, or applicable state laws, please submit an official request through our online portal:
          </p>
          <p style="margin: 16px 0;">
            <a href="privacy-request.html" class="btn btn-primary btn-sm">Submit Privacy Rights Request</a>
          </p>
          <p>
            You may also contact our designated Privacy Compliance Officer by mail or telephone:<br>
            <strong>TALTEK Commercial Roofing</strong><br>
            Attn: Privacy Compliance Officer<br>
            1214 S. Dickerson Rd, Goodlettsville, TN 37072, USA<br>
            Phone: +1 (615) 448-6349 • Email: <a href="mailto:sales@taltekroofing.com" style="color: var(--copper);">sales@taltekroofing.com</a>
          </p>
        </div>
      </div>
    </section>
    """

    render_page(
        "privacy-policy.html",
        "Privacy Policy | Tennessee TIPA & US Compliance — TALTEK Commercial Roofing",
        "TALTEK Commercial Roofing Privacy Policy. Learn about our data practices, consumer privacy rights under TIPA and CCPA, security standards, and request procedures.",
        "privacy-policy",
        content,
        path_depth=0
    )

def build_cookie_policy():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container" style="max-width: 920px;">
        <span class="eyebrow">Tracking Technologies Transparency</span>
        <h1 class="section-title">Cookie Policy</h1>
        <p style="color: var(--text-muted); font-family: var(--font-mono); font-size: 13px; margin-bottom: 24px;">
          EFFECTIVE DATE: NOVEMBER 2026 • REVISED: NOVEMBER 2026 • TALTEK COMMERCIAL ROOFING
        </p>

        <div class="editorial-body" style="color: var(--text-secondary); line-height: 1.8; font-size: 15px;">
          <p>
            This Cookie Policy explains how TALTEK Commercial Roofing ("TALTEK", "we", "us") uses cookies and similar tracking technologies on our website. We believe in complete transparency and empower visitors with granular, functional control over optional tracking technologies.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">1. What Are Cookies?</h2>
          <p>
            Cookies are small text files placed on your device by websites you visit. They are widely used to make websites function efficiently, preserve session preferences, and provide analytical data to website operators.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">2. Categories of Cookies We Use</h2>
          
          <div style="background: var(--bg-card); border: 1px solid var(--border-medium); border-radius: 6px; padding: 20px; margin: 16px 0;">
            <strong style="color: var(--text-primary); display:block; margin-bottom: 4px;">Category 1: Strictly Necessary Cookies (Always Active)</strong>
            <p style="font-size: 13px; color: var(--text-secondary); margin: 0;">
              These cookies are essential for you to navigate the website and use its features, such as accessing secure forms, maintaining load balancer routing, and recording your privacy preferences. They cannot be switched off in our systems.
            </p>
          </div>

          <div style="background: var(--bg-card); border: 1px solid var(--border-medium); border-radius: 6px; padding: 20px; margin: 16px 0;">
            <strong style="color: var(--text-primary); display:block; margin-bottom: 4px;">Category 2: Performance &amp; Analytics Cookies (Optional)</strong>
            <p style="font-size: 13px; color: var(--text-secondary); margin: 0;">
              These cookies allow us to count visits and traffic sources so we can measure and improve the technical performance of our website. They help us understand which service pages and case studies are most useful to commercial facility managers.
            </p>
          </div>

          <div style="background: var(--bg-card); border: 1px solid var(--border-medium); border-radius: 6px; padding: 20px; margin: 16px 0;">
            <strong style="color: var(--text-primary); display:block; margin-bottom: 4px;">Category 3: Functional Cookies (Optional)</strong>
            <p style="font-size: 13px; color: var(--text-secondary); margin: 0;">
              These cookies enable enhanced functionality and personalization, such as remembering your selected state on our service area map, preserving commercial roof estimator slider values, and maintaining live AI assistant chat history.
            </p>
          </div>

          <div style="background: var(--bg-card); border: 1px solid var(--border-medium); border-radius: 6px; padding: 20px; margin: 16px 0;">
            <strong style="color: var(--text-primary); display:block; margin-bottom: 4px;">Category 4: Advertising &amp; Marketing Cookies (Optional)</strong>
            <p style="font-size: 13px; color: var(--text-secondary); margin: 0;">
              These cookies may be set through our site by commercial advertising partners to build a profile of your business interests and show you relevant commercial roofing announcements on other professional platforms.
            </p>
          </div>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">3. Zero Non-Consensual Pre-Loading</h2>
          <p>
            In strict compliance with modern privacy standards, <strong>optional analytics, functional, and marketing scripts do NOT load or execute prior to receiving affirmative user consent</strong>. If you click "Reject Optional", only strictly necessary cookies are enabled.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">4. Global Privacy Control (GPC)</h2>
          <p>
            We recognize and honor Global Privacy Control (GPC) signals broadcast by supported web browsers. When GPC is detected, all optional tracking categories are automatically defaulted to opted-out.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">5. Managing Your Preferences Anytime</h2>
          <p>
            You can modify or withdraw your consent at any time by clicking the persistent button below:
          </p>
          <p style="margin: 20px 0;">
            <button type="button" class="btn btn-primary btn-sm" data-cookie-action="open-preferences">Open Cookie Preferences Manager</button>
          </p>
        </div>
      </div>
    </section>
    """

    render_page(
        "cookie-policy.html",
        "Cookie Policy | Tracking Technologies & Consent — TALTEK",
        "TALTEK Commercial Roofing Cookie Policy. Understand our cookie categories, Global Privacy Control (GPC) compliance, and manage your preferences.",
        "cookie-policy",
        content,
        path_depth=0
    )

def build_terms_page():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container" style="max-width: 920px;">
        <span class="eyebrow">Commercial Terms of Engagement</span>
        <h1 class="section-title">Terms &amp; Conditions</h1>
        <p style="color: var(--text-muted); font-family: var(--font-mono); font-size: 13px; margin-bottom: 24px;">
          EFFECTIVE DATE: NOVEMBER 2026 • TALTEK COMMERCIAL ROOFING • GOODLETTSVILLE, TN
        </p>

        <div class="editorial-body" style="color: var(--text-secondary); line-height: 1.8; font-size: 15px;">
          <p>
            Welcome to the official website of TALTEK Commercial Roofing ("TALTEK", "Company", "we", "us"). By accessing or utilizing this website (https://taltekroofing.com/), you agree to be bound by these commercial Terms and Conditions. If you do not agree to these terms, please discontinue use of this website.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">1. Website Purpose &amp; Non-Binding Estimates</h2>
          <p>
            This website provides commercial roofing educational resources, portfolio documentation, service descriptions, and preliminary calculation tools. <strong>All figures generated by the interactive Commercial Roof Estimator or Financing Calculator represent preliminary mathematical models for capital budgeting purposes only.</strong> They do NOT constitute binding bids, guaranteed pricing, credit origination, or formal contracts. Formal proposals require on-site physical core sampling, moisture scans, and written contract execution signed by an authorized TALTEK officer.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">2. Warranties &amp; Manufacturer Representation</h2>
          <p>
            References on this website to "No Dollar Limit (NDL)" warranties reflect authentic manufacturer warranty programs offered by third-party manufacturers (e.g. Johns Manville, GAF, Carlisle, Soprema). Manufacturer warranties are issued directly by the manufacturer and are governed exclusively by their specific written terms, maintenance conditions, and inspection approvals. TALTEK provides its own separate 2-Year Contractor Workmanship Warranty under executed installation contracts.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">3. Intellectual Property Rights</h2>
          <p>
            All content, graphics, vector diagrams, code, logos, and case study descriptions on this website are the intellectual property of TALTEK Commercial Roofing or licensed partners. Unauthorized copying, scraping, or reproduction of proprietary materials is strictly prohibited.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">4. Limitation of Liability</h2>
          <p>
            To the maximum extent permitted under applicable law, TALTEK shall not be liable for any indirect, incidental, consequential, or punitive damages arising from your access to or inability to access this website. While we endeavor to maintain accurate specifications, roofing building codes and manufacturer guidelines vary by local jurisdiction.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">5. Governing Law &amp; Jurisdiction</h2>
          <p>
            These Terms and Conditions shall be governed by and construed in accordance with the laws of the <strong>State of Tennessee, United States</strong>, without giving effect to conflict of law principles. Any legal action arising hereunder shall be filed exclusively in the state or federal courts located in Davidson County or Sumner County, Tennessee.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">6. Contact Information</h2>
          <p>
            For legal inquiries regarding these terms:<br>
            <strong>TALTEK Commercial Roofing</strong><br>
            1214 S. Dickerson Rd, Goodlettsville, TN 37072, USA<br>
            Phone: +1 (615) 448-6349 • Email: <a href="mailto:sales@taltekroofing.com" style="color: var(--copper);">sales@taltekroofing.com</a>
          </p>
        </div>
      </div>
    </section>
    """

    render_page(
        "terms.html",
        "Terms and Conditions | Commercial Terms of Engagement — TALTEK",
        "Terms and Conditions for TALTEK Commercial Roofing. Scope of use, non-binding estimates disclosure, warranty terms, and Tennessee governing law.",
        "terms",
        content,
        path_depth=0
    )

def build_accessibility_page():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container" style="max-width: 920px;">
        <span class="eyebrow">Digital Inclusion Standards</span>
        <h1 class="section-title">Accessibility Statement</h1>
        <p style="color: var(--text-muted); font-family: var(--font-mono); font-size: 13px; margin-bottom: 24px;">
          CONFORMANCE TARGET: WCAG 2.2 LEVEL AA • TALTEK COMMERCIAL ROOFING
        </p>

        <div class="editorial-body" style="color: var(--text-secondary); line-height: 1.8; font-size: 15px;">
          <p>
            TALTEK Commercial Roofing is committed to ensuring digital accessibility for all people, including visitors with visual, auditory, motor, or cognitive disabilities. We continually review and enhance our digital experience in alignment with the <strong>Web Content Accessibility Guidelines (WCAG) 2.2 Level AA</strong> standards.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">1. Concrete Accessibility Measures Implemented</h2>
          <p>We incorporate the following accessibility engineering standards across our entire web architecture:</p>
          <ul style="margin: 12px 0 16px 20px;">
            <li><strong>Keyboard Navigability:</strong> All navigation menus, dropdowns, modal windows, sliders, and form controls are fully navigable via standard keyboard inputs (Tab, Shift+Tab, Enter, Spacebar, Arrow keys).</li>
            <li><strong>Visible Focus Indicators:</strong> High-contrast focus rings (2px solid copper outline with offset) are rendered on all interactive elements during keyboard navigation.</li>
            <li><strong>Skip to Content Link:</strong> A dedicated, keyboard-accessible skip link is present at the very top of every page, allowing screen reader users to bypass repetitive navigation.</li>
            <li><strong>Semantic HTML Hierarchy:</strong> Proper use of document landmark regions (<code>&lt;header&gt;</code>, <code>&lt;main&gt;</code>, <code>&lt;nav&gt;</code>, <code>&lt;footer&gt;</code>, <code>&lt;aside&gt;</code>) and hierarchical heading tags (H1 through H4).</li>
            <li><strong>Accessible Form Controls:</strong> Every form input features an explicitly associated <code>&lt;label&gt;</code>, descriptive hint, and ARIA live regions for error reporting.</li>
            <li><strong>Reduced-Motion Support:</strong> Comprehensive <code>@media (prefers-reduced-motion: reduce)</code> CSS rules immediately neutralize animations, transitions, and automated loops for visitors with vestibular sensitivities.</li>
            <li><strong>High-Contrast Color Ratios:</strong> Text elements strictly exceed the WCAG 4.5:1 minimum contrast ratio against dark and light backgrounds.</li>
            <li><strong>Accessible Interactive Sliders:</strong> Our Before/After comparison slider and Estimator inputs implement ARIA slider roles (<code>aria-valuemin</code>, <code>aria-valuemax</code>, <code>aria-valuenow</code>) and support arrow key adjustments.</li>
          </ul>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">2. Assistive Technology Feedback &amp; Assistance</h2>
          <p>
            We welcome your feedback on the accessibility of the TALTEK website. If you encounter any accessibility barrier or require assistance accessing technical commercial roofing documents, please contact us directly:
          </p>
          <p style="margin: 16px 0;">
            <strong>TALTEK Commercial Roofing Accessibility Desk</strong><br>
            Phone: <a href="tel:+16154486349" style="color: var(--copper); font-weight:700;">+1 (615) 448-6349</a><br>
            Email: <a href="mailto:sales@taltekroofing.com" style="color: var(--copper);">sales@taltekroofing.com</a><br>
            Mailing Address: 1214 S. Dickerson Rd, Goodlettsville, TN 37072, USA
          </p>
          <p>We endeavor to respond to accessibility inquiries within one to two business days.</p>
        </div>
      </div>
    </section>
    """

    render_page(
        "accessibility.html",
        "Accessibility Statement | WCAG 2.2 AA Standards — TALTEK",
        "TALTEK Commercial Roofing Accessibility Statement. Details our conformance to WCAG 2.2 Level AA accessibility standards, keyboard navigation, and support contact.",
        "accessibility",
        content,
        path_depth=0
    )

def build_california_privacy():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container" style="max-width: 920px;">
        <span class="eyebrow">California Consumer Privacy Act (CCPA/CPRA)</span>
        <h1 class="section-title">California Privacy Rights Notice</h1>
        <p style="color: var(--text-muted); font-family: var(--font-mono); font-size: 13px; margin-bottom: 24px;">
          SUPPLEMENT TO TALTEK PRIVACY POLICY • DO NOT SELL OR SHARE PERSONAL INFORMATION
        </p>

        <div class="editorial-body" style="color: var(--text-secondary); line-height: 1.8; font-size: 15px;">
          <p>
            This California Privacy Rights Notice supplements TALTEK Commercial Roofing's general Privacy Policy and applies solely to California residents pursuant to the <strong>California Consumer Privacy Act of 2018 (CCPA)</strong> and the <strong>California Privacy Rights Act of 2020 (CPRA)</strong>.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">1. Notice at Collection: Categories Collected</h2>
          <p>In the preceding 12 months, TALTEK has collected the following categories of commercial information:</p>
          <ul style="margin: 12px 0 16px 20px;">
            <li><strong>Identifiers:</strong> Name, business email, telephone, company name, IP address.</li>
            <li><strong>Commercial Records:</strong> Commercial facility locations, roof dimensions, quote requests, project contracts.</li>
            <li><strong>Internet Activity:</strong> Browsing history on taltekroofing.com, interaction with estimator tools.</li>
            <li><strong>Professional Data:</strong> Job title, employer entity, commercial real estate management affiliation.</li>
          </ul>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">2. Statement Regarding "Sale" or "Sharing" of Personal Data</h2>
          <p>
            <strong>TALTEK DOES NOT SELL YOUR PERSONAL INFORMATION.</strong> We do not exchange commercial contact information or property records for monetary consideration. Furthermore, we do not share personal information with third parties for cross-context behavioral advertising without affirmative cookie consent.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">3. Your California Consumer Rights</h2>
          <p>As a California consumer, you have the right to:</p>
          <ul style="margin: 12px 0 16px 20px;">
            <li><strong>Right to Know / Access:</strong> Request disclosure of the specific pieces and categories of personal information collected.</li>
            <li><strong>Right to Delete:</strong> Request deletion of personal information collected, subject to legal record retention exemptions.</li>
            <li><strong>Right to Correct:</strong> Request correction of inaccurate personal information maintained about you.</li>
            <li><strong>Right to Opt-Out of Sale / Sharing:</strong> Opt out of any future sale or sharing of personal data.</li>
            <li><strong>Right to Non-Discrimination:</strong> Receive equal service and pricing without discrimination for exercising privacy rights.</li>
          </ul>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">4. Submitting a Verified California Request</h2>
          <p>
            To submit a request under CCPA/CPRA, please use our secure request portal:
          </p>
          <p style="margin: 16px 0;">
            <a href="privacy-request.html" class="btn btn-primary btn-sm">Submit CCPA/CPRA Privacy Request</a>
          </p>
          <p>You may also call toll-free at +1 (615) 448-6349 or email <a href="mailto:sales@taltekroofing.com" style="color: var(--copper);">sales@taltekroofing.com</a>.</p>
        </div>
      </div>
    </section>
    """

    render_page(
        "california-privacy-rights.html",
        "California Privacy Rights & Do Not Sell My Info | TALTEK",
        "California Consumer Privacy Act (CCPA/CPRA) Notice for TALTEK Commercial Roofing. Learn your rights to know, delete, correct, and opt-out of data sharing.",
        "california-privacy-rights",
        content,
        path_depth=0
    )

def build_privacy_request_page():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container" style="max-width: 860px;">
        <div class="section-header text-center">
          <span class="eyebrow">Consumer Data Rights Portal</span>
          <h1 class="section-title">Consumer Privacy Rights Request</h1>
          <p class="section-desc">
            Submit a formal privacy request under the Tennessee Information Protection Act (TIPA), California Consumer Privacy Act (CCPA/CPRA), or applicable state privacy statutes.
          </p>
        </div>

        <div style="background: var(--bg-surface); border: 1px solid var(--border-medium); border-radius: 8px; padding: clamp(1.5rem, 4vw, 3rem); margin-top: var(--space-8);">
          <form id="privacy-rights-form">
            <!-- Honeypot -->
            <input type="text" name="hp_privacy_verification" style="display:none !important;" tabindex="-1" autocomplete="off" aria-hidden="true">

            <div class="form-group">
              <label for="req_state" class="form-label">State of Residence *</label>
              <select id="req_state" name="state_of_residence" class="form-control" required>
                <option value="Tennessee" selected>Tennessee (TIPA Consumer)</option>
                <option value="California">California (CCPA/CPRA Consumer)</option>
                <option value="Virginia">Virginia (VCDPA Consumer)</option>
                <option value="Other US State">Other US State Resident</option>
              </select>
            </div>

            <div class="form-group">
              <label class="form-label">Request Type *</label>
              <div style="display: grid; gap: 10px;">
                <label class="custom-radio">
                  <input type="radio" name="request_type" value="Right to Know / Access" checked>
                  <span><strong>Right to Know / Access:</strong> Request a copy of personal information collected about you.</span>
                </label>
                <label class="custom-radio">
                  <input type="radio" name="request_type" value="Right to Delete">
                  <span><strong>Right to Delete:</strong> Request deletion of personal records maintained by TALTEK.</span>
                </label>
                <label class="custom-radio">
                  <input type="radio" name="request_type" value="Right to Correct">
                  <span><strong>Right to Correct:</strong> Request correction of inaccurate commercial contact records.</span>
                </label>
                <label class="custom-radio">
                  <input type="radio" name="request_type" value="Opt-Out of Sale / Targeted Ads">
                  <span><strong>Do Not Sell / Share / Targeted Advertising Opt-Out:</strong> Direct TALTEK not to share data.</span>
                </label>
                <label class="custom-radio">
                  <input type="radio" name="request_type" value="Appeal Decision">
                  <span><strong>Appeal a Denied Request:</strong> Submit an appeal for a previously processed privacy decision.</span>
                </label>
              </div>
            </div>

            <div class="grid grid-cols-2" style="gap: 16px;">
              <div class="form-group">
                <label for="req_first_name" class="form-label">First Name *</label>
                <input type="text" id="req_first_name" name="first_name" class="form-control" required>
              </div>
              <div class="form-group">
                <label for="req_last_name" class="form-label">Last Name *</label>
                <input type="text" id="req_last_name" name="last_name" class="form-control" required>
              </div>
            </div>

            <div class="grid grid-cols-2" style="gap: 16px;">
              <div class="form-group">
                <label for="req_email" class="form-label">Business / Personal Email *</label>
                <input type="email" id="req_email" name="email" class="form-control" required>
                <span class="form-hint">Used to verify identity and transmit request confirmation.</span>
              </div>
              <div class="form-group">
                <label for="req_phone" class="form-label">Telephone Number *</label>
                <input type="tel" id="req_phone" name="phone" class="form-control" required>
              </div>
            </div>

            <div class="form-group">
              <label for="req_details" class="form-label">Request Specifics / Additional Details</label>
              <textarea id="req_details" name="details" class="form-control" placeholder="Provide any details that assist us in identifying your records..."></textarea>
            </div>

            <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); padding: 14px; border-radius: 4px; margin-bottom: 20px; font-size: 12px; color: var(--text-secondary); line-height: 1.5;">
              <strong>Verification Notice:</strong> To protect your confidential commercial data, TALTEK will verify your identity by cross-referencing your email address and telephone against active inspection records before executing access or deletion actions.
            </div>

            <button type="submit" class="btn btn-primary" style="width: 100%;">Submit Privacy Rights Request</button>
          </form>

          <!-- Confirmation Screen -->
          <div id="privacy-request-confirmation" style="display: none; text-align: center; padding: 24px 0;">
            <div style="width: 56px; height: 56px; background: rgba(16, 185, 129, 0.15); border: 2px solid var(--status-success); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px; color: var(--status-success); font-size: 28px;">
              &check;
            </div>
            <h2 style="font-size: 24px; color: var(--text-primary); margin-bottom: 8px;">Privacy Request Recorded</h2>
            <div style="font-family: var(--font-mono); font-size: 13px; color: var(--copper); margin-bottom: 16px;">
              TRACKING ID: <span id="privacy-tracking-code">TIPA-202611-8842</span>
            </div>
            <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto 20px; font-size: 14px; line-height: 1.7;">
              Your privacy request has been logged into our compliance register. Our designated Privacy Officer will review your submission and respond within the statutory timeframe prescribed by applicable state law (e.g., 45 days under TIPA and CCPA).
            </p>
            <a href="index.html" class="btn btn-secondary btn-sm">Return to Home</a>
          </div>
        </div>
      </div>
    </section>
    """

    extra_scripts = """
  <script src="assets/js/privacy-requests.js"></script>
    """

    render_page(
        "privacy-request.html",
        "Submit a Privacy Rights Request | TIPA & CCPA Portal — TALTEK",
        "Submit an official consumer privacy rights request under Tennessee (TIPA) or California (CCPA/CPRA) law: Access, Deletion, Correction, and Opt-Out requests.",
        "privacy-request",
        content,
        path_depth=0,
        extra_scripts=extra_scripts
    )

def build_sms_terms_page():
    content = """
    <section class="section bg-primary" style="padding-top: clamp(4rem, 8vw, 6rem);">
      <div class="container" style="max-width: 920px;">
        <span class="eyebrow">Communications Compliance</span>
        <h1 class="section-title">SMS Terms &amp; Data Collection Notice</h1>
        <p style="color: var(--text-muted); font-family: var(--font-mono); font-size: 13px; margin-bottom: 24px;">
          TCPA &amp; CAN-SPAM COMPLIANCE DISCLOSURE • TALTEK COMMERCIAL ROOFING
        </p>

        <div class="editorial-body" style="color: var(--text-secondary); line-height: 1.8; font-size: 15px;">
          <p>
            TALTEK Commercial Roofing ("TALTEK") provides optional text messaging (SMS) capabilities to facilitate inspection scheduling, emergency crew dispatch updates, and project status notifications.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">1. Strict Separation of Consent</h2>
          <p>
            <strong>Requesting a commercial roofing quote or inspection does NOT automatically enroll you in marketing text messaging campaigns.</strong> In strict compliance with the Telephone Consumer Protection Act (TCPA) and CTIA guidelines:
          </p>
          <ul style="margin: 12px 0 16px 20px;">
            <li>SMS consent requires clear affirmative action (an explicit, un-checked checkbox on our quote request wizard).</li>
            <li>Consent to receive promotional SMS is never a condition of purchasing roofing services or scheduling an inspection.</li>
            <li>We do not share, sell, or disclose mobile telephone numbers or opt-in consent records to third-party marketers or affiliates.</li>
          </ul>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">2. Message Frequency &amp; Standard Rates</h2>
          <p>
            Message frequency varies based on your active commercial project schedule (typically 1 to 4 messages during an active inspection or re-roofing phase). <strong>Standard message and data rates may apply</strong> based on your mobile carrier contract.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">3. How to Opt-Out Anytime</h2>
          <p>
            You may cancel SMS communications at any time. Simply reply <strong>STOP</strong> to any text message received from TALTEK. Upon receiving your STOP command, we will transmit a final confirmation message and cease further SMS transmissions to that number.
          </p>

          <h2 style="color: var(--text-primary); font-size: 22px; margin: 32px 0 12px;">4. Customer Care &amp; Support</h2>
          <p>
            For assistance with SMS notifications, reply <strong>HELP</strong> to any message or contact our Goodlettsville dispatch desk directly at <strong>+1 (615) 448-6349</strong> or via email at <a href="mailto:sales@taltekroofing.com" style="color: var(--copper);">sales@taltekroofing.com</a>.
          </p>
        </div>
      </div>
    </section>
    """

    render_page(
        "sms-terms.html",
        "SMS Terms & Conditions & Data Collection Notice | TALTEK",
        "SMS terms, TCPA compliance disclosures, and mobile data collection practices for TALTEK Commercial Roofing. Learn message frequency, opt-out, and rates.",
        "sms-terms",
        content,
        path_depth=0
    )

if __name__ == "__main__":
    build_privacy_policy()
    build_cookie_policy()
    build_terms_page()
    build_accessibility_page()
    build_california_privacy()
    build_privacy_request_page()
    build_sms_terms_page()
    print("All legal and privacy compliance pages generated successfully!")
