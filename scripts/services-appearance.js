document.addEventListener('DOMContentLoaded', function() {
  const cards = document.querySelectorAll('.service-card, .service-card-large');
  if (!cards.length) return;

  cards.forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(24px)';
    card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
  });

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const card = entry.target;
      card.style.opacity = '1';
      card.style.transform = 'translateY(0)';
      observer.unobserve(card);
    });
  }, {
    threshold: 0.2,
  });

  cards.forEach(card => observer.observe(card));
});