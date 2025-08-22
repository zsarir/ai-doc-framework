# 🚀 START TASK - {{ project_name }} Project
> **AI Auto-Navigation Protocol | Multi-Application Task Management**

## 🎯 AI INSTRUCTIONS - READ THIS FIRST

**When to use this file**: 
- Multi-application tasks involving coordination between applications
- Project-wide configuration changes
- Cross-application integration tasks
- System-wide deployment or maintenance

## 🧠 AI AUTO-EXECUTION PROTOCOL

### Step 1: Task Analysis & Validation
```python
# AI automatically validates multi-application task requirements
def analyze_multi_app_task(task_description):
    multi_app_patterns = [
        '{{ project_name }}', 'multi-app', 'cross-app', 'integration',
        'deployment', 'system-wide', 'coordination', 'all apps'
    ]
    
    # Determine if this is truly a multi-application task
    if not any(pattern in task_description.lower() for pattern in multi_app_patterns):
        return redirect_to_appropriate_app(task_description)
    
    # Analyze complexity and affected applications
    affected_apps = identify_affected_applications(task_description)
    complexity = determine_multi_app_complexity(task_description)
    
    return {
        'project': '{{ project_name }}',
        'type': 'multi-application',
        'affected_apps': affected_apps,
        'complexity': complexity,
        'coordination_required': len(affected_apps) > 1
    }
```

### Step 0: System Validation (MANDATORY)
```python
# AI MUST validate system integrity before any task
def validate_system_first():
    validation_result = validate_system_integrity()
    
    if validation_result.startswith('STOP:'):
        return {
            'action': 'STOP_AND_ALERT_USER',
            'message': validation_result,
            'recommendations': ['Check for missing files', 'Run MIGRATE_DOCUMENTATION.md', 'Validate system structure']
        }
    
    return "SYSTEM_VALIDATED: Safe to proceed"

def validate_system_integrity():
    # Check critical system files
    critical_files = [
        '{{ project_root }}/AI_RULES.md',
        '{{ project_root }}/docs/AI_APP_GUIDE.md',
        '{{ project_root }}/error-management/MASTER_ERROR_INDEX.md'
    ]
    
    for critical_file in critical_files:
        if not file_exists(critical_file):
            return f"STOP: Missing critical system file: {critical_file}"
    
    return "SYSTEM_HEALTHY: All critical files present"
```

### Step 0.5: Check Open Issues (MANDATORY)
```python
# AI checks for open issues after system validation passes
def check_open_issues_after_validation():
    # Check for open issues across all applications
    issue_categories = [
        'incomplete-tasks', 'unresolved-errors', 'system-issues'
    ]
    
    all_issues = {}
    for category in issue_categories:
        category_issues = scan_open_issues(f"{{ project_root }}/issues/open/{category}/")
        if category_issues:
            all_issues[category] = category_issues
    
    # If open issues found, consult user
    if all_issues:
        return consult_user_about_open_issues(all_issues, task_description)
    else:
        return "NO_OPEN_ISSUES: Proceed with multi-application task"
```

### Step 2: Read Project Rules (MANDATORY)
```python
# AI MUST read project rules before proceeding
def read_project_rules():
    rules_content = read_file("{{ project_root }}/AI_RULES.md")
    
    # Extract critical rules
    critical_rules = extract_critical_rules(rules_content)
    system_requirements = extract_system_requirements(rules_content)
    
    return {
        'rules': critical_rules,
        'system_requirements': system_requirements,
        'compliance_check': validate_rules_understanding(critical_rules)
    }
```

### Step 3: Multi-Application Status Check
```python
# AI checks current status of all applications before making changes
def check_all_applications_status():
    app_status = {}
    
    # Check each application
    {% for app in applications %}
    app_status['{{ app.name }}'] = check_{{ app.name }}_status()
    {% endfor %}
    
    # Check for any critical service issues
    critical_issues = []
    for app_name, status in app_status.items():
        if status['status'] != 'healthy':
            critical_issues.append(f"{app_name}: {status['issue']}")
    
    if critical_issues:
        return {
            'status': 'APPLICATIONS_DEGRADED',
            'issues': critical_issues,
            'recommendation': 'Address application issues before proceeding'
        }
    
    return {
        'status': 'ALL_APPLICATIONS_HEALTHY',
        'details': app_status
    }
```

