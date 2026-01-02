import speech_recognition as sr
import webbrowser
import pyttsx3
import difflib
import musicLibrary
import sys
  # or whichever index speaks


# Initialize text-to-speech
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(text):
    """Speak out text using pyttsx3"""
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    """Process the recognized command"""
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open chrome" in c:
        webbrowser.open("google.com/chrome/")
    elif c.startswith("play "):
        song = c.replace("play ", "").strip()
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
            speak(f"Playing {song}")
        else:
            speak("Sorry, I don't know that song.")
    elif "stop" in c or "goodbye" in c or "exit" in c:
        speak("Shutting down. Goodbye sir.")
        sys.exit(0)
    else:
        speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    speak("Initializing Meena...")

    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source)

            word = recognizer.recognize_google(audio)
            print(f"Heard: {word}")

            # fuzzy match for "jarvis"
            matches = difflib.get_close_matches(
                word.lower(), ["jarvis"], n=1, cutoff=0.7
            )

            if matches:
                speak("Yes sir")
                with sr.Microphone() as source:
                    print("Meena Activated. Listening for command...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")
                    processCommand(command)

        except sr.UnknownValueError:
            print("Didn't catch that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google; {e}")
        except Exception as e:
            print(f"Error: {e}")
