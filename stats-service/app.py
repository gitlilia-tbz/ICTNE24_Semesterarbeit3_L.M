from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from datetime import datetime, timedelta
from collections import defaultdict

app = Flask(__name__)
CORS(app)

WORKOUT_SERVICE_URL = os.getenv('WORKOUT_SERVICE_URL', 'http://localhost:5002')

def get_user_workouts(user_id):
    try:
        response = requests.get(f"{WORKOUT_SERVICE_URL}/workouts?user_id={user_id}")
        if response.status_code == 200:
            return response.json()
        return []
    except:
        return []

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "service": "stats-service"})

@app.route('/stats/<user_id>/summary', methods=['GET'])
def get_user_stats_summary(user_id):
    workouts = get_user_workouts(user_id)
    
    if not workouts:
        return jsonify({
            "total_workouts": 0,
            "total_duration": 0,
            "total_calories": 0,
            "average_duration": 0,
            "average_calories": 0
        })
    
    total_workouts = len(workouts)
    total_duration = sum(w['duration'] for w in workouts)
    total_calories = sum(w['calories_burned'] for w in workouts)
    
    return jsonify({
        "total_workouts": total_workouts,
        "total_duration": total_duration,
        "total_calories": total_calories,
        "average_duration": round(total_duration / total_workouts, 2),
        "average_calories": round(total_calories / total_workouts, 2)
    })

@app.route('/stats/<user_id>/weekly', methods=['GET'])
def get_weekly_stats(user_id):
    workouts = get_user_workouts(user_id)
    
    # Group workouts by week
    today = datetime.now().date()
    week_start = today - timedelta(days=today.weekday())
    
    weekly_stats = defaultdict(lambda: {"workouts": 0, "duration": 0, "calories": 0})
    
    for workout in workouts:
        workout_date = datetime.strptime(workout['date'], '%Y-%m-%d').date()
        week_start_for_workout = workout_date - timedelta(days=workout_date.weekday())
        week_key = week_start_for_workout.strftime('%Y-%m-%d')
        
        weekly_stats[week_key]["workouts"] += 1
        weekly_stats[week_key]["duration"] += workout['duration']
        weekly_stats[week_key]["calories"] += workout['calories_burned']
    
    return jsonify(dict(weekly_stats))

@app.route('/stats/<user_id>/exercise-types', methods=['GET'])
def get_exercise_type_stats(user_id):
    workouts = get_user_workouts(user_id)
    
    exercise_stats = defaultdict(lambda: {"count": 0, "total_duration": 0, "total_calories": 0})
    
    for workout in workouts:
        exercise_type = workout['exercise_type']
        exercise_stats[exercise_type]["count"] += 1
        exercise_stats[exercise_type]["total_duration"] += workout['duration']
        exercise_stats[exercise_type]["total_calories"] += workout['calories_burned']
    
    # Calculate averages
    for exercise_type in exercise_stats:
        count = exercise_stats[exercise_type]["count"]
        exercise_stats[exercise_type]["avg_duration"] = round(
            exercise_stats[exercise_type]["total_duration"] / count, 2
        )
        exercise_stats[exercise_type]["avg_calories"] = round(
            exercise_stats[exercise_type]["total_calories"] / count, 2
        )
    
    return jsonify(dict(exercise_stats))

@app.route('/stats/<user_id>/recent', methods=['GET'])
def get_recent_stats(user_id):
    days = request.args.get('days', 30, type=int)
    workouts = get_user_workouts(user_id)
    
    cutoff_date = datetime.now().date() - timedelta(days=days)
    
    recent_workouts = [
        w for w in workouts 
        if datetime.strptime(w['date'], '%Y-%m-%d').date() >= cutoff_date
    ]
    
    if not recent_workouts:
        return jsonify({
            "period": f"Last {days} days",
            "workouts": 0,
            "duration": 0,
            "calories": 0
        })
    
    return jsonify({
        "period": f"Last {days} days",
        "workouts": len(recent_workouts),
        "duration": sum(w['duration'] for w in recent_workouts),
        "calories": sum(w['calories_burned'] for w in recent_workouts)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)