### Step 4: Navigate Multi-Application Documentation
```python
# AI uses project app guide for efficient navigation
def navigate_multi_app_documentation(task_requirements):
    # Read the main navigation guide
    app_guide = read_file("{{ project_root }}/docs/AI_APP_GUIDE.md")
    
    # Determine required documentation based on task
    required_docs = determine_required_multi_app_docs(task_requirements)
    
    # Read only the necessary documentation
    documentation = {}
    for doc_type in required_docs:
        doc_path = get_multi_app_doc_path(doc_type)
        documentation[doc_type] = read_file(doc_path)
    
    return documentation

def determine_required_multi_app_docs(task_requirements):
    """Map task requirements to specific multi-application documentation"""
    doc_mapping = {
        'deployment': ['DEPLOYMENT.md', 'CONFIGURATION.md'],
        'integration': ['INTEGRATION.md', 'API_DOCUMENTATION.md'],
        'monitoring': ['MONITORING.md', 'LOGGING.md'],
        'security': ['SECURITY.md', 'AUTHENTICATION.md'],
        'database': ['DATABASE.md', 'MIGRATIONS.md'],
        'troubleshooting': ['TROUBLESHOOTING.md', 'ERROR_HANDLING.md']
    }
    
    required_docs = set()
    for requirement in task_requirements:
        if requirement in doc_mapping:
            required_docs.update(doc_mapping[requirement])
    
    return list(required_docs)
```

### Step 5: Check Multi-Application Error History
```python
# AI searches for relevant multi-application error solutions
def search_multi_app_error_history(task_analysis):
    # Search across all error categories
    error_categories = {{ error_categories | tojson }}
    
    relevant_errors = {}
    for category in error_categories:
        if is_relevant_to_multi_app_task(category, task_analysis):
            category_errors = search_errors_in_category(
                f"{{ project_root }}/error-management/{category}/ERROR_INDEX.md",
                task_analysis.keywords
            )
            if category_errors:
                relevant_errors[category] = category_errors
    
    return relevant_errors
```

### Step 6: Multi-Application Task Execution
```python
# AI executes multi-application task with proper coordination
def execute_multi_app_task(task_analysis, documentation, error_history):
    # Pre-execution checks
    pre_check = perform_multi_app_pre_execution_checks(task_analysis)
    if pre_check['status'] != 'READY':
        return pre_check
    
    # Create backup for all affected applications
    if task_analysis.backup_required:
        backup_result = create_multi_app_backup(task_analysis.affected_apps)
        if backup_result['status'] != 'SUCCESS':
            return backup_result
    
    # Execute task with application coordination
    execution_plan = create_multi_app_execution_plan(task_analysis)
    execution_result = execute_with_app_coordination(execution_plan)
    
    # Validate all applications after changes
    post_validation = validate_all_applications_post_change()
    
    return {
        'execution': execution_result,
        'validation': post_validation,
        'applications_status': check_all_applications_status()
    }
```

## 🧪 MULTI-APPLICATION TESTING PROTOCOL

### Cross-Application Testing
```python
def test_multi_app_integration_post_task():
    """Comprehensive multi-application integration testing"""
    tests = {
        'inter_app_communication': test_app_communication(),
        'shared_resources': test_shared_resources(),
        'data_consistency': test_data_consistency(),
        'security_integration': test_security_integration(),
        'performance_impact': test_performance_impact()
    }
    
    failed_tests = [test for test, result in tests.items() if not result['success']]
    
    if failed_tests:
        return {
            'status': 'MULTI_APP_TESTS_FAILED',
            'failed_tests': failed_tests,
            'action': 'INVESTIGATE_AND_REPAIR'
        }
    
    return {
        'status': 'ALL_MULTI_APP_TESTS_PASSED',
        'test_results': tests
    }
```

## 📊 MULTI-APPLICATION MONITORING INTEGRATION

