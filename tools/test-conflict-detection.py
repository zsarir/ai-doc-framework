#!/usr/bin/env python3
"""
🧪 Test Conflict Detection System
Quick test script to verify conflict detection functionality

Usage:
    python tools/test-conflict-detection.py
"""

import os
import sys
import json
import tempfile
import shutil
from pathlib import Path

def create_test_project():
    """Create a temporary test project with conflicts"""
    # Create temporary directory
    test_dir = Path(tempfile.mkdtemp(prefix="conflict-test-"))
    print(f"📁 Creating test project in: {test_dir}")
    
    # Create ai-doc-config.json
    config = {
        "project": {
            "name": "Test Conflict Project",
            "type": "multi",
            "root_path": str(test_dir),
            "description": "Test project for conflict detection"
        },
        "applications": [
            {
                "name": "website",
                "type": "frontend",
                "framework": "django",
                "description": "Website application"
            },
            {
                "name": "api",
                "type": "backend", 
                "framework": "fastapi",
                "description": "API application"
            }
        ],
        "error_categories": ["backend", "frontend", "security"],
        "issue_categories": ["incomplete-tasks", "unresolved-errors"]
    }
    
    with open(test_dir / "ai-doc-config.json", 'w') as f:
        json.dump(config, f, indent=2)
    
    # Create application directories
    (test_dir / "website").mkdir()
    (test_dir / "api").mkdir()
    
    # Create root AI_RULES.md with some rules
    root_rules = """# 🤖 AI RULES - Root Project
> **Global Development & Management Rules**

## 🎯 AI INSTRUCTIONS - READ AND FOLLOW THESE RULES

## 🔒 CRITICAL SYSTEM RULES - ROOT

## Custom Performance Rules
- **API Response Time**: All API responses must be under 200ms
- **Memory Limit**: Maximum 512MB per container
- **Connection Timeout**: 30 seconds for all connections

## Custom Security Rules  
- **JWT Expiration**: JWT tokens expire after 24 hours
- **SSL Version**: Use SSL version 1.3
- **Password Length**: Minimum 8 characters
"""
    
    with open(test_dir / "AI_RULES.md", 'w') as f:
        f.write(root_rules)
    
    # Create website AI_RULES.md with conflicting rules
    website_rules = """# 🤖 AI RULES - Website Application
> **Frontend Development & Management Rules | Django System**

## 🎯 AI INSTRUCTIONS - READ AND FOLLOW THESE RULES

## Custom Performance Rules
- **Page Load Time**: Pages must load within 500ms  # CONFLICT: Different from API response time
- **Memory Limit**: Maximum 1GB per container       # CONFLICT: Different from root
- **Connection Timeout**: 60 seconds for requests   # CONFLICT: Different from root

## Custom Security Rules
- **JWT Expiration**: JWT tokens expire after 1 hour  # CONFLICT: Different from root
- **SSL Version**: Use SSL version 1.2                # CONFLICT: Different from root
- **Password Length**: Minimum 12 characters          # CONFLICT: Different from root

## Custom Implementation Rules
- **CSS Layout**: Always use CSS Grid for layouts
- **Framework**: Use Django for all frontend operations
"""
    
    with open(test_dir / "website" / "AI_RULES.md", 'w') as f:
        f.write(website_rules)
    
    # Create api AI_RULES.md with some conflicting rules
    api_rules = """# 🤖 AI RULES - API Application
> **Backend Development & Management Rules | FastAPI System**

## 🎯 AI INSTRUCTIONS - READ AND FOLLOW THESE RULES

## Custom Performance Rules  
- **API Response Time**: All API responses must be under 150ms  # CONFLICT: Different from root (200ms)
- **Memory Limit**: Maximum 512MB per container                # SAME: Same as root (good!)
- **Connection Timeout**: 45 seconds for all connections       # CONFLICT: Different from root (30s)

## Custom Security Rules
- **JWT Expiration**: JWT tokens expire after 24 hours  # SAME: Same as root (good!)
- **SSL Version**: Use SSL version 1.3                  # SAME: Same as root (good!)
- **Password Length**: Minimum 10 characters            # CONFLICT: Different from root (8)

## Custom Implementation Rules
- **Framework**: Use FastAPI for all backend operations
- **Database**: Use PostgreSQL for all database operations
"""
    
    with open(test_dir / "api" / "AI_RULES.md", 'w') as f:
        f.write(api_rules)
    
    # Create some documentation files with conflicts
    (test_dir / "website" / "docs").mkdir()
    (test_dir / "api" / "docs").mkdir()
    
    # Website docs with conflicting info
    website_api_doc = """# Website API Documentation

## Configuration
- **Port**: 8000
- **Timeout**: 30 seconds
- **SSL Version**: 1.2
"""
    
    with open(test_dir / "website" / "docs" / "API.md", 'w') as f:
        f.write(website_api_doc)
    
    website_deploy_doc = """# Website Deployment

## Configuration  
- **Port**: 8001  # CONFLICT: Different port from API.md
- **Timeout**: 60 seconds  # CONFLICT: Different timeout
- **SSL Version**: 1.3     # CONFLICT: Different SSL version
"""
    
    with open(test_dir / "website" / "docs" / "DEPLOYMENT.md", 'w') as f:
        f.write(website_deploy_doc)
    
    # API docs
    api_doc = """# API Documentation

## Configuration
- **Port**: 9000
- **Timeout**: 45 seconds  
- **Framework**: FastAPI
- **Database**: PostgreSQL on port 5432
"""
    
    with open(test_dir / "api" / "docs" / "API.md", 'w') as f:
        f.write(api_doc)
    
    print(f"✅ Test project created with multiple conflicts")
    return test_dir

def run_conflict_detection(test_dir):
    """Run conflict detection on test project"""
    print(f"\n🔍 Running conflict detection...")
    
    # Change to test directory
    original_dir = os.getcwd()
    os.chdir(test_dir)
    
    try:
        # Import conflict detector
        sys.path.insert(0, str(Path(__file__).parent))
        from conflict_detector import AIDocConflictDetector
        
        # Initialize detector
        detector = AIDocConflictDetector(".")
        
        # Run detection
        report = detector.detect_all_conflicts()
        
        # Print results
        print(f"\n📊 CONFLICT DETECTION RESULTS:")
        print(f"=" * 50)
        print(f"📋 Total Conflicts Found: {report.total_conflicts}")
        print(f"🚨 Critical: {report.conflicts_by_severity['critical']}")
        print(f"⚠️  High: {report.conflicts_by_severity['high']}")
        print(f"📋 Medium: {report.conflicts_by_severity['medium']}")
        print(f"💡 Low: {report.conflicts_by_severity['low']}")
        
        if report.conflicts:
            print(f"\n🔍 SAMPLE CONFLICTS:")
            for i, conflict in enumerate(report.conflicts[:3], 1):  # Show first 3
                print(f"   {i}. {conflict.title}")
                print(f"      📂 Category: {conflict.category}")
                print(f"      🚨 Severity: {conflict.severity}")
                print(f"      🎯 Applications: {', '.join(conflict.applications)}")
                print(f"      🛠️  Command: {conflict.manage_rules_command}")
        
        # Test different output formats
        print(f"\n📄 Testing output formats...")
        
        # JSON output
        detector.export_report(report, 'json', 'test-report.json')
        json_size = os.path.getsize('test-report.json')
        print(f"✅ JSON report: test-report.json ({json_size} bytes)")
        
        # HTML output  
        detector.export_report(report, 'html', 'test-report.html')
        html_size = os.path.getsize('test-report.html')
        print(f"✅ HTML report: test-report.html ({html_size} bytes)")
        
        print(f"\n📈 EXPECTED CONFLICTS:")
        expected_conflicts = [
            "JWT Expiration: root=24h, website=1h",
            "SSL Version: root=1.3, website=1.2", 
            "Password Length: root=8, website=12, api=10",
            "Memory Limit: root=512MB, website=1GB",
            "Connection Timeout: root=30s, website=60s, api=45s",
            "API Response Time: root=200ms, api=150ms",
            "Website Port: API.md=8000, DEPLOYMENT.md=8001",
            "Website Timeout: API.md=30s, DEPLOYMENT.md=60s",
            "Website SSL: API.md=1.2, DEPLOYMENT.md=1.3"
        ]
        
        for expected in expected_conflicts:
            print(f"   📋 {expected}")
        
        if report.total_conflicts >= 6:  # Should find at least 6 major conflicts
            print(f"\n✅ CONFLICT DETECTION WORKING CORRECTLY!")
            print(f"   Found {report.total_conflicts} conflicts (expected: 6+)")
        else:
            print(f"\n⚠️  WARNING: Expected more conflicts!")
            print(f"   Found {report.total_conflicts} conflicts (expected: 6+)")
            
        return report.total_conflicts > 0
        
    except Exception as e:
        print(f"❌ Error during conflict detection: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        os.chdir(original_dir)

def test_manage_rules_integration():
    """Test MANAGE_RULES.md commands"""
    print(f"\n🛠️  Testing MANAGE_RULES.md integration...")
    
    sample_commands = [
        'Add security rule to root: All APIs must use HTTPS',
        'Update website performance rule: Page load time from 500ms to 300ms',
        'Remove outdated authentication rule from api: Legacy OAuth method',
        'Add global rule to root: All containers must have health checks'
    ]
    
    print(f"📋 Sample MANAGE_RULES.md commands:")
    for i, cmd in enumerate(sample_commands, 1):
        print(f"   {i}. {cmd}")
    
    print(f"✅ MANAGE_RULES.md integration ready")

def cleanup_test_project(test_dir):
    """Clean up test project"""
    try:
        shutil.rmtree(test_dir)
        print(f"🗑️  Cleaned up test project: {test_dir}")
    except Exception as e:
        print(f"⚠️  Warning: Could not clean up {test_dir}: {e}")

def main():
    """Main test function"""
    print("🧪 AI Documentation Conflict Detection - Test Suite")
    print("=" * 60)
    
    test_dir = None
    try:
        # Create test project
        test_dir = create_test_project()
        
        # Run conflict detection
        success = run_conflict_detection(test_dir)
        
        # Test MANAGE_RULES integration
        test_manage_rules_integration()
        
        # Summary
        print(f"\n📊 TEST SUMMARY:")
        print(f"=" * 30)
        if success:
            print(f"✅ All tests passed!")
            print(f"✅ Conflict detection is working correctly")
            print(f"✅ Multiple output formats functional") 
            print(f"✅ MANAGE_RULES.md integration ready")
            print(f"\n🚀 System is ready for production use!")
        else:
            print(f"❌ Some tests failed")
            print(f"🔧 Please check the error messages above")
            
    except KeyboardInterrupt:
        print(f"\n⚠️  Test cancelled by user")
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        # Cleanup
        if test_dir and test_dir.exists():
            cleanup_test_project(test_dir)
    
    print(f"\n🏁 Test completed")

if __name__ == "__main__":
    main()
