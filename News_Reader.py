import json
import requests


def speak(str):
    from win32com.client import Dispatch

    speaking = Dispatch("SAPI.SpVoice")

    speaking.speak(str)


user_input = int(input("Select the category of news u would like to hear from below : \n"
                       "1. Top Headlines\n"
                       "2. Entertainment\n"
                       "3. Health\n"
                       "4. Science\n"
                       "5. Sport\n"
                       "6. Technology\n"
                       "---->>>> "))

if user_input == 1:

    news = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=e12a2dc1880047ea8262ca31471417ba").text
    news_json = json.loads(news)

    read = news_json['articles']

    for article in read:
        speak(article['title'])
        speak("Moving to the next news")


elif user_input == 2:
    news = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey"
        "=e12a2dc1880047ea8262ca31471417ba").text
    news_json = json.loads(news)

    read = news_json['articles']

    for article in read:
        speak(article['title'])
        speak("Moving to the next news")

elif user_input == 3:
    news = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=e12a2dc1880047ea8262ca31471417ba").text
    news_json = json.loads(news)

    read = news_json['articles']

    for article in read:
        speak(article['title'])
        speak("Moving to the next news")

elif user_input == 4:
    news = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=e12a2dc1880047ea8262ca31471417ba").text
    news_json = json.loads(news)

    read = news_json['articles']

    for article in read:
        speak(article['title'])
        speak("Moving to the next news")

elif user_input == 5:
    news = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=e12a2dc1880047ea8262ca31471417ba").text
    news_json = json.loads(news)

    read = news_json['articles']

    for article in read:
        speak(article['title'])
        speak("Moving to the next news")

elif user_input == 6:
    news = requests.get(
        "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey"
        "=e12a2dc1880047ea8262ca31471417ba").text
    news_json = json.loads(news)

    read = news_json['articles']

    for article in read:
        speak(article['title'])
        speak("Moving to the next news")

    """   
new = requests.get(url).text
news_json = json.loads(news)

read = news_json['articles']

for article in read:
    speak(article['title'])
    speak("Moving to the next news")


    elif 'exit' or 'terminate' or 'good bye' in query:
    speak("hoping to see you soon. Thank you for using me sir. have a nice day")
    mixer.init()
    mixer.music.load("exiting music.mp3")
    mixer.music.set_volume(0.7)
    mixer.music.play()
    break
"""
