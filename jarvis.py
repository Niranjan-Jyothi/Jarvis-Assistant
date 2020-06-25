import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia (pip3 incase of python3)
import pyautogui #pip3 install pyautogui
import psutil #pip3 install psutil
import pyjokes #pip3 install pyjokes

import datetime
import smtplib
import webbrowser as wb
import os


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime('%I:%M:%S')
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current time is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("good morning sir!")
    elif hour >=12 and hour<=18:
        speak("good afternoon sir!")
    elif hour >= 18 and hour<24:
        speak("Good evening sir!")
    else:
        speak("good night sir!")
    speak("Jarvis at your service. Please tell me how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please.")
        return "None"

    return query

def senEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login( {email.id}, {password})
    server.sendmail( from_email , to_email, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save('your image directory')

def cpu():
    usage = str(psutil.cpu_percent())
    speak(f"CPU is at {usage}" )
    battery = psutil.sensors_battery()
    speak(f"Battery is at {battery.percent}")

def jokes():
    speak(pyjokes.get_joke())

if __name__ == '__main__': #main function
    wishme()
    while True:
        query = takeCommand().lower()
        
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = {to-email.id}
                senEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("unable to send th eemail")
        elif 'search in chrome' in query:
            speak("what should I search?")
            searching = True
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            while searching:
                search = takeCommand().lower()
                if search != 'none':
                    wb.get(chromepath).open_new_tab(search + '.com')
                    searching = False

        elif 'logout' in query:
            os.system("shutdown -l")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t -l")

        elif 'restart' in query:
            os.system("shutdown -r /t 1")

        elif 'play songs' in query:
            songs_dir = '{your song directory}'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember this' in query:
            speak("what should I remember?")
            data = takeCommand()
            speak(f"You asked me to remember that {data}")
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak(f"you asked me to rememeber these points" + remember.read() )

        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
        
        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            quit()