---
layout: default
title: "Configuration Guide - AI Documentation Framework"
description: "Complete configuration instructions for setting up the AI Documentation Framework"
---

# Configuration Guide

## Configuration Types

Choose the configuration type that best fits your project structure and requirements.

### Single Application

Perfect for standalone applications with comprehensive documentation needs and focused development.

**Features:**
- Streamlined documentation structure
- Focused error management
- Single application optimization
- Simplified navigation
- Fast setup and configuration

### Multi-Application

Ideal for microservices, full-stack applications, or complex systems with multiple interconnected services.

**Features:**
- Shared and individual documentation
- Cross-application dependencies
- Coordinated error management
- Service discovery and communication
- Scalable architecture support

### Custom Configuration

Tailored for specific frameworks, languages, or architectures with custom requirements.

**Features:**
- Framework-specific templates
- Custom rule definitions
- Flexible documentation structure
- Plugin architecture support
- Advanced customization options

## Configuration Files

### ai-doc-config.json

Main configuration file containing project settings, application definitions, and framework preferences.

```json
{
  "project": {
    "name": "My Awesome Project",
    "type": "multi",
    "root_path": "/path/to/project",
    "description": "Full-stack web application",
    "version": "1.0.0"
  },
  "applications": [
    {
      "name": "frontend",
      "type": "spa",
      "framework": "react",
      "description": "React frontend application",
      "port": 3000,
      "dependencies": ["backend", "api"]
    },
    {
      "name": "backend",
      "type": "api",
      "framework": "fastapi",
      "description": "FastAPI backend service",
      "port": 8000,
      "database": "postgresql"
    },
    {
      "name": "api",
      "type": "microservice",
      "framework": "nodejs",
      "description": "Node.js microservice",
      "port": 4000
    }
  ],
  "settings": {
    "auto_update": true,
    "error_tracking": true,
    "backup_enabled": true,
    "notification_email": "admin@example.com"
  }
}
```

### AI_RULES.md

Application-specific rules and constraints that guide AI behavior and development practices.

```markdown
# AI RULES - Frontend Application
## DEVELOPMENT GUIDELINES

### Code Style
- Use functional components with React hooks
- Follow Airbnb JavaScript style guide
- Implement TypeScript for type safety
- Use ESLint and Prettier for code formatting

### Architecture
- Implement atomic design principles
- Use custom hooks for business logic
- Follow container/presentational pattern
- Implement proper error boundaries

### Security
- Validate all user inputs
- Use HTTPS for all API calls
- Implement proper authentication checks
- Sanitize data before rendering

### Performance
- Implement code splitting
- Use lazy loading for components
- Optimize bundle size
- Implement proper caching strategies
```

## Configuration Commands

### Setup Commands

```bash
# Interactive setup wizard
python tools/setup-wizard.py

# Generate single application structure
python tools/app-generator.py --type single --name myapp

# Generate multi-application structure
python tools/app-generator.py --type multi --apps web,api,admin

# Generate custom structure
python tools/app-generator.py --type custom --config config.json
```

### Validation Commands

```bash
# Check system integrity
python tools/validator.py --check-system

# Validate configuration
python tools/validator.py --check-config

# Test template generation
python tools/validator.py --test-templates

# Validate documentation structure
python tools/validator.py --validate-docs
```

### Management Commands

```bash
# Run weekly maintenance
python tools/maintenance.py --weekly

# Update documentation
python tools/update-docs.py

# Create backup
python tools/backup.py --create

# Health check
python tools/monitor.py --health-check
```

## Environment Variables

### Core Framework Settings

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `AI_DOC_FRAMEWORK_ROOT` | Root path of the project | Current directory | Optional |
| `AI_DOC_FRAMEWORK_TYPE` | Project type (single/multi/custom) | auto-detect | Optional |
| `AI_DOC_FRAMEWORK_APPS` | Comma-separated list of applications | auto-detect | Optional |
| `AI_DOC_FRAMEWORK_DEBUG` | Enable debug mode | false | Optional |

### Documentation Settings

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `AI_DOC_THEME` | Documentation theme | default | Optional |
| `AI_DOC_LANGUAGE` | Documentation language | en | Optional |
| `AI_DOC_AUTO_UPDATE` | Enable automatic documentation updates | true | Optional |

### Error Management

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `AI_ERROR_AUTO_LOG` | Automatically log errors | true | Optional |
| `AI_ERROR_CATEGORIES` | Comma-separated error categories | backend,frontend,security | Optional |

## Framework-Specific Configurations

### React Configuration

Optimized for React applications with TypeScript, Next.js, and modern tooling.

**Components:**
- Component-based architecture
- Hooks and context patterns
- TypeScript integration
- Testing with Jest and React Testing Library
- Build optimization with Webpack

