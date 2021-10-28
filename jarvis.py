import pyttsx3
import webbrowser
import wikipedia
import sys, os, subprocess
import time, datetime
import pyfiglet
from termcolor import colored
from playsound import playsound
import speech_recognition as sr

"""
Developer : suraj sharma
"""

#Printing Jarvis banner...
banner = pyfiglet.figlet_format("JARVIS")
print(colored(banner, "blue"))
print("\n\n")

# defining jarvis function so jarvis can reply to the commands
def jarvis(arguments):
    engine = pyttsx3.init()
    engine.say(arguments)
    engine.runAndWait()

#playing sound when jarvis is started
playsound('Jarvis.mp3')
jarvis("")

#setting date time to wish user good morning, good night or good evening
timing = int(datetime.datetime.now().hour)

#setting up a listener so jarvis can listen to the commands
listener = sr.Recognizer()

#this command will wish the user with greetings
with sr.Microphone() as source:
    if timing >= 0 and timing < 12:
        jarvis("good morning sir")
    elif timing >= 12 and timing < 18:
        jarvis("good afternoon sir")
    else:
        jarvis("good evening sir")
    jarvis("how may i help you today !")

#running a loop which run until or unless keyboard is interrupted
while True:

    try:
        print("\nlistening...\n")
        with sr.Microphone() as source:
            listener = sr.Recognizer()
            voice = listener.listen(source, phrase_time_limit=5)
            command = listener.recognize_google(voice).lower()
            print(command)


        if "how are you" in command:
            jarvis("i am fine sir as always")

        elif "hello" in command or "hi" in command:
            jarvis("Hello there Whatsupp")

        elif "i am also fine" in command or "i am fine" in command:
            jarvis("Nice to here that sir.")


        elif "what you can do" in command or "what can you do" in command:
            jarvis("Hello there i am jarvis, I am developed by Suraj sharma and I can perform some tasks like, i can tell you the time, open chrome for you, tell your system information, can search any thing on web for you, can also tell you about anything, like about india, about camera etc.. and many more things i can do just check out my commands")

        elif "time" in command:
            print(f"\n{time.ctime()}\n")
            jarvis(f"{time.ctime()}")

        elif "about" in command:
            info = wikipedia.summary(command[4:], sentences=2)
            print(f'\n{info}\n')
            jarvis(str(info))

        elif "search" in command:
            jarvis(f"searching for {command[7:]}")
            webbrowser.open(f'https://www.google.com/search?q={command[7:]}')

        elif "developer" in command:
            jarvis("I am developed by Suraj Sharma")

        elif "system" in command: 
            print(os.system('systeminfo'))
            jarvis("above you can see all your system information")

        elif "sleep for" in command:
            jarvis(f"sleeping for {command[10:13]} seconds")
            time.sleep(int(command[10:13]))


        elif "open youtube" in command:
            jarvis("openning, youtube")
            webbrowser.open('youtube.com')

        elif "open chrome" in command:
            jarvis(f"opening, chrome")
            subprocess.call('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')

        elif "execute" in command:
            jarvis(f"\nexecuting {command[7:]}\n")
            os.system(command[7:])
            jarvis("execution completed !")

        elif "buy" in command or "bye" in command:
            jarvis("bye and have a nice day sir ")
            sys.exit()

        else:
            jarvis("command not recognized !")

    except Exception as e:
        print(e)
