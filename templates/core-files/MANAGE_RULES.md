# 🛠️ MANAGE RULES - AI Rules Management System
> **Add, Update, Remove AI Rules | Direct System Modification**

## 🎯 AI INSTRUCTIONS - RULES MANAGEMENT PROTOCOL

**When to use this file**: 
- To add new rules to any application or root
- To update existing rules
- To remove outdated rules
- To reorganize rule categories

## 🧠 AI RULES MANAGEMENT PROTOCOL

### Step 1: Parse Rule Management Command
```python
# AI automatically parses rule management commands
def parse_rule_command(command):
    # Extract action type
    actions = {
        'add': ['add', 'create', 'insert', 'new'],
        'update': ['update', 'modify', 'change', 'edit'],
        'remove': ['remove', 'delete', 'eliminate'],
        'reorganize': ['reorganize', 'restructure', 'reorder']
    }
    
    # Extract target location - CONFIGURED APPLICATIONS
    targets = {
        'root': ['root', 'project', 'global'],
        {% for app in applications %}'{{ app.name }}': ['{{ app.name }}', '{{ app.framework }}', '{{ app.type }}'],
        {% endfor %}
    }
    
    # Extract rule category
    categories = {
        'frontend': ['frontend', 'css', 'javascript', 'template'],
        'backend': ['backend', 'django', 'fastapi', 'database'],
        'security': ['security', 'auth', 'ssl', 'csrf'],
        'performance': ['performance', 'optimization', 'speed'],
        'testing': ['testing', 'test', 'coverage', 'validation'],
        'deployment': ['deployment', 'production', 'docker'],
        'integration': ['integration', 'api', 'external']
    }
    
    return {
        'action': detect_action(command, actions),
        'target': detect_target(command, targets),
        'category': detect_category(command, categories),
        'rules': extract_rule_content(command)
    }
```

### Step 2: Locate Target Rules File
```python
# AI automatically determines which rules file to modify
def get_rules_file_path(target):
    rules_file_paths = {
        'root': '{{ project_path }}/AI_RULES.md',
        {% for app in applications %}'{{ app.name }}': '{{ project_path }}/{{ app.name }}/AI_RULES.md',
        {% endfor %}
    }
    
    return rules_file_paths[target]
```

### Step 3: Execute Rule Management Action
```python
# AI automatically executes the rule management action
def execute_rule_management(parsed_command):
    target_file = get_rules_file_path(parsed_command.target)
    
    if parsed_command.action == 'add':
        add_rules_to_file(target_file, parsed_command.category, parsed_command.rules)
    elif parsed_command.action == 'update':
        update_rules_in_file(target_file, parsed_command.category, parsed_command.rules)
    elif parsed_command.action == 'remove':
        remove_rules_from_file(target_file, parsed_command.category, parsed_command.rules)
    elif parsed_command.action == 'reorganize':
        reorganize_rules_in_file(target_file, parsed_command.new_structure)
    
    # Update rule file version
    increment_rules_version(target_file)
    
    # Update START_TASK files to reflect rule changes
    update_start_task_references(parsed_command.target)
```

## 📋 RULE MANAGEMENT EXAMPLES

### Example 1: Add Rules to Applications
{% for app in applications %}
**Command**: "Add {{ app.framework }} rules to {{ app.name }}: Use {{ app.framework }} best practices"

**AI Execution**:
```python
# Parsed result:
{
    'action': 'add',
    'target': '{{ app.name }}',
    'category': '{{ app.type }}',
    'rules': ['Use {{ app.framework }} best practices']
}

# AI automatically:
1. Opens: {{ project_path }}/{{ app.name }}/AI_RULES.md
2. Finds: "Custom {{ app.type.title() }} Rules" section
3. Adds: The new {{ app.framework }} rule
4. Updates: Version number in {{ app.name }}/AI_RULES.md
5. Updates: {{ app.name }}/START_TASK.md to emphasize rules reading
```
{% endfor %}

### Example 2: Update Global Rules
**Command**: "Update root performance rule: API response time from 200ms to 100ms"

