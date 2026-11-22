"""
TALTEK COMMERCIAL ROOFING - MASTER SITE BUILDER
Generates all 36 production pages with unified Luxury Industrial Futurism design,
SEO metadata, JSON-LD schemas, and all 12 mandatory premium features.
"""

import os

# Helper to resolve relative path depth for assets
def get_root_prefix(path_depth):
    return "../" * path_depth if path_depth > 0 else "./"

def get_header_html(root_prefix, current_page_slug=""):
    return f"""
  <!-- Skip to Main Content Link (WCAG 2.2 AA) -->
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <!-- Top Utility Bar -->
  <div class="header-utility-bar" role="complementary" aria-label="Company Quick Info">
    <div class="container utility-inner">
      <div class="utility-left">
        <span class="utility-link"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg> Goodlettsville, TN (HQ) • Serving 15 Southeastern States</span>
        <span class="utility-link"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg> BBB Accredited A+ • 10,000+ Customers Served</span>
      </div>
      <div class="utility-right">
        <a href="tel:+16154486349" class="utility-link highlight" aria-label="Call 24/7 Commercial Emergency Dispatch at (615) 448-6349">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
          24/7 Rapid Emergency Dispatch: (615) 448-6349
        </a>
        <a href="mailto:sales@taltekroofing.com" class="utility-link">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
          sales@taltekroofing.com
        </a>
      </div>
    </div>
  </div>

  <!-- Primary Site Header -->
  <header class="site-header" role="banner">
    <div class="container header-main">
      <!-- Brand Logo -->
      <a href="{root_prefix}index.html" class="brand-logo-link" aria-label="TALTEK Commercial Roofing Home">
        <img src="{root_prefix}assets/images/taltek-logo.svg" alt="TALTEK Commercial Roofing" class="brand-logo-img" width="220" height="44">
      </a>

      <!-- Desktop Navigation Menu -->
      <nav class="nav-menu" role="navigation" aria-label="Main Navigation">
        <div class="nav-item has-dropdown">
          <a href="{root_prefix}services.html" class="nav-link {'active' if current_page_slug.startswith('services') else ''}">
            Services
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </a>
          <div class="nav-dropdown" role="menu">
            <a href="{root_prefix}services/commercial-roofing.html" class="dropdown-link" role="menuitem">Commercial Installation</a>
            <a href="{root_prefix}services/industrial-roofing.html" class="dropdown-link" role="menuitem">Industrial Roofing</a>
            <a href="{root_prefix}services/roof-replacement.html" class="dropdown-link" role="menuitem">Roof Replacement</a>
            <a href="{root_prefix}services/roof-repair.html" class="dropdown-link" role="menuitem">Commercial Roof Repair</a>
            <a href="{root_prefix}services/emergency-services.html" class="dropdown-link" role="menuitem">Emergency Roofing Services</a>
            <a href="{root_prefix}services/preventative-maintenance.html" class="dropdown-link" role="menuitem">Preventative Maintenance</a>
            <a href="{root_prefix}services/tpo-roofing.html" class="dropdown-link" role="menuitem">TPO Roofing Systems</a>
            <a href="{root_prefix}services/epdm-roofing.html" class="dropdown-link" role="menuitem">EPDM Rubber Roofing</a>
            <a href="{root_prefix}services/pvc-roofing.html" class="dropdown-link" role="menuitem">PVC Chemical Resistant</a>
            <a href="{root_prefix}services/storm-protection.html" class="dropdown-link" role="menuitem">Storm Protection</a>
            <a href="{root_prefix}services/roof-assessment.html" class="dropdown-link" role="menuitem">Core Sampling &amp; Assessment</a>
            <a href="{root_prefix}services/gutter-services.html" class="dropdown-link" role="menuitem">Commercial Gutters &amp; Drainage</a>
          </div>
        </div>

        <div class="nav-item">
          <a href="{root_prefix}projects.html" class="nav-link {'active' if current_page_slug.startswith('projects') else ''}">Projects</a>
        </div>

        <div class="nav-item">
          <a href="{root_prefix}service-areas.html" class="nav-link {'active' if current_page_slug == 'service-areas' else ''}">Service Areas</a>
        </div>

        <div class="nav-item">
          <a href="{root_prefix}estimator.html" class="nav-link {'active' if current_page_slug == 'estimator' else ''}">Roof Estimator</a>
        </div>

        <div class="nav-item">
          <a href="{root_prefix}financing.html" class="nav-link {'active' if current_page_slug == 'financing' else ''}">Financing</a>
        </div>

        <div class="nav-item">
          <a href="{root_prefix}about.html" class="nav-link {'active' if current_page_slug == 'about' else ''}">About Us</a>
        </div>

        <div class="nav-item">
          <a href="{root_prefix}contact.html" class="nav-link {'active' if current_page_slug == 'contact' else ''}">Contact</a>
        </div>
      </nav>

      <!-- Header Actions -->
      <div class="header-actions">
        <a href="tel:+16154486349" class="phone-cta" aria-label="Direct Phone Line: (615) 448-6349">
          <span class="phone-cta-label">Direct Line</span>
          <span class="phone-cta-number">(615) 448-6349</span>
        </a>
        <a href="{root_prefix}request-inspection.html" class="btn btn-primary btn-sm">Schedule Inspection</a>
        
        <!-- Mobile Hamburger Toggle -->
        <button class="mobile-nav-toggle" aria-label="Open Navigation Menu" aria-expanded="false">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Navigation Drawer -->
  <div class="drawer-backdrop" aria-hidden="true"></div>
  <aside class="mobile-drawer" role="dialog" aria-modal="true" aria-label="Mobile Navigation Drawer">
    <div class="drawer-header">
      <img src="{root_prefix}assets/images/taltek-logo.svg" alt="TALTEK Logo" width="160" height="32">
      <button class="drawer-close" aria-label="Close Navigation Menu">&times;</button>
    </div>
    <nav class="drawer-links" role="navigation">
      <a href="{root_prefix}index.html" class="drawer-link">Home</a>
      <div>
        <a href="{root_prefix}services.html" class="drawer-link">Our Services</a>
        <div class="drawer-dropdown-list">
          <a href="{root_prefix}services/commercial-roofing.html" class="drawer-sublink">Commercial Installation</a>
          <a href="{root_prefix}services/industrial-roofing.html" class="drawer-sublink">Industrial Roofing</a>
          <a href="{root_prefix}services/roof-replacement.html" class="drawer-sublink">Roof Replacement</a>
          <a href="{root_prefix}services/roof-repair.html" class="drawer-sublink">Roof Repair</a>
          <a href="{root_prefix}services/emergency-services.html" class="drawer-sublink">Emergency Services</a>
          <a href="{root_prefix}services/tpo-roofing.html" class="drawer-sublink">TPO Systems</a>
          <a href="{root_prefix}services/epdm-roofing.html" class="drawer-sublink">EPDM Rubber</a>
          <a href="{root_prefix}services/pvc-roofing.html" class="drawer-sublink">PVC Chemical</a>
          <a href="{root_prefix}services/storm-protection.html" class="drawer-sublink">Storm Protection</a>
        </div>
      </div>
      <a href="{root_prefix}projects.html" class="drawer-link">Our Projects (Case Studies)</a>
      <a href="{root_prefix}service-areas.html" class="drawer-link">Service Areas (15 States)</a>
      <a href="{root_prefix}estimator.html" class="drawer-link">Interactive Roof Estimator</a>
      <a href="{root_prefix}financing.html" class="drawer-link">Financing Calculator</a>
      <a href="{root_prefix}team.html" class="drawer-link">Meet Our Team</a>
      <a href="{root_prefix}about.html" class="drawer-link">About TALTEK</a>
      <a href="{root_prefix}faq.html" class="drawer-link">FAQ</a>
      <a href="{root_prefix}careers.html" class="drawer-link">Careers</a>
      <a href="{root_prefix}contact.html" class="drawer-link">Contact Us</a>
    </nav>
    <div style="margin-top: auto; padding-top: 24px; border-top: 1px solid var(--border-subtle);">
      <a href="{root_prefix}request-inspection.html" class="btn btn-primary" style="width: 100%; margin-bottom: 12px;">Schedule Roof Inspection</a>
      <a href="tel:+16154486349" class="btn btn-secondary" style="width: 100%;">Call (615) 448-6349</a>
    </div>
  </aside>
"""

