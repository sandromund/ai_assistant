import pywhatkit as kit
import requests
from decouple import config


def search_on_youtube(query):
    kit.playonyt(query)


def search_on_google(query):
    kit.search(query)


def get_random_joke():
    return requests.get("https://icanhazdadjoke.com/", headers={'Accept': 'application/json'}).json()["joke"]


def get_weather_report(c):
    id = config("OPENWEATHER_APP_ID")
    res = res = requests.get(f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={id}")
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"
