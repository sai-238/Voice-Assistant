import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate' , 150)

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('Hi Boss! This is friday at you service')
talk('what Shall i Do ?')
try:
    with sr.Microphone() as source:
        print('Listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'friday' in command:
            talk(command)
        else:
            talk('Did you tell me something to do?')
except:
    talk("Boss i can't here you , are you talking to me")
    pass        