def get_footer_html(root_prefix):
    return f"""
  <!-- Site Footer -->
  <footer class="site-footer" role="contentinfo">
    <div class="container">
      <!-- Verified Licensing & State Authorization Strip -->
      <div class="footer-licensing-strip">
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="display: inline-block; width: 8px; height: 8px; background-color: var(--copper); border-radius: 50%;"></span>
          <strong style="color: var(--text-primary); font-size: 13px; text-transform: uppercase; letter-spacing: 0.05em;">Verified Contractor Licensing &amp; Coverage:</strong>
        </div>
        <div class="license-tag-group">
          <span class="license-tag primary">Tennessee (HQ) #CMC-C</span>
          <span class="license-tag">Alabama Board of Contractors</span>
          <span class="license-tag">Louisiana State Licensing</span>
          <span class="license-tag">Mississippi Board of Contractors</span>
          <span class="license-tag">North Carolina General Contractor</span>
          <span class="license-tag">South Carolina Specialty</span>
          <span class="license-tag">Virginia Class A Commercial</span>
        </div>
      </div>

      <!-- Main Footer Columns -->
      <div class="footer-top">
        <!-- Brand Summary -->
        <div>
          <img src="{root_prefix}assets/images/taltek-logo.svg" alt="TALTEK Commercial Roofing" width="200" height="40" style="margin-bottom: 16px;">
          <p class="footer-brand-desc">
            TALTEK Commercial Roofing is an established US-based industrial and commercial roofing enterprise headquartered in Goodlettsville, Tennessee. Engineered precision, certified single-ply membrane installations, and manufacturer No Dollar Limit (NDL) warranty eligibility across 15 Southeastern states.
          </p>
          <div style="display: flex; gap: 12px; margin-top: 16px;">
            <img src="{root_prefix}assets/images/certifications.svg" alt="Manufacturer &amp; Safety Credentials: Johns Manville, GAF, Elevate, CertainTeed, Versico, DMI Metals, OSHA 10/30 Safety, BBB A+ Accredited" style="height: 36px; width: auto; opacity: 0.85;">
          </div>
        </div>

        <!-- Services Column -->
        <div>
          <h3 class="footer-col-title">Roofing Services</h3>
          <ul class="footer-nav-list">
            <li><a href="{root_prefix}services/commercial-roofing.html" class="footer-nav-link">Commercial Installation</a></li>
            <li><a href="{root_prefix}services/industrial-roofing.html" class="footer-nav-link">Industrial &amp; Warehousing</a></li>
            <li><a href="{root_prefix}services/roof-replacement.html" class="footer-nav-link">Roof Replacement &amp; Tear-Off</a></li>
            <li><a href="{root_prefix}services/roof-repair.html" class="footer-nav-link">Targeted Leak Repairs</a></li>
            <li><a href="{root_prefix}services/emergency-services.html" class="footer-nav-link">24/7 Emergency Dispatch</a></li>
            <li><a href="{root_prefix}services/preventative-maintenance.html" class="footer-nav-link">Preventative Maintenance</a></li>
            <li><a href="{root_prefix}services/tpo-roofing.html" class="footer-nav-link">TPO Membrane Systems</a></li>
            <li><a href="{root_prefix}services/epdm-roofing.html" class="footer-nav-link">EPDM Synthetic Rubber</a></li>
            <li><a href="{root_prefix}services/pvc-roofing.html" class="footer-nav-link">PVC Chemical Resistant</a></li>
            <li><a href="{root_prefix}services/roof-assessment.html" class="footer-nav-link">Infrared Due Diligence</a></li>
          </ul>
        </div>

        <!-- Verified Case Studies Column -->
        <div>
          <h3 class="footer-col-title">Case Studies</h3>
          <ul class="footer-nav-list">
            <li><a href="{root_prefix}projects/nashville-general-hospital.html" class="footer-nav-link">Nashville General Hospital (18k sqft)</a></li>
            <li><a href="{root_prefix}projects/frost-bank-plaza.html" class="footer-nav-link">Frost Bank Plaza (Soprema PMMA)</a></li>
            <li><a href="{root_prefix}projects/krusteaz-facility.html" class="footer-nav-link">Krusteaz Manufacturing (205k sqft)</a></li>
            <li><a href="{root_prefix}projects/rapha-center.html" class="footer-nav-link">Rapha Center (TPO Mechanically Attached)</a></li>
            <li><a href="{root_prefix}projects/malone-plaza.html" class="footer-nav-link">Malone Plaza (100k sqft EPDM)</a></li>
            <li><a href="{root_prefix}projects.html" class="footer-nav-link">View Full Portfolio &rarr;</a></li>
            <li><a href="{root_prefix}service-areas.html" class="footer-nav-link">15-State Coverage Map</a></li>
            <li><a href="{root_prefix}team.html" class="footer-nav-link">Leadership &amp; Safety Officers</a></li>
            <li><a href="{root_prefix}careers.html" class="footer-nav-link">Join Our Crew (Careers)</a></li>
          </ul>
        </div>

        <!-- Corporate Headquarters & Contact -->
        <div>
          <h3 class="footer-col-title">Corporate Headquarters</h3>
          <div class="footer-contact-item">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
            <div>
              <strong>TALTEK Commercial Roofing</strong><br>
              1214 S. Dickerson Rd<br>
              Goodlettsville, TN 37072, USA
            </div>
          </div>
          <div class="footer-contact-item">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            <div>
              <strong>Dispatch &amp; Quotes:</strong><br>
              <a href="tel:+16154486349" style="color: var(--copper); font-weight: 700;">+1 (615) 448-6349</a>
            </div>
          </div>
          <div class="footer-contact-item">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
            <div>
              <strong>Commercial Estimating:</strong><br>
              <a href="mailto:sales@taltekroofing.com" style="color: var(--text-primary);">sales@taltekroofing.com</a>
            </div>
          </div>
          <div style="margin-top: 16px;">
            <a href="{root_prefix}request-inspection.html" class="btn btn-outline btn-sm" style="width: 100%;">Book Professional Inspection</a>
          </div>
        </div>
      </div>

      <!-- Legal Disclosures & Compliance Links -->
      <div class="footer-bottom">
        <div>
          &copy; 2009&ndash;2026 TALTEK Commercial Roofing. All Rights Reserved. First roof installed in 2009. Over 10,000 customers served across the Southeastern United States.
        </div>
        <div class="footer-legal-links">
          <a href="{root_prefix}privacy-policy.html">Privacy Policy</a>
          <a href="{root_prefix}cookie-policy.html">Cookie Policy</a>
          <a href="{root_prefix}terms.html">Terms &amp; Conditions</a>
          <a href="{root_prefix}accessibility.html">Accessibility (WCAG 2.2 AA)</a>
          <a href="{root_prefix}california-privacy-rights.html">California Privacy Rights</a>
          <a href="{root_prefix}privacy-request.html">Your Privacy Choices / Privacy Requests</a>
          <a href="{root_prefix}sms-terms.html">SMS Terms &amp; Communications</a>
          <button type="button" data-cookie-action="open-preferences" style="background:none; border:none; color:var(--copper); cursor:pointer; text-decoration:underline;">[ Cookie Preferences ]</button>
        </div>
      </div>
    </div>
  </footer>

  <!-- Feature 12: Sticky Mobile Action Bar -->
  <aside class="mobile-sticky-action-bar" role="complementary" aria-label="Mobile Quick Actions">
    <div class="mobile-sticky-inner">
      <a href="tel:+16154486349" class="mobile-sticky-btn mobile-sticky-call">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
        Call (615) 448-6349
      </a>
      <a href="{root_prefix}request-inspection.html" class="mobile-sticky-btn mobile-sticky-quote">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
        Request Inspection
      </a>
    </div>
  </aside>

  <!-- Feature 10: Industrial AI Assistant Chat Widget -->
  <aside class="chat-widget-container" role="complementary" aria-label="Automated Industrial Roofing Assistant">
    <button id="chat-toggle-btn" class="chat-toggle-btn" aria-label="Open Industrial Roofing AI Assistant">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
    </button>
    <div id="chat-panel" class="chat-panel" role="dialog" aria-modal="true" aria-label="TALTEK Roofing Assistant Panel">
      <div class="chat-header">
        <div class="chat-header-title">
          <span class="chat-bot-status" aria-hidden="true"></span>
          <div>
            <span class="chat-bot-name">TALTEK Industrial AI</span>
            <span class="chat-bot-badge">AUTOMATED (NON-HUMAN)</span>
          </div>
        </div>
        <button id="chat-close-btn" class="chat-close-btn" aria-label="Close Chat">&times;</button>
      </div>
      <div id="chat-messages" class="chat-messages">
        <div class="chat-bubble bot">
          <strong>TALTEK Industrial Assistant</strong><br>
          Welcome. I am an automated commercial roofing assistant. I can answer questions regarding single-ply membranes (TPO/EPDM/PVC), manufacturer NDL warranty options, Southeastern service regions, or route you to an engineering representative at (615) 448-6349. How may I assist your facility?
        </div>
      </div>
      <div id="chat-quick-chips" class="chat-quick-chips">
        <button class="chat-chip">TPO vs EPDM</button>
        <button class="chat-chip">Emergency Leak</button>
        <button class="chat-chip">NDL Warranty Info</button>
        <button class="chat-chip">Service Areas</button>
        <button class="chat-chip">Estimator Rates</button>
        <button class="chat-chip">Connect to Human</button>
      </div>
      <div class="chat-input-bar">
        <input type="text" id="chat-user-input" class="chat-input" placeholder="Type commercial roofing question..." aria-label="Chat input">
        <button type="button" id="chat-send-btn" class="chat-send-btn">SEND</button>
      </div>
      <div class="chat-disclaimer">
        Automated response engine. Conversations are logged for service quality. Call (615) 448-6349 for live engineer.
      </div>
    </div>
  </aside>

  <!-- USA Privacy & Cookie Consent Banner -->
  <aside id="cookie-banner" class="cookie-banner" role="dialog" aria-modal="false" aria-label="Cookie and Privacy Consent">
    <div class="cookie-banner-inner">
      <div class="cookie-content">
        <h4 class="cookie-title">Your Privacy Matters</h4>
        <p class="cookie-desc">
          We use cookies and similar technologies to improve your experience, analyze website performance, and support our commercial roofing services under Tennessee (TIPA) and US state privacy regulations. You can manage your preferences at any time. Review our <a href="{root_prefix}privacy-policy.html">Privacy Policy</a> and <a href="{root_prefix}cookie-policy.html">Cookie Policy</a>.
        </p>
      </div>
      <div class="cookie-actions">
        <button type="button" class="btn btn-primary btn-sm" data-cookie-action="accept-all">Accept All</button>
        <button type="button" class="btn btn-secondary btn-sm" data-cookie-action="reject-optional">Reject Optional</button>
        <button type="button" class="btn btn-outline btn-sm" data-cookie-action="customize">Customize</button>
      </div>
    </div>
  </aside>

  <!-- Cookie Preferences Customization Modal -->
  <div id="cookie-modal-backdrop" class="cookie-modal-backdrop" role="dialog" aria-modal="true" aria-label="Cookie Preferences Manager">
    <div class="cookie-modal">
      <div class="cookie-modal-header">
        <h3 style="font-size: 18px; color: var(--text-primary); margin: 0;">Privacy &amp; Cookie Preferences</h3>
        <button type="button" class="cookie-modal-close" style="background:none; border:none; font-size:24px; color:var(--text-secondary); cursor:pointer;" aria-label="Close preferences modal">&times;</button>
      </div>
      <div class="cookie-modal-body">
        <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 12px;">
          Configure granular consent categories below. Global Privacy Control (GPC) signals are honored automatically by this website.
        </p>
        <div id="gpc-detected-notice" style="display:none; background: rgba(16, 185, 129, 0.1); border: 1px solid var(--status-success); padding: 8px 12px; border-radius: 4px; font-size: 12px; color: var(--status-success); margin-bottom: 12px;">
          Global Privacy Control (GPC) active: Optional tracking pre-set to opted-out.
        </div>

        <!-- Necessary (Locked) -->
        <div class="cookie-category-item">
          <div class="cookie-category-header">
            <span class="cookie-cat-name">Strictly Necessary Cookies</span>
            <span class="cookie-cat-badge">ALWAYS ACTIVE (REQUIRED)</span>
          </div>
          <p style="font-size: 12px; color: var(--text-secondary);">Essential for core site security, server load balancing, form token verification, and persistent consent state.</p>
        </div>

        <!-- Analytics -->
        <div class="cookie-category-item">
          <div class="cookie-category-header">
            <span class="cookie-cat-name">Performance &amp; Analytics Cookies</span>
            <label class="custom-checkbox">
              <input type="checkbox" id="cookie-cat-analytics">
              <span style="font-size: 12px; color: var(--text-primary);">Enable</span>
            </label>
          </div>
          <p style="font-size: 12px; color: var(--text-secondary);">Measures site visits, bounce rates, and load performance to help optimize our technical specifications layout.</p>
        </div>

        <!-- Functional -->
        <div class="cookie-category-item">
          <div class="cookie-category-header">
            <span class="cookie-cat-name">Functional &amp; Assistant Cookies</span>
            <label class="custom-checkbox">
              <input type="checkbox" id="cookie-cat-functional">
              <span style="font-size: 12px; color: var(--text-primary);">Enable</span>
            </label>
          </div>
          <p style="font-size: 12px; color: var(--text-secondary);">Powers interactive state mapping, live AI assistant chat memory, and the roof estimator state.</p>
        </div>

        <!-- Advertising / Marketing -->
        <div class="cookie-category-item">
          <div class="cookie-category-header">
            <span class="cookie-cat-name">Advertising &amp; Retargeting Cookies</span>
            <label class="custom-checkbox">
              <input type="checkbox" id="cookie-cat-marketing">
              <span style="font-size: 12px; color: var(--text-primary);">Enable</span>
            </label>
          </div>
          <p style="font-size: 12px; color: var(--text-secondary);">Allows relevant commercial roofing announcements to be served on authorized business platforms.</p>
        </div>
      </div>
      <div class="cookie-modal-footer">
        <button type="button" class="btn btn-secondary btn-sm" data-cookie-action="reject-optional">Reject All Optional</button>
        <button type="button" id="cookie-save-preferences" class="btn btn-primary btn-sm">Save Preferences</button>
      </div>
    </div>
  </div>

  <!-- Core Scripts -->
  <script src="{root_prefix}assets/js/cookie-consent.js"></script>
  <script src="{root_prefix}assets/js/main.js"></script>
  <script src="{root_prefix}assets/js/chat-assistant.js"></script>
"""

print("Base layout templates defined.")
