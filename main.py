import speech_recognition as sr
import pyttsx3
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate' , 150)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		talk("Good Morning Boss!")

	elif hour>= 12 and hour<18:
		talk("Good Afternoon Boss!")

	else:
		talk("Good Evening Boss!")
wishMe()
talk('This is friday at you service')   
talk('what can i Do for you?')

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
    talk("Boss! i can't here you , are you talking to me")
    pass        