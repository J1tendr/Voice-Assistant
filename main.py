from logging import exception
from socket import if_nameindex
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pygame
import time
engine=pyttsx3.init('sapi5')       #voice recognition and synthesis provided by Microsoft
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',175)
def speak(audio):        # this function will program to speak something by assisstant 
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak('Hey sunshine, good morning')
    elif hour>=12 and hour<=18 :
        speak('hey,good afternoon')
    else:
        speak('hey, good evening')
    speak('how can i help you out ?')
def takecommand():
    r=sr.Recognizer()      # a class used to recognise class
    with sr.Microphone() as source:
        print('Recognising your voice....')
        r.pause_threshold=1  # seconds of non speaking audio before a phrase is considered complete 
        audio=r.listen(source)
    try:
        print('please wait...')
        query=r.recognize_google(audio,language='en-in')
        print(f'Did you mean : {query}\n')
    except exception as e:
        print('say it again,please')
        return 'none'    
    return query   
if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        if 'wikipedia' in query :
            speak('searching for your task....')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:  
            speak('opening')
            webbrowser.open('youtube.com')
        elif 'open google' in query:  
            speak('opening') 
            webbrowser.open('google.com')
        elif 'play music' in query:
            speak('playing music')
            pygame.init() 
            pygame.mixer.music.load('Alan Walker  Fade NCS Release.mp3')
            pygame.mixer.music.play()           
            time.sleep(20)           
        elif 'current time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            print(f'the current time is : {strtime}')
            speak(f'the current time is : {strtime}')
        elif 'open vs code' in query:
            codepath="C:\\Users\\91966\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak('opening vs code')
            os.startfile(codepath)
        elif ' command prompt' in query:          
            codepath="C:\\Users\\91966\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
            speak('opening command prompt')
            os.startfile(codepath)
        # speak('thankyou')
        exit()
