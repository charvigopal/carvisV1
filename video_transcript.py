import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip
import opensmile
import matplotlib.pyplot as plt
import numpy as np
import wave, sys
from reportlab.pdfgen import canvas
import random
import webbrowser
from collections import Counter
from datetime import datetime
from scipy.io import wavfile
import gtts
from playsound import playsound
import fitz
from nltk.corpus import wordnet
from fpdf import FPDF
import audioread

# import mutagen
# from mutagen.wave import WAVE

now = datetime.now()
new_now = now.strftime("%H%M%S")
# print(new_now)

print("Carvis Tips and Message Board!")
tts = gtts.gTTS("Carvis Tips and Message Board!")
tts.save("message_mode.mp3")
playsound("message_mode.mp3")
print("----------------------------------")
m1 = "Focus on delivering your message."
m2 = "Smile. Be relaxed, poised, and at ease on the outside, regardless of how you feel internally. Acting relaxed can help make you relaxed."
m3 = "Keep presenting! Your anxieties decrease the more presentations you give."
m4 = "Consider using a short icebreaker activity."
m5 = "A tasteful, humorous commentary can be effective if related to the topic."
m6 = "Explain the purpose of your presentation in one sentence that is free of professional jargon and emphasizes what participants will gain."
m7 = "Don't be compelled to fill pauses with um, ah, you know, and like. These common fillers can diminish your credibility."
m = [m1, m2, m3, m4, m5, m6, m7]
r_indices = set()
while len(r_indices) < 4:
	r_indices.add(random.randrange(0, 6))
r_indices_list = [m[x] for x in r_indices]
print(r_indices_list[0])
print(r_indices_list[1])
print(r_indices_list[2])
print(r_indices_list[3])

print("---------------------------------")

transcribed_audio_file_name = "demo.wav"	
# transcribed_audio_file_name = "charvistressedaboutbrazildata.wav"
def audio_duration(length):
	return length/60
# audio_wave = Wave(transcribed_audio_file_name)
# audio_info = audio_wave.info 
# audio_length = float(audio_info.length)
# no_of_minutes = audio_duration(audio_length)

with audioread.audio_open(transcribed_audio_file_name) as f:
	totalsec = f.duration

no_of_minutes = audio_duration(totalsec)



text_file_name = "transcription"+str(new_now)+".txt"
# text_file_name = "transcription" + str(111652) + ".txt"
# zoom_video_file_name = "zoom_call.mp4"
# audioclip = AudioFileClip(zoom_video_file_name)
# audioclip.write_audiofile(transcribed_audio_file_name)
with contextlib.closing(wave.open(transcribed_audio_file_name,'r')) as f:
	frames = f.getnframes()
	rate = f.getframerate()
	duration = frames / float(rate)
total_duration = math.ceil(duration / 60)
r = sr.Recognizer()
for i in range(0, total_duration):
	with sr.AudioFile(transcribed_audio_file_name) as source:
		audio = r.record(source, offset=i*60, duration=60)
	# f = open("transcription.txt", "a")
	f = open(text_file_name, "a")
	# f.write(r.recognize_google(audio))
	try:
		f.write(r.recognize_google(audio))
	except:
		pass
	f.write(" ")
f.close()

# sample_rate, data = wavfile.read('transcribed_speech.wav')
# time_duration = len(data)/sample_rate





# import language_tool_python
# tool = language_tool_python.LanguageTool('en-US')
# g = open("transcription.txt", "r") 
# text =tool.check(g)
# # get the matches
# matches = tool.check(text)
# g.close()

# import myprosody as mysp
# p = "transcribed_speech.wav"
# path = r"./transcribed_speech.wav" 
# print(mysp.myspsyl(p, path))  #Gives the number of syllables
# print(mysp.mysppaus(p, path)) #Gives the no. of pauses







