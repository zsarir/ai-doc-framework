# 📚 Multi-Application Project Example

This example shows how to set up the AI Documentation Framework for a **multi-application project** with multiple services and applications.

## 🏗️ Project Structure

```
multi-app-example/
├── 🎯 ai-doc-config.json         # ✅ CENTRAL CONFIGURATION FILE
├── 📄 AI_RULES.md               # AI behavior rules for entire project
├── 📄 START_TASK.md             # Project-level task initialization
├── 📄 COMPLETE_TASK.md          # Project-level task completion
├── 📁 docs/                     # Shared project documentation
├── 📁 error-management/         # Shared error management system
├── 📁 issues/                   # Shared issue tracking system
└── 📁 applications/             # Individual applications
    ├── frontend/                # React frontend application
    │   ├── 📄 AI_RULES.md       # Frontend-specific rules
    │   ├── 📄 START_TASK.md     # Frontend task initialization
    │   ├── 📄 COMPLETE_TASK.md  # Frontend task completion
    │   └── 📁 docs/             # Frontend documentation
    ├── backend-api/             # FastAPI backend service
    │   ├── 📄 AI_RULES.md       # API-specific rules
    │   ├── 📄 START_TASK.md     # API task initialization
    │   ├── 📄 COMPLETE_TASK.md  # API task completion
    │   └── 📁 docs/             # API documentation
    ├── database/                # Database service
    │   ├── 📄 AI_RULES.md       # Database-specific rules
    │   ├── 📄 START_TASK.md     # Database task initialization
    │   ├── 📄 COMPLETE_TASK.md  # Database task completion
    │   └── 📁 docs/             # Database documentation
    └── monitoring/              # Monitoring service
        ├── 📄 AI_RULES.md       # Monitoring-specific rules
        ├── 📄 START_TASK.md     # Monitoring task initialization
        ├── 📄 COMPLETE_TASK.md  # Monitoring task completion
        └── 📁 docs/             # Monitoring documentation
```

## 🎯 ai-doc-config.json Configuration

The `ai-doc-config.json` file is the **heart** of the multi-application setup:

```json
{
  "project": {
    "name": "Multi-Service E-commerce Platform",
    "type": "multi",
    "root_path": "/path/to/multi-app-example",
    "description": "A complete e-commerce platform with multiple services"
  },
  "applications": [
    {
      "name": "frontend",
      "type": "frontend",
      "framework": "react",
      "description": "Customer-facing React application"
    },
    {
      "name": "backend-api",
      "type": "backend",
      "framework": "fastapi",
      "description": "REST API for business logic"
    },
    {
      "name": "database",
      "type": "backend",
      "framework": "postgresql",
      "description": "Primary database service"
    },
    {
      "name": "monitoring",
      "type": "backend",
      "framework": "prometheus-grafana",
      "description": "Monitoring and alerting system"
    }
  ],
  "error_categories": [
    "frontend",
    "backend",
    "database",
    "infrastructure",
    "security",
    "performance",
    "integration",
    "testing"
  ],
  "issue_categories": [
    "incomplete-tasks",
    "unresolved-errors",
    "system-issues",
    "feature-requests",
    "infrastructure-issues"
  ],
  "advanced_options": {
    "ai_model_preferences": ["gpt-4", "claude-3"],
    "documentation_language": "en",
    "auto_backup": true,
    "debug_mode": false,
    "custom_templates": false
  }
}
```

## 🚀 Quick Setup

### 1. Create Project Structure

```bash
# Create the main project directory
mkdir multi-app-example
cd multi-app-example

# Copy the configuration file
cp ../ai-doc-framework/examples/sample-ai-doc-config.json ./ai-doc-config.json

# Edit the configuration for your project
nano ai-doc-config.json  # Update paths and application details
```

### 2. Run Setup Wizard

```bash
# Navigate to framework directory
cd ../ai-doc-framework

# Run setup wizard (it will detect your project)
python tools/setup-wizard.py

# Follow the interactive prompts:
# 1. Project type: multi
# 2. Confirm applications from config
# 3. Choose error categories
# 4. Select issue categories
```

### 3. Verify Setup

```bash
# Return to your project
cd ../multi-app-example

# Verify ai-doc-config.json is in correct location
ls -la ai-doc-config.json

# Check generated structure
tree -I '__pycache__' -I '*.pyc'
```

## 🎨 Key Features Demonstrated

### 1. **Central Configuration**
- Single `ai-doc-config.json` file controls everything
- All applications defined in one place
- Consistent error and issue categories across services

### 2. **Application Isolation**
- Each application has its own documentation
- Application-specific AI rules
- Independent task management per service

### 3. **Shared Resources**
- Common error management system
- Shared issue tracking
- Project-wide documentation

### 4. **Scalable Structure**
- Easy to add new applications
- Consistent structure across all services
- Maintainable at scale

