from flask import Flask, request

app = Flask(__name__)

@app.route('/app', methods=['GET'])
def get_client_ip():
    return f"Hello there"

@app.route('/health', methods=['GET'])
def health_check():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
