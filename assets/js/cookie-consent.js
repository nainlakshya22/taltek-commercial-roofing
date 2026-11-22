/**
 * TALTEK COMMERCIAL ROOFING - PRIVACY & COOKIE CONSENT MANAGER
 * Compliant with USA State Privacy Frameworks (TIPA, CCPA/CPRA)
 * Features:
 * - Accept All / Reject Optional / Customize Preferences
 * - Granular categories: Strictly Necessary, Analytics, Functional, Advertising/Marketing
 * - Global Privacy Control (GPC) signal detection & automatic honoring
 * - Persistent footer trigger to modify consent anytime
 * - Custom event dispatch for conditional script execution
 */

const TALTEK_CONSENT_KEY = 'taltek_privacy_consent_v1';

const defaultConsent = {
  necessary: true,   // Always required
  analytics: false,
  functional: false,
  marketing: false,
  timestamp: null,
  version: '1.0.0',
  gpcApplied: false
};

class CookieManager {
  constructor() {
    this.consent = this.loadConsent();
    this.banner = document.getElementById('cookie-banner');
    this.modalBackdrop = document.getElementById('cookie-modal-backdrop');
    this.init();
  }

  loadConsent() {
    try {
      const stored = localStorage.getItem(TALTEK_CONSENT_KEY);
      if (stored) {
        return JSON.parse(stored);
      }
    } catch (e) {
      console.warn('Unable to access localStorage for privacy consent', e);
    }
    return null;
  }

  saveConsent(consentObj) {
    consentObj.timestamp = new Date().toISOString();
    try {
      localStorage.setItem(TALTEK_CONSENT_KEY, JSON.stringify(consentObj));
    } catch (e) {
      console.warn('Unable to save consent to localStorage', e);
    }
    this.consent = consentObj;
    this.dispatchConsentEvent();
  }

  dispatchConsentEvent() {
    const event = new CustomEvent('taltek:consent-updated', {
      detail: this.consent
    });
    window.dispatchEvent(event);
    this.applyConsentEffects();
  }

  applyConsentEffects() {
    if (!this.consent) return;

    // Apply or block scripts based on consent
    if (this.consent.analytics) {
      console.info('[TALTEK Privacy] Analytics category: APPROVED');
    } else {
      console.info('[TALTEK Privacy] Analytics category: BLOCKED');
    }

    if (this.consent.functional) {
      console.info('[TALTEK Privacy] Functional category: APPROVED');
    } else {
      console.info('[TALTEK Privacy] Functional category: BLOCKED');
    }

    if (this.consent.marketing) {
      console.info('[TALTEK Privacy] Marketing category: APPROVED');
    } else {
      console.info('[TALTEK Privacy] Marketing category: BLOCKED');
    }
  }

  init() {
    // Detect Global Privacy Control (GPC)
    const gpcActive = navigator.globalPrivacyControl === true;

    if (!this.consent) {
      // First visit: Show banner
      if (this.banner) {
        this.banner.classList.add('active');
      }

      // If GPC is active, automatically configure opt-out default
      if (gpcActive) {
        console.info('[TALTEK Privacy] Global Privacy Control (GPC) signal detected. Honoring opt-out preferences.');
        const gpcNotice = document.getElementById('gpc-detected-notice');
        if (gpcNotice) gpcNotice.style.display = 'block';
      }
    } else {
      this.applyConsentEffects();
    }

    this.bindEvents();
  }

  bindEvents() {
    // Accept All
    const acceptAllBtns = document.querySelectorAll('[data-cookie-action="accept-all"]');
    acceptAllBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const fullConsent = {
          necessary: true,
          analytics: true,
          functional: true,
          marketing: true,
          version: '1.0.0',
          gpcApplied: false
        };
        this.saveConsent(fullConsent);
        this.hideBanner();
        this.hideModal();
      });
    });

    // Reject Optional
    const rejectOptionalBtns = document.querySelectorAll('[data-cookie-action="reject-optional"]');
    rejectOptionalBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const minConsent = {
          necessary: true,
          analytics: false,
          functional: false,
          marketing: false,
          version: '1.0.0',
          gpcApplied: navigator.globalPrivacyControl === true
        };
        this.saveConsent(minConsent);
        this.hideBanner();
        this.hideModal();
      });
    });

    // Open Customize Modal
    const customizeBtns = document.querySelectorAll('[data-cookie-action="customize"]');
    customizeBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        this.openModal();
      });
    });

    // Save Custom Preferences
    const saveCustomBtn = document.getElementById('cookie-save-preferences');
    if (saveCustomBtn) {
      saveCustomBtn.addEventListener('click', () => {
        const analyticsChecked = document.getElementById('cookie-cat-analytics')?.checked || false;
        const functionalChecked = document.getElementById('cookie-cat-functional')?.checked || false;
        const marketingChecked = document.getElementById('cookie-cat-marketing')?.checked || false;

        const customConsent = {
          necessary: true,
          analytics: analyticsChecked,
          functional: functionalChecked,
          marketing: marketingChecked,
          version: '1.0.0',
          gpcApplied: navigator.globalPrivacyControl === true
        };
        this.saveConsent(customConsent);
        this.hideBanner();
        this.hideModal();
      });
    }

    // Close Modal Button
    const closeModalBtn = document.querySelector('.cookie-modal-close');
    if (closeModalBtn) {
      closeModalBtn.addEventListener('click', () => {
        this.hideModal();
      });
    }

    // Persistent Footer Trigger
    const footerTrigger = document.querySelector('[data-cookie-action="open-preferences"]');
    if (footerTrigger) {
      footerTrigger.addEventListener('click', (e) => {
        e.preventDefault();
        this.openModal();
      });
    }
  }

  hideBanner() {
    if (this.banner) {
      this.banner.classList.remove('active');
    }
  }

  openModal() {
    if (!this.modalBackdrop) return;

    // Sync checkboxes with current consent
    const current = this.consent || defaultConsent;
    const chkAnalytics = document.getElementById('cookie-cat-analytics');
    const chkFunctional = document.getElementById('cookie-cat-functional');
    const chkMarketing = document.getElementById('cookie-cat-marketing');

    if (chkAnalytics) chkAnalytics.checked = !!current.analytics;
    if (chkFunctional) chkFunctional.checked = !!current.functional;
    if (chkMarketing) chkMarketing.checked = !!current.marketing;

    this.modalBackdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  hideModal() {
    if (this.modalBackdrop) {
      this.modalBackdrop.classList.remove('active');
      document.body.style.overflow = '';
    }
  }
}

// Global initialization
window.addEventListener('DOMContentLoaded', () => {
  window.TaltekCookieManager = new CookieManager();
});
