# 📖 Usage Guide - AI Documentation Framework

## 🎯 Getting Started

### 🔄 Version Management

#### Check Current Version
```bash
# Check your current version
python tools/version-manager.py check

# Detailed version report
python tools/version-manager.py history
```

#### Update Framework
```bash
# For v1.x users (major migration)
python tools/migrate-from-v1.py --interactive

# For v2.x users (minor updates)
python tools/update-framework.py --auto
```

### 🚨 Critical: Understanding the Architecture

Before using the framework, you **MUST** understand the file placement:

#### ✅ CORRECT Project Structure
```
your-project/                     # 📍 PROJECT ROOT
├── 🎯 ai-doc-config.json         # 🏛️ CENTRAL CONTROL FILE - Must be here!
├── 📄 AI_RULES.md               # AI behavior rules
├── 📄 START_TASK.md             # Task initialization
├── 📄 COMPLETE_TASK.md          # Task completion
├── 📁 docs/                     # Project documentation
├── 📁 error-management/         # Error system
├── 📁 issues/                   # Issue tracking
└── 📁 [applications]/          # Your apps
    ├── website/
    ├── api/
    └── database/
```

#### ❌ WRONG Placement (Will Cause Errors)
```
❌ your-project/
   ├── 📁 docs/
   │   └── ai-doc-config.json    # WRONG - Inside docs folder
   └── 📁 src/
       └── ai-doc-config.json    # WRONG - Inside src folder
```

### Basic Workflow

The AI Documentation Framework follows a simple but powerful workflow:

1. **Setup** - Initialize the framework for your project (ensure `ai-doc-config.json` is in project root)
2. **Task Execution** - Use START_TASK.md for AI task initiation
3. **Documentation** - AI automatically navigates and updates documentation
4. **Error Management** - Errors are documented and searchable
5. **Issue Tracking** - Incomplete tasks and problems are tracked
6. **Completion** - Use COMPLETE_TASK.md for task finalization

## 🚀 Task Execution Workflow

### 1. Single Application Tasks

For tasks involving only one application:

```bash
# AI should start with the application-specific START_TASK.md
# Example: For a web application task
"Read web/START_TASK.md and execute the task: Update user authentication"
```

**AI Workflow:**
1. Read `web/START_TASK.md`
2. Validate web application system integrity
3. Check for open web-specific issues
4. Read `web/AI_RULES.md` for web-specific rules
5. Navigate web documentation using `web/docs/AI_APP_GUIDE.md`
6. Search web error history
7. Execute task
8. Use `web/COMPLETE_TASK.md` for completion

### 2. Multi-Application Tasks

For tasks involving multiple applications or the entire project:

```bash
# AI should start with the root START_TASK.md
"Read START_TASK.md and execute the task: Deploy all applications to production"
```

**AI Workflow:**
1. Read root `START_TASK.md`
2. Validate entire system integrity
3. Check for open issues across all applications
4. Read root `AI_RULES.md` for project-wide rules
5. Navigate project documentation using `docs/AI_APP_GUIDE.md`
6. Search error history across all applications
7. Coordinate task execution across applications
8. Use root `COMPLETE_TASK.md` for completion

## 📋 AI Task Commands

### Task Initiation Commands

```bash
# Single application task
"Execute task for [app-name]: [task description]"
"Work on [app-name] application: [task description]"
"Update [app-name]: [specific change]"

# Multi-application task
"Execute system-wide task: [task description]"
"Update all applications: [task description]"
"Deploy entire project: [deployment details]"
```

### Task Completion Commands

```bash
# After task completion
"Task completed successfully"
"All changes implemented"
"System updated and tested"
```

## 🔍 Documentation Navigation

### AI Navigation Patterns

The AI automatically navigates documentation based on task requirements:

```python
# AI automatically determines which docs to read
def determine_required_documentation(task_description):
    if 'authentication' in task_description:
        return ['SECURITY.md', 'AUTHENTICATION.md', 'USER_MANAGEMENT.md']
    elif 'database' in task_description:
        return ['DATABASE.md', 'MIGRATIONS.md', 'SCHEMA.md']
    elif 'deployment' in task_description:
        return ['DEPLOYMENT.md', 'CONFIGURATION.md', 'ENVIRONMENT.md']
    else:
        return ['AI_APP_GUIDE.md', 'OVERVIEW.md']
```

### Documentation Hierarchy

```
docs/
├── AI_APP_GUIDE.md          # Navigation guide (always read first)
├── PROJECT_OVERVIEW.md      # Project overview
├── ARCHITECTURE.md          # System architecture
├── DEPLOYMENT.md            # Deployment procedures
├── CONFIGURATION.md         # Configuration management
├── SECURITY.md              # Security guidelines
├── DATABASE.md              # Database documentation
├── API_DOCUMENTATION.md     # API documentation
├── MONITORING.md            # Monitoring and logging
└── TROUBLESHOOTING.md       # Troubleshooting guide
```

## 🚨 Error Management Usage

### Error Documentation

When AI encounters errors, it should:

1. **Search existing errors** in `error-management/MASTER_ERROR_INDEX.md`
2. **Check category-specific errors** in `error-management/[category]/ERROR_INDEX.md`
3. **Document new errors** using the error template
4. **Update error indices** with new solutions

