import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
print(voices[0].id)

engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    '''
    Greetings to user
    :return:
    '''
    hour =int(datetime.datetime.now().hour)
    if hour <=12:
        speak("good Morning")
    elif hour > 12 and hour<=16:
        speak("good Afternoon")
    elif hour > 16 and hour <=21:
        speak("good Evening")
    else:
        speak("good Night")
    speak("My name is Aditya. Please tell me how can I help you ")

def takecommand():
    '''
    take user commands(microphone inputs and returns string output)
    :return:
    '''
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...... ")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        querry = r.recognize_google(audio,language= 'en-in')
        print(f"user said :{querry}\n")
    except Exception as e:
        print(e)
        print(" say that Again please")
        return "none"
    return querry
if __name__ == '__main__':
    speak("hello User ")
    wishMe()
    while True:

        # querry = takecommand().lower()
        querry = input("what can i do for you:")
        # logic for executing tasks
        if 'a' or 'e' or 'o'or 'i' or 'u' in querry:
            speak("searching in wikipedia....")
            querry = querry.replace("wikipedia","")
            results = wikipedia.summary(querry,sentences=3)
            speak("according to wikipedia..")
            print(results)
            speak(results)
        elif "open youtube" in querry:
            speak("searching in youtube..")
            webbrowser.open("youtube.com")
        elif "open google" in querry:
            webbrowser.open("google.com")
        elif "open stackoverflow" in querry:
            webbrowser.open("stackoverflow.com")

        elif "play music" in querry:
            musicdir ='C:\\Users\\Public\\Music'
            songs =os.listdir(musicdir)
            os.startfile(os.path.join(musicdir,songs[random.randint(1,27)]))
        elif 'time' in querry:
            strtime = datetime.datetime.now().strftime("%H:%H:%S")
            speak(f"Sir the time is {strtime}")
        elif 'open whatapp' in querry:
            speak("opening whatsapp")
            codepath ="C:\\Users\\Admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codepath)
        elif 'open linux' in querry:
            speak("opening second operating system ")
            codepath2 = "D:\\Virtual Box\\VirtualBox.exe"
            os.startfile(codepath2)
