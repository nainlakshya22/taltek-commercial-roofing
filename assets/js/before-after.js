/**
 * TALTEK COMMERCIAL ROOFING - BEFORE/AFTER INTERACTIVE SLIDER
 * Feature 03: Accessible Draggable Comparison Slider
 * Touch, Mouse, Pointer & Keyboard (WCAG 2.2 AA) support.
 */

document.addEventListener('DOMContentLoaded', () => {
  initBeforeAfterSliders();
});

function initBeforeAfterSliders() {
  const sliders = document.querySelectorAll('.before-after-container');
  sliders.forEach(slider => setupSlider(slider));
}

function setupSlider(container) {
  const handle = container.querySelector('.ba-slider-handle');
  const afterLayer = container.querySelector('.ba-after-layer');
  if (!handle || !afterLayer) return;

  let isDragging = false;
  let currentPercentage = 50;

  const updatePosition = (percent) => {
    percent = Math.max(0, Math.min(100, percent));
    currentPercentage = percent;
    handle.style.left = `${percent}%`;
    // Left side (0 to percent%) reveals BEFORE layer; Right side (percent% to 100%) reveals AFTER layer
    afterLayer.style.clipPath = `polygon(${percent}% 0, 100% 0, 100% 100%, ${percent}% 100%)`;
    handle.setAttribute('aria-valuenow', Math.round(percent));
  };

  const getPositionFromEvent = (e) => {
    const rect = container.getBoundingClientRect();
    const clientX = e.touches ? e.touches[0].clientX : e.clientX;
    const x = clientX - rect.left;
    return (x / rect.width) * 100;
  };

  // Mouse & Touch events
  const onPointerDown = (e) => {
    isDragging = true;
    container.classList.add('is-dragging');
    updatePosition(getPositionFromEvent(e));
  };

  const onPointerMove = (e) => {
    if (!isDragging) return;
    updatePosition(getPositionFromEvent(e));
  };

  const onPointerUp = () => {
    if (!isDragging) return;
    isDragging = false;
    container.classList.remove('is-dragging');
  };

  container.addEventListener('mousedown', onPointerDown);
  window.addEventListener('mousemove', onPointerMove);
  window.addEventListener('mouseup', onPointerUp);

  container.addEventListener('touchstart', onPointerDown, { passive: true });
  window.addEventListener('touchmove', onPointerMove, { passive: true });
  window.addEventListener('touchend', onPointerUp);

  // Keyboard accessibility
  handle.setAttribute('tabindex', '0');
  handle.setAttribute('role', 'slider');
  handle.setAttribute('aria-label', 'Before and after roof replacement comparison slider');
  handle.setAttribute('aria-valuemin', '0');
  handle.setAttribute('aria-valuemax', '100');
  handle.setAttribute('aria-valuenow', '50');

  handle.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') {
      updatePosition(currentPercentage - 5);
      e.preventDefault();
    } else if (e.key === 'ArrowRight') {
      updatePosition(currentPercentage + 5);
      e.preventDefault();
    } else if (e.key === 'Home') {
      updatePosition(0);
      e.preventDefault();
    } else if (e.key === 'End') {
      updatePosition(100);
      e.preventDefault();
    }
  });

  // Initialize at 50%
  updatePosition(50);
}
