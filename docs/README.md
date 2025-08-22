# 📖 AI Documentation Framework - Website Documentation

## 🌐 Website Structure

This directory contains the complete website for the AI Documentation Framework, built with modern HTML, CSS, and JavaScript.

## 📁 Directory Structure

```
docs/
├── 📄 README.md              # This file
├── 📄 index.html             # Homepage
├── 📁 pages/                 # Individual pages
│   ├── 📄 architecture.html  # 🏗️ ARCHITECTURE GUIDE
│   ├── 📄 getting-started.html
│   ├── 📄 documentation.html
│   └── 📄 examples.html
├── 📁 assets/                # Static assets
│   ├── 📁 css/
│   │   └── 📄 style.css      # Main stylesheet
│   ├── 📁 js/                # JavaScript files
│   └── 📁 images/           # Images and icons
└── 📁 [other assets]
```

## 🎯 Key Pages

### 🏗️ Architecture Guide (`pages/architecture.html`)
**📍 URL**: `/ai-doc-framework/docs/pages/architecture.html`

The most important page for understanding the framework:

- **📍 Critical File Placement**: Where `ai-doc-config.json` must be placed
- **🎯 Deep Configuration**: Complete guide to configuration options
- **🔄 System Flow**: How the framework processes tasks
- **📊 File Relationships**: Dependencies and interactions
- **🔧 Troubleshooting**: Solutions to common issues
- **📈 Scaling**: Multi-application support

### 🚀 Getting Started (`pages/getting-started.html`)
Quick setup guide with step-by-step installation instructions.

### 📚 Documentation (`pages/documentation.html`)
Complete documentation and usage examples.

### 💡 Examples (`pages/examples.html`)
Practical examples and use cases.

## 🖥️ Running the Website

### Local Development
```bash
# Navigate to docs directory
cd ai-doc-framework/docs

# Start a local server (Python 3)
python -m http.server 8000

# Or using Node.js
npx serve .

# Access the website at:
# http://localhost:8000
```

### GitHub Pages
The website is automatically deployed to GitHub Pages when pushed to the main branch.

**📍 Live URL**: `https://zsarir.github.io/ai-doc-framework/`

## 🎨 Design Features

- **📱 Responsive Design**: Works on all devices
- **🎯 Modern UI**: Clean, professional interface
- **⚡ Fast Loading**: Optimized for performance
- **♿ Accessible**: WCAG compliant
- **🌙 Dark Mode Ready**: CSS variables for theming

## 🔧 Development

### Adding New Pages
1. Create new HTML file in `pages/` directory
2. Follow the template structure from existing pages
3. Add navigation link in `index.html`
4. Update footer links if needed

### Styling Guidelines
- Use CSS custom properties (variables)
- Follow BEM methodology for class names
- Maintain consistent spacing and typography
- Test responsiveness on multiple devices

### JavaScript Features
- **Code Copy**: Copy code blocks to clipboard
- **Smooth Scrolling**: Anchor link navigation
- **Mobile Menu**: Responsive navigation toggle
- **Interactive Elements**: Hover and focus states

## 📊 SEO Optimization

- **Meta Tags**: Complete meta information
- **Structured Data**: JSON-LD schema markup
- **Performance**: Optimized images and assets
- **Accessibility**: ARIA labels and semantic HTML

## 🔗 Important Links

- **🏗️ Architecture Guide**: [`pages/architecture.html`](pages/architecture.html)
- **🚀 Getting Started**: [`pages/getting-started.html`](pages/getting-started.html)
- **📚 Documentation**: [`pages/documentation.html`](pages/documentation.html)
- **💡 Examples**: [`pages/examples.html`](pages/examples.html)
- **🏠 Homepage**: [`index.html`](index.html)

## 📞 Support

For issues with the website:
- **GitHub Issues**: [Report Website Issues](https://github.com/zsarir/ai-doc-framework/issues)
- **Architecture Questions**: Check [`pages/architecture.html`](pages/architecture.html)
- **Setup Help**: Check [`pages/getting-started.html`](pages/getting-started.html)

---

**🎯 The Architecture Guide is the most critical page for understanding the framework's file placement and system design.**