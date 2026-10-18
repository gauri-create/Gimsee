from engine.db import get_connection

def save_conversation(user_input, response):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO conversations (user_input, assistant_response)
        VALUES (?, ?)
    """, (user_input, response))

    conn.commit()
    conn.close()
