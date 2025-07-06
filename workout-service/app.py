from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import requests
import os
from datetime import datetime
import uuid

app = Flask(__name__)
CORS(app)

# Database Configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://trackmygym_user:secure_password_123@postgres:5432/trackmygym')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
USER_SERVICE_URL = os.getenv('USER_SERVICE_URL', 'http://localhost:5001')

# Workout Model
class Workout(db.Model):
    __tablename__ = 'workouts'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), nullable=False)  # Foreign key to users table
    exercise_type = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # in minutes
    calories_burned = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)
    date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'exercise_type': self.exercise_type,
            'duration': self.duration,
            'calories_burned': self.calories_burned,
            'notes': self.notes,
            'date': self.date.isoformat() if self.date else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

def verify_user_exists(user_id):
    try:
        response = requests.get(f"{USER_SERVICE_URL}/users/{user_id}", timeout=5)
        return response.status_code == 200
    except:
        return False

@app.route('/health', methods=['GET'])
def health():
    try:
        # Test database connection
        db.session.execute(db.text('SELECT 1'))
        return jsonify({"status": "healthy", "service": "workout-service", "database": "postgresql"})
    except Exception as e:
        return jsonify({"status": "unhealthy", "service": "workout-service", "error": str(e)}), 500

@app.route('/workouts', methods=['GET'])
def get_workouts():
    try:
        user_id = request.args.get('user_id')
        limit = request.args.get('limit', type=int)
        
        query = Workout.query
        
        if user_id:
            query = query.filter_by(user_id=user_id)
        
        query = query.order_by(Workout.date.desc(), Workout.created_at.desc())
        
        if limit:
            query = query.limit(limit)
        
        workouts = query.all()
        return jsonify([workout.to_dict() for workout in workouts])
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/workouts', methods=['POST'])
def create_workout():
    try:
        data = request.get_json()
        
        required_fields = ['user_id', 'exercise_type', 'duration', 'calories_burned']
        if not data or not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields: user_id, exercise_type, duration, calories_burned"}), 400
        
        # Verify user exists
        if not verify_user_exists(data['user_id']):
            return jsonify({"error": "User not found"}), 404
        
        # Parse date
        workout_date = data.get('date')
        if workout_date:
            try:
                workout_date = datetime.strptime(workout_date, '%Y-%m-%d').date()
            except ValueError:
                return jsonify({"error": "Date must be in YYYY-MM-DD format"}), 400
        else:
            workout_date = datetime.now().date()
        
        # Validate numeric fields
        try:
            duration = int(data['duration'])
            calories = int(data['calories_burned'])
            if duration <= 0 or calories <= 0:
                return jsonify({"error": "Duration and calories must be positive numbers"}), 400
        except (ValueError, TypeError):
            return jsonify({"error": "Duration and calories must be valid numbers"}), 400
        
        workout = Workout(
            user_id=data['user_id'],
            exercise_type=data['exercise_type'].strip(),
            duration=duration,
            calories_burned=calories,
            notes=data.get('notes', '').strip(),
            date=workout_date
        )
        
        db.session.add(workout)
        db.session.commit()
        
        return jsonify(workout.to_dict()), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/workouts/<workout_id>', methods=['GET'])
def get_workout(workout_id):
    try:
        workout = Workout.query.get(workout_id)
        if not workout:
            return jsonify({"error": "Workout not found"}), 404
        return jsonify(workout.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/workouts/<workout_id>', methods=['PUT'])
def update_workout(workout_id):
    try:
        workout = Workout.query.get(workout_id)
        if not workout:
            return jsonify({"error": "Workout not found"}), 404
        
        data = request.get_json()
        
        # Update fields
        for key in ['exercise_type', 'duration', 'calories_burned', 'notes']:
            if key in data:
                if key in ['duration', 'calories_burned']:
                    try:
                        value = int(data[key])
                        if value <= 0:
                            return jsonify({"error": f"{key} must be a positive number"}), 400
                        setattr(workout, key, value)
                    except (ValueError, TypeError):
                        return jsonify({"error": f"{key} must be a valid number"}), 400
                else:
                    setattr(workout, key, data[key])
        
        if 'date' in data:
            try:
                workout.date = datetime.strptime(data['date'], '%Y-%m-%d').date()
            except ValueError:
                return jsonify({"error": "Date must be in YYYY-MM-DD format"}), 400
        
        workout.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify(workout.to_dict())
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/workouts/<workout_id>', methods=['DELETE'])
def delete_workout(workout_id):
    try:
        workout = Workout.query.get(workout_id)
        if not workout:
            return jsonify({"error": "Workout not found"}), 404
        
        db.session.delete(workout)
        db.session.commit()
        
        return jsonify({"message": "Workout deleted successfully"})
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Additional endpoints for statistics
@app.route('/workouts/stats/summary/<user_id>', methods=['GET'])
def get_workout_summary(user_id):
    try:
        from sqlalchemy import func
        
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

if __name__ == '__main__':
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5002, debug=False)