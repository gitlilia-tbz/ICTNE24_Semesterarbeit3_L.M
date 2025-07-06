from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
from datetime import datetime
import logging

app = Flask(__name__)
CORS(app)

# Configuration
WEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', 'demo_key')
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

# Zürich coordinates (default location)
DEFAULT_LAT = 47.3769
DEFAULT_LON = 8.5417

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy", 
        "service": "weather-service",
        "api_key_configured": WEATHER_API_KEY != 'demo_key'
    })

@app.route('/weather/current', methods=['GET'])
def get_current_weather():
    """Get current weather for workout planning"""
    try:
        lat = request.args.get('lat', DEFAULT_LAT, type=float)
        lon = request.args.get('lon', DEFAULT_LON, type=float)
        
        params = {
            'lat': lat,
            'lon': lon,
            'appid': WEATHER_API_KEY,
            'units': 'metric',
            'lang': 'en'
        }
        
        logger.info(f"Fetching weather for coordinates: {lat}, {lon}")
        response = requests.get(WEATHER_URL, params=params, timeout=10)
        
        if response.status_code == 401:
            return jsonify({
                "error": "Weather API key not configured or invalid",
                "demo_mode": True,
                "weather_data": get_demo_weather()
            }), 200
        
        if response.status_code != 200:
            return jsonify({"error": "Weather service unavailable"}), 503
            
        weather_data = response.json()
        
        # Process and enhance weather data
        processed_data = process_weather_data(weather_data)
        
        return jsonify(processed_data)
        
    except requests.exceptions.Timeout:
        return jsonify({"error": "Weather service timeout"}), 503
    except Exception as e:
        logger.error(f"Weather API error: {str(e)}")
        return jsonify({
            "error": "Weather service error",
            "demo_mode": True,
            "weather_data": get_demo_weather()
        }), 200