# print("Grammar Feedback:\n")
# print(matches)
# str_val = ""
# for matched_word in matches:
# 	m = matched_word.ruleId
# 	str_val += m
# 	# str_val += "\n"
# print(type(matches))
# f = open("transcription.txt", "a")
# f.write("\n \n")
# f.write("Grammar Feedback: \n")
# f.write(str_val)
# f.close()


filler_words = {'like','um', 'umm', 'totally', 'hmm', 'hmmm', 'literally', 'really', 'uh', 'actually', 'so', 'very', 'simply', 'slightly', 'basically', 'just', 'also'}

import textwrap
from fpdf import FPDF

def text_to_pdf(text, filename):
	a4_width_mm = 210
	pt_to_mm = 0.35
	fontsize_pt = 10
	fontsize_mm = fontsize_pt * pt_to_mm
	margin_bottom_mm = 10
	character_width_mm = 7 * pt_to_mm
	width_text = a4_width_mm / character_width_mm

	pdf = FPDF(orientation='P', unit='mm', format='A4')
	pdf.set_auto_page_break(True, margin=margin_bottom_mm)
	pdf.add_page()
	pdf.set_font(family='Courier', size=fontsize_pt)
	splitted = text.split('\n')

	for line in splitted:
		lines = textwrap.wrap(line, width_text)
		# print("This is a line", lines)
		# print(type(lines))
		# print(".......")
		count = 0
		if len(lines) == 0:
			pdf.ln()

		for wrap in lines:
		# 	count += 1

			# print(wrap)
			# print(wrap.split(' ')
			# wrap_list = wrap.split('')
			# for word_ in wrap_list:
			# 	if word_ in filler_words:


			# if count == 4:
			# 	pdf.set_text_color(255,0,0)
			# if count == 5:
			# 	pdf.set_text_color(0, 0, 0)

			# print("....")
			pdf.cell(0, fontsize_mm, wrap, ln=1)

	pdf.output(filename, 'F')


import textstat

# input_filename = 'transcription.txt'
input_filename = text_file_name
output_filename = 'TranscriptionReport' + new_now + '.pdf'
# output_filename = 'TranscriptionReport.pdf'
file = open(input_filename)
text = file.read()
file.close()
text_to_pdf(text, output_filename)
text_to_pdf("Transcription of your speech: \n" + text, "TranscriptionReportFile.pdf")
# text_to_pdf("Transcription of your speech: \n + Your readability score is " + str(textstat.flesch_reading_ease(text)) + "\n"+ text, "TranscriptionReportFile.pdf")




def visualize(path: str):
	# reading the audio file
	raw = wave.open(path)  
	# reads all the frames
	# -1 indicates all or max frames
	signal = raw.readframes(-1)
	signal = np.frombuffer(signal, dtype ="int16")    
	# gets the frame rate
	f_rate = raw.getframerate()
	# to Plot the x-axis in seconds
	# you need get the frame rate
	# and divide by size of your signal
	# to create a Time Vector
	# spaced linearly with the size
	# of the audio file
	time = np.linspace(
		0, # start
		len(signal) / f_rate,
		num = len(signal)
	) 

	plt.figure(1)  
	plt.title("User Presentation Audio Amplitude") 

	plt.xlabel("Time")

	plt.plot(time, signal)

	# plt.show()
	plt.savefig('UserAmplitudePlot.pdf', bbox_inches='tight')

 
	# Can also save
	# the plot using
	# plt.savefig('filename')

# visualize("transcribed_speech.wav")
visualize('demo.wav')
# visualize("timurban.wav")

textfile = open(text_file_name, 'r')
# textfile = open("transcription.txt", 'r')
# print(type(textfile))
process_data =  [(line.strip()).split() for line in textfile]
# data = [line.split(',') for line in textfile.readlines()]
# data = textfile.split(',')
data = process_data[0]

# print("This is data", data)
# print("Data type", type(data))


text_str = ""
for each_word in data:
	text_str += each_word
	text_str += " "


