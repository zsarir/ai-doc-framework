// AI Documentation Framework - Main JavaScript
// Performance and functionality optimized for GitHub Pages

class WikiApp {
  constructor() {
    this.startTime = performance.now();
    this.init();
  }

  init() {
    this.setupEventListeners();
    this.setupAnimations();
    this.setupNavigation();
    this.logPerformance();
  }

  setupEventListeners() {
    // Mobile menu toggle
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const navMenu = document.getElementById('navMenu');

    if (mobileMenuBtn && navMenu) {
      mobileMenuBtn.addEventListener('click', () => {
        navMenu.classList.toggle('mobile-open');
      });
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', (e) => {
        e.preventDefault();
        const target = document.querySelector(anchor.getAttribute('href'));
        if (target) {
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      });
    });

    // Dropdown menu handling
    document.querySelectorAll('.dropdown-toggle').forEach(toggle => {
      toggle.addEventListener('click', (e) => {
        e.preventDefault();
        const dropdown = toggle.parentElement;
        dropdown.classList.toggle('open');
      });
    });
  }

  setupAnimations() {
    // Intersection Observer for animations
    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    }, observerOptions);

    // Observe elements for animation
    document.querySelectorAll('.fade-in, .slide-in-left, .slide-in-right').forEach(el => {
      observer.observe(el);
    });

    // Metric cards animation (safe version)
    this.setupMetricCards();
  }

  setupMetricCards() {
    const metricCards = document.querySelectorAll('.metric-card');

    if (metricCards.length === 0) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          this.animateMetricCard(entry.target);
        }
      });
    }, { threshold: 0.5 });

    metricCards.forEach(card => {
      observer.observe(card);
    });
  }

  animateMetricCard(card) {
    // Skip if already animated
    if (card.dataset.animated) return;

    card.dataset.animated = 'true';
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';

    setTimeout(() => {
      card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
      card.style.opacity = '1';
      card.style.transform = 'translateY(0)';
    }, 100);
  }

  setupNavigation() {
    // Highlight current page in navigation
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
      if (link.getAttribute('href') === currentPath) {
        link.classList.add('active');
      }
    });
  }

  logPerformance() {
    const endTime = performance.now();
    const loadTime = (endTime - this.startTime).toFixed(2);

    console.log(`🚀 AI Documentation Framework loaded in ${loadTime}ms`);

    // Log page information
    if (window.location.hostname.includes('github.io')) {
      console.log('📄 GitHub Pages environment detected');
    }

    // Check if we're on the home page
    if (window.location.pathname === '/ai-doc-framework/' || window.location.pathname === '/ai-doc-framework') {
      console.log('🏠 Home page loaded successfully');
    }
  }

  // Utility method for safe element selection
  static $(selector, context = document) {
    return context.querySelector(selector);
  }

  static $$(selector, context = document) {
    return context.querySelectorAll(selector);
  }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  try {
    new WikiApp();
  } catch (error) {
    console.error('❌ Wiki initialization error:', error);
  }
});

// Handle browser back/forward navigation
window.addEventListener('popstate', () => {
  // Reinitialize navigation highlighting
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-link').forEach(link => {
    link.classList.remove('active');
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });
});

// Error handling for failed resource loads
window.addEventListener('error', (e) => {
  if (e.target.tagName === 'IMG' || e.target.tagName === 'SCRIPT' || e.target.tagName === 'LINK') {
    console.warn(`⚠️ Failed to load resource: ${e.target.src || e.target.href}`);
  }
}, true);

// Performance monitoring
if ('performance' in window && 'mark' in window.performance) {
  performance.mark('wiki-start');
}

// Export for potential use in other scripts
window.WikiApp = WikiApp;
