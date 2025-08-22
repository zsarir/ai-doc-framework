#!/usr/bin/env python3
"""
AI Documentation Framework Setup Wizard
Interactive setup tool for configuring the AI Documentation Framework
"""

import os
import sys
import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional
import click
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init(autoreset=True)

class SetupWizard:
    def __init__(self):
        self.config = {}
        self.project_root = Path.cwd()
        self.framework_root = Path(__file__).parent.parent
        
    def print_banner(self):
        """Display the setup wizard banner"""
        banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║                    🤖 AI Documentation Framework                    ║
║                        Setup Wizard v1.0.0                         ║
╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
        """
        print(banner)
    
    def get_project_info(self):
        """Get basic project information"""
        print(f"{Fore.YELLOW}📋 Project Information{Style.RESET_ALL}")
        print("=" * 50)
        
        self.config['project'] = {
            'name': click.prompt("Project name", default="my-project"),
            'type': click.prompt(
                "Project type",
                type=click.Choice(['single', 'multi', 'custom']),
                default='multi'
            ),
            'description': click.prompt("Project description", default=""),
            'root_path': str(self.project_root)
        }
    
    def get_applications(self):
        """Get application information"""
        print(f"\n{Fore.YELLOW}🏗️  Applications Configuration{Style.RESET_ALL}")
        print("=" * 50)
        
        if self.config['project']['type'] == 'single':
            self.config['applications'] = [{
                'name': click.prompt("Application name", default="app"),
                'type': click.prompt(
                    "Application type",
                    type=click.Choice(['frontend', 'backend', 'fullstack', 'mobile', 'desktop']),
                    default='fullstack'
                ),
                'framework': click.prompt("Framework", default="generic"),
                'description': click.prompt("Application description", default="")
            }]
        else:
            apps = []
            while True:
                app_name = click.prompt("Application name (or 'done' to finish)", default="done")
                if app_name.lower() == 'done':
                    break
                
                app = {
                    'name': app_name,
                    'type': click.prompt(
                        f"Type for {app_name}",
                        type=click.Choice(['frontend', 'backend', 'fullstack', 'mobile', 'desktop']),
                        default='backend'
                    ),
                    'framework': click.prompt(f"Framework for {app_name}", default="generic"),
                    'description': click.prompt(f"Description for {app_name}", default="")
                }
                apps.append(app)
            
            self.config['applications'] = apps
    
    def get_error_categories(self):
        """Get error management categories"""
        print(f"\n{Fore.YELLOW}🚨 Error Management Categories{Style.RESET_ALL}")
        print("=" * 50)
        
        default_categories = ['backend', 'frontend', 'infrastructure', 'security', 'performance']
        categories = click.prompt(
            "Error categories (comma-separated)",
            default=",".join(default_categories)
        )
        
        self.config['error_categories'] = [cat.strip() for cat in categories.split(',')]
    
    def get_issue_categories(self):
        """Get issue tracking categories"""
        print(f"\n{Fore.YELLOW}📋 Issue Tracking Categories{Style.RESET_ALL}")
        print("=" * 50)
        
        default_categories = ['incomplete-tasks', 'unresolved-errors', 'system-issues']
        categories = click.prompt(
            "Issue categories (comma-separated)",
            default=",".join(default_categories)
        )
        
        self.config['issue_categories'] = [cat.strip() for cat in categories.split(',')]
    
    def get_advanced_options(self):
        """Get advanced configuration options"""
        print(f"\n{Fore.YELLOW}⚙️  Advanced Options{Style.RESET_ALL}")
        print("=" * 50)
        
        self.config['advanced'] = {
            'language': click.prompt("Documentation language", default="en"),
            'theme': click.prompt("Documentation theme", default="default"),
            'auto_backup': click.confirm("Enable automatic backups", default=True),
            'debug_mode': click.confirm("Enable debug mode", default=False)
        }
    
    def create_directory_structure(self):
        """Create the directory structure"""
        print(f"\n{Fore.YELLOW}📁 Creating Directory Structure{Style.RESET_ALL}")
        print("=" * 50)
        
        # Create main directories
        directories = [
            'docs',
            'error-management',
            'issues',
            'issues/open',
            'issues/closed',
            'issues/version-history',
            'issues/ai-session-logs'
        ]
        
        for directory in directories:
            dir_path = self.project_root / directory
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"✅ Created: {directory}")
        
        # Create error management categories
        for category in self.config['error_categories']:
            error_dir = self.project_root / 'error-management' / category
            error_dir.mkdir(parents=True, exist_ok=True)
            print(f"✅ Created: error-management/{category}")
        
        # Create issue categories
        for category in self.config['issue_categories']:
            open_dir = self.project_root / 'issues' / 'open' / category
            closed_dir = self.project_root / 'issues' / 'closed' / category
            open_dir.mkdir(parents=True, exist_ok=True)
            closed_dir.mkdir(parents=True, exist_ok=True)
            print(f"✅ Created: issues/open/{category}")
            print(f"✅ Created: issues/closed/{category}")
        
        # Create application directories
        for app in self.config['applications']:
            app_dir = self.project_root / app['name']
            app_dirs = [
                app_dir,
                app_dir / 'docs',
                app_dir / 'error-management',
                app_dir / 'issues'
            ]
            
            for directory in app_dirs:
                directory.mkdir(parents=True, exist_ok=True)
            
            print(f"✅ Created: {app['name']}/")
    
    def copy_templates(self):
        """Copy template files"""
        print(f"\n{Fore.YELLOW}📄 Copying Template Files{Style.RESET_ALL}")
        print("=" * 50)
        
        templates_dir = self.framework_root / 'templates'
        
        # Copy core files
        core_files = templates_dir / 'core-files'
        if core_files.exists():
            for file in core_files.glob('*.md'):
                shutil.copy2(file, self.project_root)
                print(f"✅ Copied: {file.name}")
        
        # Copy documentation templates
        docs_templates = templates_dir / 'documentation'
        if docs_templates.exists():
            for file in docs_templates.glob('*.md'):
                shutil.copy2(file, self.project_root / 'docs')
                print(f"✅ Copied: docs/{file.name}")
        
        # Copy error management templates
        error_templates = templates_dir / 'error-management'
        if error_templates.exists():
            for file in error_templates.glob('*.md'):
                shutil.copy2(file, self.project_root / 'error-management')
                print(f"✅ Copied: error-management/{file.name}")
        
        # Copy issue management templates
        issue_templates = templates_dir / 'issue-management'
        if issue_templates.exists():
            for file in issue_templates.glob('*.md'):
                shutil.copy2(file, self.project_root / 'issues')
                print(f"✅ Copied: issues/{file.name}")
    
    def generate_app_specific_files(self):
        """Generate application-specific files"""
        print(f"\n{Fore.YELLOW}🏗️  Generating Application-Specific Files{Style.RESET_ALL}")
        print("=" * 50)
        
        for app in self.config['applications']:
            app_dir = self.project_root / app['name']
            
            # Generate AI_RULES.md for each app
            self.generate_ai_rules(app, app_dir)
            
            # Generate START_TASK.md for each app
            self.generate_start_task(app, app_dir)
            
            # Generate COMPLETE_TASK.md for each app
            self.generate_complete_task(app, app_dir)
            
            # Generate CREATE_ISSUE_DIRECTORIES.md for each app
            self.generate_issue_directories(app, app_dir)
            
            print(f"✅ Generated files for: {app['name']}")
    
    def generate_ai_rules(self, app: Dict, app_dir: Path):
        """Generate AI_RULES.md for an application"""
        content = f"""# 🤖 AI RULES - {app['name'].title()} Application
