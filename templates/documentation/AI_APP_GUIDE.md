# 🧠 AI APP GUIDE - {{ project_name }} Project
> **AI Navigation & Documentation Guide | {{ project_type.title() }} System**

## 🎯 AI INSTRUCTIONS - READ THIS FIRST

**Purpose**: This file serves as the primary navigation guide for AI when working on {{ project_name }}. It provides efficient paths to relevant documentation based on task requirements.

## 📚 DOCUMENTATION HIERARCHY

### Project Root Documentation
- **[AI_RULES.md](AI_RULES.md)** - Critical project rules and constraints
- **[START_TASK.md](START_TASK.md)** - Multi-application task execution protocol
- **[COMPLETE_TASK.md](COMPLETE_TASK.md)** - Task completion and update protocol
- **[CREATE_ISSUE_DIRECTORIES.md](CREATE_ISSUE_DIRECTORIES.md)** - Issue management setup

### Application-Specific Documentation
{% for app in applications %}
#### {{ app.name.title() }} Application
- **[{{ app.name }}/AI_RULES.md]({{ app.name }}/AI_RULES.md)** - {{ app.name }} specific rules
- **[{{ app.name }}/START_TASK.md]({{ app.name }}/START_TASK.md)** - {{ app.name }} task execution
- **[{{ app.name }}/COMPLETE_TASK.md]({{ app.name }}/COMPLETE_TASK.md)** - {{ app.name }} task completion
- **[{{ app.name }}/CREATE_ISSUE_DIRECTORIES.md]({{ app.name }}/CREATE_ISSUE_DIRECTORIES.md)** - {{ app.name }} issue management
{% endfor %}

## 🧭 AI NAVIGATION PROTOCOL

### Step 1: Task Analysis
```python
def analyze_task_requirements(task_description):
    """Analyze task to determine required documentation"""
    
    # Determine if multi-application or single-application task
    if is_multi_application_task(task_description):
        return {
            'type': 'multi-application',
            'required_docs': get_multi_app_docs(),
            'start_file': 'START_TASK.md'
        }
    else:
        # Determine which application is involved
        app = identify_application(task_description)
        return {
            'type': 'single-application',
            'application': app,
            'required_docs': get_app_specific_docs(app),
            'start_file': f"{app}/START_TASK.md"
        }
```

### Step 2: Documentation Selection
```python
def select_required_documentation(task_analysis):
    """Select only the documentation needed for the task"""
    
    if task_analysis['type'] == 'multi-application':
        return [
            'AI_RULES.md',
            'START_TASK.md',
            'docs/AI_APP_GUIDE.md',
            'error-management/MASTER_ERROR_INDEX.md'
        ]
    else:
        app = task_analysis['application']
        return [
            f"{app}/AI_RULES.md",
            f"{app}/START_TASK.md",
            f"{app}/docs/AI_APP_GUIDE.md",
            f"{app}/error-management/MASTER_ERROR_INDEX.md"
        ]
```

## 📋 TASK-SPECIFIC DOCUMENTATION PATHS

### Multi-Application Tasks
**Use these paths for tasks involving multiple applications:**

1. **System Integration**: `START_TASK.md` → `docs/INTEGRATION.md` → `docs/DEPLOYMENT.md`
2. **Cross-App Communication**: `START_TASK.md` → `docs/API_DOCUMENTATION.md` → `docs/COMMUNICATION.md`
3. **System-Wide Security**: `START_TASK.md` → `docs/SECURITY.md` → `docs/AUTHENTICATION.md`
4. **Database Coordination**: `START_TASK.md` → `docs/DATABASE.md` → `docs/MIGRATIONS.md`

### Single-Application Tasks
**Use these paths for tasks involving a single application:**

{% for app in applications %}
#### {{ app.name.title() }} Tasks
1. **{{ app.name }} Development**: `{{ app.name }}/START_TASK.md` → `{{ app.name }}/docs/AI_APP_GUIDE.md`
2. **{{ app.name }} Configuration**: `{{ app.name }}/START_TASK.md` → `{{ app.name }}/docs/CONFIGURATION.md`
3. **{{ app.name }} Deployment**: `{{ app.name }}/START_TASK.md` → `{{ app.name }}/docs/DEPLOYMENT.md`
4. **{{ app.name }} Troubleshooting**: `{{ app.name }}/START_TASK.md` → `{{ app.name }}/docs/TROUBLESHOOTING.md`

{% endfor %}

## 🔍 ERROR SEARCH PROTOCOL

### Error Documentation Paths
```python
def get_error_documentation_paths(error_type, application=None):
    """Get paths to relevant error documentation"""
    
    if application:
        # Application-specific error documentation
        return [
            f"{application}/error-management/MASTER_ERROR_INDEX.md",
            f"{application}/error-management/{error_type}/ERROR_INDEX.md"
        ]
    else:
        # Project-wide error documentation
        return [
            'error-management/MASTER_ERROR_INDEX.md',
            f'error-management/{error_type}/ERROR_INDEX.md'
        ]
```

