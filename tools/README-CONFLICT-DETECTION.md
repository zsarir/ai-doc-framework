# 📊 AI Documentation Conflict Detection System

## 🎯 Overview

The AI Documentation Conflict Detection System automatically identifies inconsistencies and conflicts in your AI documentation framework across multi-application projects.

## 🔍 What It Detects

### 1. AI_RULES Conflicts
- **Performance Conflicts**: Different timeout values, memory limits, response times
- **Security Conflicts**: Inconsistent JWT expiration, SSL versions, password requirements
- **Implementation Conflicts**: Different coding standards, frameworks, architectures
- **Architecture Conflicts**: Port conflicts, container naming, network configurations

### 2. Documentation Conflicts
- **Technical Specifications**: Conflicting API endpoints, database schemas
- **Configuration Values**: Different environment variables, service ports
- **Implementation Guidelines**: Inconsistent coding practices across docs

## 🚀 Quick Start

### Basic Usage
```bash
# Detect all conflicts (recommended)
python tools/conflict-detector.py

# Only check AI_RULES conflicts
python tools/conflict-detector.py --rules-only

# Only check documentation conflicts  
python tools/conflict-detector.py --docs-only

# Export as JSON report
python tools/conflict-detector.py --output json

# Export as HTML report
python tools/conflict-detector.py --output html

# Filter by severity (only show high and critical)
python tools/conflict-detector.py --severity high
```

### Advanced Usage
```bash
# Check specific application only
python tools/conflict-detector.py --app website

# Custom config file location
python tools/conflict-detector.py --config /path/to/ai-doc-config.json

# Export to specific file
python tools/conflict-detector.py --output html --output-file my-report.html

# Show only critical conflicts
python tools/conflict-detector.py --severity critical
```

## 📋 Command Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `--rules-only` | Check only AI_RULES conflicts | `--rules-only` |
| `--docs-only` | Check only documentation conflicts | `--docs-only` |
| `--app APP` | Check specific application only | `--app website` |
| `--output FORMAT` | Output format (console/json/html) | `--output json` |
| `--config PATH` | Custom config file path | `--config ./config.json` |
| `--severity LEVEL` | Minimum severity (low/medium/high/critical) | `--severity high` |
| `--output-file FILE` | Custom output file path | `--output-file report.html` |

## 📊 Conflict Types and Severity

### Severity Levels

#### 🚨 Critical
- Security conflicts (SSL versions, authentication methods)
- Safety rules (robot control systems)
- Data protection inconsistencies

#### ⚠️ High  
- Port conflicts
- JWT configuration differences
- Performance timeout mismatches

#### 📋 Medium
- Documentation inconsistencies
- Implementation style differences
- Framework version conflicts

#### 💡 Low
- Cosmetic differences
- Minor configuration variations
- Non-critical style preferences

### Conflict Categories

#### 🔒 Security Conflicts
```bash
Examples:
- JWT expiration: 24h vs 1h
- SSL version: 1.2 vs 1.3  
- Password length: 8 vs 12 chars
```

#### ⚡ Performance Conflicts
```bash
Examples:
- Timeout: 30s vs 60s
- Memory limit: 512MB vs 1GB
- Response time: 200ms vs 500ms
```

#### 🛠 Implementation Conflicts
```bash
Examples:
- CSS: Grid vs Flexbox
- Database: PostgreSQL vs MySQL
- Framework: Django vs FastAPI
```

#### 🏗 Architecture Conflicts
```bash
Examples:
- Port: 8000 vs 8001
- Container: app-web vs web-app
- Network: frontend vs front-net
```

## 📄 Report Formats

### Console Output (Default)
```bash
📊 AI DOCUMENTATION CONFLICT DETECTION REPORT
===============================================
🏗️  Project: My Multi-App Project
📅 Date: 2025-01-21T10:30:00
📋 Total Conflicts: 3

📊 SEVERITY BREAKDOWN:
   🚨 Critical: 1
   ⚠️  High: 1
   📋 Medium: 1

🔍 DETAILED CONFLICTS:
   1. 🚨 Security Configuration Conflict: website vs website-api
      📂 Category: security
      🎯 Applications: website, website-api
      📝 Description: Different JWT expiration times
      💡 Resolution: Standardize JWT expiration across applications
      🛠️  MANAGE_RULES Command:
         Update root security rule: Standardize JWT expiration from website (24h) and website-api (1h)
```

### JSON Output
```json
{
  "timestamp": "2025-01-21T10:30:00",
  "project_name": "My Multi-App Project",
  "total_conflicts": 3,
  "conflicts_by_severity": {
    "critical": 1,
    "high": 1,
    "medium": 1,
    "low": 0
  },
  "conflicts": [
    {
      "id": "security_website_website-api_12345",
      "type": "rule_conflict",
      "category": "security", 
      "severity": "critical",
      "title": "Security Configuration Conflict: website vs website-api",
      "applications": ["website", "website-api"],
      "resolution_suggestion": "Standardize JWT configuration",
      "manage_rules_command": "Update root security rule: Standardize JWT expiration"
    }
  ]
}
```

### HTML Output
- Professional web-based report
- Interactive conflict details
- Color-coded severity levels
- Copy-to-clipboard commands
- Responsive design for all devices