> **{app['type'].title()} Development & Management Rules | {app['framework'].title()} System**

## 🎯 AI INSTRUCTIONS - READ AND FOLLOW THESE RULES

**This file contains CRITICAL rules for AI when working on {app['name']} tasks. These rules MUST be followed exactly.**

## 🔒 CRITICAL SYSTEM RULES - {app['name'].upper()}

### Rule #1: File Creation Priority
```python
# MANDATORY: Check for existing files before creating new ones
def prevent_duplicate_file_creation(new_file_path):
    existing_similar = find_similar_files(new_file_path)
    if existing_similar:
        return "ERROR: Must edit existing file, never create duplicates"
    return "OK: Safe to create"
```

### Rule #2: System Validation
```python
# MANDATORY: Validate system integrity before any task
def validate_{app['name']}_system_integrity():
    critical_files = ['config.py', 'main.py', 'requirements.txt']
    
    for critical_file in critical_files:
        if not exists(critical_file):
            return f"STOP: Missing critical {app['name']} file: {{critical_file}}"
    
    return "{app['name'].upper()}_SYSTEM_VALIDATED: Safe to proceed"
```

## 📋 {app['name'].upper()} COMPLIANCE CHECKLIST

### Before Any Task
```bash
✅ {app['name']} services status verified
✅ Configuration backups created
✅ Security settings validated
✅ Database connectivity verified
✅ Log rotation configured
✅ Monitoring alerts active
```

