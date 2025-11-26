#!/usr/bin/env python3
"""
Demo Flask application using vulnerable dependencies
for testing the resolved vulnerabilities feature.
"""

import os
from flask import Flask, render_template_string, request
import requests
from PIL import Image
import yaml
from datetime import datetime

app = Flask(__name__)

# Simple HTML template
TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Vulnerability Test App</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .container { max-width: 800px; margin: 0 auto; }
        .vulnerability { background: #fff3cd; padding: 10px; margin: 10px 0; border-radius: 5px; }
        .safe { background: #d4edda; padding: 10px; margin: 10px 0; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 Vulnerability Test Application</h1>
        <p>This Flask app demonstrates dependencies with known vulnerabilities.</p>
        
        <div class="vulnerability">
            <h3>⚠️ Vulnerable Dependencies Used:</h3>
            <ul>
                <li><strong>Django {{ django_version }}</strong> - Multiple vulnerabilities</li>
                <li><strong>Requests {{ requests_version }}</strong> - SSL verification issues</li>
                <li><strong>Pillow {{ pillow_version }}</strong> - Image processing vulnerabilities</li>
                <li><strong>PyYAML {{ yaml_version }}</strong> - Unsafe loading vulnerabilities</li>
                <li><strong>Flask {{ flask_version }}</strong> - Various security issues</li>
            </ul>
        </div>
        
        <div class="safe">
            <h3>✅ When Fixed:</h3>
            <p>This PR should show positive feedback about resolved vulnerabilities!</p>
        </div>
        
        <p><strong>Current Time:</strong> {{ current_time }}</p>
        <p><strong>Python Version:</strong> {{ python_version }}</p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    """Main page showing vulnerable dependencies info"""
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
    """Test endpoint that uses requests library"""
    try:
        # Simple request to test requests library
        response = requests.get('https://httpbin.org/json', timeout=5)
        return f"<h1>Requests Test</h1><p>Status: {response.status_code}</p><pre>{response.text}</pre>"
    except Exception as e:
        return f"<h1>Requests Test Failed</h1><p>Error: {str(e)}</p>"

if __name__ == '__main__':
    # Development server
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))