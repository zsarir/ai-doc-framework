# ✅ COMPLETE TASK - {{ project_name }} Project
> **AI Auto-Update Protocol | Multi-Application Task Completion**

## 🎯 AI INSTRUCTIONS - READ THIS FIRST

**When to use this file**:
- After successful completion of multi-application tasks
- When coordination between applications is complete
- After system-wide changes or deployments
- When all applications are operational and tested

## 🧠 AI AUTO-UPDATE PROTOCOL

### Step 1: Multi-Application Validation (MANDATORY)
```python
# AI validates all applications after task completion
def validate_multi_app_completion():
    """Validate successful completion across all applications"""
    
    # Check each application's health
    app_validation = {}
    {% for app in applications %}
    app_validation['{{ app.name }}'] = validate_{{ app.name }}_completion()
    {% endfor %}
    
    # Check inter-application communication
    integration_test = test_inter_app_communication()
    
    # Check system-wide resources
    system_resources = validate_system_resources()
    
    # Check security posture
    security_validation = validate_system_security()
    
    return {
        'applications': app_validation,
        'integration': integration_test,
        'resources': system_resources,
        'security': security_validation
    }
```

### Step 2: Post-Task System Validation (MANDATORY)
```python
# AI validates system integrity after task completion
def validate_system_post_task():
    """Ensure system integrity is maintained after task completion"""
    
    # Check critical files still exist
    critical_files = [
        '{{ project_root }}/AI_RULES.md',
        '{{ project_root }}/docs/AI_APP_GUIDE.md',
        '{{ project_root }}/error-management/MASTER_ERROR_INDEX.md'
    ]
    
    missing_files = []
    for file_path in critical_files:
        if not file_exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        return {
            'status': 'SYSTEM_DEGRADED',
            'missing_files': missing_files,
            'action': 'RESTORE_MISSING_FILES'
        }
    
    # Check all applications are accessible
    app_accessibility = check_all_apps_accessible()
    if not app_accessibility['all_accessible']:
        return {
            'status': 'APPS_INACCESSIBLE',
            'inaccessible_apps': app_accessibility['inaccessible'],
            'action': 'INVESTIGATE_APP_ACCESS'
        }
    
    return {
        'status': 'SYSTEM_VALIDATED',
        'all_files_present': True,
        'all_apps_accessible': True
    }
```

### Step 3: Issue Management Protocol (MANDATORY)
```python
# AI manages issues after task completion
def manage_issues_post_task():
    """Handle issue resolution and logging after task completion"""
    
    # Check if any open issues were resolved
    resolved_issues = check_resolved_issues()
    
    # Move resolved issues from open to closed
    for issue in resolved_issues:
        move_issue_to_closed(issue)
        
        # If issue was an error, document the resolution
        if issue['type'] == 'error':
            document_error_resolution(issue)
    
    # Log any new issues discovered during task
    new_issues = log_new_issues_discovered()
    
    return {
        'resolved_issues': resolved_issues,
        'new_issues_logged': new_issues,
        'total_open_issues': count_open_issues()
    }
```

### Step 4: Documentation Update Protocol (MANDATORY)
```python
# AI updates all relevant documentation
def update_multi_app_documentation():
    """Update documentation across all affected applications"""
    
    # Determine which documentation needs updates
    docs_to_update = determine_docs_to_update()
    
    # Update project-wide documentation
    project_docs_updated = update_project_documentation(docs_to_update['project'])
    
    # Update application-specific documentation
    app_docs_updated = {}
    {% for app in applications %}
    if '{{ app.name }}' in docs_to_update['applications']:
        app_docs_updated['{{ app.name }}'] = update_{{ app.name }}_documentation()
    {% endfor %}
    
    # Update integration documentation
    integration_docs_updated = update_integration_documentation()
    
    # Update version information
    version_updated = update_version_information()
    
    return {
        'project_docs': project_docs_updated,
        'app_docs': app_docs_updated,
        'integration_docs': integration_docs_updated,
        'version_updated': version_updated
    }
```

