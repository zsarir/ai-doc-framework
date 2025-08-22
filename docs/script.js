/**
 * AI Documentation Framework - Interactive JavaScript
 * Modern, responsive, and feature-rich website functionality
 */

// DOM Content Loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all features
    initializeAnimations();
    initializeScrollEffects();
    initializeMobileMenu();
    initializeInteractiveElements();
    initializeFormHandling();
    initializeCodeHighlighting();
});

// Animation on Scroll
function initializeAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                if (entry.target.classList.contains('slide-up')) {
                    entry.target.classList.add('slide-up');
                }
            }
        });
    }, observerOptions);

    // Observe all sections and cards
    document.querySelectorAll('section, .problem-card, .solution-card, .benefit-category, .step, .arch-component').forEach(el => {
        observer.observe(el);
    });
}

// Scroll Effects
function initializeScrollEffects() {
    let lastScrollTop = 0;
    const navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', function() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        // Navbar background change on scroll
        if (scrollTop > 100) {
            navbar.style.background = 'rgba(255, 255, 255, 0.98)';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.boxShadow = 'none';
        }

        // Hide/show navbar on scroll
        if (scrollTop > lastScrollTop && scrollTop > 200) {
            navbar.style.transform = 'translateY(-100%)';
        } else {
            navbar.style.transform = 'translateY(0)';
        }

        lastScrollTop = scrollTop;

        // Update progress bar
        updateScrollProgress();
    });
}

// Scroll Progress Indicator
function updateScrollProgress() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = (scrollTop / scrollHeight) * 100;

    let progressBar = document.querySelector('.scroll-progress');
    if (!progressBar) {
        progressBar = document.createElement('div');
        progressBar.className = 'scroll-progress';
        progressBar.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 0%;
            height: 3px;
            background: linear-gradient(90deg, #2563eb, #3b82f6);
            z-index: 9999;
            transition: width 0.3s ease;
        `;
        document.body.appendChild(progressBar);
    }
    progressBar.style.width = progress + '%';
}

// Mobile Menu
function initializeMobileMenu() {
    const mobileToggle = document.querySelector('.mobile-menu-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (mobileToggle && navMenu) {
        mobileToggle.addEventListener('click', function() {
            navMenu.classList.toggle('mobile-active');
            mobileToggle.classList.toggle('active');

            // Animate hamburger icon
            const icon = mobileToggle.querySelector('i');
            if (navMenu.classList.contains('mobile-active')) {
                icon.className = 'fas fa-times';
            } else {
                icon.className = 'fas fa-bars';
            }
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!mobileToggle.contains(e.target) && !navMenu.contains(e.target)) {
                navMenu.classList.remove('mobile-active');
                mobileToggle.classList.remove('active');
                mobileToggle.querySelector('i').className = 'fas fa-bars';
            }
        });
    }
}

// Mobile Menu Styles (injected dynamically)
const mobileMenuStyles = `
.nav-menu.mobile-active {
    display: flex !important;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: white;
    flex-direction: column;
    padding: 1rem;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
    border-radius: 0 0 1rem 1rem;
}

.nav-menu.mobile-active .nav-link {
    padding: 0.75rem 1rem;
    width: 100%;
    text-align: center;
    margin-bottom: 0.5rem;
}

@media (min-width: 769px) {
    .nav-menu.mobile-active {
        display: flex !important;
        position: static;
        flex-direction: row;
        padding: 0;
        box-shadow: none;
        border-radius: 0;
    }

    .nav-menu.mobile-active .nav-link {
        width: auto;
        text-align: left;
        margin-bottom: 0;
    }
}
`;

const styleSheet = document.createElement('style');
styleSheet.textContent = mobileMenuStyles;
document.head.appendChild(styleSheet);

// Interactive Elements
function initializeInteractiveElements() {
    // Card hover effects
    document.querySelectorAll('.problem-card, .solution-card, .benefit-category, .step').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    // Button ripple effect
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;

            ripple.style.cssText = `
                position: absolute;
                width: ${size}px;
                height: ${size}px;
                left: ${x}px;
                top: ${y}px;
                background: rgba(255, 255, 255, 0.3);
                border-radius: 50%;
                transform: scale(0);
                animation: ripple 0.6s linear;
                pointer-events: none;
            `;

            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(ripple);

            setTimeout(() => ripple.remove(), 600);
        });
    });

    // Floating cards animation
    animateFloatingCards();

    // Interactive statistics
    initializeStatisticsCounter();
}

// Floating Cards Animation
function animateFloatingCards() {
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.5}s`;
        card.addEventListener('mouseenter', function() {
            this.style.animationPlayState = 'paused';
        });
        card.addEventListener('mouseleave', function() {
            this.style.animationPlayState = 'running';
        });
    });
}

