-- TrackMyGym Database Schema

-- Users Table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    age INTEGER,
    weight DECIMAL(5,2),
    height DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Workouts Table
CREATE TABLE workouts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    exercise_type VARCHAR(255) NOT NULL,
    duration INTEGER NOT NULL, -- in minutes
    calories_burned INTEGER NOT NULL,
    notes TEXT,
    date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for better performance
CREATE INDEX idx_workouts_user_id ON workouts(user_id);
CREATE INDEX idx_workouts_date ON workouts(date);
CREATE INDEX idx_workouts_exercise_type ON workouts(exercise_type);
CREATE INDEX idx_users_email ON users(email);

-- Sample data for testing
INSERT INTO users (name, email, age, weight, height) VALUES 
('Lilia Mechani', 'lilia@trackmygym.com', 25, 65.5, 170.0),
('Test User', 'test@example.com', 30, 80.0, 180.0);

-- Sample workouts
INSERT INTO workouts (user_id, exercise_type, duration, calories_burned, notes, date)
SELECT 
    u.id,
    'Krafttraining',
    60,
    400,
    'Erstes Workout in der neuen PostgreSQL App!',
    CURRENT_DATE
FROM users u 
WHERE u.email = 'lilia@trackmygym.com';

INSERT INTO workouts (user_id, exercise_type, duration, calories_burned, notes, date)
SELECT 
    u.id,
    'Running',
    45,
    350,
    'Morgen-Lauf im Park',
    CURRENT_DATE - INTERVAL '1 day'
FROM users u 
WHERE u.email = 'lilia@trackmygym.com';

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Triggers for automatic updated_at
CREATE TRIGGER update_users_updated_at 
    BEFORE UPDATE ON users 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_workouts_updated_at 
    BEFORE UPDATE ON workouts 
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();