import pyttsx3
import datetime
import speech_recognition as sr
import pyjokes
import pywhatkit
import wikipediaapi
import webbrowser

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listerning...")
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:   
        print("Say that again please...")
        return "None"
    return query

def wishme():
    time = int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        speak("Good morning Sir!")
    elif time>=12 and time<18:
        speak("Good Afternoon Sir!")
    elif time>=18 and time <20:
        speak("Good evening Sir!.")
    else:
        speak("Good Night Sir!")
    speak("Your personal assistant at your service sir, how may i help you")

def timing():
    speak("Sir, Current time is" + datetime.datetime.now().strftime("%I %M %p"))

def date():
    day = (int(datetime.datetime.now().day))
    month = (str(datetime.datetime.now().month))
    year = (int(datetime.datetime.now().year))
    speak("Sir, Today's date is")
    speak(day)
    speak(month)
    speak(year)

def yourself():
    speak("first of all why do you want to know about me, So if you wanted then i will tell something about me, iam your personal assistant, i was created by prasoon. currently iam the trial version of myself. in future i will be doing amazing stuff. if you want to know more about me contact my owner.")

def jokes():
    joke = pyjokes.get_joke()
    speak(joke)

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "sleep" in query:
            speak("Ok, bye sir. see you soon. let me sleep for some time")
            break
        elif "goodbye" in query:
            speak("Ok, bye sir. see you soon. let me sleep for some time")
            break
        elif "date" in query:
            date()            
        elif "time" in query:
            timing()   
        elif "introduce yourself" in query:
            yourself()
        elif "joke" in query:
            jokes()
        elif "play song" in query:
            query = query.replace("play","")
            speak("ok Sir playing "+query)
            pywhatkit.playonyt(query)
        elif "wikipedia" in query:
            query = query.replace("wikipedia","")
            query = query.rstrip()
            query = query.lstrip()
            wiki_wiki = wikipediaapi.Wikipedia("en")
            page_py = wiki_wiki.page(query)
            results = page_py.summary[0:]
            print(results)
            speak("According to wikipedia" + results)
        elif "open youtube" in query:
            speak("Opening sir")
            webbrowser.open("youtube.com")
        elif "open facebook" in query:
            speak("Opening sir")
            webbrowser.open("facebook.com")
        elif "open instagram" in query:
            speak("Opening sir")
            webbrowser.open("instagram.com")
        elif "open google" in query:
            speak("Opening sir")
            webbrowser.open("google.com")
        elif "open vpropel" in query:
            speak("Opening sir")
            webbrowser.open("vpropel.in")
        elif "open codechef" in query:
            speak("Opening sir")
            webbrowser.open("codechef.com")
        elif "new year" in query:
            speak("OK sir")
            speak("Happy new year to everyone. may this year brings happiness in your life and you achieve all your goals. And most importantly may this corona virus leave the earth. Thank You!")
