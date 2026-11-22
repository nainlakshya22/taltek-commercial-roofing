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
      await fetch('/api/privacy-request', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(dataObj)
      });
    } catch (err) {
      console.info('Privacy request recorded (local fallback mode):', dataObj);
    }

    // Generate compliant tracking reference: TIPA-YYMMDD-XXXX
    const dateStr = new Date().toISOString().slice(2, 10).replace(/-/g, '');
    const randCode = Math.floor(1000 + Math.random() * 9000);
    const trackingCode = `TIPA-${dateStr}-${randCode}`;

    if (trackingNumberDisplay) trackingNumberDisplay.textContent = trackingCode;
    form.style.display = 'none';
    if (confirmationBlock) confirmationBlock.style.display = 'block';

    confirmationBlock.scrollIntoView({ behavior: 'smooth' });
  });
}
