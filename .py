from flask import Flask, render_template, request
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import datetime

app = Flask(__name__)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "some error occurred"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handle_query', methods=['POST'])
def handle_query():
    query = request.form['query']
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
             ["google", "https://www.google.com"]]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            say(f"Opening {site[0]} sir..")
            webbrowser.open(site[1])

    if "open music" in query:
        musicPath = r"C:\Users\Asus\Downloads\Tum Tak.mp3"
        os.startfile(musicPath)

    if "the time" in query:
        strftime = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"sir the time is {strftime}")

    return "Query handled successfully."

if __name__ == '__main__':
    app.run(debug=True)
