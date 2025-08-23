#!/usr/bin/env python3
"""
📊 AI Documentation Framework - Version Management System
Manages versions, checks compatibility, and handles version-related operations

Usage:
    python tools/version-manager.py [command] [options]
    
Commands:
    check           Check current version and compatibility
    compare         Compare two versions
    validate        Validate version format
    history         Show version history
    compatibility   Check compatibility between versions
    
Options:
    --version VER   Specify version to work with
    --format FORMAT Output format (console, json)
    --config PATH   Path to ai-doc-config.json
"""

import os
import sys
import json
import argparse
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any
import urllib.request

class VersionManager:
    """Version management system for AI Documentation Framework"""
    
    def __init__(self, project_root: str = ".", config_path: Optional[str] = None):
        self.project_root = Path(project_root).resolve()
        self.config_path = config_path or self.project_root / "ai-doc-config.json"
        self.framework_dir = self.project_root / "ai-doc-framework"
        
        # Version compatibility matrix
        self.compatibility_matrix = {
            "1.0.0": {"compatible_with": ["1.0.0", "1.1.0"], "breaking_changes": []},
            "1.1.0": {"compatible_with": ["1.0.0", "1.1.0", "1.2.0"], "breaking_changes": ["config_format"]},
            "1.2.0": {"compatible_with": ["1.1.0", "1.2.0"], "breaking_changes": ["template_structure"]},
            "2.0.0": {"compatible_with": ["2.0.0"], "breaking_changes": ["major_rewrite", "config_format", "api_changes"]}
        }
        
        # Feature matrix by version
        self.feature_matrix = {
            "1.0.0": ["basic_docs", "ai_rules", "start_task", "complete_task"],
            "1.1.0": ["basic_docs", "ai_rules", "start_task", "complete_task", "issue_management"],
            "1.2.0": ["basic_docs", "ai_rules", "start_task", "complete_task", "issue_management", "enhanced_templates"],
            "2.0.0": ["basic_docs", "ai_rules", "start_task", "complete_task", "issue_management", "enhanced_templates", 
                     "conflict_detection", "rule_management", "version_control", "html_reports"]
        }
        
    def get_current_version(self) -> Optional[str]:
        """Get current framework version"""
        
        # Check framework VERSION file
        framework_version_file = self.framework_dir / "VERSION"
        if framework_version_file.exists():
            try:
                version = framework_version_file.read_text().strip()
                return version
            except Exception:
                pass
        
        # Check project VERSION file
        project_version_file = self.project_root / "VERSION"
        if project_version_file.exists():
            try:
                version = project_version_file.read_text().strip()
                return version
            except Exception:
                pass
        
        # Check configuration file
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r') as f:
                    config = json.load(f)
                    return config.get('framework_version')
            except Exception:
                pass
        
        return None
        
    def get_latest_version(self) -> Optional[str]:
        """Get latest available version from GitHub"""
        try:
            response = urllib.request.urlopen(
                "https://api.github.com/repos/zsarir/ai-doc-framework/releases/latest"
            )
            data = json.loads(response.read().decode())
            return data['tag_name'].lstrip('v')
        except Exception:
            # Return current version as fallback
            return "2.0.0"
            
    def validate_version(self, version: str) -> bool:
        """Validate version format (semantic versioning)"""
        pattern = r'^(\d+)\.(\d+)\.(\d+)(?:-([a-zA-Z0-9\-]+))?(?:\+([a-zA-Z0-9\-]+))?$'
        return bool(re.match(pattern, version))
        
    def compare_versions(self, v1: str, v2: str) -> int:
        """Compare two versions (-1: v1 < v2, 0: v1 == v2, 1: v1 > v2)"""
        def version_tuple(v):
            # Handle pre-release versions
            if '-' in v:
                v = v.split('-')[0]
            # Handle non-numeric parts
            parts = []
            for part in v.split('.'):
                try:
                    parts.append(int(part))
                except ValueError:
                    # Skip non-numeric parts
                    continue
            return tuple(parts) if parts else (0, 0, 0)
        
        v1_tuple = version_tuple(v1)
        v2_tuple = version_tuple(v2)
        
        if v1_tuple < v2_tuple:
            return -1
        elif v1_tuple > v2_tuple:
            return 1
        else:
            return 0
            
    def is_compatible(self, from_version: str, to_version: str) -> Tuple[bool, List[str]]:
        """Check if versions are compatible"""
        if from_version not in self.compatibility_matrix:
            return False, [f"Unknown source version: {from_version}"]
        
        if to_version not in self.compatibility_matrix:
            return False, [f"Unknown target version: {to_version}"]
        
        compat_info = self.compatibility_matrix[from_version]
        
        if to_version in compat_info["compatible_with"]:
            return True, []
        else:
            breaking_changes = self.compatibility_matrix[to_version]["breaking_changes"]
            return False, breaking_changes
            
    def get_migration_path(self, from_version: str, to_version: str) -> List[str]:
        """Get migration path between versions"""
        if self.compare_versions(from_version, to_version) == 0:
            return []
        
        # For now, direct migration path
        # In future versions, this could handle intermediate steps
        return [from_version, to_version]
        
    def get_version_features(self, version: str) -> List[str]:
        """Get features available in a specific version"""
        return self.feature_matrix.get(version, [])
        
    def get_version_info(self, version: str) -> Dict[str, Any]:
        """Get comprehensive version information"""
        return {
            "version": version,
            "valid": self.validate_version(version),
            "features": self.get_version_features(version),
            "compatibility": self.compatibility_matrix.get(version, {}),
            "release_date": self._get_release_date(version),
            "breaking_changes": self.compatibility_matrix.get(version, {}).get("breaking_changes", [])
        }
        
    def _get_release_date(self, version: str) -> Optional[str]:
        """Get release date for version (placeholder - would query GitHub API)"""
        # Placeholder release dates
        release_dates = {
            "1.0.0": "2024-12-15",
            "1.1.0": "2024-12-30", 
            "1.2.0": "2025-01-10",
            "2.0.0": "2025-01-21"
        }
        return release_dates.get(version)
        
    def check_system_version(self) -> Dict[str, Any]:
        """Check current system version and status"""
        current_version = self.get_current_version()
        latest_version = self.get_latest_version()
        
        result = {
            "current_version": current_version,
            "latest_version": latest_version,
            "up_to_date": False,
            "update_available": False,
            "compatibility_status": "unknown"
        }
        
        if current_version and latest_version:
            comparison = self.compare_versions(current_version, latest_version)
            result["up_to_date"] = comparison == 0
            result["update_available"] = comparison < 0
            
            is_compatible, issues = self.is_compatible(current_version, latest_version)
            result["compatibility_status"] = "compatible" if is_compatible else "incompatible"
            result["compatibility_issues"] = issues
        
        return result
        
    def generate_version_report(self, format: str = "console") -> str:
        """Generate comprehensive version report"""
        current_version = self.get_current_version()
        latest_version = self.get_latest_version()
        system_status = self.check_system_version()
        
        if format == "json":
            report_data = {
                "timestamp": datetime.now().isoformat(),
                "current_version": current_version,
                "latest_version": latest_version,
                "system_status": system_status,
                "available_versions": list(self.compatibility_matrix.keys()),
                "features_by_version": self.feature_matrix
            }
            return json.dumps(report_data, indent=2)
        
        # Console format
        report = []
        report.append("📊 AI Documentation Framework - Version Report")
        report.append("=" * 60)
        
        report.append(f"📋 Current Version: {current_version or 'Not detected'}")
        report.append(f"📋 Latest Version: {latest_version or 'Unknown'}")
        
        if current_version:
            features = self.get_version_features(current_version)
            report.append(f"🎯 Current Features: {len(features)}")
            for feature in features:
                report.append(f"   ✅ {feature.replace('_', ' ').title()}")
        
        if system_status["update_available"]:
            report.append(f"\n🔄 Update Available!")
            report.append(f"   From: {current_version}")
            report.append(f"   To: {latest_version}")
            
            if system_status["compatibility_status"] == "incompatible":
                report.append(f"   ⚠️  Breaking changes detected:")
                for issue in system_status.get("compatibility_issues", []):
                    report.append(f"      - {issue}")
        elif system_status["up_to_date"]:
            report.append(f"\n✅ System is up to date!")
        
        # Version history
        report.append(f"\n📚 Version History:")
        for version in sorted(self.compatibility_matrix.keys(), 
                            key=lambda v: tuple(map(int, v.split('.'))), reverse=True):
            release_date = self._get_release_date(version)
            features_count = len(self.get_version_features(version))
            breaking_changes = len(self.compatibility_matrix[version]["breaking_changes"])
            
            status = ""
            if version == current_version:
                status = " (CURRENT)"
            elif version == latest_version:
                status = " (LATEST)"
            
            report.append(f"   📅 v{version}{status}")
            if release_date:
                report.append(f"      Released: {release_date}")
            report.append(f"      Features: {features_count}")
            if breaking_changes > 0:
                report.append(f"      Breaking Changes: {breaking_changes}")
        
        return "\n".join(report)
        
    def validate_project_version(self) -> Dict[str, Any]:
        """Validate project version configuration"""
        validation_result = {
            "valid": True,
            "issues": [],
            "warnings": []
        }
        
        # Check VERSION file exists
        version_files = [
            self.framework_dir / "VERSION",
            self.project_root / "VERSION"
        ]
        
        version_found = False
        for version_file in version_files:
            if version_file.exists():
                version_found = True
                try:
                    version = version_file.read_text().strip()
                    if not self.validate_version(version):
                        validation_result["issues"].append(f"Invalid version format in {version_file}: {version}")
                        validation_result["valid"] = False
                except Exception as e:
                    validation_result["issues"].append(f"Could not read {version_file}: {e}")
                    validation_result["valid"] = False
        
        if not version_found:
            validation_result["warnings"].append("No VERSION file found")
        
        # Check configuration file
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r') as f:
                    config = json.load(f)
                    
                config_version = config.get('framework_version')
                if not config_version:
                    validation_result["warnings"].append("No framework_version in configuration")
                elif not self.validate_version(config_version):
                    validation_result["issues"].append(f"Invalid framework_version in config: {config_version}")
                    validation_result["valid"] = False
                    
            except Exception as e:
                validation_result["issues"].append(f"Could not read configuration: {e}")
                validation_result["valid"] = False
        else:
            validation_result["warnings"].append("No configuration file found")
        
        return validation_result

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='📊 AI Documentation Framework - Version Management'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Check command
    check_parser = subparsers.add_parser('check', help='Check current version and status')
    check_parser.add_argument('--format', choices=['console', 'json'], default='console',
                            help='Output format')
    
    # Compare command
    compare_parser = subparsers.add_parser('compare', help='Compare two versions')
    compare_parser.add_argument('version1', help='First version')
    compare_parser.add_argument('version2', help='Second version')
    
    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate version format')
    validate_parser.add_argument('version', help='Version to validate')
    
    # History command
    history_parser = subparsers.add_parser('history', help='Show version history')
    history_parser.add_argument('--format', choices=['console', 'json'], default='console',
                              help='Output format')
    
    # Compatibility command
    compat_parser = subparsers.add_parser('compatibility', help='Check version compatibility')
    compat_parser.add_argument('from_version', help='Source version')
    compat_parser.add_argument('to_version', help='Target version')
    
    # Global options
    parser.add_argument('--config', type=str, help='Path to ai-doc-config.json')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        # Initialize version manager
        vm = VersionManager(project_root=".", config_path=args.config)
        
        if args.command == 'check':
            if hasattr(args, 'format') and args.format == 'json':
                system_status = vm.check_system_version()
                print(json.dumps(system_status, indent=2))
            else:
                report = vm.generate_version_report('console')
                print(report)
                
                # Also show validation results
                validation = vm.validate_project_version()
                if not validation["valid"] or validation["warnings"]:
                    print(f"\n🔍 Validation Results:")
                    if validation["issues"]:
                        for issue in validation["issues"]:
                            print(f"❌ {issue}")
                    if validation["warnings"]:
                        for warning in validation["warnings"]:
                            print(f"⚠️  {warning}")
        
        elif args.command == 'compare':
            result = vm.compare_versions(args.version1, args.version2)
            if result < 0:
                print(f"{args.version1} < {args.version2}")
            elif result > 0:
                print(f"{args.version1} > {args.version2}")
            else:
                print(f"{args.version1} == {args.version2}")
        
        elif args.command == 'validate':
            is_valid = vm.validate_version(args.version)
            if is_valid:
                print(f"✅ Version {args.version} is valid")
            else:
                print(f"❌ Version {args.version} is invalid")
                sys.exit(1)
        
        elif args.command == 'history':
            report = vm.generate_version_report(getattr(args, 'format', 'console'))
            print(report)
        
        elif args.command == 'compatibility':
            is_compatible, issues = vm.is_compatible(args.from_version, args.to_version)
            if is_compatible:
                print(f"✅ {args.from_version} → {args.to_version}: Compatible")
            else:
                print(f"❌ {args.from_version} → {args.to_version}: Incompatible")
                if issues:
                    print(f"Breaking changes:")
                    for issue in issues:
                        print(f"   - {issue}")
                sys.exit(1)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