// Statistics Counter Animation
function initializeStatisticsCounter() {
    const stats = document.querySelectorAll('.stat-number');
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
            }
        });
    }, { threshold: 0.5 });

    stats.forEach(stat => observer.observe(stat));
}

function animateCounter(element) {
    const target = parseInt(element.textContent.replace(/[^\d]/g, ''));
    const duration = 2000;
    const step = target / (duration / 16);
    let current = 0;

    const timer = setInterval(() => {
        current += step;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        element.textContent = Math.floor(current) + (element.textContent.includes('%') ? '%' : '');
    }, 16);
}

// Code Highlighting and Copy Functionality
function initializeCodeHighlighting() {
    document.querySelectorAll('code').forEach(block => {
        if (!block.classList.contains('no-copy')) {
            const copyBtn = document.createElement('button');
            copyBtn.className = 'copy-btn';
            copyBtn.innerHTML = '<i class="fas fa-copy"></i>';
            copyBtn.title = 'Copy to clipboard';

            copyBtn.addEventListener('click', function() {
                navigator.clipboard.writeText(block.textContent).then(() => {
                    const icon = this.querySelector('i');
                    icon.className = 'fas fa-check';
                    setTimeout(() => {
                        icon.className = 'fas fa-copy';
                    }, 2000);
                });
            });

            const wrapper = document.createElement('div');
            wrapper.className = 'code-wrapper';
            wrapper.style.position = 'relative';
            block.parentNode.insertBefore(wrapper, block);
            wrapper.appendChild(block);
            wrapper.appendChild(copyBtn);
        }
    });
}

// Form Handling (for future forms)
function initializeFormHandling() {
    // Contact form handling
    const contactForm = document.querySelector('#contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            // Handle form submission
            showNotification('Thank you for your message! We\'ll get back to you soon.', 'success');
            this.reset();
        });
    }
}

// Notification System
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.innerHTML = `
        <div class="notification-content">
            <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : 'info-circle'}"></i>
            <span>${message}</span>
        </div>
        <button class="notification-close">
            <i class="fas fa-times"></i>
        </button>
    `;

    document.body.appendChild(notification);

    // Animate in
    setTimeout(() => notification.classList.add('show'), 10);

    // Auto remove after 5 seconds
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => notification.remove(), 300);
    }, 5000);

    // Manual close
    notification.querySelector('.notification-close').addEventListener('click', function() {
        notification.classList.remove('show');
        setTimeout(() => notification.remove(), 300);
    });
}

// Add notification styles
const notificationStyles = `
.notification {
    position: fixed;
    top: 20px;
    right: -400px;
    min-width: 350px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    z-index: 10000;
    transition: all 0.3s ease;
    border-left: 4px solid #2563eb;
}

.notification.show {
    right: 20px;
}

.notification-success { border-left-color: #10b981; }
.notification-error { border-left-color: #ef4444; }
.notification-warning { border-left-color: #f59e0b; }

.notification-content {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 16px 20px;
}

.notification-content i {
    font-size: 20px;
    color: #2563eb;
}

.notification-success .notification-content i { color: #10b981; }
.notification-error .notification-content i { color: #ef4444; }
.notification-warning .notification-content i { color: #f59e0b; }

.notification-close {
    background: none;
    border: none;
    padding: 16px;
    cursor: pointer;
    color: #64748b;
    transition: color 0.2s ease;
}

.notification-close:hover {
    color: #1e293b;
}

@media (max-width: 480px) {
    .notification {
        left: 10px;
        right: 10px;
        min-width: auto;
    }

    .notification.show {
        right: 10px;
        left: 10px;
    }
}
`;

