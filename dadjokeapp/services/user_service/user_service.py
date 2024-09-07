from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# in-memory storage for users. Plans on adding a database in the future.
users = {}

@app.route('/user', methods=['POST'])
def create_user():
    username = request.json.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    user_id = str(uuid.uuid4())
    users[user_id] = {
        "id": user_id,
        "username": username,
        "favorite_jokes": []
    }
    return jsonify({"message": "User created successfully", "user_id": user_id}), 201

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/user/<user_id>/favorite', methods=['POST'])
def add_favorite_joke(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    joke = request.json.get('joke')
    if not joke:
        return jsonify({"error": "Joke is required"}), 400
    
    user['favorite_jokes'].append(joke)
    return jsonify({"message": "Joke added to favorites"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
