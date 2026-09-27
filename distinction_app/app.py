import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    env = os.environ.get('APP_ENV', 'production')
    return f"SWE40006 Task 4.3 - Distinction Level. Running in {env} mode."

@app.route('/about')
def about():
    return "This is a Distinction-level Flask app with an optimized Dockerfile and public HTTP access."

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)