import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib


engine=pyttsx3.init('sapi5') # engine is nothing but just an object
voices=engine.getProperty("voices") # it return no of voices availble in sapi5 or in engine
# print(voices) #  printing no of voices availble in engine
engine.setProperty("voice",voices[0].id) # if there is a multiple voices in sapi5 then we used to set only one voice
print("hello this is zaid welcome you to all in my screen thanks")
def speak(audio):
    '''to speak the given input'''
    engine.say(audio) # .say function is used to speak engine.just taking input as an audio
    engine.runAndWait()
def wishme():
    ''' to wishing every body based on time'''
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good morning")
    elif hour >12 and  hour <18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("iam zaid sir. please tell me how may i help you")
    
def takecommand():
    '''it take microphone input from the user and return a string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio_dat=r.listen(source)
    try:
        print("Recoginizing...")
        query = r.recognize_google(audio_dat,language="en-in")
        print(f"user said: {query}")
        # speak(query)
    except:
        print("sorry i didnt recoginze your voice\n please tell one more time")
        return "None"
    return query
def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('zaidjub@gmail.com',"z@!d7744")
    server.sendmail('zaidjub@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
    # speak("hello iam zaid")
    wishme()
    query=takecommand().lower()
    speak(query)
    # logic on excuting task based on the query
    while True:
        if "wikipedia" in query:
            speak("searching wikipedia..")
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=1)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "the time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"sir the time is {strtime}")
        elif "open code" in query:
            codepath="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "send email" in query:
            try:
                speak("what should i send")
                print("please say what should i want to send...")
                content=takecommand()
                to='ayshazuha452@gmail.com'
                sendemail(to,content)
                speak("email has been sent")
            except Exception as E:
                print(E)
                speak("sorry my friend email has not send")


        break
    speak("thankyou")
            