### After Any Changes
```bash
✅ {app['name']} services tested
✅ Authentication verified
✅ Functionality confirmed
✅ Security posture maintained
✅ Documentation updated
✅ Backup integrity verified
```

---

**🔄 Last Updated**: {self.get_current_date()} | **{app['name'].title()} Rules**: Active | **Compliance**: Mandatory

**📍 File Location**: `{app_dir}/AI_RULES.md`
"""
        
        with open(app_dir / 'AI_RULES.md', 'w') as f:
            f.write(content)
    
    def generate_start_task(self, app: Dict, app_dir: Path):
        """Generate START_TASK.md for an application"""
        content = f"""# 🚀 START TASK - {app['name'].title()} Application
> **AI Auto-Navigation Protocol | {app['framework'].title()} {app['type'].title()} Tasks**

## 🎯 AI INSTRUCTIONS - READ THIS FIRST

**When to use this file**: 
- Tasks mentioning ONLY "{app['name']}" or "{app['name']} application"
- {app['type']} development tasks
- {app['framework']} configuration tasks
- {app['name']}-only deployment/troubleshooting

## 🧠 AI AUTO-EXECUTION PROTOCOL

### Step 1: Task Analysis & Validation
```python
# AI automatically validates {app['name']} task requirements
def analyze_{app['name']}_task(task_description):
    {app['name']}_task_patterns = [
        '{app['name']}', '{app['framework']}', '{app['type']}',
        'development', 'configuration', 'deployment'
    ]
    
    # Determine if this is truly a {app['name']} task
    if not any(pattern in task_description.lower() for pattern in {app['name']}_task_patterns):
        return redirect_to_appropriate_app(task_description)
    
    return {{
        'app': '{app['name']}',
        'type': '{app['type']}',
        'framework': '{app['framework']}',
        'complexity': determine_complexity(task_description)
    }}
```

### Step 2: Read {app['name'].title()} Rules (MANDATORY)
```python
# AI MUST read {app['name']} rules before proceeding
def read_{app['name']}_rules():
    rules_content = read_file("{app_dir}/AI_RULES.md")
    
    # Extract critical rules
    critical_rules = extract_critical_rules(rules_content)
    
    return {{
        'rules': critical_rules,
        'compliance_check': validate_rules_understanding(critical_rules)
    }}
```

### Step 3: Navigate {app['name'].title()} Documentation
```python
# AI uses {app['name']} app guide for efficient navigation
def navigate_{app['name']}_documentation(task_requirements):
    # Read the main navigation guide
    app_guide = read_file("{app_dir}/docs/AI_APP_GUIDE.md")
    
    # Determine required documentation based on task
    required_docs = determine_required_{app['name']}_docs(task_requirements)
    
    # Read only the necessary documentation
    documentation = {{}}
    for doc_type in required_docs:
        doc_path = get_{app['name']}_doc_path(doc_type)
        documentation[doc_type] = read_file(doc_path)
    
    return documentation
```

## 📋 AI EXECUTION CHECKLIST

### Pre-Task Checklist
```bash
✅ VALIDATE {app['name'].upper()} SYSTEM INTEGRITY
✅ READ {app['name'].upper()} RULES (mandatory compliance)
✅ VERIFY {app['name'].upper()} SERVICE STATUS
✅ LOAD REQUIRED DOCUMENTATION
✅ SEARCH ERROR HISTORY
✅ CONFIRM BACKUP REQUIREMENTS
```

### Post-Task Checklist  
```bash
✅ TEST ALL {app['name'].upper()} SERVICES
✅ VALIDATE FUNCTIONALITY
✅ VERIFY SECURITY POSTURE
✅ BACKUP UPDATED CONFIGURATIONS
✅ UPDATE DOCUMENTATION
```

---

**🚀 {app['name'].upper()} TASK EXECUTION**: Ready for Production

**🔄 Last Updated**: {self.get_current_date()} | **{app['name'].title()} Tasks**: {app['framework']} | **Status**: Active

**📍 File Location**: `{app_dir}/START_TASK.md`
"""
        
        with open(app_dir / 'START_TASK.md', 'w') as f:
            f.write(content)
    
    def generate_complete_task(self, app: Dict, app_dir: Path):
        """Generate COMPLETE_TASK.md for an application"""
        content = f"""# ✅ COMPLETE TASK - {app['name'].title()} Application
