# 📋 CREATE ISSUE DIRECTORIES - {{ project_name }} Project
> **AI Protocol for Issue Management System Setup**

## 🎯 AI INSTRUCTIONS - READ THIS FIRST

**Purpose**: This file provides the AI with a complete protocol for creating the issue management directory structure for any application or project root.

## 🧠 AI PROTOCOL FOR ISSUE DIRECTORY CREATION

### Step 1: Determine Application Type
```python
def determine_app_type(app_path):
    """Determine the type of application for proper issue categorization"""
    
    # Check for common application patterns
    if 'website' in app_path.lower():
        return {
            'type': 'website',
            'categories': ['frontend-issues', 'backend-issues', 'django-issues', 'database-issues', 'deployment-issues']
        }
    elif 'api' in app_path.lower():
        return {
            'type': 'api',
            'categories': ['api-issues', 'endpoint-issues', 'authentication-issues', 'database-issues', 'deployment-issues']
        }
    elif 'email' in app_path.lower():
        return {
            'type': 'email-server',
            'categories': ['smtp-issues', 'imap-issues', 'delivery-issues', 'authentication-issues', 'configuration-issues']
        }
    elif 'robot' in app_path.lower():
        return {
            'type': 'robot-control',
            'categories': ['control-issues', 'safety-issues', 'hardware-issues', 'communication-issues', 'calibration-issues']
        }
    else:
        return {
            'type': 'generic',
            'categories': ['general-issues', 'system-issues', 'configuration-issues', 'deployment-issues']
        }
```

### Step 2: Create Issue Directory Structure
```python
def create_issue_directories(app_path, app_type):
    """Create the complete issue management directory structure"""
    
    # Base directories
    base_dirs = [
        f"{app_path}/issues",
        f"{app_path}/issues/open",
        f"{app_path}/issues/closed",
        f"{app_path}/issues/version-history",
        f"{app_path}/issues/ai-session-logs"
    ]
    
    # Create base directories
    for directory in base_dirs:
        create_directory(directory)
    
    # Create open issue subdirectories
    open_subdirs = [
        f"{app_path}/issues/open/incomplete-tasks",
        f"{app_path}/issues/open/unresolved-errors",
        f"{app_path}/issues/open/system-issues"
    ]
    
    # Add app-specific categories
    for category in app_type['categories']:
        open_subdirs.append(f"{app_path}/issues/open/{category}")
    
    # Create open subdirectories
    for directory in open_subdirs:
        create_directory(directory)
    
    # Create closed issue subdirectories (mirror open structure)
    closed_subdirs = [
        f"{app_path}/issues/closed/incomplete-tasks",
        f"{app_path}/issues/closed/unresolved-errors",
        f"{app_path}/issues/closed/system-issues"
    ]
    
    # Add app-specific categories to closed
    for category in app_type['categories']:
        closed_subdirs.append(f"{app_path}/issues/closed/{category}")
    
    # Create closed subdirectories
    for directory in closed_subdirs:
        create_directory(directory)
    
    return {
        'base_dirs_created': base_dirs,
        'open_subdirs_created': open_subdirs,
        'closed_subdirs_created': closed_subdirs,
        'total_directories': len(base_dirs) + len(open_subdirs) + len(closed_subdirs)
    }
```

### Step 3: Create Issue Templates
```python
def create_issue_templates(app_path, app_type):
    """Create issue templates for different categories"""
    
    templates = {
        'incomplete-task': create_incomplete_task_template(),
        'error': create_error_template(),
        'system-issue': create_system_issue_template()
    }
    
    # Create app-specific templates
    for category in app_type['categories']:
        templates[category] = create_app_specific_template(category)
    
    # Save templates to appropriate directories
    for template_name, template_content in templates.items():
        template_path = f"{app_path}/issues/templates/{template_name}_template.md"
        create_directory(f"{app_path}/issues/templates")
        write_file(template_path, template_content)
    
    return templates
```

### Step 4: Create Issue Tracker
```python
def create_issue_tracker(app_path, app_type):
    """Create the main issue tracker dashboard"""
    
    tracker_content = f"""# 📊 ISSUE TRACKER - {{ project_name }} {{ app_type['type'].title() }}
> **Issue Management Dashboard | {{ app_type['type'].title() }} Application**

## 📈 SUMMARY

### Open Issues
| Category | Count | Priority | Status |
|----------|-------|----------|--------|
| Incomplete Tasks | 0 | - | - |
| Unresolved Errors | 0 | - | - |
| System Issues | 0 | - | - |
{% for category in app_type['categories'] %}
| {{ category.replace('-', ' ').title() }} | 0 | - | - |
{% endfor %}

### Recent Activity
- No recent activity

## 🚀 QUICK ACTIONS

### Create New Issue
- [Create Incomplete Task](issues/open/incomplete-tasks/)
- [Log Unresolved Error](issues/open/unresolved-errors/)
- [Report System Issue](issues/open/system-issues/)
{% for category in app_type['categories'] %}
- [Report {{ category.replace('-', ' ').title() }}](issues/open/{{ category }}/)
{% endfor %}

### View Issues
- [View All Open Issues](issues/open/)
- [View Closed Issues](issues/closed/)
- [View Version History](issues/version-history/)
- [View AI Session Logs](issues/ai-session-logs/)

## 📊 PERFORMANCE METRICS

### Issue Resolution Stats
- **Total Issues Created**: 0
- **Issues Resolved**: 0
- **Resolution Rate**: 0%
- **Average Resolution Time**: N/A

### AI Session Stats
- **Total AI Sessions**: 0
- **Successful Resolutions**: 0
- **Failed Attempts**: 0
- **Success Rate**: 0%

## 🔧 {{ app_type['type'].title() }} SPECIFIC CATEGORIES

{% for category in app_type['categories'] %}
### {{ category.replace('-', ' ').title() }}
- **Description**: {{ category.replace('-', ' ').title() }} related issues
- **Common Causes**: To be documented
- **Resolution Patterns**: To be documented
- **Prevention Strategies**: To be documented

{% endfor %}

---

**🔄 Last Updated**: {{ current_date }} | **{{ app_type['type'].title() }} Issues**: Active | **Status**: Operational

**📍 File Location**: `{app_path}/issues/ISSUE_TRACKER.md`
"""
    
    tracker_path = f"{app_path}/issues/ISSUE_TRACKER.md"
    write_file(tracker_path, tracker_content)
    
    return tracker_path
```

