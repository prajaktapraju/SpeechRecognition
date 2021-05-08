import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import gtts
from time import ctime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


recording = sr.Recognizer()
with sr.Microphone() as source:
    recording.adjust_for_ambient_noise(source)
    speak("please say something:")
    audio = recording.listen(source)

try:
    speak("you said")
    print("you said: \n " + recording.recognize_google(audio))
except Exception as e:
    speak("unable to hear you")
