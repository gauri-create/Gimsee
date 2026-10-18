import speech_recognition as sr
import pyttsx3

from engine.command import handle_command
from engine.context import ContextManager
from engine.predictor import predict_next_action
from engine.db import init_db

init_db()

engine = pyttsx3.init()
context = ContextManager()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except:
        return ""

def run_assistant():
    speak("Intelligent assistant activated.")

    prediction = predict_next_action()
    if prediction:
        speak(f"You usually ask for {prediction} at this time.")

    while True:
        user_input = listen()
        if not user_input:
            continue

        print("User:", user_input)

        if "exit" in user_input:
            speak("Goodbye.")
            break

        response = handle_command(user_input)
        context.update(user_input, response)

        print("Assistant:", response)
        speak(response)

if __name__ == "__main__":
    run_assistant()
