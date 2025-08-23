# 🔄 Update Guide - AI Documentation Framework

## 🎯 Overview

This guide helps you update your AI Documentation Framework installation to the latest version while preserving your existing configuration and customizations.

## 📊 Version Information

### Current Version: 2.0.0
### Previous Version: 1.x.x

## 🚨 Important Notes

### For v1.x Users
**⚠️ CRITICAL**: If you're using v1.x, this is a **MAJOR UPDATE** with breaking changes. Please follow the migration guide carefully.

### For New Users
If this is your first installation, use the regular [INSTALL.md](INSTALL.md) guide instead.

## 🔍 Pre-Update Checklist

### 1. Check Current Version
```bash
# Check if you have a version file
cat VERSION 2>/dev/null || echo "Version file not found - likely v1.x"

# Check framework structure
ls -la | grep -E "(ai-doc-config\.json|START_TASK\.md|AI_RULES\.md)"
```

### 2. Backup Your Project
```bash
# Create complete backup
cp -r your-project/ your-project-backup-$(date +%Y%m%d-%H%M%S)/

# Verify backup
ls -la your-project-backup-*/
```

### 3. Check Dependencies
```bash
# Ensure Python 3.7+ is available
python3 --version

# Check required packages
pip3 list | grep -E "(colorama|pathlib)"
```

## 🚀 Update Methods

### Method 1: Automatic Update (Recommended)

#### For v2.x Users
```bash
# Navigate to your project root
cd /path/to/your-project

# Download and run update tool
curl -O https://raw.githubusercontent.com/zsarir/ai-doc-framework/main/tools/update-framework.py
python3 update-framework.py --auto

# Verify update
python3 ai-doc-framework/tools/conflict-detector.py --version
```

#### For v1.x Users (Migration Required)
```bash
# Navigate to your project root
cd /path/to/your-project

# Download migration tool
curl -O https://raw.githubusercontent.com/zsarir/ai-doc-framework/main/tools/migrate-from-v1.py
python3 migrate-from-v1.py --interactive

# Follow the interactive prompts
```

### Method 2: Manual Update

#### Step 1: Download New Framework
```bash
# Clone latest version
git clone https://github.com/zsarir/ai-doc-framework.git ai-doc-framework-new

# Or update existing clone
cd ai-doc-framework
git pull origin main
cd ..
```

#### Step 2: Backup Current Framework
```bash
# Backup current framework directory
mv ai-doc-framework/ ai-doc-framework-backup/
mv ai-doc-framework-new/ ai-doc-framework/
```

#### Step 3: Migrate Configuration
```bash
# Copy your ai-doc-config.json
cp your-project-backup-*/ai-doc-config.json ./

# Run configuration migration
python3 ai-doc-framework/tools/migrate-config.py --from-backup your-project-backup-*
```

#### Step 4: Update Project Files
```bash
# Update core files while preserving customizations
python3 ai-doc-framework/tools/update-project-files.py --preserve-custom
```

## 🔧 Migration Steps (v1.x → v2.0)

### Step 1: Pre-Migration Analysis
```bash
# Analyze current installation
python3 ai-doc-framework/tools/analyze-v1-installation.py

# Review analysis report
cat migration-analysis-report.txt
```

### Step 2: Configuration Migration
```bash
# Migrate ai-doc-config.json
python3 ai-doc-framework/tools/migrate-config.py --interactive

# Verify new configuration
python3 ai-doc-framework/tools/validate-config.py
```

### Step 3: File Structure Migration
```bash
# Migrate file structure
python3 ai-doc-framework/tools/migrate-structure.py --from-v1

# Update templates
python3 ai-doc-framework/tools/update-templates.py
```

### Step 4: Add New Features
```bash
# Add conflict detection capability
python3 ai-doc-framework/tools/setup-conflict-detection.py

# Add rule management system
python3 ai-doc-framework/tools/setup-rule-management.py

# Initialize version tracking
python3 ai-doc-framework/tools/init-version-tracking.py
```

### Step 5: Validation and Testing
```bash
# Validate system integrity
python3 ai-doc-framework/tools/validate-installation.py

# Test conflict detection
python3 ai-doc-framework/tools/test-conflict-detection.py

# Run comprehensive tests
python3 ai-doc-framework/tools/run-all-tests.py
```

## 📋 What's New in v2.0

### 🔍 Conflict Detection System
- Automatic detection of AI_RULES conflicts
- Documentation consistency verification
- Multiple report formats (Console, JSON, HTML)
- Severity-based prioritization

### 🛠️ Rule Management System
- Natural language rule commands
- Cross-application synchronization
- Automatic conflict prevention
- Version control for rules

### 📊 Enhanced Reporting
- Interactive HTML reports
- JSON export for automation
- Trend analysis capabilities
- Ready-to-use resolution commands

### 🔄 Version Management
- Semantic versioning support
- Automatic update notifications
- Migration tools and guides
- Backward compatibility checking

## 🚨 Breaking Changes in v2.0

