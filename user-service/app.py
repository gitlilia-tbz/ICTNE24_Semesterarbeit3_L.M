from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime
import uuid

app = Flask(__name__)
CORS(app)

DATA_FILE = 'data/users.json'

def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(users, f, indent=2)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "service": "user-service"})

@app.route('/users', methods=['GET'])
def get_users():
    users = load_users()
    return jsonify(list(users.values()))

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Name and email are required"}), 400
    
    users = load_users()
    
    # Check if email already exists
    for user in users.values():
        if user['email'] == data['email']:
            return jsonify({"error": "Email already exists"}), 400
    
    user_id = str(uuid.uuid4())
    user = {
        "id": user_id,
        "name": data['name'],
        "email": data['email'],
        "age": data.get('age'),
        "weight": data.get('weight'),
        "height": data.get('height'),
        "created_at": datetime.now().isoformat()
    }
    
    users[user_id] = user
    save_users(users)
    
    return jsonify(user), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    users = load_users()
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[user_id])

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    users = load_users()
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    user = users[user_id]
    
    for key in ['name', 'email', 'age', 'weight', 'height']:
        if key in data:
            user[key] = data[key]
    
    user['updated_at'] = datetime.now().isoformat()
    users[user_id] = user
    save_users(users)
    
    return jsonify(user)

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    users = load_users()
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    del users[user_id]
    save_users(users)
    
    return jsonify({"message": "User deleted successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)