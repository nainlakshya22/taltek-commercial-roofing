/**
 * TALTEK COMMERCIAL ROOFING - FINANCING CALCULATOR
 * Feature 06: Commercial Project Financing Calculator
 * Standard commercial amortization formula with legal disclaimers.
 */

document.addEventListener('DOMContentLoaded', () => {
  initFinancingCalculator();
});

function initFinancingCalculator() {
  const form = document.getElementById('financing-calc-form');
  if (!form) return;

  const costInput = document.getElementById('fin-project-cost');
  const costSlider = document.getElementById('fin-cost-slider');
  const downPaymentInput = document.getElementById('fin-down-payment');
  const termSelect = document.getElementById('fin-term-months');
  const rateInput = document.getElementById('fin-interest-rate');

  const outMonthly = document.getElementById('fin-output-monthly');
  const outTotal = document.getElementById('fin-output-total');
  const outInterest = document.getElementById('fin-output-interest');
  const outFinancedAmount = document.getElementById('fin-output-financed-amount');

  const calculate = () => {
    let cost = parseFloat(costInput.value) || 100000;
    let down = parseFloat(downPaymentInput.value) || 0;
    if (down > cost) down = cost * 0.5;

    let principal = cost - down;
    let months = parseInt(termSelect.value, 10) || 60;
    let annualRate = parseFloat(rateInput.value) || 7.5;
    let monthlyRate = (annualRate / 100) / 12;

    let monthlyPayment = 0;
    let totalRepaid = 0;
    let totalInterest = 0;

    if (monthlyRate === 0) {
      monthlyPayment = principal / months;
      totalRepaid = principal;
    } else {
      monthlyPayment = principal * (monthlyRate * Math.pow(1 + monthlyRate, months)) / (Math.pow(1 + monthlyRate, months) - 1);
      totalRepaid = monthlyPayment * months;
      totalInterest = totalRepaid - principal;
    }

    if (outMonthly) outMonthly.textContent = '$' + Math.round(monthlyPayment).toLocaleString();
    if (outTotal) outTotal.textContent = '$' + Math.round(totalRepaid).toLocaleString();
    if (outInterest) outInterest.textContent = '$' + Math.round(totalInterest).toLocaleString();
    if (outFinancedAmount) outFinancedAmount.textContent = '$' + Math.round(principal).toLocaleString();
  };

  // Sync Slider and Number Input
  if (costSlider && costInput) {
    costSlider.addEventListener('input', (e) => {
      costInput.value = e.target.value;
      calculate();
    });

    costInput.addEventListener('input', (e) => {
      let val = parseFloat(e.target.value);
      if (!isNaN(val)) {
        costSlider.value = val;
      }
      calculate();
    });
  }

  [downPaymentInput, termSelect, rateInput].forEach(elem => {
    if (elem) elem.addEventListener('input', calculate);
  });

  calculate();
}
