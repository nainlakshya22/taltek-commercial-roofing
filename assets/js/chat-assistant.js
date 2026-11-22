/**
 * TALTEK COMMERCIAL ROOFING - LIVE CHAT & AI ASSISTANT
 * Feature 10: Industrial Roofing AI Assistant
 * - Automated badge (clearly states automated/non-human)
 * - Industrial commercial knowledge base
 * - Seamless human escalation routes
 * - Privacy and consent compliance
 */

document.addEventListener('DOMContentLoaded', () => {
  initChatAssistant();
});

function initChatAssistant() {
  const toggleBtn = document.getElementById('chat-toggle-btn');
  const panel = document.getElementById('chat-panel');
  const closeBtn = document.getElementById('chat-close-btn');
  const messagesContainer = document.getElementById('chat-messages');
  const inputField = document.getElementById('chat-user-input');
  const sendBtn = document.getElementById('chat-send-btn');
  const chipsContainer = document.getElementById('chat-quick-chips');

  if (!toggleBtn || !panel) return;

  // Knowledge base for instant commercial answers
  const knowledgeBase = [
    {
      keywords: ['tpo', 'polyolefin', 'white roof', 'cool roof'],
      answer: "TPO (Thermoplastic Polyolefin) is TALTEK's most widely specified single-ply membrane. We install 60-mil and 80-mil systems with robotic heat-welded seams (3x stronger than tape). It offers high solar reflectivity (ENERGY STAR), hail resistance, and manufacturer NDL warranties up to 30 years from Johns Manville, GAF, and Carlisle."
    },
    {
      keywords: ['epdm', 'rubber', 'black roof'],
      answer: "EPDM (Ethylene Propylene Diene Monomer) synthetic rubber offers outstanding dimensional stability and 300% thermal elongation. It performs exceptionally well in freeze-thaw cycles and Northern/Mid-Atlantic climates. For example, TALTEK completed a 100,000 sq. ft. EPDM retrofit at Malone Plaza in under 60 days."
    },
    {
      keywords: ['pvc', 'chemical', 'grease', 'restaurant'],
      answer: "PVC (Polyvinyl Chloride) membranes with Elvaloy KEE formulations are engineered specifically for roofs exposed to animal fats, grease exhausts, jet fuel, and industrial acids. They are ASTM D4434 Type III certified and ideal for manufacturing plants and food processing facilities."
    },
    {
      keywords: ['emergency', 'leak', 'urgent', 'storm', 'water'],
      answer: "TALTEK maintains a 24/7 Rapid Emergency Response Team for commercial leaks and storm damage across Tennessee and our Southeastern hubs. Call our dispatch hotline immediately at +1 (615) 448-6349 for immediate priority mobilization."
    },
    {
      keywords: ['warranty', 'ndl', 'guarantee'],
      answer: "TALTEK provides Manufacturer No Dollar Limit (NDL) Warranties up to 20 to 30 years covering 100% of labor and materials, backed directly by manufacturers including Johns Manville, GAF, Carlisle, and Soprema, paired with TALTEK's standard 2-Year Contractor Workmanship Warranty."
    },
    {
      keywords: ['area', 'location', 'state', 'tennessee', 'alabama', 'licens'],
      answer: "TALTEK is headquartered at 1214 S. Dickerson Rd, Goodlettsville, TN, and operates across 15 Southeastern states, with direct contractor licensing in Tennessee, Alabama, Louisiana, Mississippi, North Carolina, South Carolina, and Virginia."
    },
    {
      keywords: ['cost', 'price', 'estimate', 'sqft', 'square foot'],
      answer: "Commercial roofing costs typically range from $7.00 to $13.50+ per square foot depending on system type (TPO/EPDM/PVC), deck condition, insulation R-value requirements, and tear-off scope. You can use our interactive Commercial Roof Estimator on this website, or schedule a physical core sample inspection."
    },
    {
      keywords: ['inspection', 'quote', 'schedule'],
      answer: "You can schedule a complimentary comprehensive commercial roof inspection right on this site! We perform non-destructive moisture scans, core sampling, and structural deck assessments. Would you like to proceed to the Request Inspection page?"
    },
    {
      keywords: ['human', 'person', 'representative', 'agent', 'call', 'talk'],
      answer: "I can connect you directly with a TALTEK commercial roofing estimator. Please call our Goodlettsville HQ at +1 (615) 448-6349 (Mon-Fri 7am-6pm CT) or email sales@taltekroofing.com."
    }
  ];

  const defaultGreeting = "Hello! I am TALTEK's Automated Industrial Roofing Assistant. How can I assist with your commercial property today?";

  const togglePanel = () => {
    panel.classList.toggle('active');
    if (panel.classList.contains('active')) {
      inputField?.focus();
    }
  };

  toggleBtn.addEventListener('click', togglePanel);
  closeBtn?.addEventListener('click', togglePanel);

  const appendMessage = (text, sender = 'bot', isHtml = false) => {
    if (!messagesContainer) return;
    const msg = document.createElement('div');
    msg.className = `chat-bubble ${sender}`;
    if (isHtml) {
      msg.innerHTML = text;
    } else {
      msg.textContent = text;
    }
    messagesContainer.appendChild(msg);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  };

  const processQuery = (userText) => {
    const textLower = userText.toLowerCase();

    // Look for matching keywords in knowledge base
    let match = null;
    for (const item of knowledgeBase) {
      if (item.keywords.some(kw => textLower.includes(kw))) {
        match = item;
        break;
      }
    }

    setTimeout(() => {
      if (match) {
        appendMessage(match.answer, 'bot');
      } else {
        appendMessage(
          "Thank you for your question. For detailed technical specifications, project proposals, or immediate engineer dispatch, please call our corporate office at <a href='tel:+16154486349' style='color: var(--copper); text-decoration: underline;'>+1 (615) 448-6349</a> or <a href='/request-inspection.html' style='color: var(--copper); text-decoration: underline;'>Request an On-Site Roof Inspection</a>.",
          'bot',
          true
        );
      }
    }, 450);
  };

  const handleSend = () => {
    const query = inputField.value.trim();
    if (!query) return;

    appendMessage(query, 'user');
    inputField.value = '';
    processQuery(query);
  };

  if (sendBtn && inputField) {
    sendBtn.addEventListener('click', handleSend);
    inputField.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        handleSend();
      }
    });
  }

  // Handle Quick Chips
  if (chipsContainer) {
    const chips = chipsContainer.querySelectorAll('.chat-chip');
    chips.forEach(chip => {
      chip.addEventListener('click', () => {
        const query = chip.textContent.trim();
        appendMessage(query, 'user');
        processQuery(query);
      });
    });
  }
}
