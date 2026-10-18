from datetime import datetime
from engine.db import get_connection

def predict_next_action():
    hour = datetime.now().hour
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT command, frequency
        FROM habits
        WHERE hour=?
        ORDER BY frequency DESC
        LIMIT 1
    """, (hour,))

    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    return None
