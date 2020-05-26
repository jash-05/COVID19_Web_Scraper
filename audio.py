import speech_recognition as sr
import pyttsx3

from intent_matcher import process_input

active = 0

def SpeakText(command):
	engine = pyttsx3.init() 
	engine.say(command)  
	engine.runAndWait()

def print_and_speak(output):
	print(output)
	SpeakText(output)

while True:

	r = sr.Recognizer()
	mic = sr.Microphone()

	with mic as source:
		r.adjust_for_ambient_noise(source)
		print('Please speak now. ')
		audio = r.listen(source)

		try:
			
			user_input = r.recognize_google(audio,key='AIzaSyDRdSN1VaRW27HxA68rZW5FesS2qoPD8')

			print(user_input)

			#User greets 'buddy' in order to activate the script
 			if user_input.lower() == 'hey buddy' or 'hi buddy':
				active=1
				print_and_speak('Hello User')
				continue

			if user_input == 'goodbye':
				active=0
				print_and_speak('goodbye user')
				continue

			if user_input == 'break': 
				print('Terminating code')
				break

			if active==1:
				print_and_speak(process_input(user_input))

		except sr.UnknownValueError:
			if active==1:
				print("Didn't catch that, please try again. ")