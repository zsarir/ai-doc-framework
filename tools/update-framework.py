#!/usr/bin/env python3
"""
🔄 AI Documentation Framework - Update System
Automatically updates existing installations to the latest version

Usage:
    python tools/update-framework.py [options]
    
Options:
    --auto              Automatic update without prompts
    --from-version VER  Specify current version for migration
    --backup-dir DIR    Custom backup directory
    --dry-run          Show what would be updated without making changes
    --force            Force update even if versions match
    --config PATH      Path to ai-doc-config.json
"""

import os
import sys
import json
import shutil
import subprocess
import argparse
import tempfile
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import urllib.request
import zipfile

# Version information
CURRENT_VERSION = "2.0.0"
SUPPORTED_VERSIONS = ["1.0.0", "1.1.0", "1.2.0", "2.0.0"]
GITHUB_REPO = "https://github.com/zsarir/ai-doc-framework"
GITHUB_API = "https://api.github.com/repos/zsarir/ai-doc-framework"

class FrameworkUpdater:
    """Main framework update system"""
    
    def __init__(self, project_root: str = ".", config_path: Optional[str] = None):
        self.project_root = Path(project_root).resolve()
        self.config_path = config_path or self.project_root / "ai-doc-config.json"
        self.framework_dir = self.project_root / "ai-doc-framework"
        self.backup_dir = None
        self.current_version = None
        self.target_version = CURRENT_VERSION
        
    def detect_current_version(self) -> Optional[str]:
        """Detect current framework version"""
        
        # Check VERSION file
        version_file = self.framework_dir / "VERSION"
        if version_file.exists():
            try:
                version = version_file.read_text().strip()
                print(f"✅ Detected version from VERSION file: {version}")
                return version
            except Exception as e:
                print(f"⚠️  Warning: Could not read VERSION file: {e}")
        
        # Check ai-doc-config.json
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r') as f:
                    config = json.load(f)
                    version = config.get('framework_version')
                    if version:
                        print(f"✅ Detected version from config: {version}")
                        return version
            except Exception as e:
                print(f"⚠️  Warning: Could not read config file: {e}")
        
        # Check for v1.x indicators
        v1_indicators = [
            self.project_root / "START_TASK.md",
            self.project_root / "AI_RULES.md",
            self.project_root / "COMPLETE_TASK.md"
        ]
        
        if any(f.exists() for f in v1_indicators):
            print("📋 Detected v1.x installation (no VERSION file)")
            return "1.0.0"
        
        print("❓ Could not detect current version")
        return None
        
    def check_for_updates(self) -> Tuple[bool, str]:
        """Check if updates are available"""
        try:
            # Get latest release from GitHub API
            response = urllib.request.urlopen(f"{GITHUB_API}/releases/latest")
            data = json.loads(response.read().decode())
            latest_version = data['tag_name'].lstrip('v')
            
            if self.current_version:
                needs_update = self._compare_versions(latest_version, self.current_version) > 0
                return needs_update, latest_version
            else:
                return True, latest_version
                
        except Exception as e:
            print(f"⚠️  Warning: Could not check for updates: {e}")
            return False, CURRENT_VERSION
            
    def _compare_versions(self, v1: str, v2: str) -> int:
        """Compare two version strings (semantic versioning)"""
        def version_tuple(v):
            return tuple(map(int, v.split('.')))
        
        v1_tuple = version_tuple(v1)
        v2_tuple = version_tuple(v2)
        
        if v1_tuple > v2_tuple:
            return 1
        elif v1_tuple < v2_tuple:
            return -1
        else:
            return 0
            
    def create_backup(self, backup_dir: Optional[str] = None) -> Path:
        """Create backup of current installation"""
        if backup_dir:
            backup_path = Path(backup_dir)
        else:
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            backup_path = self.project_root / f"backup-{timestamp}"
        
        backup_path.mkdir(exist_ok=True)
        
        print(f"📦 Creating backup at: {backup_path}")
        
        # Backup critical files
        critical_files = [
            "ai-doc-config.json",
            "AI_RULES.md", 
            "START_TASK.md",
            "COMPLETE_TASK.md",
            "MANAGE_RULES.md",
            "VERSION"
        ]
        
        for file_name in critical_files:
            source = self.project_root / file_name
            if source.exists():
                shutil.copy2(source, backup_path / file_name)
                print(f"✅ Backed up: {file_name}")
        
        # Backup framework directory
        if self.framework_dir.exists():
            framework_backup = backup_path / "ai-doc-framework"
            shutil.copytree(self.framework_dir, framework_backup)
            print(f"✅ Backed up: ai-doc-framework/")
        
        # Backup application directories
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r') as f:
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
        print(f"✅ Backup completed: {backup_path}")
        return backup_path
        
    def download_latest_framework(self) -> Path:
        """Download latest framework version"""
        print(f"📥 Downloading latest framework version...")
        
        # Create temporary directory
        temp_dir = Path(tempfile.mkdtemp(prefix="framework-update-"))
        
        try:
            # Download latest release
            download_url = f"{GITHUB_REPO}/archive/refs/heads/main.zip"
            zip_path = temp_dir / "framework.zip"
            
            print(f"📥 Downloading from: {download_url}")
            urllib.request.urlretrieve(download_url, zip_path)
            
            # Extract archive
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)
            
            # Find extracted directory
            extracted_dirs = [d for d in temp_dir.iterdir() if d.is_dir() and d.name.startswith('ai-doc-framework')]
            if not extracted_dirs:
                raise Exception("Could not find extracted framework directory")
            
            framework_source = extracted_dirs[0]
            print(f"✅ Downloaded and extracted to: {framework_source}")
            return framework_source
            
        except Exception as e:
            print(f"❌ Error downloading framework: {e}")
            shutil.rmtree(temp_dir, ignore_errors=True)
            raise
            
    def update_framework_files(self, source_dir: Path):
        """Update framework files from source"""
        print(f"🔄 Updating framework files...")
        
        # Remove old framework directory
        if self.framework_dir.exists():
            shutil.rmtree(self.framework_dir)
            print(f"🗑️  Removed old framework directory")
        
        # Copy new framework
        shutil.copytree(source_dir, self.framework_dir)
        print(f"✅ Copied new framework to: {self.framework_dir}")
        
        # Update VERSION file
        version_file = self.framework_dir / "VERSION"
        with open(version_file, 'w') as f:
            f.write(self.target_version)
        print(f"✅ Updated VERSION to: {self.target_version}")
        
    def migrate_configuration(self):
        """Migrate configuration for new version"""
        print(f"🔄 Migrating configuration...")
        
        if not self.config_path.exists():
            print(f"⚠️  No configuration file found, skipping migration")
            return
        
        try:
            with open(self.config_path, 'r') as f:
                config = json.load(f)
            
            # Add new required fields for v2.0
            config['framework_version'] = self.target_version
            config['last_updated'] = datetime.now().isoformat()
            
            if 'created_date' not in config:
                config['created_date'] = datetime.now().isoformat()
            
            # Ensure root_path is absolute
            if 'project' in config and 'root_path' not in config['project']:
                config['project']['root_path'] = str(self.project_root)
            
            # Save updated configuration
            with open(self.config_path, 'w') as f:
                json.dump(config, f, indent=2)
            
            print(f"✅ Configuration migrated successfully")
            
        except Exception as e:
            print(f"❌ Error migrating configuration: {e}")
            raise
            
    def update_project_files(self):
        """Update project-level files"""
        print(f"🔄 Updating project files...")
        
        # Update MANAGE_RULES.md if it doesn't exist
        manage_rules_file = self.project_root / "MANAGE_RULES.md"
        if not manage_rules_file.exists():
            template_file = self.framework_dir / "templates" / "core-files" / "MANAGE_RULES.md"
            if template_file.exists():
                shutil.copy2(template_file, manage_rules_file)
                print(f"✅ Added MANAGE_RULES.md")
        
        # Create VERSION file in project root
        project_version_file = self.project_root / "VERSION"
        with open(project_version_file, 'w') as f:
            f.write(self.target_version)
        print(f"✅ Updated project VERSION file")
        
        # Update CHANGELOG.md if it doesn't exist
        changelog_file = self.project_root / "CHANGELOG.md"
        if not changelog_file.exists():
            framework_changelog = self.framework_dir / "CHANGELOG.md"
            if framework_changelog.exists():
                shutil.copy2(framework_changelog, changelog_file)
                print(f"✅ Added CHANGELOG.md")
        
    def validate_update(self) -> bool:
        """Validate that update was successful"""
        print(f"🔍 Validating update...")
        
        validation_checks = []
        
        # Check VERSION file
        version_file = self.framework_dir / "VERSION"
        if version_file.exists():
            version = version_file.read_text().strip()
            if version == self.target_version:
                validation_checks.append(("VERSION file", True))
            else:
                validation_checks.append(("VERSION file", False, f"Expected {self.target_version}, got {version}"))
        else:
            validation_checks.append(("VERSION file", False, "File not found"))
        
        # Check configuration
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r') as f:
                    config = json.load(f)
                    
                if config.get('framework_version') == self.target_version:
                    validation_checks.append(("Configuration version", True))
                else:
                    validation_checks.append(("Configuration version", False, "Version not updated"))
                    
            except Exception as e:
                validation_checks.append(("Configuration file", False, str(e)))
        else:
            validation_checks.append(("Configuration file", False, "File not found"))
        
        # Check conflict detector
        conflict_detector = self.framework_dir / "tools" / "conflict-detector.py"
        if conflict_detector.exists():
            validation_checks.append(("Conflict detector", True))
        else:
            validation_checks.append(("Conflict detector", False, "Tool not found"))
        
        # Check MANAGE_RULES.md
        manage_rules = self.project_root / "MANAGE_RULES.md"
        if manage_rules.exists():
            validation_checks.append(("MANAGE_RULES.md", True))
        else:
            validation_checks.append(("MANAGE_RULES.md", False, "File not found"))
        
        # Print validation results
        all_passed = True
        for check in validation_checks:
            if check[1]:  # Success
                print(f"✅ {check[0]}: OK")
            else:  # Failure
                print(f"❌ {check[0]}: FAILED - {check[2] if len(check) > 2 else 'Unknown error'}")
                all_passed = False
        
        return all_passed
        
    def run_post_update_tasks(self):
        """Run post-update tasks"""
        print(f"🔄 Running post-update tasks...")
        
        # Test conflict detection
        try:
            conflict_detector = self.framework_dir / "tools" / "conflict-detector.py"
            if conflict_detector.exists():
                result = subprocess.run([
                    sys.executable, str(conflict_detector), "--help"
                ], capture_output=True, text=True, cwd=self.project_root)
                
                if result.returncode == 0:
                    print(f"✅ Conflict detection tool working")
                else:
                    print(f"⚠️  Warning: Conflict detection tool may have issues")
            
        except Exception as e:
            print(f"⚠️  Warning: Could not test conflict detection: {e}")
        
        # Update file permissions
        try:
            tools_dir = self.framework_dir / "tools"
            for tool_file in tools_dir.glob("*.py"):
                tool_file.chmod(0o755)
            print(f"✅ Updated tool permissions")
        except Exception as e:
            print(f"⚠️  Warning: Could not update permissions: {e}")
        
    def rollback_update(self):
        """Rollback to previous version"""
        if not self.backup_dir or not self.backup_dir.exists():
            print(f"❌ No backup found, cannot rollback")
            return False
        
        print(f"🔄 Rolling back to previous version...")
        
        try:
            # Restore framework directory
            if self.framework_dir.exists():
                shutil.rmtree(self.framework_dir)
            
            framework_backup = self.backup_dir / "ai-doc-framework"
            if framework_backup.exists():
                shutil.copytree(framework_backup, self.framework_dir)
                print(f"✅ Restored framework directory")
            
            # Restore configuration
            config_backup = self.backup_dir / "ai-doc-config.json"
            if config_backup.exists():
                shutil.copy2(config_backup, self.config_path)
                print(f"✅ Restored configuration")
            
            # Restore other files
            for file_name in ["AI_RULES.md", "START_TASK.md", "COMPLETE_TASK.md"]:
                backup_file = self.backup_dir / file_name
                target_file = self.project_root / file_name
                if backup_file.exists():
                    shutil.copy2(backup_file, target_file)
                    print(f"✅ Restored {file_name}")
            
            print(f"✅ Rollback completed successfully")
            return True
            
        except Exception as e:
            print(f"❌ Error during rollback: {e}")
            return False
            
    def update(self, auto: bool = False, dry_run: bool = False, force: bool = False) -> bool:
        """Main update process"""
        print(f"🔄 AI Documentation Framework Update System")
        print(f"=" * 50)
        
        # Detect current version
        self.current_version = self.detect_current_version()
        
        if not force:
            # Check if update is needed
            needs_update, latest_version = self.check_for_updates()
            self.target_version = latest_version
            
            if not needs_update and self.current_version:
                print(f"✅ Already up to date (v{self.current_version})")
                return True
        
        print(f"📋 Current version: {self.current_version or 'Unknown'}")
        print(f"📋 Target version: {self.target_version}")
        
        if dry_run:
            print(f"🔍 DRY RUN - No changes will be made")
            print(f"Would update from {self.current_version} to {self.target_version}")
            return True
        
        if not auto:
            response = input(f"\n🤔 Proceed with update? (y/N): ").strip().lower()
            if response != 'y':
                print(f"❌ Update cancelled by user")
                return False
        
        try:
            # Create backup
            backup_path = self.create_backup()
            
            # Download latest framework
            source_dir = self.download_latest_framework()
            
            # Update framework files
            self.update_framework_files(source_dir)
            
            # Migrate configuration
            self.migrate_configuration()
            
            # Update project files
            self.update_project_files()
            
            # Validate update
            if not self.validate_update():
                print(f"❌ Update validation failed")
                if not auto:
                    response = input(f"🤔 Rollback to previous version? (Y/n): ").strip().lower()
                    if response != 'n':
                        return self.rollback_update()
                return False
            
            # Run post-update tasks
            self.run_post_update_tasks()
            
            # Cleanup
            shutil.rmtree(source_dir.parent, ignore_errors=True)
            
            print(f"\n✅ Update completed successfully!")
            print(f"📋 Updated from {self.current_version} to {self.target_version}")
            print(f"📦 Backup available at: {backup_path}")
            print(f"\n🎯 Next steps:")
            print(f"   1. Review CHANGELOG.md for new features")
            print(f"   2. Test conflict detection: python3 ai-doc-framework/tools/conflict-detector.py")
            print(f"   3. Try rule management with MANAGE_RULES.md")
            
            return True
            
        except Exception as e:
            print(f"❌ Update failed: {e}")
            
            if not auto:
                response = input(f"🤔 Rollback to previous version? (Y/n): ").strip().lower()
                if response != 'n':
                    return self.rollback_update()
            
            return False

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='🔄 AI Documentation Framework Update System'
    )
    
    parser.add_argument('--auto', action='store_true',
                      help='Automatic update without prompts')
    parser.add_argument('--from-version', type=str,
                      help='Specify current version for migration')
    parser.add_argument('--backup-dir', type=str,
                      help='Custom backup directory')
    parser.add_argument('--dry-run', action='store_true',
                      help='Show what would be updated without making changes')
    parser.add_argument('--force', action='store_true',
                      help='Force update even if versions match')
    parser.add_argument('--config', type=str,
                      help='Path to ai-doc-config.json')
    
    args = parser.parse_args()
    
    try:
        # Initialize updater
        updater = FrameworkUpdater(
            project_root=".",
            config_path=args.config
        )
        
        # Override detected version if specified
        if args.from_version:
            updater.current_version = args.from_version
        
        # Run update
        success = updater.update(
            auto=args.auto,
            dry_run=args.dry_run,
            force=args.force
        )
        
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print(f"\n⚠️  Update cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Update system error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