> **AI Auto-Update Protocol | {app['name'].title()} Post-Task Maintenance**

## 🎯 AI INSTRUCTIONS - EXECUTE THIS AFTER {app['name'].upper()} TASKS

**When to use this file**: 
- After completing {app['name']}-only tasks
- For automatic {app['name']} documentation updates
- For {app['name']} error management updates
- For {app['name']} version control maintenance

## 🤖 AI AUTO-UPDATE PROTOCOL

### Step 1: {app['name'].title()} Task Analysis & Issue Assessment
```python
# AI automatically analyzes {app['name']} changes and checks for issues
def analyze_completed_{app['name']}_task():
    # Analyze {app['name']} specific changes
    {app['name']}_changes = {{
        'configuration': detect_{app['name']}_configuration_changes(),
        'code': detect_{app['name']}_code_changes(),
        'dependencies': detect_{app['name']}_dependency_changes(),
        'documentation': detect_{app['name']}_documentation_changes()
    }}
    
    # Check {app['name']} specific errors
    {app['name']}_errors = {{
        'runtime_errors': extract_{app['name']}_runtime_errors(),
        'configuration_errors': extract_{app['name']}_config_errors(),
        'dependency_errors': extract_{app['name']}_dependency_errors()
    }}
    
    return {{
        'app': '{app['name']}',
        'changes': {app['name']}_changes,
        'errors': {app['name']}_errors,
        'services_affected': ['{app['name']}']
    }}
```

### Step 2: {app['name'].title()} System Validation
```python
# AI validates {app['name']} integrity after task completion
def validate_{app['name']}_system_post_task():
    {app['name']}_validation = {{
        'service_status': test_{app['name']}_service(),
        'configuration': validate_{app['name']}_config(),
        'functionality': test_{app['name']}_functionality(),
        'security': validate_{app['name']}_security()
    }}
    
    # Calculate {app['name']} system health score
    health_score = calculate_{app['name']}_health_score({app['name']}_validation)
    
    if health_score < 95:
        return {{
            'status': '{app['name'].upper()}_SYSTEM_DEGRADED',
            'action': 'ALERT_USER_AND_FIX',
            'health_score': health_score
        }}
    
    return {{'status': '{app['name'].upper()}_SYSTEM_VALIDATED', 'health_score': health_score}}
```

### Step 3: {app['name'].title()} Cleanup and Debug Code Management (MANDATORY)
```python
# AI automatically cleans up {app['name']} temporary files and debug code
def cleanup_{app['name']}_and_manage_debug_code({app['name']}_analysis):
    # Only cleanup if {app['name']} task completed successfully
    if {app['name']}_analysis.task_completion.status != 'complete':
        return "{app['name'].upper()}_TASK_INCOMPLETE: Skipping cleanup until task completion"
    
    {app['name']}_cleanup_results = {{
        'temp_files_removed': [],
        'debug_code_commented': [],
        'test_files_removed': [],
        'logs_cleaned': []
    }}
    
    app_path = "{app_dir}"
    
    # Clean up {app['name']}-specific temporary files
    {app['name']}_temp_files = find_{app['name']}_temporary_files(app_path)
    for temp_file in {app['name']}_temp_files:
        if is_safe_to_remove(temp_file):
            remove_file(temp_file)
            {app['name']}_cleanup_results['temp_files_removed'].append(temp_file)
    
    # Comment out debug code in {app['name']} source files
    {app['name']}_source_files = find_{app['name']}_source_files_with_debug_code(app_path)
    for source_file in {app['name']}_source_files:
        commented_lines = comment_{app['name']}_debug_code(source_file)
        if commented_lines:
            {app['name']}_cleanup_results['debug_code_commented'].append({{
                'file': source_file,
                'lines_commented': commented_lines
            }})
    
    return {app['name']}_cleanup_results
```

## 📋 {app['name'].upper()} SUCCESS INDICATORS

### {app['name'].title()} Task Completion Checklist
```bash
✅ Post-task {app['name']} system validation completed (95%+ health score)
✅ {app['name'].title()} service functionality tested and working
✅ NO duplicate files created, existing files edited properly
✅ {app['name'].title()} rules compliance validated
✅ {app['name'].title()} documentation updated
✅ Error management updated (resolved errors documented)
✅ Issue management updated (incomplete tasks/errors logged)
✅ Version numbers incremented correctly
✅ Temporary/test/debug files cleaned up and removed
✅ Debug code commented out in source files
✅ System left in clean, production-ready state
```

