import mysql.connector
from config import DATABASE_CONFIG

def create_and_insert_data():
    # Step 1: Connect to the MySQL Database
    conn = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = conn.cursor()

    # Step 2: Create Tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        age INT,
        gender VARCHAR(10)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Workouts (
        workout_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        workout_date DATE,
        exercise_type VARCHAR(50),
        duration_minutes INT,
        calories_burned INT,
        avg_heart_rate INT,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ExerciseDetails (
        detail_id INT AUTO_INCREMENT PRIMARY KEY,
        workout_id INT,
        exercise_name VARCHAR(50),
        reps INT,
        sets INT,
        weight_kg INT,
        FOREIGN KEY (workout_id) REFERENCES Workouts(workout_id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS NutritionLogs (
        log_id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        log_date DATE,
        calories_consumed INT,
        protein_g INT,
        carbs_g INT,
        fat_g INT,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
    );
    ''')

    # Step 3: Insert Data into Tables
    users = [
        ('JohnDoe', 30, 'Male'),
        ('JaneSmith', 28, 'Female')
    ]
    cursor.executemany(
        "INSERT INTO Users (username, age, gender) VALUES (%s, %s, %s)", users
    )

    workouts = [
        (1, '2024-08-01', 'Running', 30, 300, 140),
        (1, '2024-08-02', 'Cycling', 45, 500, 135),
        (2, '2024-08-01', 'Weightlifting', 60, 400, 120)
    ]
    cursor.executemany(
        "INSERT INTO Workouts (user_id, workout_date, exercise_type, duration_minutes, calories_burned, avg_heart_rate) "
        "VALUES (%s, %s, %s, %s, %s, %s)", workouts
    )

    exercise_details = [
        (1, 'Squats', 10, 3, 80),
        (1, 'Deadlifts', 8, 3, 100),
        (2, 'Bench Press', 12, 4, 60)
    ]
    cursor.executemany(
        "INSERT INTO ExerciseDetails (workout_id, exercise_name, reps, sets, weight_kg) VALUES (%s, %s, %s, %s, %s)",
        exercise_details
    )

    nutrition_logs = [
        (1, '2024-08-01', 2500, 150, 300, 70),
        (1, '2024-08-02', 2400, 140, 290, 65),
        (2, '2024-08-01', 2200, 130, 270, 60)
    ]
    cursor.executemany(
        "INSERT INTO NutritionLogs (user_id, log_date, calories_consumed, protein_g, carbs_g, fat_g) VALUES (%s, %s, %s, %s, %s, %s)",
        nutrition_logs
    )

    # Commit and close the connection
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_and_insert_data()
