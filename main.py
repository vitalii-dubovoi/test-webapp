from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/app', methods=['GET'])
def get_client_headers():
    # Get all request headers from the client
    headers = {key: value for key, value in request.headers.items()}
    return jsonify(headers)

@app.route('/health', methods=['GET'])
def health_check():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
