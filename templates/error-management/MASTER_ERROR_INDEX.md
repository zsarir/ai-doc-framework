# 📋 MASTER ERROR INDEX - {{ project_name }} Project
> **Centralized Error Management | {{ project_type.title() }} System**

## 🎯 AI INSTRUCTIONS - READ THIS FIRST

**Purpose**: This file serves as the central index for all error documentation across the {{ project_name }} project. AI should use this to quickly locate relevant error solutions.

## 📊 ERROR CATEGORIES OVERVIEW

### Primary Error Categories
| Category | Description | Index File | Count |
|----------|-------------|------------|-------|
| **Backend** | Server-side errors, API issues, business logic | [Backend Error Index](backend/ERROR_INDEX.md) | 0 |
| **Frontend** | Client-side errors, UI/UX issues, JavaScript | [Frontend Error Index](frontend/ERROR_INDEX.md) | 0 |
| **Infrastructure** | Deployment, container, network, system issues | [Infrastructure Error Index](infrastructure/ERROR_INDEX.md) | 0 |
| **Security** | Authentication, authorization, vulnerabilities | [Security Error Index](security/ERROR_INDEX.md) | 0 |
| **Database** | Database connection, queries, migrations | [Database Error Index](database/ERROR_INDEX.md) | 0 |
| **Deployment** | CI/CD, environment, configuration issues | [Deployment Error Index](deployment/ERROR_INDEX.md) | 0 |

### Application-Specific Categories
{% for app in applications %}
#### {{ app.name.title() }} Errors
| Category | Description | Index File | Count |
|----------|-------------|------------|-------|
| **{{ app.name }} General** | {{ app.name }} specific errors | [{{ app.name }} Error Index]({{ app.name }}/ERROR_INDEX.md) | 0 |
{% endfor %}

## 🔍 ERROR SEARCH PROTOCOL

### Step 1: Error Classification
```python
def classify_error(error_message, context):
    """Classify error into appropriate category for efficient search"""
    
    # Define error patterns for each category
    error_patterns = {
        'backend': ['500', 'server error', 'api error', 'business logic', 'validation'],
        'frontend': ['javascript', 'ui', 'client', 'browser', 'css', 'html'],
        'infrastructure': ['container', 'docker', 'network', 'system', 'resource'],
        'security': ['auth', 'permission', 'token', 'jwt', 'csrf', 'vulnerability'],
        'database': ['sql', 'connection', 'query', 'migration', 'database'],
        'deployment': ['ci/cd', 'environment', 'config', 'deploy', 'build']
    }
    
    # Classify based on error message and context
    for category, patterns in error_patterns.items():
        if any(pattern in error_message.lower() for pattern in patterns):
            return category
    
    return 'general'
```

### Step 2: Error Search Strategy
```python
def search_error_solutions(error_classification, error_keywords):
    """Search for error solutions in appropriate category"""
    
    # Get the relevant error index file
    index_file = f"error-management/{error_classification}/ERROR_INDEX.md"
    
    # Search for similar errors
    similar_errors = search_error_index(index_file, error_keywords)
    
    # If no matches in primary category, search other categories
    if not similar_errors:
        similar_errors = search_all_error_categories(error_keywords)
    
    return similar_errors
```

## 📈 ERROR STATISTICS

### Overall Error Metrics
- **Total Errors Documented**: 0
- **Errors Resolved**: 0
- **Resolution Rate**: 0%
- **Average Resolution Time**: N/A
- **Most Common Error Type**: N/A
- **Most Common Error Category**: N/A

### Category-Specific Metrics
| Category | Total | Resolved | Resolution Rate | Avg Resolution Time |
|----------|-------|----------|-----------------|-------------------|
| Backend | 0 | 0 | 0% | N/A |
| Frontend | 0 | 0 | 0% | N/A |
| Infrastructure | 0 | 0 | 0% | N/A |
| Security | 0 | 0 | 0% | N/A |
| Database | 0 | 0 | 0% | N/A |
| Deployment | 0 | 0 | 0% | N/A |

## 🚀 QUICK ERROR RESOLUTION

### Common Error Patterns

#### Backend Errors
- **500 Internal Server Error**: Check server logs, database connections
- **Validation Errors**: Review input validation, data formats
- **API Errors**: Check endpoint configuration, request/response formats

