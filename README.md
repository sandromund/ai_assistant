# AI Assistant
AI that I can give commands to like Alexa, Google or Siri. 

## Status
This project is currently in early development. 
Alot more features will be added. 
Currently the voice is very robotic, so I'm looking for a way to make it sound more natural.

## Setup

Create a `.env` file for all accounts, settings and private data.
````commandline
USER=<MY_USER_NAM>
BOTNAME=<MY_AI_NAME>
OPENWEATHER_APP_ID=<MY_PERSONAL_KEY>
CITY=<MY_CITY>
````
For the weather report a free account and ID is needed form [OpenWeatherMap](https://openweathermap.org/).


## How to use
Say one of the following keywords
- google: The assistant will ask you what to google
- Joke: The assistant will tell a dad joke
- YouTube: The assistant will ask you what to open for you 
- weather: 


# Troubleshooting 
- PyAudio related error: download PyAudio wheel from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio).