# Voice Assistant in Python

# Basic Library's for Voice Assistant

import pyttsx3  # voice Output
import datetime  # For Now Current Date
import speech_recognition as sr  # For Access a Mic and speech to text Convertor in Google
import wikipedia  # For Searching in Wikipedia Website
import webbrowser  # Searching in Web
import os  # For Basic File Operation
import playsound   # Play Music
import pywhatkit as kit
import pyautogui # Control Keyboard and Mouse

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning BOSS!")  # Wish it self...

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon BOSS!")

    else:
        speak("Good Evening BOSS!")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5        #sec of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
    try:
        print("Wait for few Moments")
        query = r.recognize_google(audio, language = "en-in")
        #query = query.lower()
        print("user said: ", query)
        return query

    except Exception as e:
        #print(e)
        print("say that again please")
        speak("say that again please")


if __name__ == "__main__":
    wishme()
    while True:

        query = takecommand().lower()
        Jarvis_Name = "Balaji Assistant."
        Name_file = open("Name.text", "r")
        Name = Name_file.read()
        Name_file.close()
        #webbrowser.open(query)


        if ("in wikipedia" or "wikipedia") in query:
            try:
                speak("searching in wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except:
                speak("Tell clearly again pls")
                print("Tell clearly again pls!")

        elif "your name" in query:
            print("My good name ", Name + ", my Good Game, Helping you")
            Name = "My good name ", Name + ", my Good Game, Helping you"
            speak(Name)

        elif "your" and "birthday" in query:
            print("I am born in January 31, 2022")
            speak("I am born in January 31, 2022")

        elif "where" and ("home" or "house") in query:
            print("I live in your laptop")
            speak("I live in your laptop")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif ("open music" or "play music") in query:  # Put File Directory path in playsound argument
            playsound.playsound("File Directory.mp3")

        elif "open chrome" in query:  # It Have a New Method to open Aplication
            command = query
            command = command.replace("application", "")
            command = command.replace("app")
            command = command.replace("open", "")
            command = command.replace("the", "")
            # command = command.replace("a", "")
            if len(command) > 1:
                print("Opening App")
                pyautogui.press("win", interval=0.2)
                pyautogui.typewrite(command, interval=0.2)
                pyautogui.press("enter", interval=0.2)
            elif len(command) <= 1:
                print("Say your file name.")
                speak("Say your file name.")
                command = takecommand()
                command = command.replace("application", "")
                command = command.replace("app")
                command = command.replace("open", "")
                command = command.replace("the", "")
                pyautogui.press("win", interval=0.2)
                pyautogui.typewrite(command, interval=0.2)
                pyautogui.press("enter", interval=0.2)
            else:
                print("Opening App")
                pyautogui.press("win", interval=0.2)
                pyautogui.typewrite(command, interval=0.2)
                pyautogui.press("enter", interval=0.2)


        elif ("open notepad"  in query) or ("open my notepad" in query):

            speak("write or read")
            r = takecommand()
            if "write" in r or "right" in r:
                speak("tell me what you want to write")
                w = takecommand()
                f = open("C:\\Users\\Balaji\\Desktop\\New File.txt", "a")
                f.write(w)
                f.close()
                speak("File has been save in desktop successfully")
            elif "read" in r:
                f = open("C:\\Users\\Balaji\\Desktop\\New File.txt", "r")
                print(f)
                f.close()
                speak("File has been save in desktop successfully")

            else:
                continue

        elif "open" and "app" in query:
            command = query
            command = command.replace("application", "")
            command = command.replace("app")
            command = command.replace("open", "")
            command = command.replace("the", "")
            # command = command.replace("a", "")
            if len(command) > 1:
                print("Opening App")
                pyautogui.press("win", interval=0.2)
                pyautogui.typewrite(command, interval=0.2)
                pyautogui.press("enter", interval=0.2)
            elif len(command) <= 1:
                print("Say your file name.")
                speak("Say your file name.")
                command = takecommand()
                command = command.replace("application", "")
                command = command.replace("app")
                command = command.replace("open", "")
                command = command.replace("the", "")
                pyautogui.press("win", interval=0.2)
                pyautogui.typewrite(command, interval=0.2)
                pyautogui.press("enter", interval=0.2)
            else:
                print("Opening App")
                pyautogui.press("win", interval=0.2)
                pyautogui.typewrite(command, interval=0.2)
                pyautogui.press("enter", interval=0.2)

        elif "open" and "application" in query:
            command = query
            command = command.replace("application", "")
            command = command.replace("app")
            command = command.replace("open", "")
            command = command.replace("the", "")
            # command = command.replace("a", "")
            if len(command) > 1:
                print("Opening App")
                pyautogui.press("win", interval=0.2)
                pyautogui.typewrite(command, interval=0.2)
                pyautogui.press("enter", interval=0.2)
            elif len(command) <= 1:
                print("Say your file name.")
                speak("Say your file name.")
                command = takecommand()
                command = command.replace("application", "")
                command = command.replace("app")
                command = command.replace("open", "")
                command = command.replace("the", "")
                pyautogui.press("win", interval=0.2)
                pyautogui.typewrite(command, interval=0.2)
                pyautogui.press("enter", interval=0.2)
            else:
                print("Opening App")
                pyautogui.press("win", interval=0.2)
                pyautogui.typewrite(command, interval=0.2)
                pyautogui.press("enter", interval=0.2)

        elif "open zoom" in query:
            codepath3 = "C:\\Users\\Balaji\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(codepath3)

        elif "open gmail" in query:
            webbrowser.open("gmail.com")

        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(time)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif ("who made you" or "who created you") in query:
            speak("I have been created by Balaji.")

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "why you came to world" in query:
            speak("Thanks to Balaji. further It's a secret")

        elif "in google" in query:
            speak("searching in Google")
            print("Searching in Google")
            if "search in google" in query:
                query = query.replace("search in google", "")
            elif "search google" in query:
                query = query.replace("search google", "")
            elif "in google" in query:
                query = query.replace("in google", "")
            else:
                query = query.replace("search", "")
            search = query
            a = kit.info(search)
            print(a)
            speak(a)

        else:
            speak("its top most result")
            webbrowser.open(query)

    #  github.com/SriBalajiSMVEC
    # Thanks For visiting My GitHub page
