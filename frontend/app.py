from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

USER_SERVICE_URL = os.getenv('USER_SERVICE_URL', 'http://localhost:5001')
WORKOUT_SERVICE_URL = os.getenv('WORKOUT_SERVICE_URL', 'http://localhost:5002')
STATS_SERVICE_URL = os.getenv('STATS_SERVICE_URL', 'http://localhost:5003')

@app.route('/')
def index():
    try:
        response = requests.get(f"{USER_SERVICE_URL}/users")
        users = response.json() if response.status_code == 200 else []
    except:
        users = []
    
    return render_template('index.html', users=users)

@app.route('/user/<user_id>')
def user_dashboard(user_id):
    try:
        # Get user info
        user_response = requests.get(f"{USER_SERVICE_URL}/users/{user_id}")
        user = user_response.json() if user_response.status_code == 200 else None
        
        # Get user workouts
        workout_response = requests.get(f"{WORKOUT_SERVICE_URL}/workouts?user_id={user_id}")
        workouts = workout_response.json() if workout_response.status_code == 200 else []
        
        # Get user stats
        stats_response = requests.get(f"{STATS_SERVICE_URL}/stats/{user_id}/summary")
        stats = stats_response.json() if stats_response.status_code == 200 else {}
        
        return render_template('dashboard.html', user=user, workouts=workouts, stats=stats)
    except:
        flash('Error loading user data')
        return redirect(url_for('index'))

@app.route('/api/health')
def health_check():
    services = {}
    
    for service_name, url in [
        ('user-service', USER_SERVICE_URL),
        ('workout-service', WORKOUT_SERVICE_URL),
        ('stats-service', STATS_SERVICE_URL)
    ]:
        try:
            response = requests.get(f"{url}/health", timeout=5)
            services[service_name] = "healthy" if response.status_code == 200 else "unhealthy"
        except:
            services[service_name] = "unreachable"
    
    return jsonify(services)

# API Proxy routes for frontend JavaScript
@app.route('/api/users/', methods=['POST'])
def create_user_proxy():
    try:
        response = requests.post(f"{USER_SERVICE_URL}/users", json=request.json)
        return response.json(), response.status_code
    except:
        return {"error": "Service unavailable"}, 503

@app.route('/api/workouts/', methods=['POST'])
def create_workout_proxy():
    try:
        response = requests.post(f"{WORKOUT_SERVICE_URL}/workouts", json=request.json)
        return response.json(), response.status_code
    except:
        return {"error": "Service unavailable"}, 503

@app.route('/api/stats/<user_id>/<stat_type>')
def get_stats_proxy(user_id, stat_type):
    try:
        response = requests.get(f"{STATS_SERVICE_URL}/stats/{user_id}/{stat_type}")
        return response.json(), response.status_code
    except:
        return {"error": "Service unavailable"}, 503

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)