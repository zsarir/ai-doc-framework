# 📋 ERROR TEMPLATE - {{ project_name }} Project
> **Standardized Error Documentation Template**

## 🎯 AI INSTRUCTIONS - READ THIS FIRST

**Purpose**: This template provides a standardized format for documenting errors across the {{ project_name }} project. Use this template when creating new error documentation entries.

## 📋 ERROR DOCUMENTATION TEMPLATE

```markdown
---
error_id: "[CATEGORY]-[YYYY-MM-DD]-[SEQUENCE]"
category: "[backend|frontend|infrastructure|security|database|deployment|cross-cutting]"
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

# [ERROR TITLE]

## 🐛 Error Description
[Provide a clear, concise description of the error. Include the exact error message if available.]

## 🔍 Error Details
- **Error Type**: [Type of error - e.g., RuntimeError, ValidationError, ConnectionError]
- **Error Code**: [Error code if applicable - e.g., HTTP 500, SQL 23505]
- **Location**: [Where the error occurred - file path, function, line number]
- **Context**: [Context in which error occurred - user action, system state, etc.]
- **Stack Trace**: [Include relevant stack trace if available]

## 🚫 Impact
[Describe the impact of this error on the system, users, or business operations]

### Affected Systems
- [List affected systems, services, or components]
- [Describe how the error affects each component]

### User Impact
- [Describe how this error affects end users]
- [Include any error messages users see]

## 🔍 Root Cause Analysis

### Primary Cause
[Identify the primary cause of the error]

### Contributing Factors
- [Factor 1: Description]
- [Factor 2: Description]
- [Factor 3: Description]

### Why Not Caught Earlier
[Explain why this error wasn't caught by existing tests, monitoring, or validation]

## 🔧 Resolution

### Solution Implemented
[Describe the solution that was implemented to resolve the error]

### Code Changes
```[language]
// Before (problematic code)
[Show the problematic code]

// After (fixed code)
[Show the corrected code]
```

### Configuration Changes
[Describe any configuration changes made]

### Database Changes
[Describe any database schema or data changes]

### Infrastructure Changes
[Describe any infrastructure or deployment changes]

## ✅ Verification

### Testing Performed
- [ ] Unit tests updated and passing
- [ ] Integration tests updated and passing
- [ ] Manual testing completed
- [ ] Regression testing completed
- [ ] Performance testing (if applicable)

### Test Results
[Include test results, coverage metrics, or performance improvements]

### Regression Checklist
- [ ] Error no longer occurs in development
- [ ] Error no longer occurs in staging
- [ ] Error no longer occurs in production
- [ ] No new errors introduced
- [ ] Performance not degraded
- [ ] Functionality maintained

## 🛡️ Prevention Strategies

### Immediate Prevention
- [Action 1: Description]
- [Action 2: Description]
- [Action 3: Description]

### Long-term Prevention
- [Strategy 1: Description]
- [Strategy 2: Description]
- [Strategy 3: Description]

### Monitoring and Detection
- [Monitoring 1: Description]
- [Monitoring 2: Description]
- [Alerting: Description]

## 📚 Cross-References

### Related Documentation
- [Link to relevant documentation]
- [Link to related guides]
- [Link to configuration files]

### Related Errors
- [Link to similar errors]
- [Link to related error patterns]

### External Resources
- [Link to external documentation]
- [Link to community discussions]
- [Link to vendor documentation]

## 📊 Investigation Timeline

### Timeline of Events
| Time | Action | Result | Next Step |
|------|--------|--------|-----------|
| [Time] | [Action taken] | [Result] | [Next step] |
| [Time] | [Action taken] | [Result] | [Next step] |
| [Time] | [Action taken] | [Result] | [Next step] |

### Key Decisions Made
- [Decision 1: Rationale]
- [Decision 2: Rationale]
- [Decision 3: Rationale]

## 🏷️ Tags and Keywords
[Add relevant tags for easy discovery and categorization]

---

**🔄 Last Updated**: [Date] | **Status**: [Active/Resolved] | **Category**: [Category]

**📍 File Location**: `[path-to-error-file]`
```

## 🎯 TEMPLATE USAGE INSTRUCTIONS

### For AI
1. **Copy this template** when documenting a new error
2. **Fill in all required fields** in the YAML front matter
3. **Provide detailed information** in each section
4. **Use consistent formatting** and language
5. **Include relevant code snippets** and examples
6. **Add appropriate tags** for categorization

### Required Fields
- **error_id**: Unique identifier for the error
- **category**: Primary error category
- **severity**: Impact level of the error
- **status**: Current status of error resolution
- **first_occurrence**: When the error was first encountered
- **affected_environments**: Which environments are affected
- **tags**: Keywords for search and categorization

### Optional Fields
- **resolution_date**: When the error was resolved
- **resolution_time_hours**: Time taken to resolve
- **ai_confidence_score**: AI's confidence in the solution
- **pattern_signatures**: Regex patterns for automatic detection
- **assignee**: Person responsible for resolution
- **reviewer**: Person who reviewed the resolution

## 📋 TEMPLATE VARIATIONS

### Critical Error Template
For critical errors, include additional sections:
- **Emergency Response**: Immediate actions taken
- **Business Impact**: Financial or operational impact
- **Communication Plan**: How stakeholders were informed
- **Post-Incident Review**: Lessons learned and improvements

### Recurring Error Template
For recurring errors, include additional sections:
- **Recurrence Pattern**: How often the error occurs
- **Trigger Conditions**: What causes the error to recur
- **Previous Attempts**: Previous resolution attempts
- **Prevention Measures**: Measures to prevent recurrence

### Security Error Template
For security-related errors, include additional sections:
- **Vulnerability Assessment**: Security implications
- **Attack Vector**: How the vulnerability could be exploited
- **Security Measures**: Additional security measures implemented
- **Compliance Impact**: Impact on compliance requirements

---

**🔄 Last Updated**: {{ current_date }} | **{{ project_name }} Error Template**: Standard | **Status**: Active

**📍 File Location**: `{{ project_root }}/error-management/ERROR_TEMPLATE.md`
