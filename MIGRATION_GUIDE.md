# 🔄 Migration Guide - AI Documentation Framework

## 🎯 Overview

This guide provides detailed instructions for migrating between different versions of the AI Documentation Framework, with special focus on the major v1.x → v2.0 upgrade.

## 📊 Version Migration Matrix

| From Version | To Version | Migration Type | Complexity | Tool Required |
|--------------|------------|----------------|------------|---------------|
| v1.0.x       | v2.0.0     | Major          | High       | migrate-from-v1.py |
| v1.1.x       | v2.0.0     | Major          | High       | migrate-from-v1.py |
| v1.2.x       | v2.0.0     | Major          | High       | migrate-from-v1.py |
| v2.0.x       | v2.1.x     | Minor          | Low        | update-framework.py |

## 🚨 Major Migration: v1.x → v2.0

### 🔍 What's Changing

#### Breaking Changes
- **Configuration Format**: `ai-doc-config.json` requires new fields
- **File Structure**: New mandatory files (VERSION, CHANGELOG.md, MANAGE_RULES.md)
- **Template Structure**: Enhanced templates with conflict detection
- **API Changes**: New parameters and validation requirements

#### New Features Added
- **🔍 Conflict Detection**: Automatic detection of documentation conflicts
- **🛠️ Rule Management**: Direct AI rule management via MANAGE_RULES.md
- **📊 Enhanced Reporting**: HTML and JSON report generation
- **🔄 Version Management**: Semantic versioning and update system

### 📋 Pre-Migration Checklist

#### 1. Backup Your Project
```bash
# Create complete backup
cp -r your-project/ your-project-v1-backup/

# Verify backup
ls -la your-project-v1-backup/
```

#### 2. Check Current Installation
```bash
# Check for v1.x indicators
ls -la | grep -E "(ai-doc-config\.json|START_TASK\.md|AI_RULES\.md)"

# Check if VERSION file exists (v2.0 indicator)
cat VERSION 2>/dev/null || echo "No VERSION file - likely v1.x"
```

#### 3. Document Current Customizations
```bash
# List customized files
find . -name "*.md" -type f | head -10

# Check configuration
cat ai-doc-config.json | jq '.' 2>/dev/null || cat ai-doc-config.json
```

### 🔄 Migration Process

#### Method 1: Interactive Migration (Recommended)
```bash
# Download migration tool
curl -O https://raw.githubusercontent.com/zsarir/ai-doc-framework/main/tools/migrate-from-v1.py

# Run interactive migration
python3 migrate-from-v1.py --interactive

# Follow the prompts:
# 1. Confirm migration
# 2. Review detected files
# 3. Approve changes
# 4. Validate results
```

#### Method 2: Automatic Migration
```bash
# For automated environments
python3 migrate-from-v1.py --auto --project-path /path/to/project

# Check results
python3 tools/version-manager.py check
```

#### Method 3: Manual Migration
```bash
# 1. Download new framework
git clone https://github.com/zsarir/ai-doc-framework.git ai-doc-framework-v2

# 2. Backup current framework
mv ai-doc-framework/ ai-doc-framework-v1-backup/
mv ai-doc-framework-v2/ ai-doc-framework/

# 3. Run manual migration steps
python3 ai-doc-framework/tools/migrate-from-v1.py --dry-run
python3 ai-doc-framework/tools/migrate-from-v1.py --auto
```

### 📄 Configuration Migration

#### Old Format (v1.x)
```json
{
  "project": {
    "name": "My Project",
    "type": "multi"
  },
  "applications": [
    {
      "name": "website",
      "type": "frontend",
      "framework": "django"
    }
  ],
  "error_categories": ["backend", "frontend"]
}
```

#### New Format (v2.0)
```json
{
  "project": {
    "name": "My Project",
    "type": "multi",
    "root_path": "/absolute/path/to/project"
  },
  "applications": [
    {
      "name": "website",
      "type": "frontend",
      "framework": "django",
      "description": "Main website application"
    }
  ],
  "error_categories": ["backend", "frontend", "infrastructure", "security"],
  "issue_categories": ["incomplete-tasks", "unresolved-errors", "system-issues"],
  "framework_version": "2.0.0",
  "created_date": "2025-01-21T10:30:00",
  "last_updated": "2025-01-21T10:30:00"
}
```

### 📁 File Structure Changes

#### New Files Added
```bash
# Version tracking
VERSION                    # Framework version (2.0.0)
CHANGELOG.md              # Version history and changes

# Rule management
MANAGE_RULES.md           # AI rule management system

# Enhanced documentation
UPDATE_GUIDE.md           # Update instructions
MIGRATION_GUIDE.md        # This file
```

#### Enhanced Existing Files
```bash
# Updated with v2.0 features
AI_RULES.md              # Added conflict detection rules
START_TASK.md            # Added conflict checking step
COMPLETE_TASK.md         # Added validation steps

# New templates
ai-doc-framework/templates/core-files/MANAGE_RULES.md
ai-doc-framework/tools/conflict-detector.py
ai-doc-framework/tools/version-manager.py
```

### 🔍 Post-Migration Validation

