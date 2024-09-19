from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


JOKE_SERVICE_URL = "http://localhost:5000"
USER_SERVICE_URL = "http://localhost:5001"

@app.route('/joke', methods=['GET'])
def get_joke():
    response = requests.get(f"{JOKE_SERVICE_URL}/joke")
    return jsonify(response.json()), response.status_code

@app.route('/joke', methods=['POST'])
def add_joke():
    response = requests.post(f"{JOKE_SERVICE_URL}/joke", json=request.json)
    return jsonify(response.json()), response.status_code

@app.route('/user', methods=['POST'])
def create_user():
    response = requests.post(f"{USER_SERVICE_URL}/user", json=request.json)
    return jsonify(response.json()), response.status_code

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    response = requests.get(f"{USER_SERVICE_URL}/user/{user_id}")
    return jsonify(response.json()), response.status_code

@app.route('/user/<user_id>/favorite', methods=['POST'])
def add_favorite_joke(user_id):
    response = requests.post(f"{USER_SERVICE_URL}/user/{user_id}/favorite", json=request.json)
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