import text2emotion as te
print("Sentiment Analysis: \n")
emotion_dict = te.get_emotion(text_str)
emotion_keys = [x for x in emotion_dict]
emotion_values = [emotion_dict[x] for x in emotion_keys]

fig =  plt.figure(3, figsize = (10, 5))
plt.bar(emotion_keys, emotion_values, color ='#984ea3', width = 0.4)
plt.xlabel("Sentiment Record")
plt.ylabel("Probability Score")
plt.title("Sentiment plot of your Presentation")
plt.savefig("SentimentPlot.pdf")




# import textstat 
# # print("Dale Chall readability score", textstat.dale_chall_readability_score(text_str))

# from PIL import Image

# image_1 = Image.open(r'readability.jpg')

# im_1 = image_1.convert('RGB')
# # im_1.resize((10, 5))
# im_1.save(r'ReadabilityChart.pdf')





output = {}
freq_dict = Counter(data)
for i in range(len(data)):
	if data[i] not in output:
		output[data[i]] = 1
	else:
		output[data[i]] += 1

pronouns = {'I', 'we', 'you', 'yours', 'him', 'he', 'his', 'she', 'her', 'hers', 'We', 'You', 'it', 'they', 'them', 'theirs', 'us', 'mine', 'our', 'ours', 'us', 'myself', 'herself', 'yourself', 'ourselves'}
stopwords = ['with', 'has', 'by', 'to', 'the', 'a', 'from', 'on', 'that', 'been', 'do', 'and', 'is', 'for', 'of', 'it', 'if', 'in', 'which', 'but', 'are', 'have', 'not', 'it\'s', 'I\'m', 'am', 'at', 'so', 'will', 'be', 'an', 'that', 'was', 'this', 'can', 'we', 'you', 'I']
for word in stopwords:
	try:
		del output[word]
	except:
		pass 

for word in pronouns:
	try:
		del output[word]
	except:
		pass

words_keys = sorted(output, key=output.get, reverse=True)[:10]
# words_vals = [output[words_key] for words_key in words_keys]

words_keys = [x for x in words_keys if output[x] > 1]
words_vals = [output[words_key] for words_key in words_keys] 

fig =  plt.figure(0, figsize = (10, 5))

plt.bar(words_keys, words_vals, color ='maroon',
		width = 0.4)

plt.xlabel("Frequently spoken words")
plt.ylabel("No. of times spoken")
plt.title("Words Frequently used in Speech:")
plt.savefig("CommonWords.pdf")
# # plt.show()


pronounsOutput = dict()
for i in range(len(data)):
	if data[i] in pronouns and data[i] not in pronounsOutput:
		pronounsOutput[data[i]] = 1
	elif data[i] in pronouns and data[i] in pronounsOutput:
		pronounsOutput[data[i]] += 1

words_pronoun_keys = sorted(pronounsOutput, key = pronounsOutput.get, reverse=True)[:10]
words_pronoun_vals = [pronounsOutput[x] for x in words_pronoun_keys]
fig = plt.figure(6, figsize = (10, 5))
plt.bar(words_pronoun_keys, words_pronoun_vals, color ='crimson',
		width = 0.4)
plt.xlabel("Pronouns spoken in speech")
plt.ylabel("No. of times spoken")
plt.title("Pronouns frequently used in Speech:")
plt.savefig("PronounsPlot.pdf")



pronoun_words_keys = [" "+x+" " for x in words_pronoun_keys]
pronoun_transcription = fitz.open(output_filename)
for each_page in pronoun_transcription:
	for pronoun_word in pronoun_words_keys:
		#Search
		word_instances = each_page.searchFor(pronoun_word)
		# print("word instances", word_instances)
		#Highlight
		for inst in word_instances:

			highlight = each_page.addHighlightAnnot(inst)
			highlight.setColors(stroke = fitz.utils.getColor('yellow'))
			# highlight.setColors({"stroke": (1, 0.6, 0)})
			# highlight.setColors(colors= fitz.utils.getColor('red'))
			highlight.update()