**AI Execution**:
```python
# AI automatically:
1. Opens: {{ project_path }}/AI_RULES.md
2. Finds: Performance-related rule
3. Updates: Response time from 200ms to 100ms
4. Updates: Version number
5. Updates: All application START_TASK.md files
```

## 🔧 RULE MANAGEMENT COMMANDS

### Add Rules Command Format
```bash
"Add [number] [category] rules to [target]: [rule1], [rule2], [rule3]"

Examples:
{% for app in applications %}✅ "Add {{ app.type }} rule to {{ app.name }}: {{ app.framework }}-specific implementation"
{% endfor %}✅ "Add global rule to root: All services must have health checks"
```

### Update Rules Command Format
```bash
"Update [target] [category] rule: [old rule] → [new rule]"

Examples:
{% for app in applications %}✅ "Update {{ app.name }} performance rule: {{ app.framework }} optimization"
{% endfor %}✅ "Update root security rule: Enhanced authentication requirements"
```

### Remove Rules Command Format
```bash
"Remove [category] rule from [target]: [rule description]"

Examples:
{% for app in applications %}✅ "Remove outdated {{ app.type }} rule from {{ app.name }}: Legacy {{ app.framework }} requirement"
{% endfor %}✅ "Remove deprecated security rule from root: Old authentication method"
```

## 🎯 RULE CATEGORIES

### Standard Rule Categories
```python
# AI recognizes these rule categories automatically
rule_categories = {
    'frontend': 'CSS, JavaScript, templates, responsive design',
    'backend': 'Framework-specific, database, API design',
    'security': 'Authentication, authorization, data protection',
    'performance': 'Speed, optimization, resource usage',
    'testing': 'Test coverage, quality, automation',
    'deployment': 'Production, containers, environment',
    'integration': 'External systems, API integration',
    'monitoring': 'Logging, metrics, alerting',
    'safety': 'Robot safety, emergency protocols',
    'reliability': 'Error handling, fault tolerance'
}
```

### Application-Specific Categories
```python
# Application-specific rule categories
app_specific_categories = {
    {% for app in applications %}'{{ app.name }}': ['{{ app.framework }}', '{{ app.type }}', 'deployment', 'integration'],
    {% endfor %}
}
```

## 🔄 AUTOMATIC RULE INTEGRATION

### Update START_TASK Files After Rule Changes
```python
def update_start_task_after_rule_change(target, rule_changes):
    # Update START_TASK.md to emphasize rules reading
    start_task_files = [
        '{{ project_path }}/START_TASK.md',  # Root
        {% for app in applications %}'{{ project_path }}/{{ app.name }}/START_TASK.md',  # {{ app.name }}
        {% endfor %}
    ]
    
    for start_task_file in start_task_files:
        if target in start_task_file or target == 'root':
            add_rule_reading_emphasis(start_task_file, rule_changes.category)
            update_rule_reading_protocol(start_task_file, rule_changes)
```

### Cross-Application Rule Impact
```python
def handle_cross_app_rule_impact(rule_change):
    # If rule affects multiple applications
    if rule_change.target == 'root':
        # Update all application START_TASK files
        apps = [{% for app in applications %}'{{ app.name }}', {% endfor %}]
        for app in apps:
            update_start_task_rule_emphasis(app, rule_change)
```

## 📊 RULE VALIDATION SYSTEM

### Rule Conflict Detection
```python
def detect_rule_conflicts(new_rule, existing_rules):
    # Check for conflicting rules across applications
    conflicts = []
    applications = [{% for app in applications %}'{{ app.name }}', {% endfor %}]
    
    for app in applications:
        app_rules = load_app_rules(app)
        for existing_rule in app_rules:
            if rules_conflict(new_rule, existing_rule):
                conflicts.append({
                    'application': app,
                    'conflicting_rule': existing_rule
                })
    
    return conflicts
```

### Rule Quality Requirements
```python
def validate_rule_quality(rule_content):
    quality_checks = {
        'specificity': rule_is_specific_and_measurable(rule_content),
        'clarity': rule_is_clear_and_unambiguous(rule_content),
        'actionability': rule_provides_clear_action(rule_content),
        'measurability': rule_has_success_criteria(rule_content),
        'consistency': rule_consistent_with_project(rule_content)
    }
    
    return all(quality_checks.values())
```