### System-Wide Monitoring
```python
def setup_multi_app_monitoring_during_task():
    """Setup monitoring for all applications during task execution"""
    monitoring = {
        'app_health': monitor_all_applications(),
        'inter_app_communication': monitor_app_communication(),
        'shared_resources': monitor_shared_resources(),
        'system_performance': collect_system_metrics(),
        'error_aggregation': aggregate_errors_across_apps()
    }
    
    return monitoring
```

## 🚀 MULTI-APPLICATION TASK COMPLETION

### Task Completion Validation
```python
def validate_multi_app_task_completion(task_result):
    """Validate successful completion of multi-application task"""
    
    # All applications health check
    all_apps_health = check_all_applications_status()
    if all_apps_health['status'] != 'ALL_APPLICATIONS_HEALTHY':
        return {
            'status': 'INCOMPLETE',
            'issue': 'Not all applications are healthy',
            'action': 'REPAIR_APPLICATIONS_FIRST'
        }
    
    # Integration verification
    integration_test = test_multi_app_integration_post_task()
    if integration_test['status'] != 'ALL_MULTI_APP_TESTS_PASSED':
        return {
            'status': 'INCOMPLETE',
            'issue': 'Multi-application integration tests failed',
            'failed_tests': integration_test['failed_tests']
        }
    
    # System-wide validation
    system_validation = validate_system_wide_posture()
    if system_validation['status'] != 'SECURE':
        return {
            'status': 'INCOMPLETE',
            'issue': 'System-wide security requirements not met',
            'security_issues': system_validation['issues']
        }
    
    return {
        'status': 'COMPLETE',
        'all_applications': 'OPERATIONAL',
        'integration': 'VALIDATED',
        'system_health': 'OPTIMAL'
    }
```

## 📋 AI EXECUTION CHECKLIST

### Pre-Task Checklist
```bash
✅ VALIDATE SYSTEM INTEGRITY
✅ CHECK OPEN ISSUES (consult user if found)
✅ READ PROJECT RULES (mandatory compliance)
✅ VERIFY ALL APPLICATIONS STATUS
✅ LOAD REQUIRED DOCUMENTATION
✅ SEARCH ERROR HISTORY
✅ CONFIRM BACKUP REQUIREMENTS
✅ VALIDATE SECURITY IMPACT
```

### During Task Checklist
```bash
✅ MONITOR ALL APPLICATIONS HEALTH
✅ FOLLOW COORDINATION PROTOCOLS
✅ MAINTAIN INTER-APP COMMUNICATION
✅ TRACK SHARED RESOURCE USAGE
✅ VALIDATE DATA CONSISTENCY
✅ MONITOR PERFORMANCE IMPACT
✅ LOG ALL CHANGES
```

### Post-Task Checklist  
```bash
✅ TEST ALL APPLICATIONS INDIVIDUALLY
✅ TEST INTER-APPLICATION INTEGRATION
✅ VALIDATE SHARED RESOURCES
✅ CONFIRM DATA CONSISTENCY
✅ VERIFY SECURITY POSTURE
✅ BACKUP UPDATED CONFIGURATIONS
✅ UPDATE DOCUMENTATION
```

## 🔄 NEXT STEPS

### After Successful Task Completion
1. **Execute COMPLETE_TASK.md**: Run multi-application completion protocol
2. **Update Documentation**: Ensure all application docs are current
3. **Log Resolution**: Document any issues resolved
4. **Monitor Performance**: Verify system-wide metrics
5. **Security Audit**: Confirm all security measures active

---

## 🎯 MULTI-APPLICATION SUCCESS CRITERIA

### Completion Requirements
```python
multi_app_success_criteria = {
    'applications_operational': {{ applications | map(attribute='name') | list | tojson }},
    'integration_verified': ['inter-app_communication', 'shared_resources', 'data_consistency'],
    'security_validated': ['authentication', 'authorization', 'encryption'],
    'performance_optimized': ['response_times', 'resource_usage', 'scalability'],
    'monitoring_active': ['health_checks', 'alerts', 'metrics'],
    'documentation_updated': True,
    'backup_created': True
}
```

---

**🚀 MULTI-APPLICATION TASK EXECUTION**: Ready for Production

**🔄 Last Updated**: {{ current_date }} | **{{ project_name }} Tasks**: Multi-Application | **Status**: Active

**📍 File Location**: `{{ project_root }}/START_TASK.md`
