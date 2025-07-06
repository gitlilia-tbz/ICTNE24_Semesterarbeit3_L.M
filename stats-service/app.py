from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, text
import os
from datetime import datetime, timedelta
from collections import defaultdict

app = Flask(__name__)
CORS(app)

# Database Configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://trackmygym_user:secure_password_123@postgres:5432/trackmygym')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import Workout model (same as workout-service)
class Workout(db.Model):
    __tablename__ = 'workouts'
    
    id = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.String(36), nullable=False)
    exercise_type = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    calories_burned = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)
    date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/health', methods=['GET'])
def health():
    try:
        db.session.execute(db.text('SELECT 1'))
        return jsonify({"status": "healthy", "service": "stats-service", "database": "postgresql"})
    except Exception as e:
        return jsonify({"status": "unhealthy", "service": "stats-service", "error": str(e)}), 500

@app.route('/stats/<user_id>/summary', methods=['GET'])
def get_user_stats_summary(user_id):
    try:
        # Use SQL aggregation for better performance
        result = db.session.query(
            func.count(Workout.id).label('total_workouts'),
            func.sum(Workout.duration).label('total_duration'),
            func.sum(Workout.calories_burned).label('total_calories'),
            func.avg(Workout.duration).label('avg_duration'),
            func.avg(Workout.calories_burned).label('avg_calories')
        ).filter(Workout.user_id == user_id).first()
        
        if not result.total_workouts:
            return jsonify({
                "total_workouts": 0,
                "total_duration": 0,
                "total_calories": 0,
                "average_duration": 0,
                "average_calories": 0
            })
        
        return jsonify({
            "total_workouts": result.total_workouts or 0,
            "total_duration": result.total_duration or 0,
            "total_calories": result.total_calories or 0,
            "average_duration": round(float(result.avg_duration or 0), 2),
            "average_calories": round(float(result.avg_calories or 0), 2)
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/stats/<user_id>/weekly', methods=['GET'])
def get_weekly_stats(user_id):
    try:
        # Get workouts from last 8 weeks for better context
        weeks_ago = datetime.now().date() - timedelta(weeks=8)
        
        workouts = db.session.query(Workout).filter(
            Workout.user_id == user_id,
            Workout.date >= weeks_ago
        ).order_by(Workout.date).all()
        
        weekly_stats = defaultdict(lambda: {"workouts": 0, "duration": 0, "calories": 0})
        
        for workout in workouts:
            # Calculate week start (Monday)
            week_start = workout.date - timedelta(days=workout.date.weekday())
            week_key = week_start.strftime('%Y-%m-%d')
            
            weekly_stats[week_key]["workouts"] += 1
            weekly_stats[week_key]["duration"] += workout.duration
            weekly_stats[week_key]["calories"] += workout.calories_burned
        
        return jsonify(dict(weekly_stats))
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/stats/<user_id>/exercise-types', methods=['GET'])
def get_exercise_type_stats(user_id):
    try:
        # SQL aggregation by exercise type
        results = db.session.query(
            Workout.exercise_type,
            func.count(Workout.id).label('count'),
            func.sum(Workout.duration).label('total_duration'),
            func.sum(Workout.calories_burned).label('total_calories'),
            func.avg(Workout.duration).label('avg_duration'),
            func.avg(Workout.calories_burned).label('avg_calories')
        ).filter(Workout.user_id == user_id).group_by(Workout.exercise_type).all()
        
        exercise_stats = {}
        for result in results:
            exercise_stats[result.exercise_type] = {
                "count": result.count,
                "total_duration": result.total_duration or 0,
                "total_calories": result.total_calories or 0,
                "avg_duration": round(float(result.avg_duration or 0), 2),
                "avg_calories": round(float(result.avg_calories or 0), 2)
            }
        
        return jsonify(exercise_stats)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/stats/<user_id>/recent', methods=['GET'])
def get_recent_stats(user_id):
    try:
        days = request.args.get('days', 30, type=int)
        cutoff_date = datetime.now().date() - timedelta(days=days)
        
        result = db.session.query(
            func.count(Workout.id).label('workouts'),
            func.sum(Workout.duration).label('duration'),
            func.sum(Workout.calories_burned).label('calories')
        ).filter(
            Workout.user_id == user_id,
            Workout.date >= cutoff_date
        ).first()
        
        return jsonify({
            "period": f"Last {days} days",
            "workouts": result.workouts or 0,
            "duration": result.duration or 0,
            "calories": result.calories or 0
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/stats/<user_id>/monthly-trends', methods=['GET'])
def get_monthly_trends(user_id):
    try:
        # Get data from last 6 months
        months_ago = datetime.now().date() - timedelta(days=180)
        
        # SQL query to group by month
        results = db.session.query(
            func.date_trunc('month', Workout.date).label('month'),
            func.count(Workout.id).label('workouts'),
            func.sum(Workout.duration).label('duration'),
            func.sum(Workout.calories_burned).label('calories')
        ).filter(
            Workout.user_id == user_id,
            Workout.date >= months_ago
        ).group_by(func.date_trunc('month', Workout.date)).order_by('month').all()
        
        monthly_stats = {}
        for result in results:
            month_key = result.month.strftime('%Y-%m')
            monthly_stats[month_key] = {
                "workouts": result.workouts,
                "duration": result.duration or 0,
                "calories": result.calories or 0
            }
        
        return jsonify(monthly_stats)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/stats/<user_id>/personal-records', methods=['GET'])
def get_personal_records(user_id):
    try:
        # Find personal records
        longest_workout = db.session.query(Workout).filter(
            Workout.user_id == user_id
        ).order_by(Workout.duration.desc()).first()
        
        highest_calories = db.session.query(Workout).filter(
            Workout.user_id == user_id
        ).order_by(Workout.calories_burned.desc()).first()
        
        # Most frequent exercise type
        most_frequent = db.session.query(
            Workout.exercise_type,
            func.count(Workout.id).label('count')
        ).filter(Workout.user_id == user_id).group_by(
            Workout.exercise_type
        ).order_by(func.count(Workout.id).desc()).first()
        
        # Recent streak (consecutive workout days)
        recent_workouts = db.session.query(Workout.date).filter(
            Workout.user_id == user_id
        ).distinct().order_by(Workout.date.desc()).limit(30).all()
        
        streak = 0
        current_date = datetime.now().date()
        for i, (workout_date,) in enumerate(recent_workouts):
            expected_date = current_date - timedelta(days=i)
            if workout_date == expected_date:
                streak += 1
            else:
                break
        
        records = {
            "longest_workout": {
                "duration": longest_workout.duration if longest_workout else 0,
                "exercise_type": longest_workout.exercise_type if longest_workout else None,
                "date": longest_workout.date.isoformat() if longest_workout else None
            },
            "highest_calories": {
                "calories": highest_calories.calories_burned if highest_calories else 0,
                "exercise_type": highest_calories.exercise_type if highest_calories else None,
                "date": highest_calories.date.isoformat() if highest_calories else None
            },
            "favorite_exercise": {
                "type": most_frequent.exercise_type if most_frequent else None,
                "count": most_frequent.count if most_frequent else 0
            },
            "current_streak": {
                "days": streak,
                "description": f"{streak} consecutive days" if streak > 0 else "No current streak"
            }
        }
        
        return jsonify(records)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/stats/<user_id>/dashboard', methods=['GET'])
def get_dashboard_stats(user_id):
    """Combined endpoint for dashboard - reduces API calls"""
    try:
        # Get summary stats
        summary = db.session.query(
            func.count(Workout.id).label('total_workouts'),
            func.sum(Workout.duration).label('total_duration'),
            func.sum(Workout.calories_burned).label('total_calories')
        ).filter(Workout.user_id == user_id).first()
        
        # Get this week's stats
        week_start = datetime.now().date() - timedelta(days=datetime.now().weekday())
        week_stats = db.session.query(
            func.count(Workout.id).label('week_workouts'),
            func.sum(Workout.duration).label('week_duration'),
            func.sum(Workout.calories_burned).label('week_calories')
        ).filter(
            Workout.user_id == user_id,
            Workout.date >= week_start
        ).first()
        
        # Get recent workouts (last 5)
        recent_workouts = db.session.query(Workout).filter(
            Workout.user_id == user_id
        ).order_by(Workout.date.desc(), Workout.created_at.desc()).limit(5).all()
        
        return jsonify({
            "summary": {
                "total_workouts": summary.total_workouts or 0,
                "total_duration": summary.total_duration or 0,
                "total_calories": summary.total_calories or 0
            },
            "this_week": {
                "workouts": week_stats.week_workouts or 0,
                "duration": week_stats.week_duration or 0,
                "calories": week_stats.week_calories or 0
            },
            "recent_workouts": [
                {
                    "id": w.id,
                    "exercise_type": w.exercise_type,
                    "duration": w.duration,
                    "date": w.date.isoformat()
                } for w in recent_workouts
            ]
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=False)