### Configuration File Changes
```json
// OLD (v1.x)
{
  "project": {
    "name": "My Project",
    "type": "multi"
  }
}

// NEW (v2.0) - Required additions
{
  "project": {
    "name": "My Project", 
    "type": "multi",
    "root_path": "/absolute/path/to/project"  // NEW: Required
  },
  "framework_version": "2.0.0",              // NEW: Required
  "created_date": "2025-01-21",              // NEW: Auto-generated
  "last_updated": "2025-01-21"               // NEW: Auto-updated
}
```

### New Required Files
- `VERSION` - Framework version tracking
- `CHANGELOG.md` - Version history
- `MANAGE_RULES.md` - Rule management system

### Template Structure Changes
- Enhanced `AI_RULES.md` template with conflict detection
- New `MANAGE_RULES.md` template
- Updated `START_TASK.md` with version checking
- Enhanced `COMPLETE_TASK.md` with conflict validation

## 🔧 Post-Update Tasks

### 1. Verify Installation
```bash
# Check version
cat VERSION

# Verify all tools work
python3 ai-doc-framework/tools/conflict-detector.py --help
python3 ai-doc-framework/tools/setup-wizard.py --version
```

### 2. Update Documentation
```bash
# Review new features
cat CHANGELOG.md

# Update your project documentation
python3 ai-doc-framework/tools/update-project-docs.py
```

### 3. Configure New Features
```bash
# Set up conflict detection
python3 ai-doc-framework/tools/conflict-detector.py --setup

# Configure rule management
# Review and customize MANAGE_RULES.md for your project
```

### 4. Test Everything
```bash
# Run comprehensive tests
python3 ai-doc-framework/tools/test-all-features.py

# Test conflict detection
python3 ai-doc-framework/tools/conflict-detector.py --output console

# Test rule management
# Give MANAGE_RULES.md to AI with a test command
```

## 🚨 Troubleshooting

### Common Update Issues

#### "Version file not found"
```bash
# Solution: You're likely on v1.x
echo "1.0.0" > VERSION
python3 ai-doc-framework/tools/migrate-from-v1.py
```

#### "Configuration validation failed"
```bash
# Solution: Update configuration format
python3 ai-doc-framework/tools/fix-config.py --auto-fix
```

#### "Missing required files"
```bash
# Solution: Regenerate missing files
python3 ai-doc-framework/tools/setup-wizard.py --repair-installation
```

#### "Conflict detection not working"
```bash
# Solution: Verify ai-doc-config.json placement
ls -la ai-doc-config.json  # Must be in project root
python3 ai-doc-framework/tools/validate-config.py
```

### Rollback Procedure
If the update fails, you can rollback:

```bash
# Stop any running processes
pkill -f "conflict-detector"

# Restore backup
rm -rf ai-doc-framework/
mv ai-doc-framework-backup/ ai-doc-framework/

# Restore configuration
cp your-project-backup-*/ai-doc-config.json ./

# Verify rollback
python3 ai-doc-framework/tools/setup-wizard.py --version
```

## 📞 Getting Help

### Documentation Resources
- [CHANGELOG.md](CHANGELOG.md) - Complete list of changes
- [MIGRATION_GUIDE.md](MIGRATION_GUIDE.md) - Detailed migration instructions
- [tools/README-CONFLICT-DETECTION.md](tools/README-CONFLICT-DETECTION.md) - Conflict detection guide

### Support Channels
- **GitHub Issues**: [Report problems](https://github.com/zsarir/ai-doc-framework/issues)
- **Discussions**: [Ask questions](https://github.com/zsarir/ai-doc-framework/discussions)
- **Documentation**: [Full documentation](https://zsarir.github.io/ai-doc-framework/)

### Before Asking for Help
1. Check the [CHANGELOG.md](CHANGELOG.md) for known issues
2. Run the diagnostic tool: `python3 ai-doc-framework/tools/diagnose-issues.py`
3. Include your system information and error messages
4. Mention your previous version and update method used

## 📈 Update Success Indicators

### ✅ Successful Update Checklist
- [ ] Version file shows `2.0.0`
- [ ] `ai-doc-config.json` includes new required fields
- [ ] Conflict detection runs without errors
- [ ] MANAGE_RULES.md file exists and is properly formatted
- [ ] All existing applications still have their AI_RULES.md files
- [ ] Setup wizard shows version 2.0.0
- [ ] Test suite passes completely

### 📊 Verification Commands
```bash
# Quick verification
python3 ai-doc-framework/tools/verify-update.py

# Detailed system check
python3 ai-doc-framework/tools/system-health-check.py

# Feature verification
python3 ai-doc-framework/tools/test-all-features.py --quick
```

## 🎯 Next Steps After Update

### 1. Explore New Features
- Run conflict detection on your project
- Try the rule management system
- Generate HTML reports
- Set up CI/CD integration

### 2. Optimize Your Workflow
- Configure automated conflict detection
- Set up regular system health checks
- Integrate with your development tools
- Train your team on new features

### 3. Stay Updated
- Watch the GitHub repository for updates
- Subscribe to release notifications
- Join the community discussions
- Contribute feedback and suggestions

---

**🔄 Last Updated**: 2025-01-21  
**📋 Update Guide Version**: 2.0.0  
**🎯 Next Major Update**: v3.0.0 (Planned: Q2 2025)
