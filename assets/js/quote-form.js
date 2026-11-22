/**
 * TALTEK COMMERCIAL ROOFING - MULTI-STEP QUOTE & INSPECTION FORM
 * Feature 07: 5-Step Commercial Inspection Request Wizard
 * Complete validation, spam honeypot defense, and accessible UX.
 */

document.addEventListener('DOMContentLoaded', () => {
  initQuoteWizard();
});

function initQuoteWizard() {
  const wizard = document.getElementById('commercial-quote-wizard');
  if (!wizard) return;

  let currentStep = 1;
  const totalSteps = 5;

  const stepPanes = wizard.querySelectorAll('.wizard-step-pane');
  const stepTabs = wizard.querySelectorAll('.wizard-step-tab');
  const btnNext = wizard.querySelector('.wizard-btn-next');
  const btnPrev = wizard.querySelector('.wizard-btn-prev');
  const btnSubmit = wizard.querySelector('.wizard-btn-submit');
  const summaryBlock = document.getElementById('wizard-summary-review');

  const goToStep = (step) => {
    if (step < 1 || step > totalSteps) return;
    currentStep = step;

    // Update panes
    stepPanes.forEach(pane => {
      const paneStep = parseInt(pane.getAttribute('data-step'), 10);
      if (paneStep === currentStep) {
        pane.classList.add('active');
      } else {
        pane.classList.remove('active');
      }
    });

    // Update tabs
    stepTabs.forEach(tab => {
      const tabStep = parseInt(tab.getAttribute('data-step'), 10);
      tab.classList.remove('active', 'completed');
      if (tabStep === currentStep) {
        tab.classList.add('active');
      } else if (tabStep < currentStep) {
        tab.classList.add('completed');
      }
    });

    // Button states
    if (btnPrev) {
      btnPrev.style.display = currentStep > 1 && currentStep < 5 ? 'inline-flex' : 'none';
    }
    if (btnNext) {
      btnNext.style.display = currentStep < 4 ? 'inline-flex' : 'none';
    }
    if (btnSubmit) {
      btnSubmit.style.display = currentStep === 4 ? 'inline-flex' : 'none';
    }

    // Populate review summary before final submission
    if (currentStep === 4 && summaryBlock) {
      populateReviewSummary();
    }

    // Scroll to top of wizard
    wizard.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  const validateCurrentStep = () => {
    const activePane = wizard.querySelector(`.wizard-step-pane[data-step="${currentStep}"]`);
    if (!activePane) return true;

    let isValid = true;
    const requiredInputs = activePane.querySelectorAll('[required]');

    requiredInputs.forEach(input => {
      const group = input.closest('.form-group') || input.parentElement;
      if (!input.value.trim()) {
        group.classList.add('has-error');
        isValid = false;
      } else {
        group.classList.remove('has-error');
      }

      // Email format check
      if (input.type === 'email' && input.value.trim()) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(input.value.trim())) {
          group.classList.add('has-error');
          isValid = false;
        }
      }

      // Phone format check
      if (input.type === 'tel' && input.value.trim()) {
        const cleanPhone = input.value.replace(/\D/g, '');
        if (cleanPhone.length < 10) {
          group.classList.add('has-error');
          isValid = false;
        }
      }
    });

    return isValid;
  };

  const populateReviewSummary = () => {
    const bType = wizard.querySelector('input[name="property_type"]:checked')?.value || 'Commercial';
    const bName = wizard.querySelector('input[name="building_name"]')?.value || 'N/A';
    const cityState = (wizard.querySelector('input[name="city"]')?.value || '') + ', ' + (wizard.querySelector('select[name="state"]')?.value || '');
    const serviceType = wizard.querySelector('input[name="service_requirement"]:checked')?.value || 'Inspection';
    const sqft = wizard.querySelector('input[name="roof_sqft"]')?.value || 'N/A';
    const contactName = wizard.querySelector('input[name="full_name"]')?.value || 'N/A';
    const email = wizard.querySelector('input[name="business_email"]')?.value || 'N/A';
    const phone = wizard.querySelector('input[name="phone"]')?.value || 'N/A';

    summaryBlock.innerHTML = `
      <div class="summary-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; font-size: 13px; background: #0A0C0E; padding: 16px; border-radius: 4px; border: 1px solid var(--border-subtle); margin-top: 16px;">
        <div><strong style="color: var(--text-secondary);">Property:</strong> <span style="color: var(--text-primary);">${escapeHtml(bName)} (${escapeHtml(bType)})</span></div>
        <div><strong style="color: var(--text-secondary);">Location:</strong> <span style="color: var(--text-primary);">${escapeHtml(cityState)}</span></div>
        <div><strong style="color: var(--text-secondary);">Required Scope:</strong> <span style="color: var(--copper); font-weight: 700;">${escapeHtml(serviceType)}</span></div>
        <div><strong style="color: var(--text-secondary);">Approx. Roof Size:</strong> <span style="color: var(--text-primary);">${escapeHtml(sqft)} sq. ft.</span></div>
        <div><strong style="color: var(--text-secondary);">Contact Representative:</strong> <span style="color: var(--text-primary);">${escapeHtml(contactName)}</span></div>
        <div><strong style="color: var(--text-secondary);">Direct Phone / Email:</strong> <span style="color: var(--text-primary);">${escapeHtml(phone)} / ${escapeHtml(email)}</span></div>
      </div>
    `;
  };

  function escapeHtml(string) {
    const div = document.createElement('div');
    div.textContent = string;
    return div.innerHTML;
  }

  // Next / Prev listeners
  if (btnNext) {
    btnNext.addEventListener('click', () => {
      if (validateCurrentStep()) {
        goToStep(currentStep + 1);
      }
    });
  }

  if (btnPrev) {
    btnPrev.addEventListener('click', () => {
      goToStep(currentStep - 1);
    });
  }

  // Step Tabs Click
  stepTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const targetStep = parseInt(tab.getAttribute('data-step'), 10);
      if (targetStep < currentStep) {
        goToStep(targetStep);
      }
    });
  });

  // Submission Handling
  if (btnSubmit) {
    btnSubmit.addEventListener('click', async (e) => {
      e.preventDefault();
      if (!validateCurrentStep()) return;

      // Spam Protection: Honeypot check
      const honeypot = wizard.querySelector('input[name="hp_website_title"]');
      if (honeypot && honeypot.value) {
        console.warn('Spam submission detected by honeypot.');
        goToStep(5);
        return;
      }

      btnSubmit.disabled = true;
      btnSubmit.textContent = 'TRANSMITTING REQUEST...';

      // Gather Form Data
      const formData = new FormData(wizard.querySelector('form') || wizard);
      const dataObj = {};
      formData.forEach((value, key) => { dataObj[key] = value; });

      // Submit to backend
      try {
        const response = await fetch('/api/quote', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(dataObj)
        });

        const result = await response.json();

        if (response.ok && result.success) {
          // Genuine server reference ID
          const refCodeDisplay = document.getElementById('confirmation-ref-code');
          if (refCodeDisplay) refCodeDisplay.textContent = result.reference;

          const dispatchMsg = document.getElementById('confirmation-dispatch-msg');
          if (dispatchMsg && result.message) {
            dispatchMsg.textContent = result.message;
          }

          goToStep(5);
        } else {
          // Server returned validation or rate limit error
          const errMsg = result.error || (result.errors ? result.errors.join(' ') : 'Unable to record inspection request.');
          alert('Submission Notice: ' + errMsg);
          btnSubmit.disabled = false;
          btnSubmit.textContent = 'Submit Inspection Request';
        }
      } catch (err) {
        console.warn('Backend API endpoint offline or static mode active:', err);
        // Provide transparent fallback to direct email transmission
        const name = encodeURIComponent(dataObj.full_name || 'Commercial Client');
        const phone = encodeURIComponent(dataObj.phone || '');
        const email = encodeURIComponent(dataObj.business_email || '');
        const bName = encodeURIComponent(dataObj.building_name || 'Commercial Building');
        const bType = encodeURIComponent(dataObj.property_type || 'Commercial');
        const city = encodeURIComponent(dataObj.city || '');
        const stateVal = encodeURIComponent(dataObj.state || '');
        const sqft = encodeURIComponent(dataObj.roof_sqft || 'N/A');
        const service = encodeURIComponent(dataObj.service_requirement || 'Inspection');

        const mailBody = `COMMERCIAL ROOF INSPECTION REQUEST%0D%0A------------------------------------%0D%0ABuilding: ${bName} (${bType})%0D%0ALocation: ${city}, ${stateVal}%0D%0AApprox. Area: ${sqft} sq ft%0D%0ARequired Service: ${service}%0D%0A%0D%0ACONTACT REPRESENTATIVE%0D%0A------------------------------------%0D%0AName: ${name}%0D%0APhone: ${phone}%0D%0AEmail: ${email}`;

        const mailHref = `mailto:sales@taltekroofing.com?subject=Commercial%20Inspection%20Request%20-%20${bName}&body=${mailBody}`;

        // Populate fallback confirmation
        const refCodeDisplay = document.getElementById('confirmation-ref-code');
        if (refCodeDisplay) refCodeDisplay.textContent = 'DISPATCH-PENDING-TRANSMISSION';

        const dispatchMsg = document.getElementById('confirmation-dispatch-msg');
        if (dispatchMsg) {
          dispatchMsg.innerHTML = `
            Your inspection request details have been compiled. To ensure immediate scheduling without third-party CRM delay, transmit directly to our Goodlettsville dispatch desk:
            <div style="margin-top: 16px; display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
              <a href="${mailHref}" class="btn btn-primary btn-sm">Transmit via Email Client &rarr;</a>
              <a href="tel:+16154486349" class="btn btn-secondary btn-sm">Call Dispatch: (615) 448-6349</a>
            </div>
          `;
        }
        goToStep(5);
      }
    });
  }

  // Pre-fill from URL query params (from Roof Estimator)
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has('sqft')) {
    const sqftInput = wizard.querySelector('input[name="roof_sqft"]');
    if (sqftInput) sqftInput.value = urlParams.get('sqft');
  }
}
