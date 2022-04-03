# speech_to_text.py
import speech_recognition as sr
import time
from collections import Counter

r = sr.Recognizer()
mic = sr.Microphone()


#filename = "Hello World.wav"

# with sr.AudioFile(filename) as source:
#     audio = r.listen(source)
time_1 = time.time()
data = []
time_interval = 90
stopsignal = False
while not stopsignal:
	with mic as source:
		audio = r.listen(source)
	text = r.recognize_google(audio)
	print(text)
	text_list = text.split(" ")
	data += text_list
	time_2 = time.time()
	if time_2 - time_1 >= time_interval:
		stopsignal = True


filler_words = {'like','um', 'umm', 'totally', 'hmm', 'hmmm', 'literally', 'really', 'uh', 'actually'}
filler_output = dict()
freq_dict = Counter(data)
for i in range(len(data)):
	if data[i] in filler_words and data[i] not in filler_output:
		filler_output[data[i]] = 1
	elif data[i] in filler_words:
		filler_output[data[i]] += 1

print("Your word frequency:", freq_dict)
print("Filler words in your speech:", filler_output)





