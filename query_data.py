import mysql.connector
import pandas as pd
from config import DATABASE_CONFIG

def query_data():
    # Step 1: Connect to the MySQL Database
    conn = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = conn.cursor()

    # Step 2: Query Data from the Database
    query = """
    SELECT W.workout_date, W.exercise_type, W.duration_minutes, W.calories_burned, 
           E.exercise_name, E.reps, E.sets, E.weight_kg, 
           N.calories_consumed, N.protein_g, N.carbs_g, N.fat_g
    FROM Workouts W
    JOIN ExerciseDetails E ON W.workout_id = E.workout_id
    JOIN NutritionLogs N ON W.user_id = N.user_id AND W.workout_date = N.log_date
    WHERE W.user_id = 1;
    """

    cursor.execute(query)
    data = cursor.fetchall()

    # Load data into a Pandas DataFrame
    columns = ['Workout Date', 'Exercise Type', 'Duration (min)', 'Calories Burned', 
               'Exercise Name', 'Reps', 'Sets', 'Weight (kg)', 
               'Calories Consumed', 'Protein (g)', 'Carbs (g)', 'Fat (g)']
    df = pd.DataFrame(data, columns=columns)

    # Display the DataFrame
    print(df)

    # Example: Analyze the Data
    # Correlation between protein intake and weight lifted
    correlation = df[['Protein (g)', 'Weight (kg)']].corr().iloc[0, 1]
    print(f"Correlation between protein intake and weight lifted: {correlation:.2f}")

    # Average calories burned by exercise type
    avg_calories_by_exercise = df.groupby('Exercise Type')['Calories Burned'].mean()
    print(avg_calories_by_exercise)

    # Close the connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    query_data()
