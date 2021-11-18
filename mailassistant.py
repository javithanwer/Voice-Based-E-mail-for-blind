import speech_recognition as sr
import easyimap as e
import pyttsx3
import smtplib
import streamlit as st

from pyttsx3 import Engine

unm = "javithproject@gmail.com"
pwd = "nileshsanju"

r = sr.Recognizer()

engine: Engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 220)


def speak(str):
    st.text(str)
    engine.say(str)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str = "Speak now:"
        speak(str)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            str = "Sorry sir. I could not recognize what you said."
            speak(str)
            listen()


def sendmail():
    rec = "javithanwer95@gmail.com"

    str = "Please speak the body of the mail"
    speak(str)
    msg = listen()

    str = "You have spoken the message"
    speak(str)
    speak(msg)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(unm, pwd)
    server.sendmail(unm, rec, msg)
    server.quit()

    str = "The email has been sent successfully."
    speak(str)


def readmail():
    server = e.connect("imap.gmail.com", unm, pwd)
    server.listids()

    str = "Please say the serial number of the email you wanna read, starting from the latest"
    speak(str)

    a = listen()
    if a == "Tu":
        a = 2

    b = int(a) - 1

    email = server.mail(server.listids()[b])

    str = "The mail is from: "
    speak(str)
    speak(email.from_addr)
    str = "The subject of the mail is: "
    speak(str)
    speak(email.title)
    str = "The body of email is: "
    speak(str)
    speak(email.body)


# but=st.button("Speak")
# st.text(but)
# if but:
st.set_page_config(layout="wide")
st.empty()
print("Starting")
str = "Hello sir. I am your email assistant."
speak(str)

while 1:
    print("In loop")
    str = "What do you want to do now?"
    speak(str)

    str = "To SEND an e-mail say send. To READ an e-mail say Read. Or if you want to exit, say Exit"
    speak(str)

    ch = listen()

    if ch == 'send':
        str = "You have chosen to send an email"
        speak(str)
        sendmail()

    elif ch == 'read':
        str = "You have chosen to read an email"
        speak(str)
        readmail()

    elif ch == 'freed':
        str = "You have chosen to read an email"
        speak(str)
        readmail()

    elif ch == 'exit':
        str = "You have chosen to exit, bye bye sir"
        speak(str)
        break

    elif ch == 'picsart' or 'PicsArt':
        str = "You have chosen to exit, bye bye sir"
        speak(str)
        break


    else:
        str = "Invalid choice. You said: "
        speak(str)
        speak(ch)