### Error Categories
- **Backend Errors**: `error-management/backend/ERROR_INDEX.md`
- **Frontend Errors**: `error-management/frontend/ERROR_INDEX.md`
- **Infrastructure Errors**: `error-management/infrastructure/ERROR_INDEX.md`
- **Security Errors**: `error-management/security/ERROR_INDEX.md`
- **Database Errors**: `error-management/database/ERROR_INDEX.md`
- **Deployment Errors**: `error-management/deployment/ERROR_INDEX.md`

## 📊 ISSUE MANAGEMENT PATHS

### Issue Documentation Paths
```python
def get_issue_management_paths(application=None):
    """Get paths to issue management documentation"""
    
    if application:
        return [
            f"{application}/issues/ISSUE_TRACKER.md",
            f"{application}/issues/open/",
            f"{application}/issues/closed/"
        ]
    else:
        return [
            'issues/ISSUE_TRACKER.md',
            'issues/open/',
            'issues/closed/'
        ]
```

## 🎯 EFFICIENT DOCUMENTATION READING

### Token Optimization Strategy
```python
def optimize_documentation_reading(task_requirements):
    """Optimize documentation reading to minimize token usage"""
    
    # 1. Read only essential files first
    essential_files = get_essential_files(task_requirements)
    
    # 2. Search for specific information rather than reading entire files
    specific_info = search_for_specific_info(task_requirements)
    
    # 3. Use error history to avoid repeating mistakes
    relevant_errors = search_error_history(task_requirements)
    
    # 4. Check open issues to avoid conflicts
    open_issues = check_open_issues(task_requirements)
    
    return {
        'essential_files': essential_files,
        'specific_info': specific_info,
        'relevant_errors': relevant_errors,
        'open_issues': open_issues
    }
```

## 📁 DOCUMENTATION STRUCTURE

### Project Root Structure
```
{{ project_root }}/
├── AI_RULES.md
├── START_TASK.md
├── COMPLETE_TASK.md
├── CREATE_ISSUE_DIRECTORIES.md
├── docs/
│   ├── AI_APP_GUIDE.md
│   ├── INTEGRATION.md
│   ├── DEPLOYMENT.md
│   ├── SECURITY.md
│   ├── DATABASE.md
│   └── API_DOCUMENTATION.md
├── error-management/
│   ├── MASTER_ERROR_INDEX.md
│   ├── backend/
│   ├── frontend/
│   ├── infrastructure/
│   ├── security/
│   └── database/
└── issues/
    ├── ISSUE_TRACKER.md
    ├── open/
    └── closed/
```

### Application Structure
```
{{ project_root }}/{{ app_name }}/
├── AI_RULES.md
├── START_TASK.md
├── COMPLETE_TASK.md
├── CREATE_ISSUE_DIRECTORIES.md
├── docs/
│   ├── AI_APP_GUIDE.md
│   ├── CONFIGURATION.md
│   ├── DEPLOYMENT.md
│   └── TROUBLESHOOTING.md
├── error-management/
│   ├── MASTER_ERROR_INDEX.md
│   └── [app-specific-categories]/
└── issues/
    ├── ISSUE_TRACKER.md
    ├── open/
    └── closed/
```

## 🚀 QUICK REFERENCE

### Common Task Patterns

#### New Feature Development
1. Read `AI_RULES.md` for constraints
2. Read `START_TASK.md` for execution protocol
3. Read application-specific `AI_APP_GUIDE.md`
4. Search error history for similar features
5. Check open issues for conflicts

#### Bug Fix
1. Read `AI_RULES.md` for constraints
2. Search error documentation for similar bugs
3. Read application-specific troubleshooting docs
4. Check open issues for related problems
5. Follow `COMPLETE_TASK.md` for resolution

#### System Integration
1. Read root `AI_RULES.md` and `START_TASK.md`
2. Read `docs/INTEGRATION.md`
3. Read relevant application documentation
4. Check cross-application error history
5. Follow multi-application completion protocol

#### Deployment
1. Read `AI_RULES.md` for deployment constraints
2. Read `docs/DEPLOYMENT.md`
3. Read application-specific deployment docs
4. Check deployment error history
5. Follow deployment completion protocol

## 📈 PERFORMANCE METRICS

### Documentation Efficiency
- **Average Documentation Read Time**: Optimized for minimal token usage
- **Error Resolution Rate**: Improved through historical error documentation
- **Task Completion Rate**: Enhanced through structured navigation
- **Issue Prevention Rate**: Increased through comprehensive error tracking

---

**🔄 Last Updated**: {{ current_date }} | **{{ project_name }} AI Guide**: Active | **Status**: Operational

**📍 File Location**: `{{ project_root }}/docs/AI_APP_GUIDE.md`
