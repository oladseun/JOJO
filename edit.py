#libaries used in the buildup
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import os
import json, requests
import subprocess as sp
import webbrowser
import pyautogui

USERNAME = 'Oluwaseun'
BOTNAME = 'JOJO'

    #Greeting the user according to the time.
def greet_user():
    hour = datetime.datetime.now().hour
    if (hour >= 6) and (hour < 12):
        talk(f"Goood Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        talk(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        talk(f"Good Evening {USERNAME}")
    talk(f"I am {BOTNAME}. How may I assist you?")

#input source of command from microphone
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# for male or female voices
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
            if 'jojo' in command:
                #Removing the word 'jojo' from the command
                command = command.replace('jojo', '')
                print(command)
    except:
        return None

def run_alexa():
    greet_user()
    command = take_command()
    if command is not None:
    
    
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
        
    # to take a screenshoot
    elif 'screenshot' in command:
        print (command)
        talk('wait a second')
        screenshot = pyautogui.screenshot()
        screenshot.save("c:/Users/HP/Pictures/Screenshots/image.png")
        
    elif 'open command prompt' in command or 'open cmd' in command:
        open_cmd()
        
    elif 'ip address' in command:
        ip_address = find_my_ip()
        talk(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
        print(f'Your IP Address is {ip_address}')
    
    #command for news_headlines
    elif 'news' in command:
        talk(f"I'm reading out the latest news headlines, sir")
        talk(get_latest_news())
        print(*get_latest_news(), sep='\n')
    
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
        

    #command for weather
    elif 'weather' in query:
        ip_address = find_my_ip()
        city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
        talk(f"Getting weather report for your city {city}")
        weather, temperature, feels_like = get_weather_report(city)
        talk(f"The current temperature is {temperature}, but it feels like {feels_like}")
        talk(f"Also, the weather report talks about {weather}")
        talk("For your convenience, I am printing it on the screen sir.")
        print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
    
    # to open camera on your device (Main Function)
    elif 'open camera' in command:
        print (command)
        talk('wait a second')
        sp.run('start microsoft.windows.camera:', shell=True)
        

    elif "send an email" in query:
        speak("On what email address do I send sir? Please enter in the console: ")
        receiver_address = input("Enter email address: ")
        speak("What should be the subject sir?")
        subject = take_user_input().lower()
        speak("What is the message sir?")
        message = take_user_input().lower()
        if send_email(receiver_address, subject, message):
            speak("I've sent the email sir.")
        else:
            speak("Something went wrong while I was sending the mail. Please check the error logs sir.")
    
    elif 'command prompt' in command:    
        os.system('start cmd')
    
    elif 'soccer' in command or 'notion'in command:
        print (command)
        talk('wait a second please....')
        os.startfile(paths[command])
        
    # questioning my VA
    elif 'who are you' in command :
        print (command)
        talk('I am JOJO, your favourite virtual assistant')
        
        
    elif 'who made you' in command :
        print(command)
        talk('I was made by Oluwaseun')
    
    elif 'end' in command or 'bye' in command :
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
