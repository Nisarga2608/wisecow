from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Wisecow Application!"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "message": "Hello, this is Wisecow!",
        "status": "success"
    }
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    new_data = request.json
    response = {
        "message": "Data received!",
        "received_data": new_data,
        "status": "success"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

