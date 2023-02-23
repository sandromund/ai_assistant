import pywhatkit as kit
import requests


def search_on_youtube(query):
    kit.playonyt(query)


def search_on_google(query):
    kit.search(query)


def get_random_joke():
    return requests.get("https://icanhazdadjoke.com/", headers={'Accept': 'application/json'}).json()["joke"]
