import pyttsx3

engine = pyttsx3.init()
engine.say("Hi How are you")
engine.setProperty('rate',120)
engine.setProperty('volume',0.9)
engine.runAndWait()
