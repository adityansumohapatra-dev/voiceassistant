import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")
for i, v in enumerate(voices):
    print(i, v.id)

# Force to use the first available voice
engine.setProperty("voice", voices[0].id)

engine.say("Testing, can you hear me?")
engine.runAndWait()
