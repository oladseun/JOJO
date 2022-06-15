#libaries used in the buildup
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os
import json, requests
import subprocess as sp
#import randfacts
import webbrowser
import pyautogui

USERNAME = 'Oluwaseun'
BOTNAME = 'JOJO'

    #Greeting the user according to the time.
def greet_user():
    hour = datetime.datetime.now().hour
    if (hour >= 6) and (hour < 12):
        talk(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        talk(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        talk(f"Good Evening {USERNAME}")
    talk(f"I am {BOTNAME}. How may I assist you?")

#input source of command from microphone
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)

#function talk
def talk(text):
    engine.say(text)
    engine.runAndWait()

#paths to applications on the device
paths = {
    'soccer': "C:\\Users\\HP\\Desktop\\Pro Evolution Soccer 2017\\PES2017.exe",
    'notion': "C:\\Users\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Notion.lnk",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

# function commmand    
def take_command():
    try:
        with sr.Microphone() as source:
            listener.energy_threshold = 10000
            listener.adjust_for_ambient_noise(source, 1.2)
            #after intoduction
            print ("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            #making all commands lowercase
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    greet_user()
    global command
    command = take_command()
    # directing to youtube 
    if 'play' in command:
        print(command)
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        
    elif 'what is the time' in command:
        print (command)
        time = datetime.datetime.now().strftime('%I:%H:%p')
        print (time)
        talk('The time is ' + time)
        
    elif 'screenshot' in command:
        print (command)
        talk('wait a second')
        screenshot = pyautogui.screenshot()
        screenshot.save("c:/Users/HP/Pictures/Screenshots/image.png")
    
    #command for the who statement    
    elif 'who is' in command :
        person = command
        print(person)
        info = wikipedia.summary(person, 3)
        talk(info)

    #command for question statements
    elif 'how is'in command or 'what is' in command or 'search' in command:
        print (command)
        talk('wait a second')
        webbrowser.open(command)
        
    #command for facts
    #elif 'fact' in command:
        #print (command)
        #x = randfacts.getfact()
        #talk('Do you know that' + x) 

    #command for weather
    elif 'weather' in command:
        print (command)
        talk('The temperaure in Lagos is' + str(temperaure())) + 'degree celsius' + 'and with' + str(description())
        
    # to open camera on your device (Main Function)
    elif 'open camera' in command:
        print (command)
        talk('wait a second')
        sp.run('start microsoft.windows.camera:', shell=True)
    
    elif 'soccer' in command or 'notion'in command:
        print (command)
        talk('wait a second')
        os.startfile(paths[command])
        
    # questioning my VA
    elif 'who are you' in command :
        print (command)
        talk('I am JOJO, your favourite virtual assistant')
        
        
    elif 'who made you' in command :
        print(command)
        talk('I was made by Oluwaseun')
    
    elif 'end' in command :
        print(command)
        talk('Bye Oluwaseun, Hoping we talk soon')
        exit()
        
    elif 'hibernate' in command :
        print(command)
        talk('Device going for a long sleep.....')
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        
    elif 'shut down' in command :
        print(command)
        talk('Shutting down device........')
        os.system("shutdown /s /t 1")
        
    elif 'sleep' in command :
        print(command)
        talk('Device sleep........')
        time.sleep(90)
        
    else:
        print('Repeat command, please.')
        talk('Repeat command, please.')
    
        
        
while True:
    run_alexa()