### Step 5: Execute Complete Setup
```python
def execute_issue_directory_creation(app_path):
    """Execute the complete issue directory creation process"""
    
    # Step 1: Determine app type
    app_type = determine_app_type(app_path)
    
    # Step 2: Create directory structure
    dir_structure = create_issue_directories(app_path, app_type)
    
    # Step 3: Create templates
    templates = create_issue_templates(app_path, app_type)
    
    # Step 4: Create issue tracker
    tracker = create_issue_tracker(app_path, app_type)
    
    # Step 5: Validate setup
    validation = validate_issue_setup(app_path, app_type)
    
    return {
        'app_type': app_type,
        'directory_structure': dir_structure,
        'templates_created': len(templates),
        'tracker_created': tracker,
        'validation': validation,
        'setup_complete': validation['all_directories_exist'] and validation['tracker_exists']
    }
```

## 📁 COMPLETE DIRECTORY STRUCTURE

### Base Structure
```
{app_path}/issues/
├── open/
│   ├── incomplete-tasks/
│   ├── unresolved-errors/
│   ├── system-issues/
│   └── [app-specific-categories]/
├── closed/
│   ├── incomplete-tasks/
│   ├── unresolved-errors/
│   ├── system-issues/
│   └── [app-specific-categories]/
├── version-history/
├── ai-session-logs/
├── templates/
│   ├── incomplete-task_template.md
│   ├── error_template.md
│   ├── system-issue_template.md
│   └── [app-specific-templates].md
└── ISSUE_TRACKER.md
```

### Application-Specific Categories

#### Website Application
- `frontend-issues/`
- `backend-issues/`
- `django-issues/`
- `database-issues/`
- `deployment-issues/`

#### API Applications
- `api-issues/`
- `endpoint-issues/`
- `authentication-issues/`
- `database-issues/`
- `deployment-issues/`

#### Email Server
- `smtp-issues/`
- `imap-issues/`
- `delivery-issues/`
- `authentication-issues/`
- `configuration-issues/`

#### Robot Control
- `control-issues/`
- `safety-issues/`
- `hardware-issues/`
- `communication-issues/`
- `calibration-issues/`

## 📋 ISSUE TEMPLATE STRUCTURE

### Incomplete Task Template
```markdown
---
issue_id: "TASK-[YYYY-MM-DD]-[SEQ]"
type: "incomplete-task"
priority: "[critical|high|medium|low]"
status: "open"
created_date: "[YYYY-MM-DD HH:MM:SS UTC]"
ai_model: "[model-name]"
attempts: [number]
---

# 🚧 Incomplete Task: [Task Title]

## 📝 Task Description
[Detailed description of the incomplete task]

## 🎯 Original Requirements
[Original task requirements and objectives]

## 📊 Progress Made
[What was accomplished before the task became incomplete]

## 🚫 Blocking Issues
[Issues that prevented task completion]

## 🔄 Next Steps
[What needs to be done to complete the task]

## 📚 Related Documentation
[Links to relevant documentation]

## 🏷️ Tags
[tags, for, categorization]
```

### Error Template
```markdown
---
issue_id: "ERROR-[YYYY-MM-DD]-[SEQ]"
type: "error"
category: "[error-category]"
severity: "[critical|high|medium|low]"
status: "open"
created_date: "[YYYY-MM-DD HH:MM:SS UTC]"
ai_model: "[model-name]"
attempts: [number]
---

# ❌ Error: [Error Title]

## 🐛 Error Description
[Detailed description of the error]

## 🔍 Error Details
- **Error Type**: [Type of error]
- **Error Code**: [Error code if applicable]
- **Location**: [Where the error occurred]
- **Context**: [Context in which error occurred]

## 🚫 Impact
[Impact of the error on the system]

## 🔧 Attempted Solutions
[List of solutions already attempted]

## 💡 Proposed Solutions
[Potential solutions to try]

## 📚 Related Documentation
[Links to relevant error documentation]

## 🏷️ Tags
[tags, for, categorization]
```

## 🚀 USAGE INSTRUCTIONS

### For AI
1. **Read this file** when setting up issue management for a new application
2. **Execute the protocol** using the provided Python functions
3. **Validate the setup** to ensure all directories and files are created
4. **Update the tracker** with initial information

### For Users
1. **Run the setup** by providing this file to AI
2. **Customize categories** if needed for your specific application
3. **Verify the structure** matches your requirements
4. **Start using** the issue management system

---

**🔄 Last Updated**: {{ current_date }} | **{{ project_name }} Issue Management**: Setup Protocol | **Status**: Ready

**📍 File Location**: `{{ project_root }}/CREATE_ISSUE_DIRECTORIES.md`