@app.route('/weather/workout-advice', methods=['GET'])
def get_workout_advice():
    """Get personalized workout advice based on weather"""
    try:
        lat = request.args.get('lat', DEFAULT_LAT, type=float)
        lon = request.args.get('lon', DEFAULT_LON, type=float)
        activity_type = request.args.get('activity', 'general')
        
        # Get current weather
        weather_response = requests.get(f"http://localhost:5004/weather/current?lat={lat}&lon={lon}")
        
        if weather_response.status_code != 200:
            return jsonify({"error": "Could not fetch weather data"}), 503
            
        weather_data = weather_response.json()
        
        if weather_data.get('demo_mode'):
            weather_info = weather_data['weather_data']
        else:
            weather_info = weather_data
        
        advice = generate_workout_advice(weather_info, activity_type)
        
        return jsonify({
            "weather": weather_info,
            "advice": advice,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Workout advice error: {str(e)}")
        return jsonify({"error": str(e)}), 500

def process_weather_data(raw_data):
    """Process raw weather API data into workout-friendly format"""
    try:
        return {
            "temperature": round(raw_data['main']['temp'], 1),
            "feels_like": round(raw_data['main']['feels_like'], 1),
            "humidity": raw_data['main']['humidity'],
            "weather_main": raw_data['weather'][0]['main'],
            "weather_description": raw_data['weather'][0]['description'].title(),
            "wind_speed": raw_data.get('wind', {}).get('speed', 0),
            "visibility": raw_data.get('visibility', 10000) / 1000,  # Convert to km
            "city": raw_data.get('name', 'Unknown'),
            "country": raw_data.get('sys', {}).get('country', ''),
            "sunrise": raw_data.get('sys', {}).get('sunrise'),
            "sunset": raw_data.get('sys', {}).get('sunset'),
            "timestamp": datetime.now().isoformat(),
            "outdoor_suitable": is_outdoor_suitable(raw_data),
            "workout_conditions": get_workout_conditions_rating(raw_data)
        }
    except KeyError as e:
        logger.error(f"Error processing weather data: {e}")
        return get_demo_weather()

def get_demo_weather():
    """Return demo weather data when API is not available"""
    return {
        "temperature": 18.5,
        "feels_like": 17.8,
        "humidity": 65,
        "weather_main": "Clouds",
        "weather_description": "Partly Cloudy",
        "wind_speed": 2.1,
        "visibility": 10.0,
        "city": "Zurich",
        "country": "CH",
        "sunrise": None,
        "sunset": None,
        "timestamp": datetime.now().isoformat(),
        "outdoor_suitable": True,
        "workout_conditions": "good",
        "demo_mode": True
    }

def is_outdoor_suitable(weather_data):
    """Determine if weather is suitable for outdoor workouts"""
    temp = weather_data['main']['temp']
    weather_main = weather_data['weather'][0]['main']
    wind_speed = weather_data.get('wind', {}).get('speed', 0)
    
    # Bad weather conditions
    if weather_main in ['Thunderstorm', 'Tornado']:
        return False
    
    if weather_main == 'Rain' and temp < 10:
        return False
        
    # Extreme temperatures
    if temp < -5 or temp > 35:
        return False
        
    # Very high wind
    if wind_speed > 15:  # m/s
        return False
        
    return True

def get_workout_conditions_rating(weather_data):
    """Rate workout conditions as excellent, good, fair, or poor"""
    temp = weather_data['main']['temp']
    weather_main = weather_data['weather'][0]['main']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data.get('wind', {}).get('speed', 0)
    
    if not is_outdoor_suitable(weather_data):
        return "poor"
    
    # Excellent conditions
    if (15 <= temp <= 22 and 
        weather_main in ['Clear', 'Clouds'] and 
        humidity < 70 and 
        wind_speed < 5):
        return "excellent"
    
    # Good conditions
    if (10 <= temp <= 27 and 
        weather_main not in ['Rain', 'Snow', 'Thunderstorm'] and 
        humidity < 80):
        return "good"
    
    # Fair conditions
    return "fair"

def generate_workout_advice(weather_info, activity_type):
    """Generate personalized workout advice based on weather and activity"""
    temp = weather_info['temperature']
    weather_main = weather_info['weather_main']
    conditions_rating = weather_info['workout_conditions']
    
    advice = {
        "primary_message": "",
        "activity_suggestions": [],
        "safety_tips": [],
        "gear_recommendations": []
    }
    
    # Primary message based on conditions
    if conditions_rating == "excellent":
        advice["primary_message"] = "🌟 Perfect weather for outdoor workouts!"
    elif conditions_rating == "good":
        advice["primary_message"] = "☀️ Great weather for exercising outside!"
    elif conditions_rating == "fair":
        advice["primary_message"] = "🌤️ Decent weather - outdoor workouts possible with preparation."
    else:
        advice["primary_message"] = "🏠 Better to workout indoors today."
    
    # Activity suggestions
    if weather_main in ['Rain', 'Drizzle']:
        advice["activity_suggestions"] = [
            "Indoor gym session",
            "Home yoga or stretching",
            "Covered running tracks",
            "Swimming (indoor pool)"
        ]
    elif weather_main == 'Snow':
        advice["activity_suggestions"] = [
            "Winter sports (skiing, snowboarding)",
            "Indoor cardio workouts",
            "Hot yoga sessions",
            "Gym strength training"
        ]
    elif 5 <= temp <= 15:
        advice["activity_suggestions"] = [
            "Running or jogging",
            "Cycling",
            "Outdoor fitness classes",
            "Hiking"
        ]
    elif 15 < temp <= 25:
        advice["activity_suggestions"] = [
            "All outdoor activities",
            "Running, cycling, sports",
            "Outdoor yoga",
            "Beach volleyball"
        ]
    elif temp > 25:
        advice["activity_suggestions"] = [
            "Early morning or evening workouts",
            "Swimming",
            "Water sports",
            "Shaded outdoor activities"
        ]
    else:
        advice["activity_suggestions"] = [
            "Indoor gym workouts",
            "Hot yoga",
            "Indoor climbing",
            "Dance classes"
        ]
    
    # Safety tips
    if temp > 25:
        advice["safety_tips"] = [
            "Stay well hydrated",
            "Take frequent breaks",
            "Avoid midday sun",
            "Wear light, breathable clothing"
        ]
    elif temp < 5:
        advice["safety_tips"] = [
            "Warm up thoroughly indoors",
            "Layer your clothing",
            "Protect extremities",
            "Be visible if running in dark"
        ]
    elif weather_main in ['Rain', 'Snow']:
        advice["safety_tips"] = [
            "Watch for slippery surfaces",
            "Increase visibility with bright colors",
            "Shorten workout duration",
            "Check equipment for water resistance"
        ]
    
    # Gear recommendations
    if weather_main == 'Rain':
        advice["gear_recommendations"] = ["Waterproof jacket", "Non-slip shoes", "Waterproof bag"]
    elif temp < 10:
        advice["gear_recommendations"] = ["Thermal layers", "Gloves", "Warm hat", "Windproof jacket"]
    elif temp > 25:
        advice["gear_recommendations"] = ["Sun hat", "Sunglasses", "SPF 30+ sunscreen", "Extra water bottle"]
    else:
        advice["gear_recommendations"] = ["Comfortable athletic wear", "Good running shoes", "Water bottle"]
    
    return advice

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=False)