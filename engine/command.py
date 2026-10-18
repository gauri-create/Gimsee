from engine.memory import save_conversation
from engine.habits import track_habit

def handle_command(user_input):
    user_input = user_input.lower()

    if "time" in user_input:
        from datetime import datetime
        response = f"The time is {datetime.now().strftime('%H:%M')}"
    elif "hello" in user_input:
        response = "Hello Sudhanshu! How can I help you today?"
    else:
        response = "I am learning. Please teach me this command."

    save_conversation(user_input, response)
    track_habit(user_input)

    return response
