from flask import Flask, request

app = Flask(__name__)

@app.route('/app', methods=['GET'])
def get_client_ip():
    # Check if the request has the 'X-Forwarded-For' header
    if 'X-Forwarded-For' in request.headers:
        # Get the first IP in the 'X-Forwarded-For' header, which is the client's real IP
        client_ip = request.headers['X-Forwarded-For'].split(',')[0].strip()
    else:
        # Fall back to the direct remote address if 'X-Forwarded-For' is not present
        client_ip = request.remote_addr
    
    return f"Hello there, your IP is - {client_ip}"

@app.route('/health', methods=['GET'])
def health_check():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
