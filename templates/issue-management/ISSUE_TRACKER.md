# 📊 ISSUE TRACKER - {{ project_name }} Project
> **Issue Management Dashboard | {{ project_type.title() }} System**

## 🎯 AI INSTRUCTIONS - READ THIS FIRST

**Purpose**: This file serves as the central dashboard for tracking all issues across the {{ project_name }} project. AI should use this to monitor open issues and track resolution progress.

## 📈 SUMMARY

### Open Issues Overview
| Category | Count | Priority | Status |
|----------|-------|----------|--------|
| **Incomplete Tasks** | 0 | - | - |
| **Unresolved Errors** | 0 | - | - |
| **System Issues** | 0 | - | - |
{% for category in issue_categories %}
| **{{ category.replace('-', ' ').title() }}** | 0 | - | - |
{% endfor %}

### Recent Activity
- No recent activity

## 🚀 QUICK ACTIONS

### Create New Issue
- [Create Incomplete Task](issues/open/incomplete-tasks/)
- [Log Unresolved Error](issues/open/unresolved-errors/)
- [Report System Issue](issues/open/system-issues/)
{% for category in issue_categories %}
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
- **Open Issues**: 0
- **Critical Issues**: 0

### AI Session Stats
- **Total AI Sessions**: 0
- **Successful Resolutions**: 0
- **Failed Attempts**: 0
- **Success Rate**: 0%
- **Average Session Duration**: N/A

## 🔍 ISSUE CATEGORIES

### Core Categories

#### Incomplete Tasks
- **Description**: Tasks that were started but not completed
- **Common Causes**: Time constraints, technical blockers, scope changes
- **Resolution Patterns**: Break down into smaller tasks, remove blockers
- **Prevention Strategies**: Better planning, regular check-ins

#### Unresolved Errors
- **Description**: Errors that have been encountered but not yet resolved
- **Common Causes**: Complex technical issues, missing information
- **Resolution Patterns**: Root cause analysis, systematic debugging
- **Prevention Strategies**: Better error handling, comprehensive testing

#### System Issues
- **Description**: Issues affecting the overall system functionality
- **Common Causes**: Infrastructure problems, configuration issues
- **Resolution Patterns**: System-wide analysis, infrastructure fixes
- **Prevention Strategies**: Monitoring, regular maintenance

### Application-Specific Categories
{% for category in issue_categories %}
#### {{ category.replace('-', ' ').title() }}
- **Description**: {{ category.replace('-', ' ').title() }} related issues
- **Common Causes**: To be documented
- **Resolution Patterns**: To be documented
- **Prevention Strategies**: To be documented

{% endfor %}

## 📋 ISSUE MANAGEMENT WORKFLOW

### Issue Creation
```python
def create_new_issue(issue_type, description, priority, category=None):
    """Create a new issue with proper categorization"""
    
    # Generate unique issue ID
    issue_id = generate_issue_id(issue_type)
    
    # Create issue file with template
    issue_file = create_issue_file(issue_id, issue_type, description, priority, category)
    
    # Update issue tracker
    update_issue_tracker(issue_id, 'created')
    
    # Notify relevant parties
    notify_issue_creation(issue_id, priority)
    
    return issue_id
```

### Issue Resolution
```python
def resolve_issue(issue_id, resolution_details):
    """Mark an issue as resolved and document the resolution"""
    
    # Update issue status
    update_issue_status(issue_id, 'resolved')
    
    # Document resolution details
    document_issue_resolution(issue_id, resolution_details)
    
    # Move to closed issues
    move_issue_to_closed(issue_id)
    
    # Update metrics
    update_resolution_metrics(issue_id)
    
    # If it was an error, document in error management
    if is_error_issue(issue_id):
        document_error_resolution(issue_id)
```

### Issue Monitoring
```python
def monitor_open_issues():
    """Monitor all open issues for updates and escalations"""
    
    # Check for stale issues
    stale_issues = find_stale_issues()
    
    # Check for critical issues
    critical_issues = find_critical_issues()
    
    # Update issue priorities
    update_issue_priorities()
    
    # Generate alerts
    generate_issue_alerts(stale_issues, critical_issues)
    
    return {
        'stale_issues': stale_issues,
        'critical_issues': critical_issues,
        'alerts_generated': len(stale_issues) + len(critical_issues)
    }
```

## 📊 ISSUE TEMPLATES

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
category: "[category]"
assignee: "[name]"
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

### Error Issue Template
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
assignee: "[name]"
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

## 📈 PERFORMANCE TRACKING

### Issue Metrics
- **Issue Creation Rate**: Number of new issues per time period
- **Issue Resolution Rate**: Number of resolved issues per time period
- **Issue Aging**: Time issues remain open
- **Issue Distribution**: Distribution across categories and priorities

### AI Performance Metrics
- **AI Resolution Success Rate**: Percentage of issues resolved by AI
- **AI Session Efficiency**: Time taken by AI to resolve issues
- **AI Learning Rate**: Improvement in AI issue resolution over time
- **AI Error Rate**: Percentage of AI attempts that fail

## 🔄 AUTOMATION FEATURES

### Automatic Issue Management
- **Issue Aging Alerts**: Automatic alerts for stale issues
- **Priority Escalation**: Automatic escalation of high-priority issues
- **Resolution Tracking**: Automatic tracking of resolution progress
- **Metrics Updates**: Automatic updates of performance metrics

### AI Integration
- **AI Issue Analysis**: AI analysis of issue patterns and trends
- **AI Resolution Suggestions**: AI suggestions for issue resolution
- **AI Learning**: AI learning from resolved issues
- **AI Automation**: AI automation of routine issue management tasks

---

**🔄 Last Updated**: {{ current_date }} | **{{ project_name }} Issue Management**: Active | **Status**: Operational

**📍 File Location**: `{{ project_root }}/issues/ISSUE_TRACKER.md`
