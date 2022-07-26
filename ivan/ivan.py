from __future__ import print_function
import datetime
import os.path
import time
import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good morning")
    elif hour >= 12 and hour < 18:
        talk("Good Afternoon")
    else:
        talk("Good evenning")
def word():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    command = command_one(recognizer, microphone)
    return command
def talk(text, rate = 200):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def command_one(recognizer, microphone):
     # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source,duration=1)
        audio = recognizer.listen(source)
        recognizer.pause_threshold =1
    try:  
            query = recognizer.recognize_google(audio, language='en-us')
            print(query)    
    except Exception as e:
            print(e) 
            # talk("Say that again Please...")
            return"None"
    return query

def listOrDict(var):
    if isinstance(var, list):
        return var[0]['plaintext']
    else:
        return var['plaintext']

while True:

    command = word().lower()
    
    if 'Ivan'in command:
        wish()
        talk('I am here, How can i help you')
        command = word().lower()
        if 'what about you' in command:
            talk('I am normal as usual as you')
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            print(time)
            talk('current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'joke' in command:
            talk(pyjokes.get_joke())
            print(pyjokes.get_joke)

        elif 'good bye' in command:
            sys.exit()
        elif 'open google' in command:
            webbrowser.open('www.google.co.in')
            talk("opening google")
        elif 'open youtube' in command:
            webbrowser.open("www.youtube.com")
        elif 'play music' in command:
            talk("What song would you like")
            command = word().lower()
            pywhatkit.playonyt(command)
            # webbrowser.open('https://www.youtube.com/watch?v=NYjTGl6YLKQ')
            # music_dir = "start explorer C:/Users/Gost/Music/  "
            # musics = os.system(music_dir)
            # os.startfile(os.path.join(music_dir, musics[0]))
        elif "search for"in command:
            search_term = command.split("for")[-1]
            url = f"https://google.com/search?q={search_term}"
            webbrowser.get().open(url)
            talk(f'Here is what I found for {search_term} on google')
  
        else:
            talk('Sorry I did not hear your question, Please repeat again.')  