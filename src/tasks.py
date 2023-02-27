import pywhatkit as kit
import requests
from decouple import config


def search_on_youtube(query):
    kit.playonyt(query)


def search_on_google(query):
    kit.search(query)


def get_random_joke():
    return requests.get("https://icanhazdadjoke.com/", headers={'Accept': 'application/json'}).json()["joke"]


def get_weather_report():
    my_id, city = config("OPENWEATHER_APP_ID"), config("CITY")
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_id}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    answer = f"The weather is {weather}. The temperature is {temperature}℃ and feels like {feels_like}℃"
    return answer
