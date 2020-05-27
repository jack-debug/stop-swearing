import os
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
try:
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("Error: Audio could not be understood")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
