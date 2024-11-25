import logging
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Configure logging to stdout
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

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
