---
layout: default
title: "Search - AI Documentation Framework"
description: "Search through the comprehensive AI Documentation Framework documentation"
---

# Search Documentation

<div class="search-container">
  <div class="search-box">
    <input type="text" id="searchInput" placeholder="Search documentation..." />
    <button class="search-btn">
      <i class="fas fa-search"></i>
    </button>
  </div>

  <div class="search-filters">
    <select id="categoryFilter">
      <option value="all">All Categories</option>
      <option value="installation">Installation</option>
      <option value="usage">Usage</option>
      <option value="configuration">Configuration</option>
      <option value="architecture">Architecture</option>
      <option value="features">Features</option>
      <option value="examples">Examples</option>
      <option value="troubleshooting">Troubleshooting</option>
    </select>

    <select id="typeFilter">
      <option value="all">All Types</option>
      <option value="guide">Guide</option>
      <option value="tutorial">Tutorial</option>
      <option value="reference">Reference</option>
      <option value="example">Example</option>
    </select>
  </div>

  <div id="searchResults" class="search-results">
    <!-- Search results will appear here -->
  </div>
</div>

<script>
// Simple client-side search functionality
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('searchInput');
  const searchResults = document.getElementById('searchResults');

  // Search data (in a real implementation, this would come from a search index)
  const searchData = [
    {
      title: "Installation Guide",
      description: "Complete installation instructions for setting up the AI Documentation Framework",
      url: "/guides/installation/",
      category: "installation",
      type: "guide"
    },
    {
      title: "Usage Guide",
      description: "Learn how to effectively use the framework with AI assistants",
      url: "/guides/usage/",
      category: "usage",
      type: "guide"
    },
    {
      title: "Configuration Guide",
      description: "Complete configuration instructions and options",
      url: "/guides/configuration/",
      category: "configuration",
      type: "guide"
    },
    {
      title: "Architecture Overview",
      description: "Deep dive into the framework architecture and design principles",
      url: "/core/architecture/",
      category: "architecture",
      type: "reference"
    },
    {
      title: "Core Features",
      description: "Explore the comprehensive features and capabilities",
      url: "/core/features/",
      category: "features",
      type: "reference"
    },
    {
      title: "Single Application Example",
      description: "Example implementation for single React applications",
      url: "/examples/single-app/",
      category: "examples",
      type: "example"
    }
  ];

  function performSearch(query) {
    if (!query.trim()) {
      searchResults.innerHTML = '<p class="no-results">Enter a search term to find documentation</p>';
      return;
    }

    const results = searchData.filter(item => {
      const searchText = `${item.title} ${item.description}`.toLowerCase();
      return searchText.includes(query.toLowerCase());
    });

    displayResults(results, query);
  }

  function displayResults(results, query) {
    if (results.length === 0) {
      searchResults.innerHTML = `<p class="no-results">No results found for "${query}"</p>`;
      return;
    }

    const resultsHtml = results.map(result => `
      <div class="search-result-item">
        <h3><a href="${result.url}">${result.title}</a></h3>
        <p class="result-description">${result.description}</p>
        <div class="result-meta">
          <span class="category-tag">${result.category}</span>
          <span class="type-tag">${result.type}</span>
        </div>
      </div>
    `).join('');

    searchResults.innerHTML = resultsHtml;
  }

  // Debounced search
  let searchTimeout;
  searchInput.addEventListener('input', function() {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(() => {
      performSearch(this.value);
    }, 300);
  });

  // Initial search
  performSearch('');
});
</script>

<style>
.search-container {
  max-width: 800px;
  margin: 2rem auto;
}

.search-box {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
}

.search-box input {
  flex: 1;
  padding: 1rem;
  border: 2px solid var(--border-color);
  border-radius: var(--border-radius);
  font-size: 1rem;
  transition: var(--transition);
}

.search-box input:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

.search-btn {
  padding: 1rem 1.5rem;
  background: var(--primary-color);
  color: white;
  border: none;
  border-radius: var(--border-radius);
  cursor: pointer;
  transition: var(--transition);
}

.search-btn:hover {
  background: var(--primary-dark);
}

.search-filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
}

.search-filters select {
  padding: 0.5rem 1rem;
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius);
  background: var(--bg-primary);
  font-size: 0.9rem;
}

.search-results {
  min-height: 200px;
}

.search-result-item {
  padding: 1.5rem;
  border: 1px solid var(--border-color);
  border-radius: var(--border-radius);
  margin-bottom: 1rem;
  background: var(--bg-primary);
  transition: var(--transition);
}

.search-result-item:hover {
  border-color: var(--primary-color);
  box-shadow: var(--shadow);
}

.search-result-item h3 {
  margin-bottom: 0.5rem;
}

.search-result-item h3 a {
  color: var(--text-primary);
  text-decoration: none;
  font-size: 1.2rem;
}

.search-result-item h3 a:hover {
  color: var(--primary-color);
}

.result-description {
  color: var(--text-secondary);
  margin-bottom: 1rem;
  line-height: 1.5;
}

.result-meta {
  display: flex;
  gap: 0.5rem;
}

.category-tag, .type-tag {
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.8rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.category-tag {
  background: var(--primary-light);
  color: var(--primary-dark);
}

.type-tag {
  background: var(--secondary-color);
  color: white;
}

.no-results {
  text-align: center;
  color: var(--text-muted);
  font-style: italic;
  padding: 2rem;
}

@media (max-width: 768px) {
  .search-box {
    flex-direction: column;
  }

  .search-filters {
    flex-direction: column;
  }

  .search-container {
    padding: 0 1rem;
  }
}
</style>
