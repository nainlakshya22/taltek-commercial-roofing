/**
 * TALTEK COMMERCIAL ROOFING - PORTFOLIO FILTER
 * Feature 04: Filterable Commercial & Industrial Portfolio
 */

document.addEventListener('DOMContentLoaded', () => {
  initPortfolioFilter();
});

function initPortfolioFilter() {
  const filterBtns = document.querySelectorAll('.portfolio-filter-bar .filter-btn');
  const projectCards = document.querySelectorAll('.project-grid .project-card');
  const countDisplay = document.getElementById('portfolio-results-count');

  if (!filterBtns.length || !projectCards.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      // Toggle active button
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterValue = btn.getAttribute('data-filter');
      let visibleCount = 0;

      projectCards.forEach(card => {
        const categories = card.getAttribute('data-categories') || '';
        const catArray = categories.split(' ').map(c => c.trim().toLowerCase());

        if (filterValue === 'all' || catArray.includes(filterValue.toLowerCase())) {
          card.style.display = 'flex';
          visibleCount++;
        } else {
          card.style.display = 'none';
        }
      });

      if (countDisplay) {
        countDisplay.textContent = `Showing ${visibleCount} Project${visibleCount === 1 ? '' : 's'}`;
      }
    });
  });
}