## 🎪 RULE MANAGEMENT EXAMPLES FOR {{ project_name }}

### Example A: Add Project-Specific Rules
**User Input**: 
```
Task: Add security rules to all applications:
{% for app in applications %}1. {{ app.name }} ({{ app.framework }}): Enhanced {{ app.type }} security
{% endfor %}
```

**AI Execution**:
```python
# AI automatically processes each application:
{% for app in applications %}
# {{ app.name }} ({{ app.framework }})
1. Opens: {{ project_path }}/{{ app.name }}/AI_RULES.md
2. Finds: "Custom Security Rules" section
3. Adds: {{ app.framework }}-specific security rule
4. Updates: {{ app.name }}/AI_RULES.md version
5. Updates: {{ app.name }}/START_TASK.md to emphasize security rules
{% endfor %}
```

### Example B: Update Performance Rules
**User Input**: 
```
Task: Update all application performance rules: Response time limit 150ms
```

**AI Execution**:
```python
# AI automatically updates all applications:
{% for app in applications %}
# {{ app.name }}
- Update: {{ app.framework }} performance configuration
- Ensure: 150ms response time compliance
- Validate: {{ app.type }} optimization requirements
{% endfor %}
```

## 🛠 SYSTEM INTEGRATION

### Integration with Conflict Detection
```python
def integrate_with_conflict_detector():
    # After rule changes, run conflict detection
    from conflict_detector import AIDocConflictDetector
    
    detector = AIDocConflictDetector("{{ project_path }}")
    report = detector.detect_all_conflicts()
    
    if report.total_conflicts > 0:
        alert_user_of_conflicts(report)
        suggest_conflict_resolution(report)
```

### Integration with START_TASK Files
```python
def integrate_rules_with_start_tasks():
    # Update all START_TASK.md files to emphasize rules reading
    start_task_files = [
        '{{ project_path }}/START_TASK.md',
        {% for app in applications %}'{{ project_path }}/{{ app.name }}/START_TASK.md',
        {% endfor %}
    ]
    
    for start_task_file in start_task_files:
        add_rules_reading_protocol(start_task_file)
        emphasize_rule_compliance(start_task_file)
```

## 📋 RULE MANAGEMENT COMMAND PATTERNS

### Add Rules Commands
```bash
# Pattern: "Add [category] rule(s) to [target]: [rule content]"

{% for app in applications %}✅ "Add {{ app.type }} rule to {{ app.name }}: Use {{ app.framework }} for all {{ app.type }} operations"
{% endfor %}✅ "Add performance rule to root: All APIs under 150ms response time"
```

### Update Rules Commands
```bash
# Pattern: "Update [target] [category] rule: [old] → [new]"

{% for app in applications %}✅ "Update {{ app.name }} performance rule: {{ app.framework }} optimization guidelines"
{% endfor %}✅ "Update root testing rule: Coverage 80% → 90%"
```

### Remove Rules Commands
```bash
# Pattern: "Remove [category] rule from [target]: [rule description]"

{% for app in applications %}✅ "Remove outdated {{ app.type }} rule from {{ app.name }}: Legacy {{ app.framework }} requirement"
{% endfor %}✅ "Remove deprecated security rule from root: Legacy auth method"
```

## 🔗 AUTOMATIC LINK UPDATES

### Update References After Rule Changes
```python
def update_references_after_rule_change(target, rule_changes):
    # Update all relevant files
    files_to_update = [
        f"{{ project_path }}/{target}/START_TASK.md",
        f"{{ project_path }}/{target}/COMPLETE_TASK.md",
        f"{{ project_path }}/{target}/docs/AI_APP_GUIDE.md"
    ]
    
    for file_path in files_to_update:
        if file_exists(file_path):
            update_rule_references(file_path, rule_changes)
```

## 📊 RULE MANAGEMENT TRACKING

### Rule Change Logging
```python
def log_rule_change(target, action, category, rule_content, timestamp):
    # Log rule changes for audit and tracking
    rule_change_log = {
        'timestamp': timestamp,
        'project': '{{ project_name }}',
        'target': target,
        'action': action,
        'category': category,
        'rule_content': rule_content,
        'ai_agent': 'AI Assistant',
        'validation_passed': True
    }
    
    # Add to project-specific rule change history
    append_to_rule_change_log(rule_change_log)
```

