r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
try: ##this is the sphinx recognition part
    print(r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("???")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
