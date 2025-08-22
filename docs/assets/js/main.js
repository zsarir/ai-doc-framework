// AI Documentation Framework Wiki - Interactive JavaScript

document.addEventListener('DOMContentLoaded', function() {
    initializeWiki();
});

function initializeWiki() {
    setupNavigation();
    setupSearch();
    setupAnimations();
    setupFeatureCards();
    setupUseCaseTabs();
    setupMetrics();
    initializeCodeHighlighting();
}

// Navigation Setup
function setupNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.section');
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navMenu = document.querySelector('.nav-menu');

    // Mobile menu toggle
    if (mobileMenuBtn && navMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            navMenu.classList.toggle('mobile-open');
            const isOpen = navMenu.classList.contains('mobile-open');
            mobileMenuBtn.innerHTML = isOpen ? '<i class="fas fa-times"></i>' : '<i class="fas fa-bars"></i>';
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!navMenu.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
                navMenu.classList.remove('mobile-open');
                mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
            }
        });
    }

    // Smooth scrolling navigation
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = link.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);

            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }

            // Update active link
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');

            // Close mobile menu after navigation
            if (navMenu && navMenu.classList.contains('mobile-open')) {
                navMenu.classList.remove('mobile-open');
                if (mobileMenuBtn) {
                    mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
                }
            }
        });
    });

    // Update active navigation on scroll
    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (scrollY >= sectionTop - 100) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').substring(1) === current) {
                link.classList.add('active');
            }
        });
    });
}

// Search Functionality
function setupSearch() {
    const searchInput = document.getElementById('searchInput');
    const searchableContent = document.querySelectorAll('h1, h2, h3, h4, h5, h6, p, .feature-card h3, .quickstart-card h3');

    // Only setup search if search input exists on the page
    if (!searchInput) {
        return;
    }

    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();

        if (query.length < 2) {
            clearSearchHighlights();
            return;
        }

        searchableContent.forEach(element => {
            const text = element.textContent.toLowerCase();
            if (text.includes(query)) {
                highlightElement(element, query);
                element.style.display = 'block';
            } else {
                element.style.display = 'none';
            }
        });
    });
}

function highlightElement(element, query) {
    const text = element.textContent;
    const regex = new RegExp(`(${query})`, 'gi');
    const highlightedText = text.replace(regex, '<mark class="search-highlight">$1</mark>');
    element.innerHTML = highlightedText;
}

function clearSearchHighlights() {
    document.querySelectorAll('.search-highlight').forEach(mark => {
        const parent = mark.parentNode;
        parent.innerHTML = parent.textContent;
    });

    // Show all elements
    document.querySelectorAll('h1, h2, h3, h4, h5, h6, p, .feature-card h3, .quickstart-card h3').forEach(element => {
        element.style.display = 'block';
    });
}

// Feature Cards Animation
function setupFeatureCards() {
    const featureCards = document.querySelectorAll('.feature-card');

    featureCards.forEach(card => {
        card.addEventListener('click', () => {
            card.classList.toggle('expanded');

            // Close other expanded cards
            featureCards.forEach(otherCard => {
                if (otherCard !== card) {
                    otherCard.classList.remove('expanded');
                }
            });
        });
    });
}

// Use Case Tabs
function setupUseCaseTabs() {
    window.showUseCase = function(caseType) {
        // Hide all use case content
        document.querySelectorAll('.usecase-content').forEach(content => {
            content.classList.remove('active');
        });

        // Remove active class from all tabs
        document.querySelectorAll('.usecase-tab').forEach(tab => {
            tab.classList.remove('active');
        });

        // Show selected content and activate tab
        document.getElementById(`${caseType}-case`).classList.add('active');
        event.target.classList.add('active');
    };
}

// Metrics Animation
function setupMetrics() {
    const metricCards = document.querySelectorAll('.metric-card');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateMetricCard(entry.target);
            }
        });
    }, { threshold: 0.5 });

    metricCards.forEach(card => {
        observer.observe(card);
    });
}

function animateMetricCard(card) {
    const chart = card.querySelector('.chart-circle');
    const percentage = chart.style.getPropertyValue('--percentage').replace('%', '');
    const text = chart.querySelector('.chart-text');

    let current = 0;
    const increment = percentage / 60;
    const timer = setInterval(() => {
        current += increment;
        if (current >= percentage) {
            current = percentage;
            clearInterval(timer);
        }
        text.textContent = Math.round(current) + '%';
    }, 50);
}

// Animations on Scroll
function setupAnimations() {
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
    document.querySelectorAll('.feature-card, .quickstart-card, .metric-card, .example-item').forEach(element => {
        element.classList.add('fade-in');
        observer.observe(element);
    });

    // Stagger animations for grid items
    document.querySelectorAll('.features-grid .feature-card').forEach((element, index) => {
        element.style.animationDelay = `${index * 0.1}s`;
    });

    document.querySelectorAll('.quickstart-grid .quickstart-card').forEach((element, index) => {
        element.style.animationDelay = `${index * 0.15}s`;
    });
}

