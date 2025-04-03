"""
Simple Flask test application to verify Docker networking
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello from Edmonton Docker Test</h1><p>If you can see this, Docker networking is working correctly!</p>"

if __name__ == '__main__':
    # This is crucial - bind to 0.0.0.0 for Docker
    app.run(host='0.0.0.0', port=5000, debug=True)