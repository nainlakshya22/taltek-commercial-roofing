/**
 * TALTEK COMMERCIAL ROOFING - MAIN SCRIPT
 * Navigation, Sticky Header, Stats Counter & Accessibility
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileDrawer();
  initStatsCounter();
  initScrollReveals();
  highlightActiveNav();
});

// 1. Sticky Header
function initStickyHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  const handleScroll = () => {
    if (window.scrollY > 20) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
}

// 2. Mobile Drawer
function initMobileDrawer() {
  const toggleBtn = document.querySelector('.mobile-nav-toggle');
  const drawer = document.querySelector('.mobile-drawer');
  const closeBtn = document.querySelector('.drawer-close');
  const backdrop = document.querySelector('.drawer-backdrop');

  if (!toggleBtn || !drawer) return;

  const openDrawer = () => {
    drawer.classList.add('open');
    if (backdrop) backdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
    toggleBtn.setAttribute('aria-expanded', 'true');
    closeBtn?.focus();
  };

  const closeDrawer = () => {
    drawer.classList.remove('open');
    if (backdrop) backdrop.classList.remove('active');
    document.body.style.overflow = '';
    toggleBtn.setAttribute('aria-expanded', 'false');
    toggleBtn.focus();
  };

  toggleBtn.addEventListener('click', openDrawer);
  closeBtn?.addEventListener('click', closeDrawer);
  backdrop?.addEventListener('click', closeDrawer);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('open')) {
      closeDrawer();
    }
  });
}

// 3. Stats Counter Animation
function initStatsCounter() {
  const counters = document.querySelectorAll('[data-counter-target]');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseFloat(el.getAttribute('data-counter-target'));
        const prefix = el.getAttribute('data-counter-prefix') || '';
        const suffix = el.getAttribute('data-counter-suffix') || '';
        const isDecimal = target % 1 !== 0;

        let start = 0;
        const duration = 1800;
        const startTime = performance.now();

        const update = (now) => {
          const progress = Math.min((now - startTime) / duration, 1);
          const easeProgress = 1 - Math.pow(1 - progress, 3); // Ease out cubic
          const current = start + (target - start) * easeProgress;

          if (isDecimal) {
            el.textContent = `${prefix}${current.toFixed(1)}${suffix}`;
          } else {
            el.textContent = `${prefix}${Math.floor(current).toLocaleString()}${suffix}`;
          }

          if (progress < 1) {
            requestAnimationFrame(update);
          } else {
            el.textContent = `${prefix}${isDecimal ? target.toFixed(1) : target.toLocaleString()}${suffix}`;
          }
        };

        requestAnimationFrame(update);
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.2 });

  counters.forEach(c => observer.observe(c));
}

// 4. Scroll Reveals
function initScrollReveals() {
  const elements = document.querySelectorAll('.reveal-init');
  if (!elements.length) return;

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    elements.forEach(el => el.classList.add('revealed'));
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  elements.forEach(el => observer.observe(el));
}

// 5. Highlight Active Nav Item
function highlightActiveNav() {
  const currentPath = window.location.pathname.replace(/\/$/, '') || '/index.html';
  const navLinks = document.querySelectorAll('.nav-link, .drawer-link, .drawer-sublink');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;
    const cleanHref = href.replace(/\/$/, '');
    if (cleanHref === currentPath || (currentPath.endsWith(cleanHref) && cleanHref !== '')) {
      link.classList.add('active');
    }
  });
}