### Step 5: Error Management Protocol (MANDATORY)
```python
# AI documents any errors encountered and their resolutions
def document_multi_app_errors():
    """Document errors encountered during multi-application task"""
    
    # Collect errors from all applications
    all_errors = {}
    {% for app in applications %}
    all_errors['{{ app.name }}'] = collect_{{ app.name }}_errors()
    {% endfor %}
    
    # Document new errors
    new_errors_documented = []
    for app_name, errors in all_errors.items():
        for error in errors:
            if error['new']:
                documented_error = document_error_in_category(
                    error, 
                    f"{{ project_root }}/error-management/{error['category']}/"
                )
                new_errors_documented.append(documented_error)
    
    # Update error indices
    error_indices_updated = update_error_indices()
    
    return {
        'new_errors_documented': new_errors_documented,
        'error_indices_updated': error_indices_updated,
        'total_errors_processed': len(new_errors_documented)
    }
```

### Step 6: Multi-Application Cleanup and Debug Code Management (MANDATORY)
```python
# AI cleans up temporary files and debug code across all applications
def cleanup_multi_app_and_manage_debug_code():
    """Clean up temporary files and debug code across all applications"""
    
    cleanup_results = {
        'temp_files_removed': [],
        'debug_code_commented': [],
        'test_files_removed': [],
        'logs_cleaned': [],
        'config_backups_cleaned': []
    }
    
    # Clean up each application
    {% for app in applications %}
    {{ app.name }}_cleanup = cleanup_{{ app.name }}_app()
    cleanup_results['temp_files_removed'].extend({{ app.name }}_cleanup['temp_files'])
    cleanup_results['debug_code_commented'].extend({{ app.name }}_cleanup['debug_code'])
    cleanup_results['test_files_removed'].extend({{ app.name }}_cleanup['test_files'])
    cleanup_results['logs_cleaned'].extend({{ app.name }}_cleanup['logs'])
    cleanup_results['config_backups_cleaned'].extend({{ app.name }}_cleanup['config_backups'])
    {% endfor %}
    
    # Clean up project-level temporary files
    project_cleanup = cleanup_project_level_files()
    cleanup_results['temp_files_removed'].extend(project_cleanup['temp_files'])
    cleanup_results['debug_code_commented'].extend(project_cleanup['debug_code'])
    
    return cleanup_results
```

## 📊 SUCCESS INDICATORS

### Multi-Application Success Criteria
```python
multi_app_success_criteria = {
    'all_applications_operational': True,
    'inter_app_communication_verified': True,
    'system_resources_optimized': True,
    'security_posture_maintained': True,
    'documentation_updated': True,
    'errors_documented': True,
    'issues_resolved': True,
    'temporary_files_cleaned': True,
    'debug_code_commented': True,
    'system_left_clean': True
}
```

### Validation Checklist
```bash
✅ All applications tested and operational
✅ Inter-application communication verified
✅ System resources optimized and available
✅ Security posture maintained and validated
✅ All documentation updated and current
✅ New errors documented with resolutions
✅ Open issues resolved and moved to closed
✅ Temporary/test/debug files cleaned up and removed
✅ Debug code commented out in source files
✅ Log files cleaned and organized
✅ System left in clean, production-ready state
```

## 🔄 NEXT STEPS

### After Successful Multi-Application Task Completion
1. **Verify All Applications**: Ensure all applications are running correctly
2. **Test Integration**: Verify inter-application communication
3. **Monitor Performance**: Check system-wide performance metrics
4. **Update Monitoring**: Ensure monitoring and alerting are active
5. **Document Changes**: Update any remaining documentation
6. **Backup Systems**: Create backups of updated configurations
7. **Notify Stakeholders**: Inform relevant parties of completion

## 📈 PERFORMANCE METRICS

### Task Completion Metrics
```python
completion_metrics = {
    'task_duration': 'measured_in_minutes',
    'applications_affected': {{ applications | length }},
    'files_modified': 'count_of_modified_files',
    'errors_encountered': 'count_of_errors',
    'errors_resolved': 'count_of_resolved_errors',
    'documentation_updated': 'count_of_updated_docs',
    'issues_resolved': 'count_of_resolved_issues',
    'cleanup_performed': True
}
```

---

**✅ MULTI-APPLICATION TASK COMPLETION**: Successfully Completed

**🔄 Last Updated**: {{ current_date }} | **{{ project_name }} Tasks**: Multi-Application | **Status**: Complete

**📍 File Location**: `{{ project_root }}/COMPLETE_TASK.md`
