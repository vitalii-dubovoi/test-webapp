from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/environment', methods=['GET'])
def get_environment_variables():
    # Convert environment variables to a dictionary and return as JSON
    env_variables = dict(os.environ)
    return jsonify(env_variables)

@app.route('/health', methods=['GET'])
def health_check():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
