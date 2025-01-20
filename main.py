import logging
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Configure logging to stdout
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

@app.route('/', methods=['GET'])
def greetings():
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    message = f"Hi there, are you coming from {ip_address}?"
    logger.info(f"Greeting endpoint called. IP Address: {ip_address}")
    return message
    

@app.route('/environment', methods=['GET'])
def get_environment_variables():
    env_variables = dict(os.environ)
    logger.info("Environment variables accessed")
    return jsonify(env_variables)

@app.route('/health', methods=['GET'])
def health_check():
    logger.info("Health check endpoint called")
    return 'OK', 200

if __name__ == '__main__':
    logger.info("Starting Flask application")
    app.run(host='0.0.0.0', port=5000)
