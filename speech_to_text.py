import speech_recognition as sr
import time
from collections import Counter
import matplotlib.pyplot as plt


# plt.style.use('seaborn-dark-palette')

r = sr.Recognizer()
mic = sr.Microphone()


#filename = "Hello World.wav"

# with sr.AudioFile(filename) as source:
#     audio = r.listen(source)
time_1 = time.time()
data = []
time_interval = 30
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

# print("Your word frequency:", freq_dict)
# print("Filler words in your speech:", filler_output)

words_filler_key = list(filler_output.keys())
words_filler_vals = list(filler_output.values())

fig =  plt.figure(figsize = (10, 5))

plt.bar(words_filler_key, words_filler_vals, color ='maroon',
        width = 0.4)

plt.xlabel("Filler words spoken")
plt.ylabel("No. of times spoken")
plt.title("Filler words used in Speech:")
plt.show()