pronoun_transcription.save('PronounsTranscription.pdf')














# words_freq = dict()
# for key in words_key: 
# 	= output
common_words_keys = [" "+x+" " for x in words_keys]
common_transcription = fitz.open(output_filename)
for each_page in common_transcription:
	for common_word in common_words_keys:
		#Search
		word_instances = each_page.searchFor(common_word)
		# print("word instances", word_instances)
		#Highlight
		for inst in word_instances:

			highlight = each_page.addHighlightAnnot(inst)
			highlight.setColors(stroke = fitz.utils.getColor('yellow'))
			# highlight.setColors({"stroke": (1, 0.6, 0)})
			# highlight.setColors(colors= fitz.utils.getColor('red'))
			highlight.update()

common_transcription.save('CommonWordsTranscription.pdf')





# ### Filler Words ### 

filler_output = dict()
freq_dict = Counter(data)
for i in range(len(data)):
	if data[i] in filler_words and data[i] not in filler_output:
		filler_output[data[i]] = 1
	elif data[i] in filler_words:
		filler_output[data[i]] += 1

words_filler_key = list(filler_output.keys())
words_filler_vals = list(filler_output.values())

fig =  plt.figure(2, figsize = (10, 5))

plt.bar(words_filler_key, words_filler_vals, color ='blue',
		width = 0.4)

plt.xlabel("Filler words spoken")
plt.ylabel("No. of times spoken")
plt.title("Filler words used in Speech:")
# plt.show()
plt.savefig("FillerWords.pdf")



filler_update_words = {' like ',' um ', ' umm ', ' totally ', ' hmm ', ' hmmm ', ' literally ', ' really ', ' uh ', ' actually ', ' so ', ' very ', ' simply ', ' slightly ', ' basically ', ' just ', ' also '}

open_transcription = fitz.open(output_filename)
for each_page in open_transcription:
	for filler_word in filler_update_words:
		#Search
		word_instances = each_page.searchFor(filler_word)
		# print("word instances", word_instances)
		#Highlight
		for inst in word_instances:

			highlight = each_page.addHighlightAnnot(inst)
			highlight.setColors(stroke = fitz.utils.getColor('red'))
			# highlight.setColors(colors= fitz.utils.getColor('red'))
			highlight.update()

open_transcription.save('FillerWordsTranscription.pdf')




longWordsOutput = dict()
for i in range(len(data)):
	if data[i] not in longWordsOutput and len(data[i]) >= 9:
		longWordsOutput[data[i]] = 1
	elif data[i] in longWordsOutput and len(data[i]) >= 9:
		longWordsOutput[data[i]] += 1

# list(longWordsOutput.keys())
# list(longWordsOutput.values())
words_long_key =  sorted(longWordsOutput, key=longWordsOutput.get, reverse=True)[:7]
words_long_key = [x for x in words_long_key if longWordsOutput[x] > 1]
words_long_vals = [longWordsOutput[x] for x in words_long_key]

fig = plt.figure(4, figsize = (10, 5))
plt.bar(words_long_key, words_long_vals, color ='purple',
		width = 0.4)

plt.xlabel("Key words spoken")
plt.ylabel("No. of times spoken")
plt.title("Key words used in Speech:")
# plt.show()
plt.savefig("LongWords.pdf")






long_transcription = fitz.open(output_filename)
for each_page in long_transcription:
	for long_word in words_long_key:
		#Search
		word_instances = each_page.searchFor(long_word)
		# print("word instances", word_instances)
		#Highlight
		for inst in word_instances:

			highlight = each_page.addHighlightAnnot(inst)
			highlight.setColors(stroke = fitz.utils.getColor('green'))
			# highlight.setColors(colors= fitz.utils.getColor('red'))
			highlight.update()

long_transcription.save('LongWordsTranscription.pdf')






