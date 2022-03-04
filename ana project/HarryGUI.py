import googlestt as gs
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import datetime
import random
from playsound import playsound
import pywhatkit
import pyjokes
import pyautogui
from requests import get
import pyaudio
import db
import camera

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
engine.setProperty('voices',voices[0].id)
def tocall():
    gs.main()
    return gs.printtext().lower()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Harry,your personal assisstant Please tell how can I help you!!!")

def takeCommand():
   
    r=sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Listening.....")
        r.pause_threshold=0.5
        audio=r.listen(source)

    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please.....")
        return "None"
    
    return query

def Task_Gui():
    wishMe()
    while True:
    
        print("Listening.....")
        gs.main()
        query=gs.printtext().lower()
        print("Recognizing.....")

        if 'how are you' in query:
            come =['I am cool , but my CPU runs hot Anyway what can i do for you?','Couldnt be better, what do you want?','Just finished removing chrome Was eating quite a lot of ram. By the way what do you want?']
            speak(random.choice(come))
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
            

        elif 'search' in query:
            speak("Searching wikipedia.....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            query=query.replace("search","")
            query=query.replace("in","")
            query=query.replace(" ","")
            speak("According to wikipedia.....")
            print(results)
            speak(results)
            speak("Do you want me to save it for further use")
            ans = tocall()
            if 'yes' in ans:
                speak("Saving it for further use") 
                db.insertindb(query,results)
            else:
                speak("Dont tell me i didnt warn you")

        elif 'find' in query:
            query=query.replace("find","")
            query=query.replace("in","")
            query=query.replace("database","")
            query=query.replace(" ","")
            speak("Searching.....")
            s=db.getdata(query)
            if ("No data found" in s):
                speak("Sorry, I could not find it")
            
            else:
                speak("Here are the results")
                print(s)
                speak(s)
        

       

        # elif 'website' in query:
        #     speak("Launching...")
        #     query=query.replace("harry","")
        #     query=query.replace("website","")
        #     web1=query.replace("open","")
        #     web2='https://'+web1+'.com'
        #     webbrowser.open(web2)
        #     speak("Launched!")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")

        # elif 'open vscode' in query:
        #     codePath = "C:\Users\HP\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Code.exe"
        #     os.startfile(codePath)

        # elif 'search on youtube' in query:
        #     query=query.replace("search on youtube","")
        #     speak(f"Playing {query}")
        #     pywhatkit.playonyt(query)

        elif 'joke' in query:
            jokes=speak(pyjokes.get_joke())
            print(jokes)

        elif 'ip address' in query:
            ip=get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif "open camera" in query:
            camera.openCamera()

        elif 'screenshot' in query:
            speak("What should be the name of the file?")
            fname=takeCommand()
            fpath=fname+".png"
            ss=pyautogui.screenshot()
            ss.save("C:\\Users\HP\\OneDrive\\Desktop\\ana project\\"+fpath)
            os.startfile("C:\\Users\\HP\\OneDrive\\Desktop\\ana project\\"+fpath)
            speak("Here is your screenshot!")

        
        
        elif 'exit' in query:
            speak("Bye. Before you go ,i have to tell you a joke")
            jokes=pyjokes.get_joke()
            speak(jokes)
            print(jokes)
            speak("Hope you enjoyed the experience")
            exit()