---

**✅ {app['name'].upper()} COMPLETION STATUS**: Production Ready

**🔄 Last Updated**: {self.get_current_date()} | **Application**: {app['name'].title()} | **Type**: Single App Completion

**📍 File Location**: `{app_dir}/COMPLETE_TASK.md`
"""
        
        with open(app_dir / 'COMPLETE_TASK.md', 'w') as f:
            f.write(content)
    
    def generate_issue_directories(self, app: Dict, app_dir: Path):
        """Generate CREATE_ISSUE_DIRECTORIES.md for an application"""
        content = f"""# 🏗️ CREATE ISSUE DIRECTORIES - {app['name'].title()} Application
> **Initialize {app['name'].title()} Issue Management System**

## 🎯 AI INSTRUCTIONS - {app['name'].upper()} ISSUE DIRECTORY CREATION

**Purpose**: Create the complete issue management directory structure specifically for the {app['name']} application.

**When to use**: Before using {app['name']} issue management system or when setting up issue tracking for {app['name']} tasks.

## 🧠 AI {app['name'].upper()} ISSUE DIRECTORY CREATION PROTOCOL

### Step 1: {app['name'].title()} Application Validation
```python
# AI validates this is being run for {app['name']} application
def validate_{app['name']}_application():
    app_path = "{app_dir}"
    app_type = "{app['type']}"
    
    # Verify {app['name']}-specific files exist
    required_files = [
        f"{{app_path}}/AI_RULES.md",
        f"{{app_path}}/START_TASK.md",
        f"{{app_path}}/COMPLETE_TASK.md",
        f"{{app_path}}/docs/AI_APP_GUIDE.md"
    ]
    
    return all(file_exists(f) for f in required_files)
```

### Step 2: Create {app['name'].title()} Issue Directory Structure
```python
# AI creates complete {app['name']} issue management structure
def create_{app['name']}_issue_directories():
    app_path = "{app_dir}"
    
    # {app['name']}-specific issue directories
    directories_to_create = [
        f"{{app_path}}/issues/",
        f"{{app_path}}/issues/open/",
        f"{{app_path}}/issues/open/incomplete-tasks/",
        f"{{app_path}}/issues/open/unresolved-errors/",
        f"{{app_path}}/issues/open/system-issues/",
        f"{{app_path}}/issues/closed/",
        f"{{app_path}}/issues/closed/incomplete-tasks/",
        f"{{app_path}}/issues/closed/unresolved-errors/",
        f"{{app_path}}/issues/closed/system-issues/",
        f"{{app_path}}/issues/version-history/",
        f"{{app_path}}/issues/ai-session-logs/"
    ]
    
    # Create all directories
    for directory in directories_to_create:
        create_directory_if_not_exists(directory)
```

## 📁 Complete {app['name'].title()} Issue Directory Structure

```bash
{app_dir}/issues/
├── ISSUE_TRACKER.md                           # {app['name']} dashboard
├── open/                                      # Active {app['name']} issues
│   ├── incomplete-tasks/
│   │   ├── template.md                        # {app['name']} task template
│   │   └── [{app['name'].upper()}-TASK-YYYY-MM-DD-###.md]    # Individual {app['name']} tasks
│   ├── unresolved-errors/
│   │   ├── template.md                        # {app['name']} error template
│   │   └── [{app['name'].upper()}-ERROR-YYYY-MM-DD-###.md]   # Individual {app['name']} errors
│   └── system-issues/
│       ├── template.md                        # {app['name']} system template
│       └── [{app['name'].upper()}-SYSTEM-YYYY-MM-DD-###.md]  # Individual system issues
├── closed/                                    # Resolved {app['name']} issues
│   ├── incomplete-tasks/                      # Completed {app['name']} tasks
│   ├── unresolved-errors/                     # Resolved {app['name']} errors
│   ├── system-issues/                         # Fixed {app['name']} system issues
│   └── RESOLUTION_ARCHIVE.md                  # {app['name']} resolution archive
├── version-history/
│   ├── V1.0.0-{app['name']}-initial-setup.md # {app['name']} version history
│   └── VERSION.md                             # Current {app['name']} version
└── ai-session-logs/
    ├── [YYYY-MM-DD-model-session-###.md]     # {app['name']} AI session logs
    └── SESSION_INDEX.md                       # {app['name']} session index
```

## 🚀 {app['name'].title()} Issue Management Commands

### Initialize {app['name'].title()} Issues
```bash
# Pattern: "Initialize {app['name']} issues"
"Initialize issues for: {app_dir}"
```