## 📋 Generated File Structure

After running the setup wizard, you'll get:

### Root Level Files
- `ai-doc-config.json` - Central configuration ✅
- `AI_RULES.md` - Project-wide AI behavior rules
- `START_TASK.md` - Multi-application task initialization
- `COMPLETE_TASK.md` - Multi-application task completion

### Shared Systems
- `docs/` - Project documentation and guides
- `error-management/` - Shared error tracking system
- `issues/` - Shared issue management system

### Application-Specific Structure
Each application gets:
```
applications/[app-name]/
├── AI_RULES.md           # App-specific AI rules
├── START_TASK.md         # App-specific task initialization
├── COMPLETE_TASK.md      # App-specific task completion
├── docs/                 # App-specific documentation
│   ├── API_REFERENCE.md
│   ├── TROUBLESHOOTING.md
│   └── DEPLOYMENT.md
├── error-management/     # App-specific error tracking
└── issues/               # App-specific issue tracking
```

## 🔧 Usage Examples

### Starting a Frontend Task

```bash
# For frontend-specific tasks
cd applications/frontend

# AI will read:
# 1. Root ai-doc-config.json (project structure)
# 2. applications/frontend/AI_RULES.md (React-specific rules)
# 3. applications/frontend/START_TASK.md (frontend task protocol)
```

### Starting a Backend API Task

```bash
# For API-specific tasks
cd applications/backend-api

# AI will read:
# 1. Root ai-doc-config.json (project structure)
# 2. applications/backend-api/AI_RULES.md (FastAPI-specific rules)
# 3. applications/backend-api/START_TASK.md (API task protocol)
```

### Starting a Project-Level Task

```bash
# For cross-application tasks
cd ../..  # Back to project root

# AI will read:
# 1. ai-doc-config.json (all applications)
# 2. AI_RULES.md (project-wide rules)
# 3. START_TASK.md (multi-app task protocol)
```

## 🛡️ Best Practices

### 1. **Configuration Management**
- Keep `ai-doc-config.json` in project root
- Use version control for configuration changes
- Validate configuration before major changes

### 2. **Application Organization**
- Group related applications in subdirectories
- Use consistent naming conventions
- Document application dependencies

### 3. **Error Management**
- Use shared error categories for consistency
- Document application-specific errors locally
- Regularly review and update error documentation

### 4. **Issue Tracking**
- Use project-level issues for cross-application problems
- Use application-specific issues for local problems
- Maintain clear issue ownership and responsibility

## 🔄 Maintenance

### Adding New Applications

```bash
# 1. Update ai-doc-config.json
nano ai-doc-config.json  # Add new application

# 2. Run setup wizard to generate new structure
cd ../ai-doc-framework
python tools/setup-wizard.py

# 3. Customize generated files
cd ../multi-app-example
# Edit applications/[new-app]/AI_RULES.md
```

### Updating Configuration

```bash
# 1. Edit configuration
nano ai-doc-config.json

# 2. Validate changes
python ../ai-doc-framework/tools/validator.py --check-config

# 3. Update generated files if needed
python ../ai-doc-framework/tools/setup-wizard.py --update-only
```

## 📊 Monitoring and Health Checks

### System Validation
```bash
# Check overall system health
python ../ai-doc-framework/tools/validator.py --full

# Check specific application
python ../ai-doc-framework/tools/validator.py --app frontend

# Check configuration integrity
python ../ai-doc-framework/tools/validator.py --config
```

### Performance Monitoring
```bash
# Monitor documentation system performance
python ../ai-doc-framework/tools/performance-monitor.py

# Check file sizes and optimization
python ../ai-doc-framework/tools/optimizer.py --analyze
```

## 🚨 Troubleshooting

### Common Issues

#### 1. Configuration Not Found
```bash
# Check if ai-doc-config.json exists in project root
ls -la ai-doc-config.json

# Verify it's not in wrong location
find . -name "ai-doc-config.json" -type f
```

#### 2. Application Structure Missing
```bash
# Regenerate application structure
python ../ai-doc-framework/tools/setup-wizard.py --force

# Or manually recreate
python ../ai-doc-framework/tools/app-generator.py --app frontend
```

#### 3. Permission Issues
```bash
# Fix file permissions
chmod -R 755 .
chmod 644 ai-doc-config.json

# Check ownership
ls -la
```

## 📞 Support

- **Documentation**: [Full Multi-App Guide](../../docs/architecture-guide.md)
- **Examples**: [Other Examples](../)
- **Issues**: [Report Problems](https://github.com/zsarir/ai-doc-framework/issues)

---

**🎯 This example demonstrates the full power of the AI Documentation Framework for complex, multi-application projects.**

**📍 Remember: The `ai-doc-config.json` file is your single source of truth - keep it in your project root!**