## 🛠 Integration with MANAGE_RULES.md

Every conflict report includes ready-to-use `MANAGE_RULES.md` commands:

### Example Resolution Commands
```bash
# Add standardized rule
"Add performance rule to root: All APIs under 150ms response time"

# Update conflicting rule  
"Update website security rule: JWT expiration from 24h to 1h"

# Remove outdated rule
"Remove deprecated authentication rule from website-api: Legacy OAuth method"
```

### Workflow Integration
1. **Detect Conflicts**: Run `python tools/conflict-detector.py`
2. **Review Report**: Analyze conflicts and severity
3. **Resolve Conflicts**: Use provided `MANAGE_RULES.md` commands
4. **Verify Resolution**: Re-run conflict detection
5. **Document Changes**: Update relevant documentation

## 📈 Conflict Detection Patterns

### Performance Pattern Detection
```python
performance_patterns = [
    r'timeout.*?(\d+).*?(second|minute|ms)',
    r'response.*?time.*?(\d+).*?(ms|second)', 
    r'memory.*?limit.*?(\d+).*?(mb|gb)',
    r'max.*?connections.*?(\d+)'
]
```

### Security Pattern Detection
```python
security_patterns = [
    r'jwt.*?expir.*?(\d+).*?(hour|minute|day)',
    r'password.*?length.*?(\d+)',
    r'ssl.*?version.*?(1\.\d|2\.\d|3\.\d)',
    r'rate.*?limit.*?(\d+)'
]
```

### Implementation Pattern Detection
```python
implementation_patterns = [
    r'use.*?(css grid|flexbox)',
    r'database.*?(postgres|mysql|sqlite)',
    r'framework.*?(django|fastapi|flask)',
    r'coding.*?style.*?(pep8|google|airbnb)'
]
```

## 🔧 Configuration

### ai-doc-config.json Integration
The conflict detector automatically reads your project configuration:
```json
{
  "project": {
    "name": "My Project",
    "type": "multi"
  },
  "applications": [
    {
      "name": "website",
      "type": "frontend", 
      "framework": "django"
    },
    {
      "name": "website-api",
      "type": "backend",
      "framework": "fastapi"
    }
  ]
}
```

### Custom Conflict Patterns
You can extend the conflict detection by modifying the patterns in `conflict-detector.py`:
```python
# Add custom patterns for your domain
custom_patterns = {
    'database': [
        r'connection.*?pool.*?(\d+)',
        r'query.*?timeout.*?(\d+)', 
        r'max.*?rows.*?(\d+)'
    ]
}
```

## 📊 Exit Codes

- **0**: No conflicts or only low/medium severity conflicts
- **1**: High or critical severity conflicts found
- **1**: Error during execution

## 🎯 Best Practices

### Regular Conflict Detection
```bash
# Run weekly conflict detection
0 9 * * 1 cd /path/to/project && python tools/conflict-detector.py --output html

# Run after major changes
git hook: python tools/conflict-detector.py --severity high
```

### Conflict Resolution Strategy
1. **Critical First**: Resolve security and safety conflicts immediately
2. **High Priority**: Address architecture and performance conflicts 
3. **Medium Priority**: Standardize implementation approaches
4. **Low Priority**: Address during regular maintenance

### Prevention
- **Code Reviews**: Include conflict detection in PR process
- **Documentation Standards**: Establish project-wide standards
- **Regular Audits**: Schedule monthly conflict detection reviews
- **Team Training**: Educate team on common conflict sources

## 🔗 Integration Points

### CI/CD Integration
```yaml
# GitHub Actions example
- name: Detect Documentation Conflicts
  run: |
    python tools/conflict-detector.py --severity high
    if [ $? -eq 1 ]; then
      echo "High/Critical conflicts found - failing build"
      exit 1
    fi
```

### Pre-commit Hook
```bash
#!/bin/sh
# .git/hooks/pre-commit
python tools/conflict-detector.py --rules-only --severity high
exit $?
```

## 📞 Troubleshooting

### Common Issues

#### "Config file not found"
```bash
Error: ai-doc-config.json not found at ./ai-doc-config.json
Solution: Run python tools/setup-wizard.py first
```

#### "No applications found"
```bash
Warning: No applications with AI_RULES.md found
Solution: Ensure applications have been set up with proper AI_RULES.md files
```

#### "Permission denied"
```bash
Error: Cannot read AI_RULES.md files
Solution: Check file permissions and project structure
```

### Performance Issues
- Large projects: Use `--app` flag to check specific applications
- Memory usage: Increase system memory for very large documentation sets
- Network issues: Ensure all file paths are accessible

## 📚 Related Documentation

- **[MANAGE_RULES.md](../MANAGE_RULES.md)**: Rule management system
- **[AI_RULES.md](../AI_RULES.md)**: Project-wide AI rules  
- **[USAGE.md](../USAGE.md)**: Complete framework usage guide
- **[Architecture Guide](../docs/pages/architecture.html)**: System architecture

---

**🎯 Keep your AI documentation system conflict-free and consistent!**

**🔄 Last Updated**: 2025-01-21 | **Conflict Detection**: Production Ready | **Integration**: Complete
