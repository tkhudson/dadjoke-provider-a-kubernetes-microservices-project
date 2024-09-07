from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# in-memory storage for jokes. Plans on adding a database in the future.
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "Why don't eggs tell jokes? They'd crack each other up!",
]

@app.route('/joke', methods=['GET'])
def get_random_joke():
    return jsonify({"joke": random.choice(jokes)})

@app.route('/joke', methods=['POST'])
def add_joke():
    new_joke = request.json.get('joke')
    if new_joke:
        jokes.append(new_joke)
        return jsonify({"message": "Joke added successfully", "id": len(jokes) - 1}), 201
    return jsonify({"error": "No joke provided"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