## ⚡ QUICK RULE MANAGEMENT EXAMPLES

### Add Multiple Rules to Different Applications
```bash
User: "Add these rules:
{% for app in applications %}{{ loop.index }}. {{ app.name }}: Use {{ app.framework }} async operations for all database calls
{% endfor %}"

AI Auto-Execution:
{% for app in applications %}✅ Parse: {{ app.framework }} rule for {{ app.name }}
✅ Open: {{ project_path }}/{{ app.name }}/AI_RULES.md
✅ Add: Rule to "Custom {{ app.type.title() }} Rules" section
✅ Update: Version and START_TASK emphasis
{% endfor %}✅ Validate: No conflicts across applications
```

### Update Global Rule Affecting All Applications
```bash
User: "Update global security rule: JWT expiration from 24 hours to 1 hour"

AI Auto-Execution:
✅ Parse: Update security rule for root
✅ Open: {{ project_path }}/AI_RULES.md
✅ Find: JWT expiration rule in security section
✅ Update: 24 hours → 1 hour
✅ Update: Root AI_RULES.md version
{% for app in applications %}✅ Update: {{ app.name }}/START_TASK.md to emphasize new security rule
{% endfor %}✅ Check: All applications for JWT configuration impact
```

## 🎯 RULE MANAGEMENT SUCCESS VALIDATION

### After Rule Management Task
```python
def validate_rule_management_success(management_result):
    validation_checks = {
        'rules_added_correctly': verify_rules_in_target_file(management_result),
        'formatting_correct': verify_rule_formatting(management_result),
        'no_conflicts': verify_no_rule_conflicts_across_apps(management_result),
        'versions_updated': verify_version_increments(management_result),
        'start_task_updated': verify_start_task_emphasis(management_result),
        'cross_references_valid': validate_all_rule_references(management_result)
    }
    
    return all(validation_checks.values())
```

## 🏁 RULE MANAGEMENT COMPLETION

### Success Criteria
```bash
✅ Rules added/updated/removed successfully
✅ Target AI_RULES.md file(s) updated correctly
✅ Version numbers incremented appropriately
✅ START_TASK files updated to emphasize rules
✅ No rule conflicts detected across applications
✅ All cross-references remain valid
✅ Rule compliance validation added to relevant files
```

### Post-Management Updates
```python
def complete_rule_management_task():
    # Update rule change log
    log_rule_management_completion()
    
    # Validate system integrity across all applications
    validate_entire_rules_system()
    
    # Update rule statistics
    update_global_rule_statistics()
    
    # Generate rule impact report
    generate_rule_impact_report()
    
    # Run conflict detection
    run_conflict_detection_check()
```

---

## 🎯 CRITICAL AI PROTOCOL

1. **Parse Command Correctly**: Understand exactly what rule management is requested
2. **Validate Target**: Ensure target application/root is correct ({{ project_name }})
3. **Check Conflicts**: Verify new rules don't conflict across applications
4. **Update Systematically**: Update all related files and references
5. **Validate Completely**: Ensure all updates are correct and consistent

## 📊 RULE MANAGEMENT SUCCESS METRICS

- **Rule Addition Success**: >99% successful rule additions
- **Conflict Detection**: 100% conflict detection before addition
- **System Integration**: 100% successful integration with START_TASK files
- **Version Control**: 100% accurate version tracking
- **Cross-Reference Accuracy**: 100% valid references after changes
- **Multi-Application Consistency**: 100% consistent rules across applications

---

**🚀 RULE MANAGEMENT SYSTEM READY FOR {{ project_name }}**

**✅ AI can now manage rules directly in the documentation system**
**✅ Complete integration with START_TASK and COMPLETE_TASK workflows**
**✅ Automatic validation and conflict detection across all applications**
**✅ Support for all configured applications: {% for app in applications %}{{ app.name }}{% if not loop.last %}, {% endif %}{% endfor %}**

**🔄 Last Updated**: {{ current_date }} | **Rule Management**: Production Ready | **Integration**: Complete
