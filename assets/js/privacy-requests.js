/**
 * TALTEK COMMERCIAL ROOFING - PRIVACY RIGHTS REQUEST HANDLER
 * USA State Privacy Law Framework: Tennessee (TIPA), California (CCPA/CPRA)
 */

document.addEventListener('DOMContentLoaded', () => {
  initPrivacyRequestForm();
});

function initPrivacyRequestForm() {
  const form = document.getElementById('privacy-rights-form');
  const confirmationBlock = document.getElementById('privacy-request-confirmation');
  const trackingNumberDisplay = document.getElementById('privacy-tracking-code');

  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Check honeypot
    const hp = form.querySelector('input[name="hp_privacy_verification"]');
    if (hp && hp.value) {
      console.warn('Privacy form spam attempt detected.');
      return;
    }

    const submitBtn = form.querySelector('button[type="submit"]');
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.textContent = 'VERIFYING & RECORDING REQUEST...';
    }

    const formData = new FormData(form);
    const dataObj = {};
    formData.forEach((val, key) => { dataObj[key] = val; });

    try {
      const response = await fetch('/api/privacy-request', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dataObj)
      });

      const result = await response.json();

      if (response.ok && result.success) {
        if (trackingNumberDisplay) {
          trackingNumberDisplay.textContent = result.tracking_code;
        }
        form.style.display = 'none';
        if (confirmationBlock) confirmationBlock.style.display = 'block';
        confirmationBlock.scrollIntoView({ behavior: 'smooth' });
      } else {
        const errMsg = result.error || (result.errors ? result.errors.join(' ') : 'Unable to record privacy request.');
        alert('Privacy Portal Notice: ' + errMsg);
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = 'Submit Privacy Rights Request';
        }
      }
    } catch (err) {
      console.warn('Privacy request API offline or static mode active:', err);
      const reqType = encodeURIComponent(dataObj.request_type || 'Privacy Rights Inquiry');
      const reqState = encodeURIComponent(dataObj.state_of_residence || 'Tennessee');
      const name = encodeURIComponent(dataObj.full_name || '');
      const email = encodeURIComponent(dataObj.email || '');
      const mailtoUrl = `mailto:sales@taltekroofing.com?subject=Privacy%20Rights%20Request%20(${reqState})&body=Statutory%20Privacy%20Request:%20${reqType}%0D%0AName:%20${name}%0D%0AEmail:%20${email}%0D%0AState:%20${reqState}`;

      if (trackingNumberDisplay) {
        trackingNumberDisplay.textContent = 'DIRECT-COMPLIANCE-PREPARED';
      }
      form.style.display = 'none';
      if (confirmationBlock) {
        confirmationBlock.style.display = 'block';
        confirmationBlock.innerHTML = `
          <div style="text-align: center; padding: 24px; background: rgba(216,117,53,0.08); border: 1px solid var(--border-accent); border-radius: 6px;">
            <h3 style="color: var(--copper); font-size: 20px; margin-bottom: 8px;">Statutory Privacy Request Prepared</h3>
            <p style="color: var(--text-secondary); font-size: 14px; max-width: 600px; margin: 0 auto 16px; line-height: 1.6;">
              Your formal request under applicable US state privacy law has been formatted. Click below to transmit directly to our Privacy Compliance Officer:
            </p>
            <div style="display: flex; justify-content: center; gap: 12px; flex-wrap: wrap;">
              <a href="${mailtoUrl}" class="btn btn-primary btn-sm">Transmit to Compliance Officer &rarr;</a>
              <a href="tel:+16154486349" class="btn btn-secondary btn-sm">Phone: (615) 448-6349</a>
            </div>
          </div>
        `;
        confirmationBlock.scrollIntoView({ behavior: 'smooth' });
      }
    }
  });
}
