import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
from time import ctime
import gtts


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

   

def speaking(audioString):
    print(audioString)
    tts = gtts(text = audioString, lang= 'en-in')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning prajakta")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

     
    else:
        speak("Good Evening")

    speak("Hello, how can i help you") 

def takeCommand():
    #It tke microphone input  from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        speak("Please say something")
        r.pause_threshold=1
        audio = r.listen(source)

        
    try:
        speak("please wait..")
        
        query = r.recognize_google(audio, language='en-in')
        speak(f"You said: {query}\n")

    except Exception as e:
        # print(e)
        speak("please say that again")
        return "None"
    return query 
      


if __name__ == "__main__":
    speak("welcome to AI world")
    wishMe()
    takeCommand()