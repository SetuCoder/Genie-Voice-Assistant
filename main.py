# Importing Modules
import requests
from functions.online_func import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_whatsapp_message
import pyttsx3
from functions.os_func import open_calculator, open_camera, open_terminal, open_notepad, open_spotify
import speech_recognition as sr
from decouple import config
from datetime import datetime, date
from random import choice
from utils import opening_text
from pprint import pprint
from bs4 import BeautifulSoup
import pyfiglet
import pyautogui
import os
import webbrowser

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

# Initializing the engine - use 'sapi5' for Windown, 'nsss' for macOS and 'eSpeak' for Linux
engine = pyttsx3.init('nsss')

# Set Rate
engine.setProperty('rate', 220)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (voices[0].id for Male, voices[1].id for Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

wake_word = "geni"

# Defining Local Functions
def hour():
    current_time_hour = datetime.now().hour
    return current_time_hour

def minute():
    current_time_minute = datetime.now().minute
    return current_time_minute

def second():
    current_time_second = datetime.now().second
    return current_time_second

def dayanddate():
    current_dateandday = datetime.now()
    return current_dateandday

def make_request(url):
    response = requests.get(url)
    return response.text

# Text to Speech Conversion
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Takes Input from User
def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-gb')
        if not 'exit' in query or 'stop' in query or 'bye' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 20 and hour < 6:
                speak("Good night, take care!")
            else:
                speak('Have a good day!')
            exit()
    except Exception:
        query = ''
    return query

# Getting the audio
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
        except Exception as e:
            pass    
    return said.lower()

# If else ladder
if __name__ == '__main__':
    # Decor text
    decor = pyfiglet.figlet_format("Genie", font = "slant")
    print(decor)

    while True:
        text = get_audio().lower()

        wake_word = "geni"
        
        # Checks for wake word
        if text.count(wake_word) > 0:
            speak("Yes boss")
            query = take_user_input().lower()
            
            # System functions
            if 'open notepad' in query:
                speak("Opening notepad")
                open_notepad()
                print("Notepad opened")

            elif 'open spotify' in query:
                speak("Opening spotify")
                open_spotify()
                print("Spotify opened")

            elif 'open terminal' in query:
                speak("Opening terminal")
                open_terminal()
                print("Terminal opened")

            elif 'open camera' in query:
                speak("Opening camera")
                open_camera()
                print("Camera opened")

            elif 'open calculator' in query:
                speak("Opening calculator")
                open_calculator()
                print("Calculator opened")

            elif 'screenshot' in query:
                screenshot = pyautogui.screenshot()
                screenshot.save(r'/Users/setukumar/Desktop/Screenshots/Screenshot.png')
                speak("Screenshot saved in your screenshot folder. Have a look at it.")

            elif 'ip address' in query:
                ip_address = find_my_ip()
                speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen.')
                print(f'Your IP Address is {ip_address}')

            elif 'type' in query:
                type_text = take_user_input().lower()
                pyautogui.write(type_text)

            elif 'press enter' in query:
                pyautogui.press('enter')

            elif 'shutdown the computer' in query:
                os.system("shutdown /s /t 1")

            # Basic queries
            elif 'time' in query:
                hour = hour()
                minute = minute()
                second = second()
                speak(f'The time is {hour} hours, {minute} minutes and {second} seconds. \n For your convenience, I am printing it on the screen.')
                print(f'The time is {hour} hours, {minute} minutes and {second} seconds.')

            elif 'date' in query:
                current_dateandday = datetime.now()
                date = current_dateandday.strftime("%-d")
                month = current_dateandday.strftime("%B")
                year = current_dateandday.strftime("%Y")
                speak(f"Today is {date} {month} {year}. \n For your convenience, I am printing it on the screen.")
                print(f"Today is {date} {month} {year}.")

            elif 'day' in query:
                current_dateandday = datetime.now()
                day = current_dateandday.strftime("%    a")
                speak(f"Today is {day}day. \n For your convenience, I am printing it on the screen.")
                print(f"Today is {day}day.")

            # Online functions
            elif 'wikipedia' in query:
                speak(f'What do you want to search on Wikipedia?')
                search_query = take_user_input().lower()
                results = search_on_wikipedia(search_query)
                speak(f"According to Wikipedia, {results}")
                speak("For your convenience, I am printing it on the screen.")
                print(results)

            elif 'youtube' in query:
                speak(f'What do you want me to play on Youtube?')
                video = take_user_input()
                play_on_youtube(video)

            elif 'search on google' in query:
                speak(f'What do you want to search on Google?')
                query = take_user_input().lower()
                search_on_google(query)

            elif "send a whatsapp message" in query:
                # Make sure whatsapp web is open and you're logged in with your account
                speak(
                    'To which number should I send the message? Please enter in the console.')
                number = input("Enter the number: ")
                speak("What is the message?")
                message = take_user_input().lower()
                send_whatsapp_message(number, message)
                speak("I've sent the message.")

            elif 'open amazon prime' in query:
                webbrowser.open('https://www.primevideo.com/')
                speak("Amazon prime has been opened.")

            elif 'open netflix' in query:
                webbrowser.open('https://www.netflix.com/')
                speak("Netflix has ben opened.")

            elif 'open hotstar' in query:
                webbrowser.open('https://www.hotstar.com/')
                speak("Hotstar has ben opened.")

            elif 'joke' in query:
                speak(f"Hope you like this one")
                joke = get_random_joke()
                speak(joke)
                speak("For your convenience, I am printing it on the screen")
                pprint(joke)

            elif "advice" in query:
                speak(f"Here's an advice for you")
                advice = get_random_advice()
                speak(advice)
                speak("For your convenience, I am printing it on the screen")
                pprint(advice)

            elif "trending movies" in query:
                speak(f"Some of the trending movies are: {get_trending_movies()}")
                speak("For your convenience, I am printing them on the screen")
                print(*get_trending_movies(), sep='\n')

            elif 'news' in query:
                speak(f"I'm reading out the latest news headlines")
                speak(str(get_latest_news()))
                speak("For your convenience, I am printing it on the screen")
                print(*get_latest_news(), sep='\n')

            elif 'weather' in query:
                ip_address = find_my_ip()
                city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
                speak(f"Getting weather report for your city {city}")
                weather, temperature, feels_like = get_weather_report(city)
                speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
                speak(f"Also, the weather report talks about {weather}")
                speak("For your convenience, I am printing it on the screen")
                print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

            elif 'covid' in query:
                html_data = make_request('https://www.worldometers.info/coronavirus/')
                soup = BeautifulSoup(html_data, 'html.parser')
                total_global_row = soup.find_all('tr', {'class': 'total_row'})[-1]
                total_cases = total_global_row.find_all('td')[2].get_text()
                new_cases = total_global_row.find_all('td')[3].get_text()
                total_recovered = total_global_row.find_all('td')[6].get_text()
                speak(f'The total cases are {total_cases}')
                speak(f'New cases are {new_cases[1:]}')
                speak(f'Total recovered count is {total_recovered}')
                speak("For your convenience, I am printing it on the screen")
                print(f" Total cases : {total_cases}\n New cases : {new_cases[1:]}\n Total Recovered : {total_recovered}\n")
                speak("Here are the stats for COVID-19")

            # General queries and fun
            elif 'thank you' in query:
                speak("You're welcome.")

            elif 'who are you' in query:
                speak("Since 10,300 AD, I am an assistant to Alladin. \n And now, you are my boss.")

            elif 'who am i' in query:
                speak("If you could talk, you're definetly a human. \n I guess.")

            elif 'who is your boss' in query:
                speak("You are my boss")

            elif 'what can you do' in query:
                speak("I can do a varierty of things, ranging from telling you the time to sending a whatsapp message on your behalf. \n Check the Read Me page on my GitHub repository to know more about me.")
                print("https://github.com/SetuCoder/Genie-Voice-Assistant/")

            else:
                speak("Sorry, I don't know that yet.")