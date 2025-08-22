#!/usr/bin/env python3
"""
📊 AI Documentation Framework - Conflict Detection System
Detects conflicts in AI_RULES and documentation across multi-application projects

Usage:
    python tools/conflict-detector.py [options]
    
Options:
    --rules-only        Check only AI_RULES conflicts
    --docs-only         Check only documentation conflicts  
    --app APP_NAME      Check specific application only
    --output FORMAT     Output format: console, json, html (default: console)
    --config CONFIG     Path to ai-doc-config.json (default: ./ai-doc-config.json)
    --severity LEVEL    Minimum severity: low, medium, high, critical (default: medium)
"""

import os
import sys
import json
import argparse
import re
from typing import Dict, List, Tuple, Optional, Any
from pathlib import Path
from dataclasses import dataclass, asdict
from datetime import datetime
import difflib

@dataclass
class ConflictItem:
    """Represents a single conflict detected in the system"""
    id: str
    type: str  # 'rule_conflict', 'doc_conflict', 'implementation_conflict'
    category: str  # 'performance', 'security', 'implementation', 'architecture'
    severity: str  # 'low', 'medium', 'high', 'critical'
    title: str
    description: str
    applications: List[str]
    conflicting_content: List[Dict[str, Any]]
    resolution_suggestion: str
    manage_rules_command: str

@dataclass
class ConflictReport:
    """Complete conflict detection report"""
    timestamp: str
    project_name: str
    project_path: str
    total_conflicts: int
    conflicts_by_severity: Dict[str, int]
    conflicts_by_category: Dict[str, int]
    conflicts: List[ConflictItem]
    recommendations: List[str]
    summary: str