### Create {app['name'].title()}-Specific Issue
```bash  
# Pattern: "Create [type] issue for {app['name']}: [description]"
Examples:
✅ "Create system issue for {app['name']}: Service startup failing"
✅ "Create error issue for {app['name']}: Database connection timeout"
✅ "Create task issue for {app['name']}: Configuration update incomplete"
```

---

**🔄 Last Updated**: {self.get_current_date()} | **{app['name'].title()} Issues**: Ready | **Integration**: Complete
"""
        
        with open(app_dir / 'CREATE_ISSUE_DIRECTORIES.md', 'w') as f:
            f.write(content)
    
    def get_current_date(self) -> str:
        """Get current date in YYYY-MM-DD format"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d")
    
    def save_configuration(self):
        """Save configuration to file"""
        config_file = self.project_root / 'ai-doc-config.json'

        # Validate file location (must be in project root)
        if str(config_file.parent) != str(self.project_root):
            print(f"\n{Fore.RED}❌ ERROR: ai-doc-config.json must be saved in project root!{Style.RESET_ALL}")
            print(f"   Expected: {self.project_root}/ai-doc-config.json")
            print(f"   Attempted: {config_file}")
            return False

        with open(config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

        print(f"\n{Fore.GREEN}✅ Configuration saved to: {config_file}{Style.RESET_ALL}")
        print(f"   {Fore.BLUE}📍 File Location: Project Root (CORRECT){Style.RESET_ALL}")
        return True
    
    def run(self):
        """Run the complete setup wizard"""
        self.print_banner()
        
        try:
            # Get project information
            self.get_project_info()
            
            # Get applications
            self.get_applications()
            
            # Get error categories
            self.get_error_categories()
            
            # Get issue categories
            self.get_issue_categories()
            
            # Get advanced options
            self.get_advanced_options()
            
            # Create directory structure
            self.create_directory_structure()
            
            # Copy templates
            self.copy_templates()
            
            # Generate app-specific files
            self.generate_app_specific_files()
            
            # Save configuration
            config_saved = self.save_configuration()
            if not config_saved:
                print(f"\n{Fore.RED}❌ Setup failed: Configuration could not be saved{Style.RESET_ALL}")
                return

            # Success message
            print(f"\n{Fore.GREEN}🎉 Setup Complete!{Style.RESET_ALL}")
            print("=" * 50)
            print(f"✅ AI Documentation Framework installed successfully")
            print(f"✅ Project: {self.config['project']['name']}")
            print(f"✅ Type: {self.config['project']['type']}")
            print(f"✅ Applications: {len(self.config['applications'])}")
            print(f"✅ Error Categories: {len(self.config['error_categories'])}")
            print(f"✅ Issue Categories: {len(self.config['issue_categories'])}")
            print(f"✅ Configuration: {self.project_root}/ai-doc-config.json (Project Root)")
            print(f"✅ Conflict Detection: Available via tools/conflict-detector.py")
            print(f"✅ Rule Management: MANAGE_RULES.md system ready")
            print(f"\n📚 Next Steps:")
            print(f"   1. Review the generated files")
            print(f"   2. Verify ai-doc-config.json is in project root")
            print(f"   3. Customize AI_RULES.md for your specific needs")
            print(f"   4. Start using START_TASK.md for AI tasks")
            print(f"   5. Run conflict detection: python tools/conflict-detector.py")
            print(f"   6. Use MANAGE_RULES.md for rule management")
            print(f"   7. Check USAGE.md for detailed instructions")
            
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}⚠️  Setup cancelled by user{Style.RESET_ALL}")
            sys.exit(1)
        except Exception as e:
            print(f"\n{Fore.RED}❌ Setup failed: {e}{Style.RESET_ALL}")
            sys.exit(1)

@click.command()
@click.option('--debug', is_flag=True, help='Enable debug mode')
@click.option('--config', type=click.Path(exists=True), help='Use existing configuration file')
def main(debug: bool, config: Optional[str]):
    """AI Documentation Framework Setup Wizard"""
    
    if debug:
        os.environ['AI_DOC_FRAMEWORK_DEBUG'] = '1'
    
    wizard = SetupWizard()
    
    if config:
        # Load existing configuration
        with open(config, 'r') as f:
            wizard.config = json.load(f)
        print(f"{Fore.BLUE}📋 Loaded configuration from: {config}{Style.RESET_ALL}")
    
    wizard.run()

if __name__ == '__main__':
    main()
