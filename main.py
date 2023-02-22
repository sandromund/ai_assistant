from decouple import config
from src.assistant import Assistant

if __name__ == '__main__':
    ai = Assistant(user=config('USER'), name=config('BOTNAME'))
    ai.greeting()
    while True:
        query = ai.listen()
        ai.perform_task(query)
