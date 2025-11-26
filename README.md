# 🐍 Test Resolved Vulnerabilities - Python

This repository demonstrates the **resolved vulnerabilities feedback** feature in dependency-review-action using Python dependencies.

## Overview

This repository contains a Flask web application with intentionally vulnerable Python packages to test the positive feedback when security issues are resolved.

## Vulnerable Dependencies

The `requirements.txt` includes packages with known vulnerabilities:

- **Django 3.1.0** - Multiple security vulnerabilities
- **requests 2.25.0** - SSL certificate verification issues
- **Pillow 8.0.0** - Image processing vulnerabilities
- **PyYAML 5.3.1** - Unsafe YAML loading vulnerabilities
- **Flask 1.1.1** - Various security issues in older versions
- **jinja2 2.10.1** - Template injection vulnerabilities
- **werkzeug 1.0.0** - Debug mode vulnerabilities
- **urllib3 1.25.8** - Various HTTP client vulnerabilities

## Demo Application

The repository includes a simple Flask web application (`app.py`) that:
- Uses multiple vulnerable dependencies
- Displays information about current package versions
- Provides test endpoints to demonstrate functionality
- Shows which vulnerabilities exist

## Testing the Feature

### 🚀 Quick Test

1. **View the existing PR** (if available) or create a new one
2. **Upgrade/remove vulnerable packages** in `requirements.txt`:
   ```
   Django>=4.2.0
   requests>=2.28.0
   Pillow>=9.0.0
   PyYAML>=6.0
   Flask>=2.2.0
   jinja2>=3.1.0
   werkzeug>=2.2.0
   urllib3>=1.26.0
   ```
3. **Create PR** and watch the resolved vulnerabilities feedback!

### 📋 Expected Results

**In PR Comments:**
```
🎉 **8+ vulnerabilities resolved** by upgrading Python packages:

| Package | Old Version | Severity | Advisory |
|---------|-------------|----------|----------|
| Django | 3.1.0 | High | Multiple Django vulnerabilities |
| requests | 2.25.0 | Moderate | SSL verification bypass |
| Pillow | 8.0.0 | High | Image processing vulnerabilities |
...
```

**In Action Logs:**
- Detailed Python vulnerability information
- JSON output for automation
- Package-specific security details

## Testing Scenarios

### Scenario 1: Upgrade All Packages
```bash
git checkout -b upgrade-all-python-deps
# Update requirements.txt with latest secure versions
git commit -m "feat: upgrade all Python dependencies to resolve vulnerabilities"
```

### Scenario 2: Remove Unnecessary Packages
```bash
git checkout -b remove-unused-python-deps  
# Remove Django, Pillow, and other unused packages
git commit -m "feat: remove unused Python packages with vulnerabilities"
```

### Scenario 3: Mixed Changes
```bash
git checkout -b mixed-python-changes
# Upgrade some packages, remove others, keep some as-is
git commit -m "feat: mixed Python dependency security improvements"
```

## Workflow Features

The GitHub Actions workflow (`.github/workflows/test-resolved-vulnerabilities.yml`):
- ✅ Tests with Python 3.9
- ✅ Installs dependencies for validation
- ✅ Uses `david-wiggs/dependency-review-action@main`
- ✅ Shows Python-specific resolved vulnerability output
- ✅ Includes application testing

## Running Locally

```bash
# Install dependencies (in virtual environment recommended)
pip install -r requirements.txt

# Run the demo application
python app.py

# Visit http://localhost:5000 to see vulnerability info
```

## Security Notes

⚠️ **Important**: This repository contains intentionally vulnerable dependencies for testing purposes. Do not use in production!

✅ **After testing**: Upgrade to secure versions of all packages.

## Integration with CI/CD

The resolved vulnerabilities feature provides:
- **JSON output** for automation scripts
- **Positive feedback** to encourage security improvements
- **Detailed logging** for security auditing
- **Multi-language support** across Python, Node.js, Java, etc.

---

**Ready to test?** Create a PR that upgrades the vulnerable Python packages and see the resolved vulnerabilities feature in action! 🚀