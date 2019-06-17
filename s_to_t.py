#Python 2.x program for Speech Recognition 

import speech_recognition as sr 
def recognize():
	r = sr.Recognizer()
	m = sr.Microphone() 
	print("speak")

	with m as source:	
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source) 	
	try: 
		text = r.recognize_google(audio) 
		return ("YOU SAID: "+text) 
		#error occurs when google could not understand what was said 
	
	except sr.UnknownValueError: 
		return ("Speech Recognition could not understand audio") 
	
	except sr.RequestError as e: 
		return ("Could not request results from Google Speech Recognition service; {0}".format(e)) 


