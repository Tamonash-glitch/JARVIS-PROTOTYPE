import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import random
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

def speak(audio):
    '''
    sets up the ability to speak
    '''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''
    greets the user after collecting the time thus deciding what to say
    '''
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Night")
    speak("Greetings sir i am jarvis, at your service")

def takeCommand():
    '''
    takes microphone input from the user and returns string output
    '''
    r=sr.Recognizer()
    with sr.Microphone() as source :
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said; {query}\n")
    except Exception as e :
        print("say that again please...")
        return "none"
    return query




if __name__== "__main__":
    speak("initialising jarvis ... jarvis initialized")
    print("initialising jarvis ... jarvis initialized")
    wishMe()
    while True:
        query=takeCommand().lower()
        #logic for executing the tasks based on query
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "open spotify" in query:
            webbrowser.open("spotify.com")
        elif "play music" in query:
            music_dir = "C:\\songs"
            songs=os.listdir(music_dir)
            songnum=random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[songnum]))
        elif "the time" in query :
            strTime=datetime.datetime.now().strftime("%H,%M,%S")
            print(strTime)
            speak(f"sir the time is{strTime}")
        elif"open code" in query:
            codepath=r"C:\Users\tamon\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)