import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def create_and_write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"File '{file_path}' created and written successfully.")
    except IOError:
        print(f"An error occurred while creating or writing to file '{file_path}'.")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Rafael! Please tell me how may I help you")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 1000
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again Please...")
        return "None"
    return query.lower()

def execute_command(query):
    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif "open youtube" in query:
        webbrowser.open("youtube.com")

    elif "open google" in query:
        webbrowser.open("google.com")

    elif "open stack overflow" in query:
        webbrowser.open("stackoverflow.com")

 
    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H, %M, %S")
        speak(f"Sir, the time is {strTime}")

    elif "open code" in query:
        codePath = "C:\\Users\\Humai\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Adjust this path accordingly
        os.startfile(codePath)

    

file_path = "pass.txt"
content = "password"
create_and_write_file(file_path, content)

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        if "exit" in query:
            speak("Goodbye Sir!")
            exit()
        else:
            execute_command(query)