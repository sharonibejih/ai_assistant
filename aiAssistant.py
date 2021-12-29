import speech_recognition as sr
import pyttsx3
import datetime
from time import sleep

print('Loading your fashion assistant - ASTRA')

engine=pyttsx3.init()

""" VOICE"""
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # reduce the speed

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 170)     # setting up new voice rate


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour>=12 and hour<16:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source, 10, 3)

        try:
            # a user should be able to select a langauge.
            statement=r.recognize_google(audio,language='en')
            print(f"You said: {statement}\n")

        except Exception as e:
            speak("Sorry, Astra didn't get that. Please repeat")
            return takeCommand()
        return statement

speak("Loading your fashion assistant Astra")
wishMe()


if __name__=='__main__':

    while True:
        speak("Talk to me. How can I help you?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "ok bye" in statement or "stop" in statement or "thank you" in statement or "thanks" in statement:
            speak('Your fashion assistant, Astra, is shutting down. Good bye ')
            print('Your fashion assistant, Astra, is shutting down. Good bye ')
            break

        if "cloth" in statement or "shop" in statement or "buy" in statement:
            speak("Kindly tell me the following, accordingly:")
            print("Kindly tell me the following, accordingly:\n")
            sleep(0.15)

            speak("What's the age of the person you are purchasing for?")
            print("What's the age of the person you are purchasing for?\n")
            age = takeCommand()
                            
            speak("What Occasion is the outfit for? Casual, Dinner Party, or Official")
            print("What Occasion is the outfit for? Casual, Dinner Party, or Official\n")            
            occasion = takeCommand()
            

            speak("What's your budget for a suitable outfit? It could be between $40 to $1000")
            print("What's your budget for a suitable outfit? It could be between $40 to $1000\n")
            budget = takeCommand()

            speak("Give me a minute to recommend some wears to you...")
            print("Give me a minute to recommend some wears to you...\n")

        else:
            speak("You can say stop to shut me up or you can tell me what you'd like to shop again")
            print("You can say 'stop' to shut me up or you can tell me what you'd like to shop again")