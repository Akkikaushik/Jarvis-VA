import sounddevice as sd 
import pyttsx3
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import smtplib 
import write 
import wavio as wv



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()
#code for wishing 
def wishMe(): 
    hour =int(datetime.datetime.now().hour) 
    if hour >= 0 and hour < 12: 
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak(" Akshit sir. I am Jarvis . Please tell me how may I help you")

#code for listening to the command
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...") 
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo()
    server.starttls() 
    server.login('akshitkaushik1999@gmail.com', 'your-password') 
    server.sendmail('akshitkaushik1999@gmail.com', to,content) 
    server.close()

if __name__ == '__main__':
    wishMe() 
    k = 1
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query 
        if 'wikipedia' in query:
            speak('Searching Wikipedia...') 
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia") 
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open_new("https://www.youtube.com/?gl=IN")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'E:\\songs'  
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sir, the time is {strTime}")
        elif 'record audio' in query:
            freq = 44100
            duration = 15
            # This will start recorder with the given values of
            #duration and sample frequency
            recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
            sd.wait()  # makes the program wait and recover from deadlock
            # This will convert the NumPy array to an audio file
            # with the given sampling frequency
            # Here the NumPy array is converted to audio file 
            wv.write("recording1.wav", recording, freq, sampwidth = 2)
        elif 'open code' in query:
            codePath= "C:\\Users\\HP\\OneDrive\\Desktop\\python\\Jarvis VA\\Jarvis VA.exe" #location of my project
            os.startfile(codePath)
        elif 'exit' in query: 
            k=0
        elif 'email to akshit' in query:
            try:
                speak("What should I say?")
                content=takeCommand() 
                to="akshitkauhsik1999@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")

        if k == 0:
            speak("going to sleep in 3 2 1")
            break
