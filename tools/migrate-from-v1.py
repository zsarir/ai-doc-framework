#!/usr/bin/env python3
"""
🔄 AI Documentation Framework - v1.x to v2.0 Migration Tool
Migrates existing v1.x installations to v2.0 with conflict detection and rule management

Usage:
    python tools/migrate-from-v1.py [options]
    
Options:
    --interactive       Interactive migration with prompts
    --auto             Automatic migration without prompts
    --backup-dir DIR   Custom backup directory
    --dry-run          Show what would be migrated without making changes
    --project-path PATH Path to project root (default: current directory)
"""

import os
import sys
import json
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any

class V1ToV2Migrator:
    """Migration tool for v1.x to v2.0 upgrade"""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root).resolve()
        self.backup_dir = None
        
        # v1.x file patterns
        self.v1_files = [
            "ai-doc-config.json",
            "AI_RULES.md",
            "START_TASK.md", 
            "COMPLETE_TASK.md"
        ]
        
        # v1.x application structure
        self.v1_app_files = [
            "AI_RULES.md",
            "START_TASK.md",
            "COMPLETE_TASK.md",
            "docs/AI_APP_GUIDE.md"
        ]
        
    def detect_v1_installation(self) -> Dict[str, Any]:
        """Detect v1.x installation and analyze structure"""
        detection_result = {
            "is_v1": False,
            "version": None,
            "files_found": [],
            "applications": [],
            "issues": []
        }
        
        # Check for v1.x indicators
        v1_indicators = 0
        for file_name in self.v1_files:
            file_path = self.project_root / file_name
            if file_path.exists():
                detection_result["files_found"].append(file_name)
                v1_indicators += 1
        
        # Check for VERSION file (v2.0 indicator)
        version_file = self.project_root / "VERSION"
        if version_file.exists():
            try:
                version = version_file.read_text().strip()
                if version.startswith("2."):
                    detection_result["issues"].append("Already v2.0 - no migration needed")
                    return detection_result
                else:
                    detection_result["version"] = version
            except Exception:
                pass
        
        # Check configuration for applications
        config_file = self.project_root / "ai-doc-config.json"
        if config_file.exists():
            try:
                with open(config_file, 'r') as f:
                    config = json.load(f)
                    
                # Check if it's v1.x format (missing v2.0 fields)
                if 'framework_version' not in config:
                    detection_result["is_v1"] = True
                    detection_result["version"] = "1.0.0"  # Default v1 version
                
                # Find applications
                for app in config.get('applications', []):
                    app_name = app['name']
                    app_dir = self.project_root / app_name
                    if app_dir.exists():
                        app_info = {
                            "name": app_name,
                            "path": str(app_dir),
                            "files": []
                        }
                        
                        # Check for v1 app files
                        for file_name in self.v1_app_files:
                            file_path = app_dir / file_name
                            if file_path.exists():
                                app_info["files"].append(file_name)
                        
                        detection_result["applications"].append(app_info)
                        
            except Exception as e:
                detection_result["issues"].append(f"Could not read config: {e}")
        
        # Determine if this is v1.x
        if v1_indicators >= 2 and not detection_result.get("version", "").startswith("2."):
            detection_result["is_v1"] = True
            if not detection_result["version"]:
                detection_result["version"] = "1.0.0"
        
        return detection_result
        
    def create_migration_backup(self) -> Path:
        """Create backup before migration"""
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_path = self.project_root / f"v1-backup-{timestamp}"
        backup_path.mkdir(exist_ok=True)
        
        print(f"📦 Creating v1.x backup at: {backup_path}")
        
        # Backup root files
        for file_name in self.v1_files:
            source = self.project_root / file_name
            if source.exists():
                shutil.copy2(source, backup_path / file_name)
                print(f"✅ Backed up: {file_name}")
        
        # Backup framework directory if exists
        framework_dir = self.project_root / "ai-doc-framework"
        if framework_dir.exists():
            framework_backup = backup_path / "ai-doc-framework"
            shutil.copytree(framework_dir, framework_backup)
            print(f"✅ Backed up: ai-doc-framework/")
        
        # Backup application directories
        config_file = self.project_root / "ai-doc-config.json"
        if config_file.exists():
            try:
                with open(config_file, 'r') as f:
                    config = json.load(f)
                    
                for app in config.get('applications', []):
                    app_name = app['name']
                    app_dir = self.project_root / app_name
                    if app_dir.exists():
                        app_backup = backup_path / app_name
                        shutil.copytree(app_dir, app_backup)
                        print(f"✅ Backed up: {app_name}/")
            except Exception as e:
                print(f"⚠️  Warning: Could not backup applications: {e}")
        
        self.backup_dir = backup_path
        return backup_path
        
    def migrate_configuration(self) -> bool:
        """Migrate ai-doc-config.json to v2.0 format"""
        config_file = self.project_root / "ai-doc-config.json"
        
        if not config_file.exists():
            print(f"❌ Configuration file not found: {config_file}")
            return False
        
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
            
            print(f"🔄 Migrating configuration to v2.0 format...")
            
            # Add v2.0 required fields
            config['framework_version'] = "2.0.0"
            config['last_updated'] = datetime.now().isoformat()
            
            if 'created_date' not in config:
                config['created_date'] = datetime.now().isoformat()
            
            # Ensure project has root_path
            if 'project' in config:
                if 'root_path' not in config['project']:
                    config['project']['root_path'] = str(self.project_root)
            
            # Add default error categories if missing
            if 'error_categories' not in config:
                config['error_categories'] = [
                    "backend", "frontend", "infrastructure", 
                    "security", "testing", "deployment"
                ]
            
            # Add default issue categories if missing
            if 'issue_categories' not in config:
                config['issue_categories'] = [
                    "incomplete-tasks", "unresolved-errors", "system-issues"
                ]
            
            # Save updated configuration
            with open(config_file, 'w') as f:
                json.dump(config, f, indent=2)
            
            print(f"✅ Configuration migrated successfully")
            return True
            
        except Exception as e:
            print(f"❌ Error migrating configuration: {e}")
            return False
            
    def add_v2_files(self) -> bool:
        """Add new v2.0 files"""
        print(f"📄 Adding v2.0 files...")
        
        try:
            # Add VERSION file
            version_file = self.project_root / "VERSION"
            with open(version_file, 'w') as f:
                f.write("2.0.0")
            print(f"✅ Added VERSION file")
            
            # Add CHANGELOG.md
            changelog_file = self.project_root / "CHANGELOG.md"
            if not changelog_file.exists():
                changelog_content = f"""# Changelog - {self.project_root.name}

## [2.0.0] - {datetime.now().strftime('%Y-%m-%d')}

### 🔄 Migrated from v1.x

#### New Features Added
- **🔍 Conflict Detection**: Automatic detection of documentation conflicts
- **🛠️ Rule Management**: Direct AI rule management via MANAGE_RULES.md
- **📊 Enhanced Reporting**: HTML and JSON report generation
- **🔄 Version Management**: Semantic versioning and update system

#### Migration Notes
- Migrated from v1.x installation
- All existing configuration and customizations preserved
- New features available immediately

---

## Previous Versions

Previous version history was not tracked in v1.x installations.
"""
                with open(changelog_file, 'w') as f:
                    f.write(changelog_content)
                print(f"✅ Added CHANGELOG.md")
            
            # Add MANAGE_RULES.md template
            manage_rules_file = self.project_root / "MANAGE_RULES.md"
            if not manage_rules_file.exists():
                # Try to copy from framework template
                framework_dir = self.project_root / "ai-doc-framework"
                template_file = framework_dir / "templates" / "core-files" / "MANAGE_RULES.md"
                
                if template_file.exists():
                    shutil.copy2(template_file, manage_rules_file)
                    print(f"✅ Added MANAGE_RULES.md from template")
                else:
                    # Create basic MANAGE_RULES.md
                    basic_content = f"""# 🛠️ MANAGE RULES - AI Rules Management System
> **Add, Update, Remove AI Rules | Direct System Modification**

## 🎯 AI INSTRUCTIONS - RULES MANAGEMENT PROTOCOL

**When to use this file**: 
- To add new rules to any application or root
- To update existing rules
- To remove outdated rules
- To reorganize rule categories

## 📋 RULE MANAGEMENT EXAMPLES

### Add Rules Command Format
```bash
"Add [category] rule to [target]: [rule content]"

Examples:
✅ "Add security rule to root: All APIs must use HTTPS"
✅ "Add performance rule to website: Page load time under 2 seconds"
```

### Update Rules Command Format
```bash
"Update [target] [category] rule: [old rule] → [new rule]"

Examples:
✅ "Update root security rule: JWT expiration from 24h to 1h"
```

### Remove Rules Command Format
```bash
"Remove [category] rule from [target]: [rule description]"

Examples:
✅ "Remove outdated authentication rule from api: Legacy OAuth method"
```

---

**🔄 Last Updated**: {datetime.now().strftime('%Y-%m-%d')} | **Rule Management**: Production Ready
"""
                    with open(manage_rules_file, 'w') as f:
                        f.write(basic_content)
                    print(f"✅ Added basic MANAGE_RULES.md")
            
            return True
            
        except Exception as e:
            print(f"❌ Error adding v2.0 files: {e}")
            return False
            
    def update_existing_files(self) -> bool:
        """Update existing files for v2.0 compatibility"""
        print(f"🔄 Updating existing files for v2.0...")
        
        try:
            # Update AI_RULES.md with v2.0 enhancements
            ai_rules_file = self.project_root / "AI_RULES.md"
            if ai_rules_file.exists():
                content = ai_rules_file.read_text()
                
                # Add conflict detection rules if not present
                if "conflict detection" not in content.lower():
                    additional_rules = f"""

## 🔍 Conflict Detection Rules (v2.0)

### Rule Management Integration
- **MANAGE_RULES.md Usage**: Use MANAGE_RULES.md for all rule modifications
- **Conflict Prevention**: Check for rule conflicts before adding new rules
- **Cross-Application Consistency**: Ensure rules are consistent across applications

### Version Control
- **Version Tracking**: All rule changes must update version information
- **Change Documentation**: Document all rule modifications in CHANGELOG.md
- **Backup Before Changes**: Create backup before major rule modifications

---

**🔄 Updated for v2.0**: {datetime.now().strftime('%Y-%m-%d')} | **Conflict Detection**: Enabled
"""
                    
                    with open(ai_rules_file, 'a') as f:
                        f.write(additional_rules)
                    print(f"✅ Enhanced AI_RULES.md with v2.0 features")
            
            # Update START_TASK.md with conflict detection
            start_task_file = self.project_root / "START_TASK.md"
            if start_task_file.exists():
                content = start_task_file.read_text()
                
                if "conflict detection" not in content.lower():
                    # Add conflict detection step
                    conflict_step = f"""

### Step 0.5: Run Conflict Detection (v2.0 Feature)
```python
# NEW: Check for documentation conflicts before starting
def check_conflicts_before_task():
    conflict_result = run_conflict_detection()
    
    if conflict_result.total_conflicts > 0:
        alert_user("Conflicts detected - review before proceeding")
        return conflict_result
    
    return None
```

"""
                    # Insert after first step
                    updated_content = content.replace(
                        "### Step 1:", 
                        conflict_step + "### Step 1:"
                    )
                    
                    with open(start_task_file, 'w') as f:
                        f.write(updated_content)
                    print(f"✅ Enhanced START_TASK.md with conflict detection")
            
            return True
            
        except Exception as e:
            print(f"❌ Error updating existing files: {e}")
            return False
            
    def setup_conflict_detection(self) -> bool:
        """Set up conflict detection for migrated project"""
        print(f"🔍 Setting up conflict detection...")
        
        try:
            # Ensure framework directory exists
            framework_dir = self.project_root / "ai-doc-framework"
            if not framework_dir.exists():
                print(f"⚠️  Framework directory not found - conflict detection may not work")
                return False
            
            # Check if conflict detector exists
            conflict_detector = framework_dir / "tools" / "conflict-detector.py"
            if conflict_detector.exists():
                # Make executable
                conflict_detector.chmod(0o755)
                print(f"✅ Conflict detector ready")
                
                # Test conflict detection
                try:
                    import subprocess
                    result = subprocess.run([
                        sys.executable, str(conflict_detector), "--help"
                    ], capture_output=True, text=True, cwd=self.project_root)
                    
                    if result.returncode == 0:
                        print(f"✅ Conflict detection tested successfully")
                    else:
                        print(f"⚠️  Warning: Conflict detection test failed")
                        
                except Exception as e:
                    print(f"⚠️  Warning: Could not test conflict detection: {e}")
            else:
                print(f"⚠️  Conflict detector not found in framework")
                return False
            
            return True
            
        except Exception as e:
            print(f"❌ Error setting up conflict detection: {e}")
            return False
            
    def validate_migration(self) -> Dict[str, Any]:
        """Validate that migration was successful"""
        print(f"🔍 Validating migration...")
        
        validation_result = {
            "success": True,
            "checks": [],
            "warnings": [],
            "errors": []
        }
        
        # Check VERSION file
        version_file = self.project_root / "VERSION"
        if version_file.exists():
            try:
                version = version_file.read_text().strip()
                if version == "2.0.0":
                    validation_result["checks"].append("VERSION file: OK")
                else:
                    validation_result["errors"].append(f"VERSION file has wrong version: {version}")
                    validation_result["success"] = False
            except Exception as e:
                validation_result["errors"].append(f"Could not read VERSION file: {e}")
                validation_result["success"] = False
        else:
            validation_result["errors"].append("VERSION file missing")
            validation_result["success"] = False
        
        # Check configuration
        config_file = self.project_root / "ai-doc-config.json"
        if config_file.exists():
            try:
                with open(config_file, 'r') as f:
                    config = json.load(f)
                    
                if config.get('framework_version') == "2.0.0":
                    validation_result["checks"].append("Configuration version: OK")
                else:
                    validation_result["errors"].append("Configuration version not updated")
                    validation_result["success"] = False
                    
                if 'last_updated' in config:
                    validation_result["checks"].append("Configuration timestamp: OK")
                else:
                    validation_result["warnings"].append("Configuration missing timestamp")
                    
            except Exception as e:
                validation_result["errors"].append(f"Could not validate configuration: {e}")
                validation_result["success"] = False
        else:
            validation_result["errors"].append("Configuration file missing")
            validation_result["success"] = False
        
        # Check MANAGE_RULES.md
        manage_rules_file = self.project_root / "MANAGE_RULES.md"
        if manage_rules_file.exists():
            validation_result["checks"].append("MANAGE_RULES.md: OK")
        else:
            validation_result["warnings"].append("MANAGE_RULES.md missing")
        
        # Check conflict detection
        framework_dir = self.project_root / "ai-doc-framework"
        conflict_detector = framework_dir / "tools" / "conflict-detector.py"
        if conflict_detector.exists():
            validation_result["checks"].append("Conflict detector: OK")
        else:
            validation_result["warnings"].append("Conflict detector not found")
        
        return validation_result
        
    def migrate(self, interactive: bool = True, dry_run: bool = False) -> bool:
        """Main migration process"""
        print(f"🔄 AI Documentation Framework v1.x → v2.0 Migration")
        print(f"=" * 60)
        
        # Detect v1.x installation
        detection = self.detect_v1_installation()
        
        if not detection["is_v1"]:
            if detection["issues"]:
                for issue in detection["issues"]:
                    print(f"❌ {issue}")
            else:
                print(f"❌ No v1.x installation detected")
            return False
        
        print(f"✅ Detected v1.x installation")
        print(f"📋 Version: {detection['version']}")
        print(f"📋 Files found: {len(detection['files_found'])}")
        print(f"📋 Applications: {len(detection['applications'])}")
        
        if dry_run:
            print(f"\n🔍 DRY RUN - No changes will be made")
            print(f"Would migrate:")
            for file_name in detection["files_found"]:
                print(f"   - {file_name}")
            for app in detection["applications"]:
                print(f"   - {app['name']}/ ({len(app['files'])} files)")
            return True
        
        if interactive:
            print(f"\n🤔 Proceed with migration to v2.0?")
            print(f"   - Backup will be created automatically")
            print(f"   - All existing files will be preserved")
            print(f"   - New v2.0 features will be added")
            
            response = input(f"Continue? (y/N): ").strip().lower()
            if response != 'y':
                print(f"❌ Migration cancelled by user")
                return False
        
        try:
            # Create backup
            backup_path = self.create_migration_backup()
            
            # Migrate configuration
            if not self.migrate_configuration():
                print(f"❌ Configuration migration failed")
                return False
            
            # Add v2.0 files
            if not self.add_v2_files():
                print(f"❌ Failed to add v2.0 files")
                return False
            
            # Update existing files
            if not self.update_existing_files():
                print(f"❌ Failed to update existing files")
                return False
            
            # Setup conflict detection
            if not self.setup_conflict_detection():
                print(f"⚠️  Warning: Conflict detection setup incomplete")
            
            # Validate migration
            validation = self.validate_migration()
            
            if not validation["success"]:
                print(f"❌ Migration validation failed:")
                for error in validation["errors"]:
                    print(f"   - {error}")
                return False
            
            # Show results
            print(f"\n✅ Migration completed successfully!")
            print(f"📋 Migrated from v{detection['version']} to v2.0.0")
            print(f"📦 Backup available at: {backup_path}")
            
            print(f"\n✅ Validation Results:")
            for check in validation["checks"]:
                print(f"   ✅ {check}")
            
            if validation["warnings"]:
                print(f"\n⚠️  Warnings:")
                for warning in validation["warnings"]:
                    print(f"   ⚠️  {warning}")
            
            print(f"\n🎯 Next Steps:")
            print(f"   1. Test conflict detection: python3 ai-doc-framework/tools/conflict-detector.py")
            print(f"   2. Review MANAGE_RULES.md for rule management")
            print(f"   3. Check CHANGELOG.md for new features")
            print(f"   4. Update your team on new v2.0 capabilities")
            
            return True
            
        except Exception as e:
            print(f"❌ Migration failed: {e}")
            return False

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='🔄 AI Documentation Framework v1.x → v2.0 Migration'
    )
    
    parser.add_argument('--interactive', action='store_true',
                      help='Interactive migration with prompts')
    parser.add_argument('--auto', action='store_true',
                      help='Automatic migration without prompts')
    parser.add_argument('--backup-dir', type=str,
                      help='Custom backup directory')
    parser.add_argument('--dry-run', action='store_true',
                      help='Show what would be migrated without making changes')
    parser.add_argument('--project-path', type=str, default=".",
                      help='Path to project root')
    
    args = parser.parse_args()
    
    try:
        # Initialize migrator
        migrator = V1ToV2Migrator(project_root=args.project_path)
        
        # Determine interaction mode
        interactive = args.interactive or not args.auto
        
        # Run migration
        success = migrator.migrate(
            interactive=interactive,
            dry_run=args.dry_run
        )
        
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print(f"\n⚠️  Migration cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Migration error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