const notificationStyleSheet = document.createElement('style');
notificationStyleSheet.textContent = notificationStyles;
document.head.appendChild(notificationStyleSheet);

// Smooth Scrolling for Anchor Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const headerOffset = 80;
            const elementPosition = target.offsetTop;
            const offsetPosition = elementPosition - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// Performance Optimization
function optimizePerformance() {
    // Lazy load images if any
    const images = document.querySelectorAll('img[data-src]');
    if (images.length > 0) {
        const imageObserver = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });

        images.forEach(img => imageObserver.observe(img));
    }
}

// Keyboard Navigation
document.addEventListener('keydown', function(e) {
    // Escape key to close mobile menu
    if (e.key === 'Escape') {
        const navMenu = document.querySelector('.nav-menu');
        const mobileToggle = document.querySelector('.mobile-menu-toggle');

        if (navMenu && navMenu.classList.contains('mobile-active')) {
            navMenu.classList.remove('mobile-active');
            mobileToggle.classList.remove('active');
            mobileToggle.querySelector('i').className = 'fas fa-bars';
        }
    }
});

// Accessibility Improvements
function initializeAccessibility() {
    // Add ARIA labels and roles
    document.querySelectorAll('.btn').forEach(btn => {
        if (!btn.getAttribute('aria-label')) {
            btn.setAttribute('aria-label', btn.textContent.trim());
        }
    });

    // Add skip link
    const skipLink = document.createElement('a');
    skipLink.href = '#main-content';
    skipLink.className = 'skip-link';
    skipLink.textContent = 'Skip to main content';
    document.body.insertBefore(skipLink, document.body.firstChild);

    // Focus management
    document.querySelectorAll('a, button, input, textarea, select').forEach(el => {
        el.addEventListener('focus', function() {
            this.style.outline = '2px solid #2563eb';
            this.style.outlineOffset = '2px';
        });

        el.addEventListener('blur', function() {
            this.style.outline = '';
            this.style.outlineOffset = '';
        });
    });
}

// Initialize accessibility
initializeAccessibility();

// Performance optimization
optimizePerformance();

// Add copy button styles
const copyButtonStyles = `
.code-wrapper {
    position: relative;
    margin: 1rem 0;
}

.copy-btn {
    position: absolute;
    top: 8px;
    right: 8px;
    background: rgba(0, 0, 0, 0.7);
    color: white;
    border: none;
    border-radius: 4px;
    padding: 4px 8px;
    cursor: pointer;
    font-size: 12px;
    opacity: 0;
    transition: all 0.3s ease;
}

.code-wrapper:hover .copy-btn {
    opacity: 1;
}

.copy-btn:hover {
    background: rgba(0, 0, 0, 0.9);
    transform: scale(1.1);
}

.skip-link {
    position: absolute;
    top: -40px;
    left: 6px;
    background: #2563eb;
    color: white;
    padding: 8px 16px;
    text-decoration: none;
    border-radius: 4px;
    z-index: 1000;
    transition: top 0.3s ease;
}

.skip-link:focus {
    top: 6px;
}
`;

const copyButtonStyleSheet = document.createElement('style');
copyButtonStyleSheet.textContent = copyButtonStyles;
document.head.appendChild(copyButtonStyleSheet);

// Page Load Performance
window.addEventListener('load', function() {
    // Remove loading class from body if it exists
    document.body.classList.remove('loading');

    // Add loaded class for animations
    document.body.classList.add('loaded');

    // Show notification after page loads (optional)
    setTimeout(() => {
        showNotification('Welcome to AI Documentation Framework! Explore the revolutionary features below.', 'info');
    }, 1000);
});

// Error Handling
window.addEventListener('error', function(e) {
    console.error('JavaScript error:', e.error);
    // Could send error to monitoring service
});

window.addEventListener('unhandledrejection', function(e) {
    console.error('Unhandled promise rejection:', e.reason);
    // Could send error to monitoring service
});

// Export functions for potential use in other scripts
window.AIDocFramework = {
    showNotification,
    animateCounter,
    initializeAnimations
};
