from email.mime import audio
from platform import python_branch
from turtle import speed
from unittest import result
import pyttsx3 #importing pyttx3 to take an voice from our computer which is sappi5
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# taking the engine variable to get the voice from our computer using pyttx3 and its module init
engine=pyttsx3.init('sapi5')
# getting the voice property
voices=engine.getProperty('voices')
# print(voices[0].id)
# setting the voice property or playing the voice
engine.setProperty('voice', voices[0].id)

def speak(audio):
    """this function will speak according to the parameter which we will pass inside it, so basically it will speak
    according to the parameter using the voice which we have set using pyttx3 module in above codes,so firstly we
    are taking engine variable and passing the audio parameter inside it then we are playing it """
    engine.say(audio)
    engine.runAndWait()    

def wishme():
    """this function will check the current time with the help of datetime method then it speaks or wish to the user
    according to the statements what we are passing with the conditions in below"""
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning mister arvind karanje")
    elif hour>=12 and hour<=18:
        speak("good afternoon mister arvind karanje")
    elif hour>18 and hour<23:
        speak("good evening mister arvind karanje sir")
    speak("i am jarvis........sir please tell me how may i help you")    
    speak("sir press 1 to continue with the voice interaction...")
    speak("sir press 2 to continue the interaction with me by keyboard...")

def takecomand():
    """it takes microphone input from the user and returns string output"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    return query

if __name__=="__main__":
    wishme()
    print("Press 1 for voice interaction with your jarvis assistance...")
    print("press 2 for keyboard interaction with your jarvis assistance...")
    usr=int(input("Enter your choice= "))
    if usr==1:
        speak("Hello mister Arvind sir now you can talk with me iam your assistance.....and i strictly follow your orders sir..."
              " say loudly whatever you want to perform ..")
        print("Hello mr Arvind now you can talk with me iam your assistance..and i strictly follow your orders sir"
              "say loudly whatever you want to perform ..")
        while True:
            query=takecomand().lower()
            #logic for executing takes based on query
            if 'wikipedia' in query:
                speak("searching wikipedia...")
                query=query.replace('wikipedia', "")
                results=wikipedia.summary(query, sentences=2)
                print(results)
                speak("According to wikipedia")
                speak(results)
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")    
            elif 'open google' in query:
                webbrowser.open("google.com")
            elif 'stack overflow' in query:
                webbrowser.open("stackoverflow.com")
            elif 'play music' in query:
                music_dir='C:\\Users\\RiyanCom\\Desktop\\musics'
                songs=os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
                print(f"{songs[0]} is playing now")
            elif 'time'in query:
                strtime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir the time is {strtime}")
            elif 'code' in query:
                # vscode_Dir="C:\\Users\\RiyanCom\\Desktop\\Visual Studio Code.lnk"
                vsdir="C:\\Users\\RiyanCom\\AppData\\Local\\Programs\\Microsoft VS Code"
                os.startfile(vsdir)
            elif 'quit' or 'exit' or 'end' or 'close' in query:
                exit()
            else:
                webbrowser.open(query)    

    elif usr==2:
        while True:
            speak("Hello mister Arvind sir now you cam interact with me using your keyboard..iam your assistance jarvis "
                  " and i strictly follow your orders sir.....type in below what you want")
            print("Hello mister Arvind now you can interact with me using your keyboard..iam your assistance jarvis"
                  " and i strictly follow your orders sir type in below what you want")
            query=input().lower()
            if 'wikipedia' in query:
                speak("Searching wikipedia...")
                query=query.replace('wikipedia', "")
                results=wikipedia.summary(query, sentences=5)
                print(results)
                speak("According to wikipedia")
                speak(results)
            elif 'youtube' in query:
                webbrowser.open("youtube.com")
            elif 'facebook' in query:
                webbrowser.open("Facebook.com") 
            elif 'sex' in query:
                webbrowser.open("fitness master virat kohli")
            elif 'chrome' in query:
                webbrowser.open("chrome.com")
            elif 'music' in query:
                msdir='C:\\Users\\RiyanCom\\Desktop\\musics'
                music_dir=os.listdir(msdir)
                print(music_dir)
                os.startfile(os.path.join(msdir, music_dir[0]))
                print(f"{music_dir[0]} is playing now")
            elif 'google' in query:
                webbrowser.open("google.com")
            elif 'stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
            elif 'time' in query:
                strtime=datetime.datetime.now.strftime("%H:%M:%S")
                print(strtime)
                speak(f"sir the time is {strtime}")
            elif 'code' in query:
                vsdir="C:\\Users\\RiyanCom\\Desktop\\Visual Studio Code.lnk"
                os.startfile(vsdir)
            elif 'quit' or 'exit' or 'close' or 'end' in query:
                exit()
            else:
                webbrowser.open(query)
    else:
        speak("wrong input please press a valid option 1 or 2")   
                