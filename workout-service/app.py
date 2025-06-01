from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import requests
from datetime import datetime
import uuid

app = Flask(__name__)
CORS(app)

DATA_FILE = 'data/workouts.json'
USER_SERVICE_URL = os.getenv('USER_SERVICE_URL', 'http://localhost:5001')

def load_workouts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_workouts(workouts):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(workouts, f, indent=2)

def verify_user_exists(user_id):
    try:
        response = requests.get(f"{USER_SERVICE_URL}/users/{user_id}")
        return response.status_code == 200
    except:
        return False

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "service": "workout-service"})

@app.route('/workouts', methods=['GET'])
def get_workouts():
    user_id = request.args.get('user_id')
    workouts = load_workouts()
    
    if user_id:
        user_workouts = [w for w in workouts.values() if w['user_id'] == user_id]
        return jsonify(user_workouts)
    
    return jsonify(list(workouts.values()))

@app.route('/workouts', methods=['POST'])
def create_workout():
    data = request.get_json()
    
    required_fields = ['user_id', 'exercise_type', 'duration', 'calories_burned']
    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    
    # Verify user exists
    if not verify_user_exists(data['user_id']):
        return jsonify({"error": "User not found"}), 404
    
    workouts = load_workouts()
    
    workout_id = str(uuid.uuid4())
    workout = {
        "id": workout_id,
        "user_id": data['user_id'],
        "exercise_type": data['exercise_type'],
        "duration": data['duration'],  # in minutes
        "calories_burned": data['calories_burned'],
        "notes": data.get('notes', ''),
        "date": data.get('date', datetime.now().strftime('%Y-%m-%d')),
        "created_at": datetime.now().isoformat()
    }
    
    workouts[workout_id] = workout
    save_workouts(workouts)
    
    return jsonify(workout), 201

@app.route('/workouts/<workout_id>', methods=['GET'])
def get_workout(workout_id):
    workouts = load_workouts()
    if workout_id not in workouts:
        return jsonify({"error": "Workout not found"}), 404
    return jsonify(workouts[workout_id])

@app.route('/workouts/<workout_id>', methods=['PUT'])
def update_workout(workout_id):
    workouts = load_workouts()
    if workout_id not in workouts:
        return jsonify({"error": "Workout not found"}), 404
    
    data = request.get_json()
    workout = workouts[workout_id]
    
    for key in ['exercise_type', 'duration', 'calories_burned', 'notes', 'date']:
        if key in data:
            workout[key] = data[key]
    
    workout['updated_at'] = datetime.now().isoformat()
    workouts[workout_id] = workout
    save_workouts(workouts)
    
    return jsonify(workout)

@app.route('/workouts/<workout_id>', methods=['DELETE'])
def delete_workout(workout_id):
    workouts = load_workouts()
    if workout_id not in workouts:
        return jsonify({"error": "Workout not found"}), 404
    
    del workouts[workout_id]
    save_workouts(workouts)
    
    return jsonify({"message": "Workout deleted successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)