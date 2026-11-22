/**
 * TALTEK COMMERCIAL ROOFING - INTERACTIVE ROOF ESTIMATOR
 * Feature 02: Dynamic Commercial & Industrial Roof Estimator
 * Configurable pricing model with clear non-binding legal disclaimers.
 */

document.addEventListener('DOMContentLoaded', () => {
  initRoofEstimator();
});

function initRoofEstimator() {
  const container = document.getElementById('roof-estimator-app');
  if (!container) return;

  // State object
  const state = {
    buildingType: 'warehouse',
    roofArea: 25000,
    roofCondition: 'fair',
    existingMaterial: 'tpo',
    desiredSystem: 'jm-tpo-60',
    projectType: 'replacement', // 'replacement' or 'repair'
    locationState: 'TN'
  };

  // Base material costs per sq ft (benchmark industrial ranges)
  const systemBaseRates = {
    'jm-tpo-60': { min: 7.20, max: 10.50, name: 'Johns Manville 60-Mil TPO (20-Yr NDL Eligible)' },
    'jm-tpo-80': { min: 8.50, max: 12.00, name: 'Johns Manville 80-Mil Extreme TPO (25-30 Yr NDL Eligible)' },
    'elevate-epdm': { min: 7.80, max: 11.20, name: 'Elevate RubberGard EPDM (Firestone Single-Ply)' },
    'carlisle-epdm': { min: 7.80, max: 11.20, name: 'Elevate RubberGard EPDM (Firestone Single-Ply)' },
    'gaf-everguard': { min: 7.50, max: 10.80, name: 'GAF EverGuard Commercial TPO' },
    'pvc-chemical': { min: 8.90, max: 13.00, name: 'PVC Chemical & Grease Resistant Membrane' },
    'soprema-pmma': { min: 7.50, max: 10.80, name: 'GAF EverGuard Commercial TPO' },
    'metal-retrofit': { min: 8.00, max: 12.50, name: 'Flute-Fill Metal Roof TPO Retrofit' }
  };

  // Condition multipliers (tear-off and insulation replacement)
  const conditionMultipliers = {
    'good': 1.0,
    'fair': 1.10,
    'deteriorated': 1.25,
    'severe': 1.45 // High insulation saturation requires full teardown
  };

  // Project type multiplier
  const projectTypeMultipliers = {
    'replacement': 1.0,
    'repair': 0.35 // Partial restoration / targeted repair scope
  };

  // DOM Elements
  const areaSlider = document.getElementById('est-roof-area');
  const areaInput = document.getElementById('est-area-number');
  const priceDisplay = document.getElementById('est-price-range');
  const summaryArea = document.getElementById('est-summary-area');
  const summarySystem = document.getElementById('est-summary-system');
  const summaryScope = document.getElementById('est-summary-scope');
  const summaryCondition = document.getElementById('est-summary-condition');
  const prefillCta = document.getElementById('est-transfer-quote-btn');

  // Calculation Function
  const calculateEstimate = () => {
    const system = systemBaseRates[state.desiredSystem] || systemBaseRates['jm-tpo-60'];
    const condMult = conditionMultipliers[state.roofCondition] || 1.10;
    const typeMult = projectTypeMultipliers[state.projectType] || 1.0;

    const baseMin = system.min * condMult * typeMult;
    const baseMax = system.max * condMult * typeMult;

    const totalMin = Math.round(state.roofArea * baseMin);
    const totalMax = Math.round(state.roofArea * baseMax);

    // Format currency
    const fmtMin = '$' + totalMin.toLocaleString();
    const fmtMax = '$' + totalMax.toLocaleString();

    if (priceDisplay) {
      priceDisplay.textContent = `${fmtMin} – ${fmtMax}`;
    }

    if (summaryArea) summaryArea.textContent = `${state.roofArea.toLocaleString()} sq. ft.`;
    if (summarySystem) summarySystem.textContent = system.name;
    if (summaryScope) summaryScope.textContent = state.projectType === 'replacement' ? 'Full Tear-Off & Replacement' : 'Targeted Repair & Seam Restoration';
    if (summaryCondition) summaryCondition.textContent = capitalizeFirstLetter(state.roofCondition);

    // Update CTA link with query params to prefill request-inspection.html
    if (prefillCta) {
      const params = new URLSearchParams({
        building: state.buildingType,
        sqft: state.roofArea,
        system: state.desiredSystem,
        scope: state.projectType,
        condition: state.roofCondition
      });
      prefillCta.setAttribute('href', `request-inspection.html?${params.toString()}`);
    }
  };

  function capitalizeFirstLetter(string) {
    if (!string) return '';
    return string.charAt(0).toUpperCase() + string.slice(1);
  }

  // Handle Area Slider & Input
  if (areaSlider && areaInput) {
    areaSlider.addEventListener('input', (e) => {
      const parsed = parseInt(e.target.value, 10);
      if (!isNaN(parsed) && parsed > 0) {
        state.roofArea = parsed;
        areaInput.value = state.roofArea;
        calculateEstimate();
      }
    });

    areaInput.addEventListener('input', (e) => {
      let raw = e.target.value.replace(/[^0-9]/g, '');
      if (raw === '') {
        // Allow user to clear input while typing without breaking calculation
        return;
      }
      let val = parseInt(raw, 10);
      if (!isNaN(val) && val > 0) {
        val = Math.max(500, Math.min(1000000, val));
        state.roofArea = val;
        areaSlider.value = Math.min(300000, val);
        calculateEstimate();
      }
    });

    areaInput.addEventListener('blur', () => {
      let val = parseInt(areaInput.value, 10);
      if (isNaN(val) || val < 1000) val = 1000;
      if (val > 1000000) val = 1000000;
      state.roofArea = val;
      areaInput.value = val;
      areaSlider.value = Math.min(300000, val);
      calculateEstimate();
    });
  }

  // Handle Tile Selections (Building Type, Desired System, Condition)
  const setupTileGroup = (selectorClass, stateKey) => {
    const tiles = document.querySelectorAll(selectorClass);
    tiles.forEach(tile => {
      tile.addEventListener('click', () => {
        tiles.forEach(t => t.classList.remove('active'));
        tile.classList.add('active');
        state[stateKey] = tile.getAttribute('data-value');
        calculateEstimate();
      });
    });
  };

  setupTileGroup('.building-tile', 'buildingType');
  setupTileGroup('.system-tile', 'desiredSystem');
  setupTileGroup('.condition-tile', 'roofCondition');
  setupTileGroup('.project-type-tile', 'projectType');

  // Initial calculation
  calculateEstimate();
}
