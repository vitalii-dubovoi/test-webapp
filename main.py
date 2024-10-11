from flask import Flask, request

app = Flask(__name__)

@app.route('/app', methods=['GET'])
def get_client_ip():
    # Get the client's IP address
    client_ip = request.remote_addr
    # Return the response with the client's IP
    return f"Hello there, your IP is - {client_ip}"

@app.route('/health', methods=['GET'])
def health_check():
    # Simply return a 200 OK status
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
