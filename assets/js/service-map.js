/**
 * TALTEK COMMERCIAL ROOFING - INTERACTIVE SERVICE AREA MAP
 * Feature 08: 15-State Southeastern Operations & Verified Licensing
 */

document.addEventListener('DOMContentLoaded', () => {
  initServiceMap();
});

function initServiceMap() {
  const mapSvg = document.querySelector('.taltek-service-map');
  const ttState = document.getElementById('tt-state-name');
  const ttStatus = document.getElementById('tt-status');
  const ttLicense = document.getElementById('tt-license');
  const ttProjects = document.getElementById('tt-projects');
  const externalSummary = document.getElementById('state-detail-panel');

  if (!mapSvg) return;

  const stateData = {
    'Tennessee': {
      status: 'Headquarters & Primary Dispatch Hub',
      address: '1214 S. Dickerson Rd, Goodlettsville, TN 37072',
      phone: '+1 (615) 448-6349',
      license: 'Tennessee Board for Licensing Contractors (Classified CMC-C Commercial)',
      projects: '5,200+ Commercial & Industrial Roofs Installed',
      highlights: 'Nashville General Hospital (18k sqft), Rapha Center (10.5k sqft)',
      isHq: true
    },
    'Alabama': {
      status: 'Verified Licensed State — Regional Hub (Birmingham)',
      phone: '+1 (615) 448-6349',
      license: 'Alabama State Licensing Board for General Contractors',
      projects: '840+ Commercial Installations & Replacements',
      highlights: 'Industrial Distribution Centers, High-Wind Fastening Specs',
      isHq: false
    },
    'Mississippi': {
      status: 'Verified Licensed State — Gulf Region Operations',
      phone: '+1 (615) 448-6349',
      license: 'Mississippi State Board of Contractors (Commercial Roofing)',
      projects: '620+ Commercial Projects',
      highlights: 'Heavy Storm Defense, Severe Weather Emergency Deployments',
      isHq: false
    },
    'Louisiana': {
      status: 'Verified Licensed State — Gulf Coast Operations',
      phone: '+1 (615) 448-6349',
      license: 'Louisiana State Licensing Board for Contractors',
      projects: '510+ Industrial & Marine Atmosphere Installations',
      highlights: 'Chemical Resistant PVC & Single-Ply Waterproofing',
      isHq: false
    },
    'North Carolina': {
      status: 'Verified Licensed State — Regional Hub (Charlotte)',
      phone: '+1 (615) 448-6349',
      license: 'North Carolina Licensing Board for General Contractors (Commercial)',
      projects: '920+ Commercial & Multi-Family Facilities',
      highlights: 'Piedmont Triad Distribution Hubs, Johns Manville NDL Systems',
      isHq: false
    },
    'South Carolina': {
      status: 'Verified Licensed State — Coastal & Upstate Hubs',
      phone: '+1 (615) 448-6349',
      license: 'South Carolina Commercial Contractors Licensing Board',
      projects: '710+ Projects Completed',
      highlights: 'Manufacturing Facilities, Hurricane Uplift Engineered Systems',
      isHq: false
    },
    'Virginia': {
      status: 'Verified Licensed State — Mid-Atlantic Hub (Richmond)',
      phone: '+1 (615) 448-6349',
      license: 'Virginia Board for Contractors (Class A Commercial Roofing)',
      projects: '830+ Institutional & Commercial Roofs',
      highlights: 'Government Facilities, Cold Weather EPDM & TPO Applications',
      isHq: false
    },
    'Kentucky': {
      status: 'Operational Southeastern Territory',
      phone: '+1 (615) 448-6349',
      license: 'Commercial Deployment Ready & Insured',
      projects: '440+ Completed Projects',
      highlights: 'Krusteaz Manufacturing Facility (205,869 sq ft TPO)',
      isHq: false
    },
    'Georgia': {
      status: 'Operational Southeastern Territory',
      phone: '+1 (615) 448-6349',
      license: 'Commercial Logistics & Rapid Dispatch',
      projects: '890+ Completed Projects',
      highlights: 'Atlanta Metro Logistics Parks, Johns Manville Systems',
      isHq: false
    },
    'Florida': {
      status: 'Operational Southeastern Territory',
      phone: '+1 (615) 448-6349',
      license: 'Emergency Disaster Response & Logistics Support',
      projects: '650+ Commercial Support Operations',
      highlights: 'Severe Storm Post-Hurricane Disaster Recovery Teams',
      isHq: false
    },
    'Arkansas': {
      status: 'Operational Southeastern Territory',
      phone: '+1 (615) 448-6349',
      license: 'Commercial Deployment Support',
      projects: '260+ Facilities Serviced',
      highlights: 'Agricultural Processing & Warehousing Roof Systems',
      isHq: false
    }
  };

  const statePaths = mapSvg.querySelectorAll('.state-path');

  const selectState = (stateName) => {
    const data = stateData[stateName] || {
      status: 'Southeastern Operational Area',
      license: 'Certified Commercial Roofing',
      projects: 'Active Service Region',
      phone: '+1 (615) 448-6349'
    };

    if (ttState) ttState.textContent = stateName.toUpperCase() + (data.isHq ? ' (HEADQUARTERS)' : '');
    if (ttStatus) ttStatus.textContent = data.status.toUpperCase();
    if (ttLicense) ttLicense.textContent = 'License: ' + data.license;
    if (ttProjects) ttProjects.textContent = 'Projects: ' + data.projects;

    if (externalSummary) {
      externalSummary.innerHTML = `
        <div class="state-selected-card" style="background: var(--bg-card); border: 1px solid var(--border-accent); border-radius: 6px; padding: 24px;">
          <div style="font-family: var(--font-mono); font-size: 11px; color: var(--copper); font-weight: 700; margin-bottom: 6px;">[ SERVICE REGION SPECIFICATION ]</div>
          <h3 style="font-size: 22px; color: var(--text-primary); margin-bottom: 8px;">${stateName} ${data.isHq ? '<span style="font-size: 12px; color: var(--copper); background: rgba(216,117,53,0.15); padding: 2px 8px; border-radius: 2px;">HQ LOCATION</span>' : ''}</h3>
          <p style="color: var(--text-secondary); font-size: 14px; margin-bottom: 16px;">${data.status}</p>
          <div style="display: grid; gap: 8px; font-size: 13px; margin-bottom: 20px; border-top: 1px solid var(--border-subtle); padding-top: 12px;">
            <div><strong style="color: var(--text-primary);">Licensing:</strong> <span style="color: var(--text-secondary);">${data.license}</span></div>
            <div><strong style="color: var(--text-primary);">Track Record:</strong> <span style="color: var(--text-secondary);">${data.projects}</span></div>
            ${data.address ? `<div><strong style="color: var(--text-primary);">Physical Office:</strong> <span style="color: var(--text-secondary);">${data.address}</span></div>` : ''}
            ${data.highlights ? `<div><strong style="color: var(--text-primary);">Key Project Highlights:</strong> <span style="color: var(--text-secondary);">${data.highlights}</span></div>` : ''}
          </div>
          <a href="/request-inspection.html?state=${encodeURIComponent(stateName)}" class="btn btn-primary btn-sm">Request ${stateName} Inspection</a>
        </div>
      `;
    }
  };

  statePaths.forEach(path => {
    path.addEventListener('mouseenter', () => {
      const stateName = path.getAttribute('data-state');
      if (stateName) selectState(stateName);
    });

    path.addEventListener('click', () => {
      const stateName = path.getAttribute('data-state');
      if (stateName) selectState(stateName);
    });
  });

  // Default select Tennessee
  selectState('Tennessee');
}
