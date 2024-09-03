import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk():
    engine.say("I am your Alexa")
    engine.runAndWait()

def take_command():
    try :
            with sr.Microphone() as source:
                print("Listening...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'alexa' in command:
                    command = command.replace('alexa','')
                    print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time = datetime.datetime().now().strftime('%I : %M  %p')
        print(time)
        talk('current time is' + time)
    
    elif 'wikipedia' in command:
        person = command.replace('wikepedia','')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    else:
        talk('please say that again')


run_alexa()

    