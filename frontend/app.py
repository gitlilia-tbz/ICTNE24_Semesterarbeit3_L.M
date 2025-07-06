from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests
import os
import logging

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-fallback-key')

USER_SERVICE_URL = os.getenv('USER_SERVICE_URL', 'http://localhost:5001')
WORKOUT_SERVICE_URL = os.getenv('WORKOUT_SERVICE_URL', 'http://localhost:5002')
STATS_SERVICE_URL = os.getenv('STATS_SERVICE_URL', 'http://localhost:5003')
WEATHER_SERVICE_URL = os.getenv('WEATHER_SERVICE_URL', 'http://localhost:5004')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    try:
        response = requests.get(f"{USER_SERVICE_URL}/users")
        users = response.json() if response.status_code == 200 else []
        
        # Get weather info for homepage
        weather_info = get_weather_info()
        
    except:
        users = []
        weather_info = None
    
    return render_template('index.html', users=users, weather=weather_info)

@app.route('/user/<user_id>')
def user_dashboard(user_id):
    try:
        # Get user info
        user_response = requests.get(f"{USER_SERVICE_URL}/users/{user_id}")
        user = user_response.json() if user_response.status_code == 200 else None
        
        # Get user workouts
        workout_response = requests.get(f"{WORKOUT_SERVICE_URL}/workouts?user_id={user_id}&limit=10")
        workouts = workout_response.json() if workout_response.status_code == 200 else []
        
        # Get user stats
        stats_response = requests.get(f"{STATS_SERVICE_URL}/stats/{user_id}/summary")
        stats = stats_response.json() if stats_response.status_code == 200 else {}
        
        # Get weather info for workout planning
        weather_info = get_weather_info()
        workout_advice = get_workout_advice() if weather_info else None
        
        return render_template('dashboard.html', 
                             user=user, 
                             workouts=workouts, 
                             stats=stats,
                             weather=weather_info,
                             workout_advice=workout_advice)
    except Exception as e:
        logger.error(f"Dashboard error: {e}")
        flash('Error loading user data')
        return redirect(url_for('index'))

def get_weather_info():
    """Get current weather information"""
    try:
        response = requests.get(f"{WEATHER_SERVICE_URL}/weather/current", timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        logger.warning(f"Weather service unavailable: {e}")
    return None

def get_workout_advice():
    """Get workout advice based on weather"""
    try:
        response = requests.get(f"{WEATHER_SERVICE_URL}/weather/workout-advice", timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        logger.warning(f"Workout advice unavailable: {e}")
    return None

@app.route('/api/health')
def health_check():
    services = {}
    
    service_urls = [
        ('user-service', USER_SERVICE_URL),
        ('workout-service', WORKOUT_SERVICE_URL),
        ('stats-service', STATS_SERVICE_URL),
        ('weather-service', WEATHER_SERVICE_URL)
    ]
    
    for service_name, url in service_urls:
        try:
            response = requests.get(f"{url}/health", timeout=5)
            if response.status_code == 200:
                health_data = response.json()
                services[service_name] = health_data.get('status', 'unknown')
            else:
                services[service_name] = "unhealthy"
        except:
            services[service_name] = "unreachable"
    
    return jsonify(services)

# Weather API endpoints for frontend
@app.route('/api/weather/current')
def weather_current():
    try:
        lat = request.args.get('lat', type=float)
        lon = request.args.get('lon', type=float)
        
        params = {}
        if lat and lon:
            params = {'lat': lat, 'lon': lon}
            
        response = requests.get(f"{WEATHER_SERVICE_URL}/weather/current", params=params, timeout=5)
        return response.json(), response.status_code
    except:
        return {"error": "Weather service unavailable"}, 503

@app.route('/api/weather/workout-advice')
def weather_workout_advice():
    try:
        lat = request.args.get('lat', type=float)
        lon = request.args.get('lon', type=float)
        activity = request.args.get('activity', 'general')
        
        params = {'activity': activity}
        if lat and lon:
            params.update({'lat': lat, 'lon': lon})
            
        response = requests.get(f"{WEATHER_SERVICE_URL}/weather/workout-advice", params=params, timeout=5)
        return response.json(), response.status_code
    except:
        return {"error": "Weather advice unavailable"}, 503

# Existing API proxy routes
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
    app.run(host='0.0.0.0', port=5000, debug=False)