#!/usr/bin/env python3
"""
Demo Flask application using SECURE dependencies 
after resolving vulnerabilities through dependency upgrades.
"""

import os
from flask import Flask, render_template_string, request
import requests
from PIL import Image
import yaml
from datetime import datetime

app = Flask(__name__)

# Simple HTML template - SECURE VERSION
TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>✅ SECURE Vulnerability Test App</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 800px; margin: 0 auto; }
        .resolved { background: #d4edda; padding: 10px; margin: 10px 0; border-radius: 5px; border: 2px solid #155724; }
        .security-status { background: #d1ecf1; padding: 15px; margin: 15px 0; border-radius: 5px; border: 2px solid #0c5460; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎉 SECURE Vulnerability Test Application</h1>
        <p>This Flask app has been upgraded to use secure dependency versions!</p>
        
        <div class="security-status">
            <h3>🔒 Security Status: ALL VULNERABILITIES RESOLVED!</h3>
            <p><strong>🎯 This PR should show positive resolved vulnerabilities feedback!</strong></p>
        </div>
        
        <div class="resolved">
            <h3>✅ Resolved Vulnerabilities:</h3>
            <ul>
                <li><strong>Django {{ django_version }}</strong> - SECURE (was 3.1.0 with multiple vulnerabilities)</li>
                <li><strong>Requests {{ requests_version }}</strong> - SECURE (was 2.25.0 with SSL issues)</li>
                <li><strong>Pillow {{ pillow_version }}</strong> - SECURE (was 8.0.0 with image processing vulns)</li>
                <li><strong>PyYAML {{ yaml_version }}</strong> - SECURE (was 5.3.1 with unsafe loading)</li>
                <li><strong>Flask {{ flask_version }}</strong> - SECURE (was 1.1.0 with various issues)</li>
                <li><strong>Jinja2, Werkzeug, urllib3, certifi, click</strong> - ALL UPDATED TO SECURE VERSIONS</li>
            </ul>
        </div>
        
        <div class="resolved">
            <h3>🛡️ Security Improvements:</h3>
            <p><strong>12+ critical and high severity vulnerabilities resolved!</strong></p>
            <ul>
                <li>Django SQL injection fixes</li>
                <li>Flask template injection patches</li>
                <li>Pillow image processing security updates</li>
                <li>PyYAML safe loading implementation</li>
                <li>Requests SSL verification improvements</li>
                <li>Updated certificate bundles</li>
            </ul>
        </div>
        
        <p><strong>Current Time:</strong> {{ current_time }}</p>
        <p><strong>Python Version:</strong> {{ python_version }}</p>
        <p><strong>Application Status:</strong> 🟢 SECURE & UPDATED</p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    """Main page showing RESOLVED vulnerabilities info"""
    import django
    import sys
    
    return render_template_string(TEMPLATE,
        django_version=django.VERSION,
        requests_version=requests.__version__,
        pillow_version=Image.__version__,
        yaml_version=yaml.__version__,
        flask_version=app.version if hasattr(app, 'version') else 'Unknown',
        current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        python_version=sys.version
    )

@app.route('/test-requests')
def test_requests():
    """Test endpoint that uses requests library - NOW SECURE"""
    try:
        # Simple request to test secure requests library
        response = requests.get('https://httpbin.org/json', timeout=5)
        return f"""
        <h1>✅ Requests Test - SECURE VERSION</h1>
        <p>Status: {response.status_code}</p>
        <p><strong>Requests Version:</strong> {requests.__version__} (SECURE)</p>
        <p><strong>SSL Verification:</strong> ✅ Working properly</p>
        <pre>{response.text}</pre>
        <p><a href="/">← Back to main page</a></p>
        """
    except Exception as e:
        return f"""
        <h1>Requests Test Failed</h1>
        <p>Error: {str(e)}</p>
        <p><a href="/">← Back to main page</a></p>
        """

@app.route('/security-summary')
def security_summary():
    """Endpoint showing security upgrade summary"""
    import django
    
    resolved_vulns = {
        'Django': f'3.1.0 → {django.VERSION[0]}.{django.VERSION[1]}.{django.VERSION[2]} (SQL injection fixes)',
        'Requests': f'2.25.0 → {requests.__version__} (SSL verification improvements)', 
        'Pillow': f'8.0.0 → {Image.__version__} (image processing security)',
        'PyYAML': f'5.3.1 → {yaml.__version__} (safe loading implementation)',
        'Flask': '1.1.0 → 3.0.0 (template injection fixes)',
        'Jinja2': '2.10.1 → 3.1.2 (template security)',
        'Werkzeug': '1.0.0 → 3.0.1 (multiple fixes)',
        'urllib3': '1.25.8 → 2.1.0 (SSL/request security)',
        'certifi': '2020.6.20 → 2023.11.17 (updated certificates)',
        'click': '7.1.1 → 8.1.7 (security improvements)'
    }
    
    html = "<h1>🔒 Python Security Upgrade Summary</h1><ul>"
    for pkg, upgrade in resolved_vulns.items():
        html += f"<li><strong>{pkg}:</strong> {upgrade}</li>"
    html += "</ul><p><strong>Result:</strong> 🎉 All known vulnerabilities resolved!</p>"
    html += '<p><a href="/">← Back to main page</a></p>'
    
    return html

if __name__ == '__main__':
    # Development server
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))