import pyttsx3
from datetime import datetime
import speech_recognition as sr
import logging
import random
import src.tasks as tasks


class Assistant:

    def __init__(self, user, name):
        self.user = user
        self.name = name
        self.engine = pyttsx3.init('sapi5')
        self.engine.setProperty('rate', 190)
        self.engine.setProperty('volume', 1.0)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

        self.opening_text = [
            "Cool, I'm on it sir.",
            "Okay sir, I'm working on it.",
            "Just a second sir.",
        ]

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def greeting(self):
        hour = datetime.now().hour
        if (hour >= 6) and (hour < 12):
            self.speak(f"Good Morning {self.user}")
        elif (hour >= 12) and (hour < 16):
            self.speak(f"Good afternoon {self.user}")
        elif (hour >= 16) and (hour < 19):
            self.speak(f"Good Evening {self.user}")
        self.speak(f"I am {self.name}. How may I assist you?")

    def good_by(self):
        hour = datetime.now().hour
        if 21 <= hour < 6:
            self.speak(f"Good night {self.user}, take care!")
        else:
            self.speak(f'Have a good day {self.user}!')

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            logging.debug('Listening....')
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            logging.debug('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            if 'exit' in query or 'stop' in query:
                self.good_by()
                exit()
            self.speak(random.choice(self.opening_text))

        except Exception:
            self.speak('Sorry, I could not understand. Could you please say that again?')
            query = 'None'
        return query.lower()

    def perform_task(self, query):
        if "google" in query:
            self.speak('What do you want to search on Google, sir?')
            tasks.search_on_google(self.listen())
        elif "youtube" in query:
            self.speak('What do you want to search on YouTube, sir?')
            tasks.search_on_youtube(self.listen())
        elif "joke" in query:
            self.speak(tasks.get_random_joke())
        elif "weather" in query:
            self.speak(tasks.get_weather_report())