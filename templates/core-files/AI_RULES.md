# 🤖 AI RULES - {{ project_name }} Project
> **{{ project_type.title() }} Development & Management Rules | Multi-Application System**

## 🎯 AI INSTRUCTIONS - READ AND FOLLOW THESE RULES

**This file contains CRITICAL rules for AI when working on {{ project_name }} tasks. These rules MUST be followed exactly.**

## 🔒 CRITICAL SYSTEM RULES - {{ project_name.upper() }}

### Rule #1: File Creation Prohibition (CRITICAL)
```python
# MANDATORY check before creating ANY file
def prevent_duplicate_file_creation(new_file_path):
    existing_similar = find_similar_files(new_file_path)
    if existing_similar:
        return "ERROR: Must edit existing file, never create duplicates"
    return "OK: Safe to create"
```

### Rule #2: System Integrity Validation (CRITICAL)
```python
# MANDATORY execution at every task start
def validate_system_integrity():
    critical_files = ['AI_RULES.md', 'START_TASK.md', 'COMPLETE_TASK.md']
    
    for critical_file in critical_files:
        if not exists(critical_file):
            return f"STOP: Missing critical file: {critical_file}"
    
    return "SYSTEM_VALIDATED: All critical files present"
```

### Rule #3: User Alerting Protocol (CRITICAL)
```python
# MANDATORY: Stop and alert user if system integrity issues found
def check_system_integrity_before_task():
    validation_result = validate_system_integrity()
    
    if validation_result.startswith("STOP:"):
        return {
            'action': 'STOP_AND_ALERT_USER',
            'message': validation_result,
            'recommendations': [
                'Check for missing files',
                'Run MIGRATE_DOCUMENTATION.md',
                'Validate system structure'
            ]
        }
    
    return "SYSTEM_READY: Safe to proceed"
```

## 📋 {{ project_name.upper() }} COMPLIANCE CHECKLIST

### Before Any Task
```bash
✅ System integrity validated
✅ Open issues checked
✅ Required documentation loaded
✅ Error history searched
✅ Backup requirements confirmed
✅ Security impact assessed
```

### After Any Changes
```bash
✅ All services tested
✅ Functionality verified
✅ Security posture maintained
✅ Documentation updated
✅ Error management updated
✅ Issue tracking updated
✅ Version control maintained
```

---

**🔄 Last Updated**: {{ current_date }} | **{{ project_name.title() }} Rules**: Active | **Compliance**: Mandatory

**📍 File Location**: `{{ project_root }}/AI_RULES.md`
