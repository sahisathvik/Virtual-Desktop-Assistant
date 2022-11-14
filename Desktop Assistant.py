import gtts
import numpy as np
import pyautogui
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime
from datetime import date
import pyjokes
import pywhatkit
import smtplib
import cv2
import googletrans
from googletrans import Translator
import playsound
from gtts import gTTS
import os
from bs4 import BeautifulSoup
import subprocess
import requests
import json
from win32com.client import Dispatch
from google_trans_new import google_translator

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def hello():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning, I am ronaldo, how can i help you")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon, I am ronaldo, how can i help you")
    else:
        speak("Hello, Good Evening, I am ronaldo, how can i help you")

def takeCommand():
    listener = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            print('Recoznising')
            command = listener.recognize_google(voice)
            print(command)

    except:
        speak('sorry, Can you say that again')
        return 'None'

    return command

def Take_query():
    hello()

    while (True):

        query = takeCommand().lower()

        if "open google" in query:
            speak("Opening Google")
            webbrowser.open("www.google.com")
            continue

        elif 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("opening youtube")
            continue

        elif 'directions' in query:
            webbrowser.open_new_tab("https://www.google.co.in/maps/@17.4809431,78.3955979,15z")
            speak("opening google maps")
            continue

        elif 'open gmail' in query:
            webbrowser.open_new_tab("gmail.com")
            speak("opening gmail")
            continue

        elif 'convert' in query:
            speak('speak anything')
            print(takeCommand())
            break

        elif 'open instagram' in query:
            webbrowser.open_new_tab("https://www.instagram.com/")
            speak("opening instagram")
            continue

        elif 'spotify' in query:
            webbrowser.open_new_tab("https://open.spotify.com/")
            speak("opening spotify")
            continue

        elif 'amazon' in query:
            webbrowser.open_new_tab("https://www.amazon.in/")
            speak("opening amazon")
            continue

        elif 'send email' in query:
            try:
                speak('enter sender email')
                se_e = input()
                speak('enter receiver email')
                re_e = input()
                speak('what should I sent')
                mes = takeCommand()
                speak('enter your password')
                paw = input()
                ser = smtplib.SMTP('smtp.gmail.com', 587)
                ser.starttls()
                ser.login(se_e, paw)
                ser.sendmail(se_e, re_e, mes)
                speak('email was sent')
            except Exception as e:
                print(e)
                speak('sorry, mail could not be sent')

        elif 'control' in query:
            cap = cv2.VideoCapture(0)
            yellow_lower = np.array([22, 93, 0])
            yellow_upper = np.array([45, 255, 255])
            p_y = 0
            while True:
                ret, frame = cap.read()
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
                con, hie = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for c in con:
                    area = cv2.contourArea(c)
                    if area > 300:
                        x, y, w, h = cv2.boundingRect(c)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        if y < p_y:
                            pyautogui.press('down')
                        p_y = y
                cv2.imshow('frame', frame)
                if cv2.waitKey(10) == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif 'whatsapp' in query:
            speak('enter the number')
            s1 = '+91'
            s2 = input()
            s3 = ("".join([s1, s2]))
            speak('what is the message')
            message = takeCommand()
            print(message)
            h = int(input())
            m = int(input())
            pywhatkit.sendwhatmsg(s3, message, h, m)
            speak('message sent')
            continue

        elif 'date' in query:
            today = date.today()
            n = today.strftime("%B %d, %Y")
            speak('the date is')
            speak(n)

        elif 'shutdown' in query:
            speak("Shutting down, bye")
            exit()

        elif 'time' in query:
            now = datetime.datetime.now().strftime('%I:%M %p')
            speak("current time is")
            speak(now)

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            continue

        elif 'translate' in query:
            speak('speak now')
            audio = takeCommand().lower()
            print(googletrans.LANGUAGES)
            speak('select the language')
            s = input()
            translate = googletrans.Translator()
            translated = translate.translate(audio, dest=s)
            print(translated.text)
            converted = gtts.gTTS(translated.text, lang=s)
            speak('enter file name')
            file1 = input()
            file2 = '.mp3'
            file = file1 + file2
            converted.save(file)
            playsound.playsound(file)
            os.remove(file)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'webcam' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(0)
                if k == 1:
                    break
            cap.release()
            cv2.destroyAllWindows()
            break

        elif "tell me about" in query:
            query = query.replace('tell me about', '')
            result = wikipedia.summary(query, sentences=1)
            speak(result)

        elif 'your name' in query:
            speak('my name is ronaldo, Your Virtual Assistant')

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)
            exit()

        elif 'thank you' in query:
            speak('your welcome')

        elif 'good morning' in query:
            speak('A very good morning to you too')

        elif 'good afternoon' in query:
            speak('A very good afternoon')

        elif 'good evening' in query:
            speak('Good evening to you too')

        elif 'good night' in query:
            speak('Good night, sweet dreams')


if __name__ == '__main__':
    Take_query()