class AIDocConflictDetector:
    """Main conflict detection system"""
    
    def __init__(self, project_root: str = ".", config_path: Optional[str] = None):
        self.project_root = Path(project_root).resolve()
        self.config_path = config_path or self.project_root / "ai-doc-config.json"
        self.config = self._load_config()
        self.applications = self._discover_applications()
        
        # Conflict detection patterns
        self.rule_patterns = {
            'performance': [
                r'timeout.*?(\d+).*?(second|minute|ms)',
                r'response.*?time.*?(\d+).*?(ms|second)',
                r'memory.*?limit.*?(\d+).*?(mb|gb)',
                r'max.*?connections.*?(\d+)',
                r'cache.*?ttl.*?(\d+)'
            ],
            'security': [
                r'jwt.*?expir.*?(\d+).*?(hour|minute|day)',
                r'password.*?length.*?(\d+)',
                r'ssl.*?version.*?(1\.\d|2\.\d|3\.\d)',
                r'rate.*?limit.*?(\d+)',
                r'session.*?timeout.*?(\d+)'
            ],
            'implementation': [
                r'use.*?(css grid|flexbox)',
                r'database.*?(postgres|mysql|sqlite)',
                r'framework.*?(django|fastapi|flask)',
                r'port.*?(\d{4,5})',
                r'coding.*?style.*?(pep8|google|airbnb)'
            ],
            'architecture': [
                r'port.*?(\d{4,5})',
                r'container.*?name.*?([a-zA-Z0-9\-_]+)',
                r'network.*?([a-zA-Z0-9\-_]+)',
                r'volume.*?([a-zA-Z0-9\-_/]+)',
                r'environment.*?([A-Z_]+)'
            ]
        }
        
    def _load_config(self) -> Dict[str, Any]:
        """Load ai-doc-config.json"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"❌ ERROR: Config file not found at {self.config_path}")
            print("🔧 Please run the setup wizard first: python tools/setup-wizard.py")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"❌ ERROR: Invalid JSON in config file: {e}")
            sys.exit(1)
            
    def _discover_applications(self) -> Dict[str, Path]:
        """Discover all applications in the project"""
        apps = {}
        
        # Add root as an application
        if (self.project_root / "AI_RULES.md").exists():
            apps['root'] = self.project_root
            
        # Add configured applications
        if 'applications' in self.config:
            for app_config in self.config['applications']:
                app_name = app_config['name']
                app_path = self.project_root / app_name
                
                if app_path.exists() and (app_path / "AI_RULES.md").exists():
                    apps[app_name] = app_path
                    
        return apps
        
    def detect_all_conflicts(self, rules_only: bool = False, docs_only: bool = False) -> ConflictReport:
        """Detect all conflicts in the project"""
        conflicts = []
        
        if not docs_only:
            # 1. AI_RULES conflicts across applications
            rule_conflicts = self._detect_ai_rules_conflicts()
            conflicts.extend(rule_conflicts)
            
        if not rules_only:
            # 2. Documentation conflicts within each application
            doc_conflicts = self._detect_documentation_conflicts()
            conflicts.extend(doc_conflicts)
            
        # 3. Generate comprehensive report
        report = self._generate_report(conflicts)
        return report
        
    def _detect_ai_rules_conflicts(self) -> List[ConflictItem]:
        """Detect conflicts between AI_RULES files across applications"""
        conflicts = []
        rules_data = {}
        
        # Load all AI_RULES files
        for app_name, app_path in self.applications.items():
            rules_file = app_path / "AI_RULES.md"
            if rules_file.exists():
                rules_data[app_name] = self._parse_ai_rules_file(rules_file)
                
        # Compare rules across applications
        app_names = list(rules_data.keys())
        for i, app1 in enumerate(app_names):
            for app2 in app_names[i+1:]:
                app_conflicts = self._compare_ai_rules(app1, rules_data[app1], app2, rules_data[app2])
                conflicts.extend(app_conflicts)
                
        return conflicts
        
    def _parse_ai_rules_file(self, rules_file: Path) -> Dict[str, List[str]]:
        """Parse AI_RULES.md file and extract rules by category"""
        rules_by_category = {}
        
        try:
            with open(rules_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Find all rule sections
            sections = re.findall(r'##\s*([^#\n]+)\s*Rules?\s*\n(.*?)(?=##|$)', content, re.DOTALL | re.IGNORECASE)
            
            for section_name, section_content in sections:
                category = section_name.strip().lower()
                rules = re.findall(r'-\s*\*\*([^*]+)\*\*[:\s]*([^\n]+)', section_content)
                rules_by_category[category] = rules
                
        except Exception as e:
            print(f"⚠️  Warning: Could not parse {rules_file}: {e}")
            
        return rules_by_category
        
    def _compare_ai_rules(self, app1: str, rules1: Dict, app2: str, rules2: Dict) -> List[ConflictItem]:
        """Compare AI_RULES between two applications"""
        conflicts = []
        
        # Find common categories
        common_categories = set(rules1.keys()) & set(rules2.keys())
        
        for category in common_categories:
            category_conflicts = self._detect_category_conflicts(
                app1, rules1[category], app2, rules2[category], category
            )
            conflicts.extend(category_conflicts)
            
        return conflicts
        
    def _detect_category_conflicts(self, app1: str, rules1: List, app2: str, rules2: List, category: str) -> List[ConflictItem]:
        """Detect conflicts within a specific rule category"""
        conflicts = []
        
        # Check for pattern-based conflicts
        for pattern_type, patterns in self.rule_patterns.items():
            if pattern_type == category or category in pattern_type:
                for pattern in patterns:
                    app1_matches = []
                    app2_matches = []
                    
                    # Find matches in app1 rules
                    for rule_name, rule_desc in rules1:
                        matches = re.findall(pattern, f"{rule_name} {rule_desc}", re.IGNORECASE)
                        if matches:
                            app1_matches.append((rule_name, rule_desc, matches))
                            
                    # Find matches in app2 rules
                    for rule_name, rule_desc in rules2:
                        matches = re.findall(pattern, f"{rule_name} {rule_desc}", re.IGNORECASE)
                        if matches:
                            app2_matches.append((rule_name, rule_desc, matches))
                            
                    # Compare matches for conflicts
                    if app1_matches and app2_matches:
                        conflict = self._analyze_pattern_conflict(
                            app1, app1_matches, app2, app2_matches, category, pattern
                        )
                        if conflict:
                            conflicts.append(conflict)
                            
        return conflicts
        
    def _analyze_pattern_conflict(self, app1: str, matches1: List, app2: str, matches2: List, 
                                category: str, pattern: str) -> Optional[ConflictItem]:
        """Analyze pattern matches to determine if there's a conflict"""
        
        # Extract values from matches
        values1 = set()
        values2 = set()
        
        for _, _, matches in matches1:
            for match in matches:
                if isinstance(match, tuple):
                    values1.add(match[0])  # First capturing group
                else:
                    values1.add(match)
                    
        for _, _, matches in matches2:
            for match in matches:
                if isinstance(match, tuple):
                    values2.add(match[0])  # First capturing group
                else:
                    values2.add(match)
                    
        # Check if values conflict (different non-empty values)
        if values1 and values2 and values1 != values2:
            conflict_id = f"{category}_{app1}_{app2}_{hash(pattern)}"
            severity = self._determine_severity(category, values1, values2)
            
            # Create conflict description
            title = f"{category.title()} Configuration Conflict: {app1} vs {app2}"
            description = f"Different {category} configurations detected between {app1} and {app2}"
            
            conflicting_content = [
                {
                    "application": app1,
                    "values": list(values1),
                    "rules": [{"name": name, "description": desc} for name, desc, _ in matches1]
                },
                {
                    "application": app2,
                    "values": list(values2),
                    "rules": [{"name": name, "description": desc} for name, desc, _ in matches2]
                }
            ]
            
            resolution_suggestion = self._generate_resolution_suggestion(category, app1, app2, values1, values2)
            manage_rules_command = self._generate_manage_rules_command(category, app1, app2, values1, values2)
            
            return ConflictItem(
                id=conflict_id,
                type='rule_conflict',
                category=category,
                severity=severity,
                title=title,
                description=description,
                applications=[app1, app2],
                conflicting_content=conflicting_content,
                resolution_suggestion=resolution_suggestion,
                manage_rules_command=manage_rules_command
            )
            
        return None
        
    def _detect_documentation_conflicts(self) -> List[ConflictItem]:
        """Detect conflicts within documentation of each application"""
        conflicts = []
        
        for app_name, app_path in self.applications.items():
            if app_name == 'root':
                continue
                
            app_conflicts = self._detect_app_documentation_conflicts(app_name, app_path)
            conflicts.extend(app_conflicts)
            
        return conflicts
        
    def _detect_app_documentation_conflicts(self, app_name: str, app_path: Path) -> List[ConflictItem]:
        """Detect documentation conflicts within a specific application"""
        conflicts = []
        
        # Find all documentation files
        docs_dir = app_path / "docs"
        if not docs_dir.exists():
            return conflicts
            
        doc_files = list(docs_dir.glob("**/*.md"))
        
        # Check for conflicting information across documentation files
        for i, doc1 in enumerate(doc_files):
            for doc2 in doc_files[i+1:]:
                file_conflicts = self._compare_documentation_files(app_name, doc1, doc2)
                conflicts.extend(file_conflicts)
                
        return conflicts
        
    def _compare_documentation_files(self, app_name: str, doc1: Path, doc2: Path) -> List[ConflictItem]:
        """Compare two documentation files for conflicts"""
        conflicts = []
        
        try:
            with open(doc1, 'r', encoding='utf-8') as f:
                content1 = f.read()
            with open(doc2, 'r', encoding='utf-8') as f:
                content2 = f.read()
                
            # Look for conflicting technical specifications
            for category, patterns in self.rule_patterns.items():
                for pattern in patterns:
                    matches1 = re.findall(pattern, content1, re.IGNORECASE)
                    matches2 = re.findall(pattern, content2, re.IGNORECASE)
                    
                    if matches1 and matches2 and set(matches1) != set(matches2):
                        conflict = self._create_doc_conflict(
                            app_name, doc1, doc2, category, matches1, matches2, pattern
                        )
                        if conflict:
                            conflicts.append(conflict)
                            
        except Exception as e:
            print(f"⚠️  Warning: Could not compare {doc1} and {doc2}: {e}")
            
        return conflicts
        
    def _create_doc_conflict(self, app_name: str, doc1: Path, doc2: Path, category: str,
                           matches1: List, matches2: List, pattern: str) -> Optional[ConflictItem]:
        """Create a documentation conflict item"""
        
        conflict_id = f"doc_{app_name}_{category}_{hash(str(doc1) + str(doc2) + pattern)}"
        severity = "medium"  # Documentation conflicts are generally medium severity
        
        title = f"Documentation Conflict in {app_name}: {doc1.name} vs {doc2.name}"
        description = f"Conflicting {category} information found in documentation files"
        
        conflicting_content = [
            {
                "file": str(doc1.relative_to(self.project_root)),
                "values": matches1
            },
            {
                "file": str(doc2.relative_to(self.project_root)),
                "values": matches2
            }
        ]
        
        resolution_suggestion = (
            f"Review {category} configurations in {doc1.name} and {doc2.name}. "
            f"Ensure consistent values across all documentation."
        )
        
        manage_rules_command = (
            f'Update {app_name} {category} documentation: '
            f'Standardize conflicting values between {doc1.name} and {doc2.name}'
        )
        
        return ConflictItem(
            id=conflict_id,
            type='doc_conflict',
            category=category,
            severity=severity,
            title=title,
            description=description,
            applications=[app_name],
            conflicting_content=conflicting_content,
            resolution_suggestion=resolution_suggestion,
            manage_rules_command=manage_rules_command
        )
        
    def _determine_severity(self, category: str, values1: set, values2: set) -> str:
        """Determine the severity of a conflict"""
        
        # Critical conflicts
        critical_categories = ['security', 'safety']
        if category in critical_categories:
            return 'critical'
            
        # High severity conflicts
        high_impact_patterns = ['port', 'ssl', 'jwt', 'password', 'timeout']
        if any(pattern in category for pattern in high_impact_patterns):
            return 'high'
            
        # Performance conflicts are typically medium
        if category == 'performance':
            return 'medium'
            
        # Default to low for implementation differences
        return 'low'
        
    def _generate_resolution_suggestion(self, category: str, app1: str, app2: str, 
                                      values1: set, values2: set) -> str:
        """Generate a resolution suggestion for the conflict"""
        
        suggestions = {
            'performance': f'Standardize {category} settings. Consider using the more restrictive value for consistency.',
            'security': f'Use the most secure configuration. Review security requirements for both {app1} and {app2}.',
            'implementation': f'Choose one implementation approach and apply consistently across both applications.',
            'architecture': f'Ensure unique values where required (e.g., ports) or standardize where appropriate.'
        }
        
        base_suggestion = suggestions.get(category, 'Review and standardize the conflicting configurations.')
        
        return (
            f"{base_suggestion}\n"
            f"Current values: {app1}: {values1}, {app2}: {values2}\n"
            f"Use MANAGE_RULES.md to update the conflicting rules."
        )
        
    def _generate_manage_rules_command(self, category: str, app1: str, app2: str,
                                     values1: set, values2: set) -> str:
        """Generate MANAGE_RULES.md command to resolve the conflict"""
        
        # Choose the target application based on priority (root > specific apps)
        target_app = 'root' if 'root' in [app1, app2] else app1
        
        # Generate command based on conflict type
        if category == 'security' or category == 'performance':
            return (
                f'Update {target_app} {category} rule: '
                f'Standardize conflicting values from {app1} ({list(values1)}) and {app2} ({list(values2)})'
            )
        else:
            return (
                f'Add {category} rule to {target_app}: '
                f'Standardize implementation between {app1} and {app2}'
            )
            
    def _generate_report(self, conflicts: List[ConflictItem]) -> ConflictReport:
        """Generate comprehensive conflict report"""
        
        timestamp = datetime.now().isoformat()
        project_name = self.config.get('project', {}).get('name', 'Unknown Project')
        
        # Count conflicts by severity and category
        conflicts_by_severity = {'low': 0, 'medium': 0, 'high': 0, 'critical': 0}
        conflicts_by_category = {}
        
        for conflict in conflicts:
            conflicts_by_severity[conflict.severity] += 1
            if conflict.category not in conflicts_by_category:
                conflicts_by_category[conflict.category] = 0
            conflicts_by_category[conflict.category] += 1
            
        # Generate recommendations
        recommendations = self._generate_recommendations(conflicts)
        
        # Generate summary
        total_conflicts = len(conflicts)
        critical_count = conflicts_by_severity['critical']
        high_count = conflicts_by_severity['high']
        
        if total_conflicts == 0:
            summary = "✅ No conflicts detected! Your documentation system is consistent."
        elif critical_count > 0:
            summary = f"🚨 CRITICAL: {critical_count} critical conflicts require immediate attention!"
        elif high_count > 0:
            summary = f"⚠️ HIGH: {high_count} high-priority conflicts found."
        else:
            summary = f"📋 {total_conflicts} minor conflicts detected."
            
        return ConflictReport(
            timestamp=timestamp,
            project_name=project_name,
            project_path=str(self.project_root),
            total_conflicts=total_conflicts,
            conflicts_by_severity=conflicts_by_severity,
            conflicts_by_category=conflicts_by_category,
            conflicts=conflicts,
            recommendations=recommendations,
            summary=summary
        )
        
    def _generate_recommendations(self, conflicts: List[ConflictItem]) -> List[str]:
        """Generate actionable recommendations based on conflicts"""
        recommendations = []
        
        if not conflicts:
            recommendations.append("✅ Your documentation system is well-maintained!")
            return recommendations
            
        # General recommendations
        recommendations.append("📋 Use MANAGE_RULES.md to resolve rule conflicts systematically.")
        recommendations.append("🔄 Run conflict detection regularly to prevent issues.")
        
        # Severity-based recommendations
        critical_conflicts = [c for c in conflicts if c.severity == 'critical']
        high_conflicts = [c for c in conflicts if c.severity == 'high']
        
        if critical_conflicts:
            recommendations.append(f"🚨 Address {len(critical_conflicts)} critical conflicts immediately!")
            
        if high_conflicts:
            recommendations.append(f"⚠️ Prioritize resolving {len(high_conflicts)} high-priority conflicts.")
            
        # Category-based recommendations
        categories = set(c.category for c in conflicts)
        
        if 'security' in categories:
            recommendations.append("🔒 Security conflicts detected - review authentication and authorization rules.")
            
        if 'performance' in categories:
            recommendations.append("⚡ Performance conflicts found - standardize timeout and resource settings.")
            
        if 'implementation' in categories:
            recommendations.append("🛠 Implementation conflicts detected - choose consistent coding standards.")
            
        return recommendations
        
    def export_report(self, report: ConflictReport, format: str = 'console', output_file: Optional[str] = None):
        """Export conflict report in specified format"""
        
        if format == 'console':
            self._print_console_report(report)
        elif format == 'json':
            self._export_json_report(report, output_file)
        elif format == 'html':
            self._export_html_report(report, output_file)
        else:
            print(f"❌ Unknown output format: {format}")
            
    def _print_console_report(self, report: ConflictReport):
        """Print report to console with colored output"""
        print("\n" + "=" * 80)
        print(f"📊 AI DOCUMENTATION CONFLICT DETECTION REPORT")
        print("=" * 80)
        print(f"🏗️  Project: {report.project_name}")
        print(f"📅 Date: {report.timestamp}")
        print(f"📁 Path: {report.project_path}")
        print(f"📋 Total Conflicts: {report.total_conflicts}")
        
        print(f"\n📊 SEVERITY BREAKDOWN:")
        severity_colors = {'critical': '🚨', 'high': '⚠️ ', 'medium': '📋', 'low': '💡'}
        for severity, count in report.conflicts_by_severity.items():
            if count > 0:
                icon = severity_colors.get(severity, '📋')
                print(f"   {icon} {severity.title()}: {count}")
                
        print(f"\n📂 CATEGORY BREAKDOWN:")
        for category, count in report.conflicts_by_category.items():
            print(f"   🔹 {category.title()}: {count}")
            
        print(f"\n📝 SUMMARY:")
        print(f"   {report.summary}")
        
        if report.conflicts:
            print(f"\n🔍 DETAILED CONFLICTS:")
            for i, conflict in enumerate(report.conflicts, 1):
                severity_icon = severity_colors.get(conflict.severity, '📋')
                print(f"\n   {i}. {severity_icon} {conflict.title}")
                print(f"      📂 Category: {conflict.category}")
                print(f"      🎯 Applications: {', '.join(conflict.applications)}")
                print(f"      📝 Description: {conflict.description}")
                print(f"      💡 Resolution: {conflict.resolution_suggestion}")
                print(f"      🛠️  MANAGE_RULES Command:")
                print(f"         {conflict.manage_rules_command}")
                
        print(f"\n💡 RECOMMENDATIONS:")
        for i, rec in enumerate(report.recommendations, 1):
            print(f"   {i}. {rec}")
            
        print(f"\n🛠️  NEXT STEPS:")
        print(f"   1. Use MANAGE_RULES.md to resolve conflicts")
        print(f"   2. Re-run conflict detection to verify fixes")
        print(f"   3. Update documentation standards to prevent future conflicts")
        
        print("\n" + "=" * 80 + "\n")
        
    def _export_json_report(self, report: ConflictReport, output_file: Optional[str]):
        """Export report as JSON"""
        output_path = output_file or f"conflict-report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(asdict(report), f, indent=2, ensure_ascii=False)
            
        print(f"📄 JSON report exported to: {output_path}")
        
    def _export_html_report(self, report: ConflictReport, output_file: Optional[str]):
        """Export report as HTML"""
        output_path = output_file or f"conflict-report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.html"
        
        html_template = self._generate_html_template(report)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_template)
            
        print(f"📄 HTML report exported to: {output_path}")
        
    def _generate_html_template(self, report: ConflictReport) -> str:
        """Generate HTML template for the report"""
        
        conflicts_html = ""
        severity_colors = {'critical': '#dc2626', 'high': '#ea580c', 'medium': '#d97706', 'low': '#65a30d'}
        
        for i, conflict in enumerate(report.conflicts, 1):
            color = severity_colors.get(conflict.severity, '#6b7280')
            conflicts_html += f"""
            <div class="conflict-item" style="border-left: 4px solid {color};">
                <h3 style="color: {color};">{i}. {conflict.title}</h3>
                <p><strong>Category:</strong> {conflict.category}</p>
                <p><strong>Severity:</strong> {conflict.severity}</p>
                <p><strong>Applications:</strong> {', '.join(conflict.applications)}</p>
                <p><strong>Description:</strong> {conflict.description}</p>
                <p><strong>Resolution:</strong> {conflict.resolution_suggestion}</p>
                <div class="manage-rules-command">
                    <strong>MANAGE_RULES Command:</strong>
                    <code>{conflict.manage_rules_command}</code>
                </div>
            </div>
            """
            
        recommendations_html = ""
        for i, rec in enumerate(report.recommendations, 1):
            recommendations_html += f"<li>{rec}</li>"
            
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>AI Documentation Conflict Report - {report.project_name}</title>
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 20px; background-color: #f8fafc; }}
                .container {{ max-width: 1200px; margin: 0 auto; background: white; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); overflow: hidden; }}
                .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; text-align: center; }}
                .content {{ padding: 30px; }}
                .summary-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 20px 0; }}
                .summary-card {{ background: #f8fafc; padding: 20px; border-radius: 8px; text-align: center; }}
                .conflict-item {{ background: #f9fafb; padding: 20px; margin: 15px 0; border-radius: 8px; }}
                .manage-rules-command {{ background: #1f2937; color: #e5e7eb; padding: 15px; border-radius: 4px; margin-top: 10px; }}
                code {{ background: #374151; color: #f3f4f6; padding: 2px 6px; border-radius: 3px; }}
                .recommendations {{ background: #ecfdf5; padding: 20px; border-radius: 8px; border-left: 4px solid #10b981; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>📊 AI Documentation Conflict Report</h1>
                    <p>{report.project_name}</p>
                    <p>Generated: {report.timestamp}</p>
                </div>
                <div class="content">
                    <h2>📋 Summary</h2>
                    <p><strong>{report.summary}</strong></p>
                    
                    <div class="summary-grid">
                        <div class="summary-card">
                            <h3>Total Conflicts</h3>
                            <h2 style="color: #dc2626;">{report.total_conflicts}</h2>
                        </div>
                        <div class="summary-card">
                            <h3>Critical</h3>
                            <h2 style="color: #dc2626;">{report.conflicts_by_severity['critical']}</h2>
                        </div>
                        <div class="summary-card">
                            <h3>High</h3>
                            <h2 style="color: #ea580c;">{report.conflicts_by_severity['high']}</h2>
                        </div>
                        <div class="summary-card">
                            <h3>Medium</h3>
                            <h2 style="color: #d97706;">{report.conflicts_by_severity['medium']}</h2>
                        </div>
                        <div class="summary-card">
                            <h3>Low</h3>
                            <h2 style="color: #65a30d;">{report.conflicts_by_severity['low']}</h2>
                        </div>
                    </div>
                    
                    <h2>🔍 Detailed Conflicts</h2>
                    {conflicts_html or "<p>✅ No conflicts detected!</p>"}
                    
                    <div class="recommendations">
                        <h2>💡 Recommendations</h2>
                        <ul>{recommendations_html}</ul>
                    </div>
                    
                    <h2>🛠️ Next Steps</h2>
                    <ol>
                        <li>Use MANAGE_RULES.md to resolve conflicts</li>
                        <li>Re-run conflict detection to verify fixes</li>
                        <li>Update documentation standards to prevent future conflicts</li>
                    </ol>
                </div>
            </div>
        </body>
        </html>
        """

def main():
    """Main entry point for the conflict detector"""
    parser = argparse.ArgumentParser(
        description='📊 AI Documentation Framework - Conflict Detection System'
    )
    
    parser.add_argument('--rules-only', action='store_true',
                      help='Check only AI_RULES conflicts')
    parser.add_argument('--docs-only', action='store_true',
                      help='Check only documentation conflicts')
    parser.add_argument('--app', type=str,
                      help='Check specific application only')
    parser.add_argument('--output', type=str, default='console',
                      choices=['console', 'json', 'html'],
                      help='Output format (default: console)')
    parser.add_argument('--config', type=str,
                      help='Path to ai-doc-config.json')
    parser.add_argument('--severity', type=str, default='medium',
                      choices=['low', 'medium', 'high', 'critical'],
                      help='Minimum severity level (default: medium)')
    parser.add_argument('--output-file', type=str,
                      help='Output file path (for json/html formats)')
    
    args = parser.parse_args()
    
    try:
        print("🔍 Starting AI Documentation Conflict Detection...")
        
        # Initialize detector
        detector = AIDocConflictDetector(
            project_root=".",
            config_path=args.config
        )
        
        # Run detection
        report = detector.detect_all_conflicts(
            rules_only=args.rules_only,
            docs_only=args.docs_only
        )
        
        # Filter by severity
        severity_levels = {'low': 1, 'medium': 2, 'high': 3, 'critical': 4}
        min_severity_level = severity_levels[args.severity]
        
        filtered_conflicts = [
            c for c in report.conflicts 
            if severity_levels[c.severity] >= min_severity_level
        ]
        
        # Update report with filtered conflicts
        report.conflicts = filtered_conflicts
        report.total_conflicts = len(filtered_conflicts)
        
        # Recalculate statistics
        conflicts_by_severity = {'low': 0, 'medium': 0, 'high': 0, 'critical': 0}
        conflicts_by_category = {}
        
        for conflict in filtered_conflicts:
            conflicts_by_severity[conflict.severity] += 1
            if conflict.category not in conflicts_by_category:
                conflicts_by_category[conflict.category] = 0
            conflicts_by_category[conflict.category] += 1
            
        report.conflicts_by_severity = conflicts_by_severity
        report.conflicts_by_category = conflicts_by_category
        
        # Export report
        detector.export_report(report, args.output, args.output_file)
        
        # Exit with appropriate code
        if any(c.severity in ['critical', 'high'] for c in filtered_conflicts):
            sys.exit(1)  # Exit with error for critical/high conflicts
        else:
            sys.exit(0)  # Success
            
    except Exception as e:
        print(f"❌ Error during conflict detection: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