### Error Search Commands

```bash
# Search for similar errors
"Check error history for: [error description]"
"Look for previous solutions to: [problem]"
"Search error documentation for: [symptom]"
```

### Error Documentation Commands

```bash
# Document new error
"Document this error: [error details]"
"Add error to [category]: [error description]"
"Update error index with solution: [resolution]"
```

## 📋 Issue Management Usage

### Issue Tracking

The framework automatically tracks:

- **Incomplete Tasks** - Tasks that couldn't be completed
- **Unresolved Errors** - Errors that need attention
- **System Issues** - Infrastructure or configuration problems

### Issue Commands

```bash
# Log incomplete task
"Log incomplete task: [task description] - [reason]"
"Create issue for: [problem description]"

# Check open issues
"Check for open issues before starting"
"Review pending issues"

# Resolve issues
"Mark issue as resolved: [issue-id]"
"Close issue: [issue-id] - [resolution]"
```

## 🔧 Customization

### Application-Specific Rules

Each application can have custom rules in its `AI_RULES.md`:

```markdown
# Example: Web application specific rules
## WEB APPLICATION RULES
- Never modify production CSS without testing
- Always validate user input
- Check browser compatibility for UI changes
- Test responsive design for mobile devices
```

### Framework-Specific Rules

Different frameworks have different requirements:

```markdown
# Example: React application rules
## REACT SPECIFIC RULES
- Use functional components with hooks
- Follow React best practices
- Test components before deployment
- Optimize bundle size
```

## 📊 Monitoring and Validation

### System Health Checks

The framework includes automatic health checks:

```python
def validate_system_health():
    checks = {
        'documentation_completeness': check_doc_completeness(),
        'error_documentation': check_error_docs(),
        'issue_tracking': check_issue_system(),
        'file_integrity': check_file_integrity()
    }
    return checks
```

### Performance Metrics

Track framework effectiveness:

- **Token Reduction** - How much AI token usage is reduced
- **Navigation Speed** - How quickly AI finds relevant documentation
- **Error Resolution Rate** - How often documented errors are resolved
- **Task Completion Rate** - How often tasks are completed successfully

## 🛠️ Advanced Features

### Automated Cleanup

The framework automatically cleans up after tasks:

```python
def cleanup_after_task():
    # Remove temporary files
    cleanup_temp_files()
    
    # Comment out debug code
    comment_debug_code()
    
    # Clean up test files
    cleanup_test_files()
    
    # Organize logs
    organize_logs()
```

### Version Control Integration

Automatic version management:

```python
def update_versions():
    # Update documentation versions
    update_doc_versions()
    
    # Update error management versions
    update_error_versions()
    
    # Update issue tracking versions
    update_issue_versions()
```

## 🔄 Maintenance

### Regular Maintenance Tasks

```bash
# Weekly maintenance
python tools/maintenance.py --weekly

# Monthly maintenance
python tools/maintenance.py --monthly

# Quarterly review
python tools/maintenance.py --quarterly
```

### Documentation Updates

```bash
# Update documentation
python tools/update-docs.py

# Validate documentation
python tools/validate-docs.py

# Generate reports
python tools/generate-reports.py
```

## 📈 Best Practices

### For AI Assistants

1. **Always start with START_TASK.md** - Don't skip the initialization
2. **Read AI_RULES.md first** - Understand the constraints
3. **Search error history** - Don't repeat known solutions
4. **Document everything** - Keep the knowledge base updated
5. **Use the cleanup system** - Keep the system clean

### For Developers

1. **Customize AI_RULES.md** - Add project-specific rules
2. **Keep documentation updated** - Maintain current information
3. **Document errors promptly** - Help future AI assistants
4. **Review issue tracking** - Address pending problems
5. **Validate system regularly** - Ensure framework health

### For Teams

1. **Standardize usage** - Use consistent patterns
2. **Share knowledge** - Contribute to error documentation
3. **Review effectiveness** - Monitor framework performance
4. **Update templates** - Improve based on usage
5. **Train team members** - Ensure everyone can use the framework

## 🚨 Troubleshooting

### Common Issues

#### AI Not Following Rules
```bash
# Check if AI_RULES.md is being read
"Verify AI_RULES.md is being followed"
"Check rule compliance"
```

#### Documentation Not Found
```bash
# Validate documentation structure
python tools/validator.py --check-docs
"Check documentation completeness"
```

#### Error History Not Working
```bash
# Validate error management
python tools/validator.py --check-errors
"Check error documentation structure"
```

### Debug Mode

Enable debug mode for detailed information:

```bash
export AI_DOC_FRAMEWORK_DEBUG=1
python tools/setup-wizard.py --debug
```

## 📞 Support

### Getting Help

- **Documentation**: Check the framework documentation
- **Error History**: Search for similar issues
- **Issue Tracking**: Check for known problems
- **Community**: Ask in discussions or issues

### Reporting Problems

```bash
# Generate support report
python tools/support-report.py

# Run diagnostics
python tools/diagnostic.py
```

---

**📖 Usage Guide Complete!**

This guide covers the essential usage patterns for the AI Documentation Framework. For advanced features and customization, see the [CONFIGURATION.md](CONFIGURATION.md) guide.
