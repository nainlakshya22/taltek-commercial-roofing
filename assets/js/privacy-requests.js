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
      console.error('Privacy request transmission error:', err);
      alert('Network Notice: Unable to connect to TALTEK compliance register. Please contact our Privacy Compliance Officer directly at sales@taltekroofing.com or +1 (615) 448-6349.');
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Retry Submission';
      }
    }
  });
}