list_of_synonyms = []
synonyms_dict = dict()
for each_word in words_long_key:
	synonyms = []
	if len(each_word) > 8:
		for syn in wordnet.synsets(each_word):
			for i in syn.lemmas():
				if i.name() != each_word:
					synonyms.append(i.name())
		synonyms_dict[each_word] = set(synonyms)
		# list_of_synonyms.append(set(synonyms))

# print("List of synonyms", list_of_synonyms)
# print("Synonyms Dictionary", synonyms_dict)

synonyms_pdf = FPDF()
synonyms_pdf.add_page()
synonyms_pdf.set_font("Times",  style = 'B',  size = 12)
synonyms_pdf.cell(200, 10, txt = "Synonyms to the frequently used keywords", ln = 1, align = 'C')
synonyms_pdf.set_font("Times",  size = 12)
line_count = 1
for each_word in synonyms_dict:
	line_count += 1
	new_txt = str(each_word) + ": " + str(synonyms_dict[each_word])
	synonyms_pdf.cell(200, 10, txt = new_txt, ln = line_count, align = 'L')
synonyms_pdf.output('Synonyms.pdf')


intro_pdf = FPDF()
intro_pdf.add_page()
intro_pdf.set_font("Times", style = 'B', size = 16)
intro_pdf.set_text_color(0,0,255)    
intro_pdf.cell(200, 10, txt ="Welcome to your Carvis Report!", ln = 1, align = 'C')
intro_pdf.set_font("Times",  size = 12)
l1 = "Here are the insights from the audio you recorded or the recording you specified. We hope you find them "
l2= "helpful: feel free to take notes to help you improve! First, let us look at your commonly-used "
l3 = "filler words and where they appear in the transcript of your speech."
l4 = "Hint: Best to use as few filler words as possible"
l5 = "Great speaker uses only 1 filler word per minute while an average speaker uses 5 filler word per minute."
l6 = "You spoke about " + str(sum(words_filler_vals)/ no_of_minutes) + " filler words per minute"
intro_pdf.cell(200, 10, txt = l1, ln = 2, align = 'L')
intro_pdf.cell(200, 10, txt = l2, ln = 3, align = 'L')
intro_pdf.cell(200, 10, txt = l3, ln = 4, align = 'L')
intro_pdf.cell(200, 10, txt = l4, ln = 5, align = 'L')
intro_pdf.cell(200, 10, txt = l5, ln = 6, align = 'L')
intro_pdf.cell(200, 10, txt = l6, ln = 7, align = 'L')

intro_pdf.output('CarvisIntro.pdf')

# intro_text = "Welcome to your Carvis report! Here are the insights from the audio you recorded or the recording you specified. We hope you find them helpful: feel free to take notes to help you improve! First, let us look at your commonly-used filler words and where they appear in the transcript of your speech."

# text_to_pdf(intro_text, "CarvisIntro.pdf")


def text_to_pdf1(text, filename):
	a4_width_mm = 210
	pt_to_mm = 0.35
	fontsize_pt = 10
	fontsize_mm = fontsize_pt * pt_to_mm
	margin_bottom_mm = 10
	character_width_mm = 7 * pt_to_mm
	width_text = a4_width_mm / character_width_mm

	pdf = FPDF(orientation='P', unit='mm', format='A4')
	pdf.set_auto_page_break(True, margin=margin_bottom_mm)
	pdf.set_text_color(0, 0, 255)
	pdf.add_page()
	pdf.set_font(family='Courier', size=fontsize_pt)
	splitted = text.split('\n')

	for line in splitted:
		lines = textwrap.wrap(line, width_text)
		count = 0
		if len(lines) == 0:
			pdf.ln()

		for wrap in lines:
			pdf.cell(0, fontsize_mm, wrap, ln=1)

	pdf.output(filename, 'F')






key1 = "Next, let us look at some of the frequently-occuring keywords in your speech and where they appear in the transcript of your speech. " 
key2 = "As you look at the graph of keywords, think about what each keyword represents. Is it a word that is essential to conveying the meaning of your speech? If so, it might be alright for the keyword to be repeated many times. " 
key3 = "If you wish to reduce repetition for some of the keywords, we have listed some synonyms for the commonly-used keywords. "
text_to_pdf1(key1 + key2 + key3, "KeyWordIntro.pdf")



