# speech_to_text.py
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
	audio = r.listen(source)
	
#filename = "Hello World.wav"

# with sr.AudioFile(filename) as source:
#     audio = r.listen(source)

text = r.recognize_google(audio)
print(text)