#### Frontend Errors
- **JavaScript Errors**: Check browser console, script loading
- **UI Rendering Issues**: Check CSS, HTML structure, responsive design
- **API Integration Errors**: Check API endpoints, authentication

#### Infrastructure Errors
- **Container Issues**: Check Docker configuration, resource limits
- **Network Problems**: Check connectivity, firewall rules
- **System Resource Issues**: Check CPU, memory, disk space

#### Security Errors
- **Authentication Failures**: Check credentials, token validity
- **Authorization Issues**: Check user permissions, role assignments
- **CSRF Errors**: Check CSRF tokens, form submissions

#### Database Errors
- **Connection Issues**: Check database server, connection strings
- **Query Errors**: Check SQL syntax, table structure
- **Migration Problems**: Check migration files, database schema

#### Deployment Errors
- **Build Failures**: Check build configuration, dependencies
- **Environment Issues**: Check environment variables, configuration
- **Deployment Failures**: Check deployment scripts, target environment

## 📋 ERROR DOCUMENTATION TEMPLATE

### Standard Error Entry Format
```markdown
---
error_id: "[CATEGORY]-[YYYY-MM-DD]-[SEQUENCE]"
category: "[backend|frontend|infrastructure|security|database|deployment]"
subcategory: "[specific-component]"
severity: "[critical|high|medium|low]"
status: "[active|investigating|resolved|recurring]"
first_occurrence: "[YYYY-MM-DD HH:MM:SS UTC]"
last_occurrence: "[YYYY-MM-DD HH:MM:SS UTC]"
resolution_date: "[YYYY-MM-DD HH:MM:SS UTC]"
resolution_time_hours: [number]
affected_environments: ["development","staging","production"]
affected_components: ["list","of","components"]
tags: ["keyword1","keyword2","keyword3"]
ai_confidence_score: [0.0-1.0]
pattern_signatures: ["regex_or_signature_1","regex_or_signature_2"]
related_errors: ["ERROR-ID-1","ERROR-ID-2"]
assignee: "[name]"
reviewer: "[name]"
---

# Error Title

## Error Description
[Detailed description of the error]

## Error Details
- **Error Type**: [Type of error]
- **Error Code**: [Error code if applicable]
- **Location**: [Where the error occurred]
- **Context**: [Context in which error occurred]

## Impact
[Impact of the error on the system]

## Root Cause Analysis
[Primary cause + contributing factors + why not caught]

## Resolution
[Code/config/db/infrastructure changes with before/after snippets]

## Verification
[Tests (unit/integration/manual), regression checklist]

## Prevention Strategies
[Immediate and long-term; monitoring/detection notes]

## Cross-References
[Related errors, documentation, and tags for future discovery]
```

## 🔄 ERROR MANAGEMENT WORKFLOW

### Error Discovery
1. **Error Occurs**: System detects or user reports error
2. **Initial Assessment**: Determine severity and impact
3. **Classification**: Categorize error using classification function
4. **Search History**: Look for similar errors in error index

### Error Resolution
1. **Investigation**: Analyze error details and root cause
2. **Solution Development**: Create fix based on analysis
3. **Testing**: Verify solution resolves the error
4. **Documentation**: Document error and resolution

### Error Prevention
1. **Pattern Recognition**: Identify common error patterns
2. **Prevention Measures**: Implement preventive measures
3. **Monitoring**: Set up monitoring for similar errors
4. **Training**: Update team knowledge and procedures

## 📊 PERFORMANCE METRICS

### Error Management Efficiency
- **Error Detection Time**: Time from occurrence to detection
- **Error Resolution Time**: Time from detection to resolution
- **Error Prevention Rate**: Reduction in recurring errors
- **Documentation Quality**: Completeness and accuracy of error docs

### AI Integration Metrics
- **AI Error Recognition Rate**: Percentage of errors AI can identify
- **AI Solution Accuracy**: Accuracy of AI-provided solutions
- **AI Learning Rate**: Improvement in AI error handling over time

---

**🔄 Last Updated**: {{ current_date }} | **{{ project_name }} Error Management**: Active | **Status**: Operational

**📍 File Location**: `{{ project_root }}/error-management/MASTER_ERROR_INDEX.md`