// Code Highlighting
function initializeCodeHighlighting() {
    // Add copy button to code blocks
    document.querySelectorAll('pre code').forEach(block => {
        const button = document.createElement('button');
        button.className = 'copy-button';
        button.innerHTML = '<i class="fas fa-copy"></i>';
        button.title = 'Copy to clipboard';

        button.addEventListener('click', () => {
            navigator.clipboard.writeText(block.textContent).then(() => {
                button.innerHTML = '<i class="fas fa-check"></i>';
                setTimeout(() => {
                    button.innerHTML = '<i class="fas fa-copy"></i>';
                }, 2000);
            });
        });

        block.parentNode.style.position = 'relative';
        block.parentNode.appendChild(button);
    });
}

// Utility Functions
function showQuickStart() {
    document.querySelector('#quickstart').scrollIntoView({
        behavior: 'smooth',
        block: 'start'
    });
}

function scrollToFeatures() {
    document.querySelector('#features').scrollIntoView({
        behavior: 'smooth',
        block: 'start'
    });
}

function loadPage(pageUrl) {
    // Simple page loading simulation
    console.log(`Loading page: ${pageUrl}`);

    // In a real implementation, you would load the page content here
    // For now, we'll just show an alert
    alert(`This would load: ${pageUrl}\n\nIn a full implementation, this would dynamically load the page content.`);
}

// Interactive Architecture Diagram
function initializeArchitectureDiagram() {
    const nodes = document.querySelectorAll('.diagram-node');

    nodes.forEach(node => {
        node.addEventListener('mouseenter', () => {
            // Add glow effect
            node.style.boxShadow = '0 0 20px rgba(99, 102, 241, 0.3)';
        });

        node.addEventListener('mouseleave', () => {
            // Remove glow effect
            node.style.boxShadow = '';
        });
    });
}

// Performance Monitoring
function setupPerformanceMonitoring() {
    // Monitor page load performance
    window.addEventListener('load', () => {
        if ('performance' in window) {
            const perfData = performance.getEntriesByType('navigation')[0];
            console.log('Page load time:', perfData.loadEventEnd - perfData.fetchStart, 'ms');
        }
    });

    // Monitor user interactions
    document.addEventListener('click', (e) => {
        if (e.target.matches('.btn, .nav-link, .feature-card')) {
            console.log('User clicked:', e.target.textContent || e.target.className);
        }
    });
}

// Accessibility Enhancements
function setupAccessibility() {
    // Add ARIA labels and roles
    document.querySelectorAll('.feature-card').forEach(card => {
        card.setAttribute('role', 'button');
        card.setAttribute('tabindex', '0');
        card.setAttribute('aria-expanded', 'false');

        card.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                card.click();
            }
        });

        card.addEventListener('click', () => {
            const expanded = card.classList.contains('expanded');
            card.setAttribute('aria-expanded', expanded.toString());
        });
    });

    // Add skip links
    const skipLink = document.createElement('a');
    skipLink.href = '#main-content';
    skipLink.className = 'skip-link';
    skipLink.textContent = 'Skip to main content';
    document.body.insertBefore(skipLink, document.body.firstChild);
}

// Initialize additional features
function initializeAdvancedFeatures() {
    initializeArchitectureDiagram();
    setupPerformanceMonitoring();
    setupAccessibility();

    // Add loading states
    document.querySelectorAll('.btn').forEach(button => {
        button.addEventListener('click', function() {
            if (!this.classList.contains('loading')) {
                this.classList.add('loading');
                setTimeout(() => {
                    this.classList.remove('loading');
                }, 1000);
            }
        });
    });
}

// Initialize everything when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    initializeWiki();
    initializeAdvancedFeatures();
});

// Export functions for global use
window.showQuickStart = showQuickStart;
window.scrollToFeatures = scrollToFeatures;
window.loadPage = loadPage;
window.showUseCase = window.showUseCase || function() {};

// Error handling
window.addEventListener('error', (e) => {
    console.error('Wiki JavaScript error:', e.error);
});

// Service Worker for offline functionality (future enhancement)
// Disabled for now to prevent 404 errors on GitHub Pages
// if ('serviceWorker' in navigator) {
//     window.addEventListener('load', () => {
//         navigator.serviceWorker.register('/ai-doc-framework/sw.js')
//             .then(registration => {
//                 console.log('Service Worker registered:', registration);
//             })
//             .catch(error => {
//                 console.log('Service Worker registration failed:', error);
//             });
//     });
// }

// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
    const searchInput = document.getElementById('searchInput');

    // Ctrl/Cmd + K for search focus
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        if (searchInput) {
            searchInput.focus();
        }
    }

    // Escape to clear search
    if (e.key === 'Escape') {
        if (searchInput) {
            searchInput.value = '';
            clearSearchHighlights();
        }
    }
});

// Theme toggle (future enhancement)
function setupThemeToggle() {
    const themeToggle = document.createElement('button');
    themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
    themeToggle.className = 'theme-toggle';
    themeToggle.title = 'Toggle dark mode';

    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        const isDark = document.body.classList.contains('dark-mode');
        localStorage.setItem('wiki-theme', isDark ? 'dark' : 'light');
        themeToggle.innerHTML = isDark ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
    });

    // Load saved theme
    const savedTheme = localStorage.getItem('wiki-theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
    }

    document.querySelector('.nav-container').appendChild(themeToggle);
}

// Initialize theme toggle
document.addEventListener('DOMContentLoaded', setupThemeToggle);
