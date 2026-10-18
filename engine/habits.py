from datetime import datetime
from engine.db import get_connection

def track_habit(command):
    hour = datetime.now().hour

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, frequency FROM habits
        WHERE command=? AND hour=?
    """, (command, hour))

    row = cursor.fetchone()

    if row:
        cursor.execute("""
            UPDATE habits
            SET frequency = frequency + 1
            WHERE id=?
        """, (row[0],))
    else:
        cursor.execute("""
            INSERT INTO habits (command, hour)
            VALUES (?, ?)
        """, (command, hour))

    conn.commit()
    conn.close()