pronoun1 = "Next, let us take a look at your frequency of using different pronouns and where they appear in the transcript of your speech. "

pronoun2 = "Look at the differences between the frequency of I or you and the frequency of we. If you are talking about a group effort and tend to say I or you more than you say we, consider using we more to create a more collaborative atmosphere. " 

pronoun3 = "Now, here is your challenge: which insights can you glean from looking at your pronoun distribution below?"
text_to_pdf1(pronoun1 + pronoun2 + pronoun3, 'PronounIntro.pdf')

sentiment1 = "Finally, we can explore what our system thinks your sentiment is based on the text of your speech. What do you infer from the plot below?"
text_to_pdf1(sentiment1, 'SentimentIntro.pdf')

ending1 = "That is it for now! Please come back soon to explore insights from more of your recordings or from any Internet video recordings! Happy practicing!"
text_to_pdf1(ending1, 'EndingIntro.pdf')



# print("This is text", text_str)
# print("Text type", type(text_str))

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Input text - to summarize
text = text_str

# Tokenizing the text
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

# Creating a frequency table to keep the
# score of each word

freqTable = dict()
for word in words:
	word = word.lower()
	if word in stopWords:
		continue
	if word in freqTable:
		freqTable[word] += 1
	else:
		freqTable[word] = 1

# Creating a dictionary to keep the score
# of each sentence
sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
	for word, freq in freqTable.items():
		if word in sentence.lower():
			if sentence in sentenceValue:
				sentenceValue[sentence] += freq
			else:
				sentenceValue[sentence] = freq



sumValues = 0
for sentence in sentenceValue:
	sumValues += sentenceValue[sentence]

# Average value of a sentence from the original text

average = int(sumValues / len(sentenceValue))

# Storing sentences into our summary.
summary = ''
for sentence in sentences:
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
		summary += " " + sentence


# summary_file = open("summary.txt", "w")
 
# #write string to file
# summary_file.write(summary)
 
# #close file
# summary_file.close()

summary_filename = 'SummaryReport' + new_now + '.pdf'
text_to_pdf("Summary of the speech: \n" + summary, summary_filename)





from PyPDF2 import PdfFileMerger
pdfs = [ 'CarvisIntro.pdf','FillerWords.pdf', 'FillerWordsTranscription.pdf', 'KeyWordIntro.pdf',
		'LongWords.pdf', 'LongWordsTranscription.pdf', 'Synonyms.pdf', 'PronounIntro.pdf' , 'PronounsPlot.pdf', 'PronounsTranscription.pdf', 
		'SentimentIntro.pdf', 'SentimentPlot.pdf','CommonWords.pdf', 'CommonWordsTranscription.pdf', 'TranscriptionReportFile.pdf', 'EndingIntro.pdf']
merger = PdfFileMerger()
for pdf in pdfs:
	merger.append(pdf)

print("............")
print("Preparing your Report!")
print("Please type your first name:" )
user_name = str(input())

report_name = user_name + new_now + ".pdf"

merger.write(report_name)
# merger.write("Carvis Report1.pdf")
merger.close()

# path = 'Carvis Report1.pdf'
path = report_name
webbrowser.open_new(path)











# from fpdf import FPDF
   
# pdf = FPDF()   
   
# # Add a page
# pdf.add_page()
   
# # set style and size of font 
# # that you want in the pdf
# pdf.set_font("Arial", size = 11)
  
# # open the text file in read mode
# f = open("transcription.txt", "r")
  
# # insert the texts in pdf
# count = 0
# ln_val = 1
# for x in f:
# 	if count % 6 == 0:
# 		# col += 10
# 		ln_val += 1
# 	pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
# 	count += 1
# # save the pdf with name .pdf
# pdf.output("Final Report.pdf")  