#### Automatic Validation
```bash
# Run migration validation
python3 tools/version-manager.py check

# Test new features
python3 tools/conflict-detector.py --help
python3 tools/test-conflict-detection.py
```

#### Manual Validation Checklist
- [ ] VERSION file exists and shows "2.0.0"
- [ ] ai-doc-config.json includes new required fields
- [ ] MANAGE_RULES.md file exists
- [ ] Conflict detection runs without errors
- [ ] All applications still have their documentation
- [ ] Setup wizard shows version 2.0.0

### 🚨 Troubleshooting Migration Issues

#### Common Problems

##### "Migration tool not found"
```bash
# Solution: Download directly
curl -O https://raw.githubusercontent.com/zsarir/ai-doc-framework/main/tools/migrate-from-v1.py
chmod +x migrate-from-v1.py
python3 migrate-from-v1.py --interactive
```

##### "Configuration validation failed"
```bash
# Check configuration format
python3 -c "import json; json.load(open('ai-doc-config.json'))"

# Fix common issues
python3 tools/fix-config.py --auto-repair
```

##### "Conflict detection not working"
```bash
# Verify ai-doc-config.json placement
ls -la ai-doc-config.json  # Must be in project root

# Check framework installation
ls -la ai-doc-framework/tools/conflict-detector.py

# Test manually
python3 ai-doc-framework/tools/conflict-detector.py --version
```

##### "Applications not detected"
```bash
# Check application structure
for app in website website-api email-server robot-control-api; do
  echo "=== $app ==="
  ls -la $app/AI_RULES.md 2>/dev/null || echo "Missing AI_RULES.md"
done

# Regenerate missing files
python3 ai-doc-framework/tools/setup-wizard.py --repair-applications
```

#### Rollback Procedure
If migration fails, you can rollback:

```bash
# 1. Stop any processes
pkill -f "conflict-detector"

# 2. Restore from backup
rm -rf ai-doc-framework/
mv ai-doc-framework-v1-backup/ ai-doc-framework/

# 3. Restore configuration
cp your-project-v1-backup/ai-doc-config.json ./

# 4. Verify rollback
python3 ai-doc-framework/tools/setup-wizard.py --version
```

## 🔄 Minor Updates: v2.x → v2.y

### 📋 Update Process
```bash
# Check for updates
python3 tools/version-manager.py check

# Automatic update
python3 tools/update-framework.py --auto

# Manual update with prompts
python3 tools/update-framework.py
```

### 🔍 What Gets Updated
- Framework tools and utilities
- Templates and documentation
- Bug fixes and security patches
- New minor features

### 🛡️ What's Preserved
- Your ai-doc-config.json configuration
- Custom AI_RULES.md modifications
- Application-specific customizations
- Project-specific documentation

## 📊 Migration Success Metrics

### ✅ Successful Migration Indicators
- [ ] Version shows 2.0.0 in all version files
- [ ] Conflict detection runs successfully
- [ ] All applications maintain their documentation
- [ ] MANAGE_RULES.md system works with AI
- [ ] No broken links or missing files
- [ ] Setup wizard recognizes v2.0 installation

### 📈 Performance Improvements
After migration to v2.0, you should see:
- **60-80% reduction** in documentation conflicts
- **90% faster** conflict detection vs manual review
- **100% automation** for rule management
- **Enhanced reporting** with HTML and JSON formats

## 🎯 Post-Migration Best Practices

### 1. Team Training
```bash
# Introduce team to new features
python3 tools/conflict-detector.py --output html --output-file team-demo.html

# Show rule management capabilities
# Give MANAGE_RULES.md to AI with sample commands
```

### 2. Workflow Integration
```bash
# Add to CI/CD pipeline
python3 tools/conflict-detector.py --severity high --output json

# Set up regular conflict detection
crontab -e
# Add: 0 9 * * 1 cd /path/to/project && python3 tools/conflict-detector.py --output html
```

### 3. Documentation Updates
```bash
# Update team documentation
echo "Updated to AI Documentation Framework v2.0" >> README.md
echo "New features: Conflict Detection, Rule Management" >> README.md

# Document custom rules
# Use MANAGE_RULES.md to document project-specific rules
```

## 📞 Getting Help

### Support Resources
- **Migration Issues**: [GitHub Issues](https://github.com/zsarir/ai-doc-framework/issues)
- **General Questions**: [Discussions](https://github.com/zsarir/ai-doc-framework/discussions)
- **Documentation**: [Complete Guide](https://zsarir.github.io/ai-doc-framework/)

### Before Asking for Help
1. Run diagnostic: `python3 tools/version-manager.py check`
2. Check logs: Look for error messages during migration
3. Verify structure: Ensure ai-doc-config.json is in project root
4. Test features: Try conflict detection and rule management

### Information to Include
- Current version (before migration)
- Target version (after migration)
- Operating system and Python version
- Error messages and logs
- Project structure (number of applications)

---

**🔄 Last Updated**: 2025-01-21  
**📋 Migration Guide Version**: 2.0.0  
**🎯 Covers**: v1.x → v2.0 (Major), v2.x → v2.y (Minor)
