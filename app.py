from flask import Flask, send_from_directory, Response, jsonify
import requests

app = Flask(__name__)
HOMEWIZARD_URL = "http://192.168.50.57/api/v1/data"

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/data')
def data():
    try:
        resp = requests.get(HOMEWIZARD_URL, timeout=5)
        resp.raise_for_status()
        return Response(resp.content, status=resp.status_code, content_type=resp.headers.get('Content-Type', 'application/json'))
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
