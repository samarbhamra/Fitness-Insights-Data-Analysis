import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from config import DATABASE_CONFIG
import mysql.connector

def visualize_data():
    # Step 1: Connect to the MySQL Database
    conn = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = conn.cursor()

    # Step 2: Query Data for Visualization
    query = """
    SELECT W.exercise_type, SUM(W.calories_burned) AS total_calories, AVG(N.protein_g) AS avg_protein
    FROM Workouts W
    JOIN NutritionLogs N ON W.user_id = N.user_id AND W.workout_date = N.log_date
    GROUP BY W.exercise_type;
    """

    cursor.execute(query)
    data = cursor.fetchall()

    # Load data into a Pandas DataFrame
    df = pd.DataFrame(data, columns=['Exercise Type', 'Total Calories Burned', 'Avg Protein Intake (g)'])

    # Step 3: Bar plot of total calories burned by exercise type
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Exercise Type', y='Total Calories Burned', data=df)
    plt.title('Total Calories Burned by Exercise Type')
    plt.xlabel('Exercise Type')
    plt.ylabel('Total Calories Burned')
    plt.show()

    # Step 4: Scatter plot of average protein intake vs total calories burned
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Avg Protein Intake (g)', y='Total Calories Burned', data=df)
    plt.title('Avg Protein Intake vs Total Calories Burned')
    plt.xlabel('Avg Protein Intake (g)')
    plt.ylabel('Total Calories Burned')
    plt.show()

    # Close the connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    visualize_data()
