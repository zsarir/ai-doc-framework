# 📦 Installation Guide - AI Documentation Framework

## 🎯 Prerequisites

### System Requirements
- **Python**: 3.8 or higher
- **Git**: For cloning the repository
- **Operating System**: Linux, macOS, or Windows
- **Disk Space**: Minimum 50MB for framework installation

### Python Dependencies
```bash
# Core dependencies
python >= 3.8
pip >= 20.0

# Optional dependencies for advanced features
jinja2 >= 3.0.0
pyyaml >= 6.0
click >= 8.0.0
colorama >= 0.4.4
```

## 🚀 Installation Methods

### Method 1: Git Clone (Recommended)

```bash
# Clone the repository
git clone https://github.com/zsarir/ai-doc-framework.git
cd ai-doc-framework

# Install Python dependencies
pip install -r requirements.txt

# Run the setup wizard
python tools/setup-wizard.py
```

### Method 2: Direct Download

```bash
# Download the latest release
wget https://github.com/zsarir/ai-doc-framework/archive/refs/tags/v1.0.0.zip
unzip v1.0.0.zip
cd ai-doc-framework-1.0.0

# Install dependencies
pip install -r requirements.txt
```

### Method 3: Using pip (Future Release)

```bash
# Install via pip (when available)
pip install ai-doc-framework

# Initialize in your project
ai-doc-framework init
```

## 🔧 Setup Wizard

The setup wizard will guide you through the initial configuration:

```bash
python tools/setup-wizard.py
```

### Setup Options

1. **Project Type Selection**
   - Single Application
   - Multi-Application
   - Custom Configuration

2. **Application Configuration**
   - Application names
   - Framework types
   - Technology stack

3. **Directory Structure**
   - Project root path
   - Documentation location
   - Error management setup

4. **Template Customization**
   - Custom rules
   - Specific requirements
   - Integration preferences

## 📁 Directory Structure Setup

### Automatic Setup
The framework will create the following structure:

```
your-project/
├── 📄 AI_RULES.md                    # Root-level AI rules
├── 📄 START_TASK.md                  # Root task initialization
├── 📄 COMPLETE_TASK.md               # Root task completion
├── 📄 CREATE_ISSUE_DIRECTORIES.md    # Issue management setup
├── 📁 docs/                          # Project documentation
│   ├── 📄 AI_APP_GUIDE.md           # Navigation guide
│   ├── 📄 PROJECT_OVERVIEW.md       # Project overview
│   └── 📄 VERSION.md                # Version control
├── 📁 error-management/              # Error documentation
│   ├── 📄 MASTER_ERROR_INDEX.md     # Central error index
│   └── 📁 [categories]/             # Error categories
├── 📁 issues/                        # Issue tracking
│   ├── 📄 ISSUE_TRACKER.md          # Issue dashboard
│   ├── 📁 open/                     # Active issues
│   └── 📁 closed/                   # Resolved issues
└── 📁 [applications]/               # Individual applications
    ├── 📄 AI_RULES.md               # App-specific rules
    ├── 📄 START_TASK.md             # App task initialization
    ├── 📄 COMPLETE_TASK.md          # App task completion
    └── 📁 [app-specific-structure]  # App documentation
```

### Manual Setup
If you prefer manual setup:

```bash
# Create basic structure
mkdir -p {docs,error-management,issues}

# Copy template files
cp templates/core-files/* .
cp templates/documentation/* docs/
cp templates/error-management/* error-management/
cp templates/issue-management/* issues/
```

## ⚙️ Configuration

### Environment Variables
```bash
# Framework configuration
export AI_DOC_FRAMEWORK_ROOT="/path/to/your/project"
export AI_DOC_FRAMEWORK_TYPE="multi"  # single, multi, custom
export AI_DOC_FRAMEWORK_APPS="web,api,admin"

# Optional settings
export AI_DOC_FRAMEWORK_THEME="default"
export AI_DOC_FRAMEWORK_LANGUAGE="en"
```

### Configuration File
Create `ai-doc-config.json`:

```json
{
  "project": {
    "name": "My Project",
    "type": "multi",
    "root_path": "/path/to/project",
    "description": "Project description"
  },
  "applications": [
    {
      "name": "web",
      "type": "frontend",
      "framework": "react",
      "description": "Frontend application"
    },
    {
      "name": "api",
      "type": "backend",
      "framework": "fastapi",
      "description": "Backend API"
    }
  ],
  "error_categories": [
    "backend",
    "frontend",
    "infrastructure",
    "security",
    "performance"
  ],
  "issue_categories": [
    "incomplete-tasks",
    "unresolved-errors",
    "system-issues"
  ]
}
```

## 🔍 Verification

### System Check
```bash
# Verify installation
python tools/validator.py --check-system

# Validate configuration
python tools/validator.py --check-config

# Test template generation
python tools/validator.py --test-templates
```

### Expected Output
```
✅ System check passed
✅ Configuration valid
✅ Templates generated successfully
✅ Framework ready for use
```

## 🚨 Troubleshooting

### Common Issues

#### Python Version Error
```bash
# Error: Python version too old
# Solution: Upgrade Python
python --version  # Should be 3.8+
```

#### Permission Denied
```bash
# Error: Permission denied when creating directories
# Solution: Check permissions
chmod +x tools/*.py
```

#### Missing Dependencies
```bash
# Error: Module not found
# Solution: Install dependencies
pip install -r requirements.txt
```

#### Template Generation Failed
```bash
# Error: Template generation failed
# Solution: Check configuration
python tools/validator.py --debug
```

### Debug Mode
```bash
# Enable debug mode for detailed output
export AI_DOC_FRAMEWORK_DEBUG=1
python tools/setup-wizard.py --debug
```

## 📊 Post-Installation

### First Steps
1. **Review Configuration**
   ```bash
   cat ai-doc-config.json
   ```

2. **Test AI Integration**
   ```bash
   python tools/test-ai-integration.py
   ```

3. **Generate Documentation**
   ```bash
   python tools/generate-docs.py
   ```

4. **Validate Structure**
   ```bash
   python tools/validator.py --full
   ```

### Next Steps
- Read [USAGE.md](USAGE.md) for usage instructions
- Check [CONFIGURATION.md](CONFIGURATION.md) for advanced configuration
- Review [examples/](examples/) for implementation examples

## 🔄 Updates

### Framework Updates
```bash
# Update framework
git pull origin main
pip install -r requirements.txt --upgrade

# Regenerate templates if needed
python tools/update-templates.py
```

### Configuration Updates
```bash
# Update configuration
python tools/config-updater.py

# Migrate existing setup
python tools/migrate-config.py
```

## 📞 Support

### Getting Help
- **Documentation**: [Full Documentation](https://github.com/zsarir/ai-doc-framework/wiki)
- **Issues**: [GitHub Issues](https://github.com/zsarir/ai-doc-framework/issues)
- **Discussions**: [GitHub Discussions](https://github.com/zsarir/ai-doc-framework/discussions)

### Installation Support
```bash
# Run diagnostic tool
python tools/diagnostic.py

# Generate support report
python tools/support-report.py
```

---

**📦 Installation Complete!** 

Your AI Documentation Framework is now ready to use. Check the [USAGE.md](USAGE.md) guide for next steps.
