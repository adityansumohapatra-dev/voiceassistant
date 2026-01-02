import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
recognizer=sr.Recognizer()
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif "open facebook" in c.lower():
      webbrowser.open("https://facebook.com")
   elif "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")
   elif c.lower().startswith("play"):
      song=c.lower().split()[1]
      link= musicLibrary.music[song]
      webbrowser.open(link)
if __name__=="__main__":
    speak("Initializing Jarvis..") #listen to the wake word jarvis
#obtaining audio from the microphone from now
    while True:
        r=sr.Recognizer()
        print('recognizing.....')
        with sr.Microphone() as source:
           print("Say 'Jarvis' to wake...")
           audio = r.listen(source)
           command=r.recognize_google(audio)
           processCommand(command)
        try:
           word=r.recognize_google(audio)
           import difflib
           if difflib.get_close_matches("jarvis", [word.lower()], cutoff=0.7):
             speak("yes sir")
        except Exception as e:
           print("Error;{0}".format(e))














































































