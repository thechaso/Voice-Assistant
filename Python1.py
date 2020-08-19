# Features: wikipedia, youtube, google, mix, music, time, pycharm, email,
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing Jarvis")


def speak(text):
   engine = pyttsx3.init()
   engine.say("{}".format(text))
   engine.runAndWait()


speak("Initializing Jarvis")
speak(
   "Type in your name, Email, and Pasword. Should you choose to enter False Email Credentials if you are feeling Uncomfortable, you will not be able to send emails throuh me.")
master = input("Name: ")
email = input("Email: ")
password = input("Password: ")


def wishMe():
   hour = datetime.datetime.now().hour
   if 0 <= hour < 12:
       speak("Good Morning. " + master)
   elif 12 <= hour < 18:
       speak("Good Afternoon. " + master)
   else:
       speak("Good Evening. " + master)
   speak("I am Jarvis. How may I help you")


def takeCommand():
   r = sr.Recognizer()
   with sr.Microphone() as source:
       print("Listening...")
       audio = r.listen(source)
   try:
       print("Recognizing...")
       query = r.recognize_google(audio, language="en-in")
       print(f"user said: {query}\n")
   except Exception as e:
       print("Say that again please")
       speak("Say that again plaese")
       query = None
   return query


def sendEmail(to, content):
   server = smtplib.SMTP("smtp.gmail.com", 587)
   server.ehlo()
   server.starttls()
   server.login(email, password)
   server.sendmail(email, to, content)
   server.close()


wishMe()
query = takeCommand()


def main():
   global query
   if "wikipedia" in query.lower():
       speak("Searching Wikipedia...")
       query = query.replace("wikipedia", "")
       results = wikipedia.summary(query, sentences=2)
       print(results)
       speak(results)
   elif "open youtube" in query.lower():
       url = "youtube.com"
       chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
       webbrowser.get(chrome_path).open(url)
   elif "open google" in query.lower():
       url = "google.com"
       chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
       webbrowser.get(chrome_path).open(url)
   elif "play mix" in query.lower():
       url = "https://www.youtube.com/watch?v=FjQk-2jHevs&list=RDFjQk-2jHevs&start_radio=1"
       chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
       webbrowser.get(chrome_path).open(url)
   elif "play music" in query.lower():
       url = "https://www.youtube.com/watch?v=VBlFHuCzPgY"
       chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
       webbrowser.get(chrome_path).open(url)
   elif "time" in query.lower():
       strTime = datetime.datetime.now().strftime("%H:%M:%S")
       lst = list(strTime)
       col_ind = lst.index(":")
       gen = "AM"
       hour = []
       strHour = []
       min = []
       strMin = []
       for i in range(col_ind):
           hour.append(lst[i])
       for i in range(len(hour) - 1):
           strHour = hour[i] + hour[i + 1]
       for i in range(col_ind + 1, col_ind + 3):
           min.append(lst[i])
       for i in range(len(min) - 1):
           strMin = min[i] + min[i + 1]
       if int(strHour) >= 12:
           gen = "PM"
       speak(master + ". The local time is " + strHour + "  " + strMin + " " + gen)
   elif "open pycharm" in query.lower():
       code_path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains"
       os.startfile(code_path)
   elif "email" in query.lower():
       try:
           speak("Type in the recipients email adress")
           to = input("Recipient's Email: ")
           speak("What should I send")
           content = takeCommand()
           sendEmail(to, content)
           speak(master + ". Email has been sent successfully")
       except Exception as e:
           print(e)
           speak("Faied to send Email")
   elif "goodbye" or "bye" or "see you" or "go to sleep" in query.lower():
       speak("see you later" + master + ". It was a pleasure talking to you")
       quit()
   else:
       speak("I am not familiar with this command. Please try again" + master)
   if query.lower() == "jarvis":
       query = takeCommand()


main()
"""
run = True
while run:
   query = takeCommand()
   main()
"""