**Configuration:**
```json
{
  "framework": "react",
  "features": ["typescript", "nextjs", "testing", "optimization"],
  "tools": ["eslint", "prettier", "webpack"]
}
```

### Vue.js Configuration

Tailored for Vue 3 applications with Composition API and modern development practices.

**Components:**
- Composition API patterns
- Vue Router integration
- Pinia for state management
- Component testing with Vue Test Utils
- Vite build tooling

**Configuration:**
```json
{
  "framework": "vue",
  "version": "3.x",
  "features": ["composition-api", "router", "pinia", "testing"],
  "tools": ["vite", "vue-test-utils"]
}
```

### Angular Configuration

Structured for Angular applications with standalone components and modern architecture.

**Components:**
- Standalone components
- Angular Material integration
- RxJS patterns
- Unit testing with Jasmine
- Angular CLI optimization

**Configuration:**
```json
{
  "framework": "angular",
  "features": ["standalone-components", "material", "rxjs", "testing"],
  "tools": ["angular-cli", "jasmine", "karma"]
}
```

### Django Configuration

Backend configuration for Django applications with REST framework and modern practices.

**Components:**
- Django REST framework
- PostgreSQL/MongoDB integration
- Authentication and permissions
- Testing with pytest
- Docker containerization

**Configuration:**
```json
{
  "framework": "django",
  "features": ["rest-framework", "authentication", "testing", "docker"],
  "database": "postgresql",
  "tools": ["pytest", "docker", "nginx"]
}
```

### FastAPI Configuration

Modern Python API configuration with async support and automatic documentation.

**Components:**
- Async/await patterns
- Automatic OpenAPI docs
- Pydantic validation
- WebSocket support
- Background tasks

**Configuration:**
```json
{
  "framework": "fastapi",
  "features": ["async", "openapi", "validation", "websockets"],
  "tools": ["uvicorn", "pytest", "pydantic"]
}
```

### Flask Configuration

Lightweight configuration for Flask applications with extensions and best practices.

**Components:**
- Flask-SQLAlchemy integration
- JWT authentication
- Flask-RESTful API patterns
- Testing with pytest
- Gunicorn deployment

**Configuration:**
```json
{
  "framework": "flask",
  "features": ["sqlalchemy", "jwt", "restful", "testing"],
  "tools": ["pytest", "gunicorn", "nginx"]
}
```

## Advanced Configuration

### Custom Templates

Create custom documentation templates for specific requirements:

```bash
# Generate custom template
python tools/app-generator.py --template custom --name my-template

# List available templates
python tools/app-generator.py --list-templates

# Apply custom template
python tools/app-generator.py --apply-template my-template
```

### Plugin Configuration

Extend framework functionality with custom plugins:

```json
{
  "plugins": [
    {
      "name": "custom-linter",
      "type": "code-quality",
      "enabled": true,
      "config": {
        "rules": "strict",
        "auto_fix": true
      }
    },
    {
      "name": "security-scanner",
      "type": "security",
      "enabled": true,
      "config": {
        "scan_frequency": "daily",
        "report_format": "json"
      }
    }
  ]
}
```

### Integration Configuration

Configure integrations with external tools and services:

```json
{
  "integrations": {
    "github": {
      "enabled": true,
      "token": "your-github-token",
      "repository": "username/repo",
      "auto_sync": true
    },
    "slack": {
      "enabled": true,
      "webhook": "https://hooks.slack.com/...",
      "channels": ["#devops", "#alerts"],
      "notifications": ["errors", "updates"]
    },
    "datadog": {
      "enabled": false,
      "api_key": "your-api-key",
      "metrics": ["performance", "errors", "usage"]
    }
  }
}
```

## Validation & Testing

### System Validation

Comprehensive validation of framework installation and configuration:

```bash
# Full system validation
python tools/validator.py --full-check

# Quick health check
python tools/monitor.py --health-check

# Performance validation
python tools/validator.py --performance-test
```

### Configuration Testing

Test configuration changes before applying them:

```bash
# Test configuration file
python tools/validator.py --test-config config.json

# Validate framework settings
python tools/validator.py --validate-settings

# Dry run configuration
python tools/app-generator.py --dry-run --config config.json
```

### Documentation Validation

Ensure documentation structure and content are correct:

```bash
# Validate all documentation
python tools/validator.py --validate-docs

# Check documentation links
python tools/validator.py --check-links

# Generate documentation report
python tools/reports.py --docs-report
```

This comprehensive configuration guide should help you set up and customize the AI Documentation Framework for your specific needs. Remember to validate your configuration after making changes and test thoroughly before deploying to production.
