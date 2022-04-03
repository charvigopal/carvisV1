# speech_to_text.py
import speech_recognition as sr
import time

r = sr.Recognizer()
mic = sr.Microphone()


#filename = "Hello World.wav"

# with sr.AudioFile(filename) as source:
#     audio = r.listen(source)
time_1 = time.time()
data = ""
time_interval = 10
stopsignal = False
while not stopsignal:
	with mic as source:
		audio = r.listen(source)
	text = r.recognize_google(audio)
	print(text)
	data += text
	time_2 = time.time()
	if time_2 - time_1 >= time_interval:
		stopsignal = True

