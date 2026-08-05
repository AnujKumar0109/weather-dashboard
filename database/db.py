import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():

    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )


def save_weather(data):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO weather_history
    (
        city,
        temperature,
        humidity,
        weather_description
    )
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            data["name"],
            data["main"]["temp"],
            data["main"]["humidity"],
            data["weather"][0]["description"]
        )
    )

    conn.commit()
    cursor.close()
    conn.close()
    
    
def get_weather_history():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT city,
           temperature,
           humidity,
           weather_description,
           recorded_at
    FROM weather_history
    ORDER BY recorded_at DESC;
    """

    cursor.execute(query)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows    



def get_statistics():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT city,
               temperature,
               humidity,
               recorded_at
        FROM weather_history
        ORDER BY recorded_at;
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def get_total_searches():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM weather_history")

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total