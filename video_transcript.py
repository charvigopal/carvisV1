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


now = datetime.now()
new_now = now.strftime("%H%M%S")
print(new_now)

print("Carvis Tips and Message Board!")
print("----------------------------------")
m1 = "Focus on delivering your message."
m2 = "Smile. Be relaxed, poised, and at ease on the outside, regardless of how you feel internally. Acting relaxed can help make you relaxed."
m3 = "Keep presenting! Your anxieties decrease the more presentations you give."
m4 = "Consider using a short icebreaker activity."
m5 = "A tasteful, humorous commentary can be effective if related to the topic."
m6 = "Explain the purpose of your presentation in one sentence that is free of professional jargon and emphasizes what participants will gain."
m = [m1, m2, m3, m4, m5, m6]
r_indices = set()
while len(r_indices) < 3:
	r_indices.add(random.randrange(0, 5))
r_indices_list = [m[x] for x in r_indices]
print(r_indices_list[0])
print(r_indices_list[1])
print(r_indices_list[2])

print("---------------------------------")

transcribed_audio_file_name = "transcribed_speech.wav"
# zoom_video_file_name = "togo.mp4"
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
	f = open("transcription.txt", "a")
	f.write(r.recognize_google(audio))
	f.write(" ")
f.close()


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

        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)

    pdf.output(filename, 'F')


input_filename = 'transcription.txt'
output_filename = 'TranscriptionReport.pdf'
file = open(input_filename)
text = file.read()
file.close()
text_to_pdf(text, output_filename)



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

visualize("transcribed_speech.wav")

textfile = open("transcription.txt", 'r')
# print(type(textfile))
process_data =  [(line.strip()).split() for line in textfile]
# data = [line.split(',') for line in textfile.readlines()]
# data = textfile.split(',')
data = process_data[0]

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









output = {}
freq_dict = Counter(data)
for i in range(len(data)):
	if data[i] not in output:
		output[data[i]] = 1
	else:
		output[data[i]] += 1

stopwords = ['to', 'the', 'a', 'from', 'I', 'that', 'me', 'do', 'and', 'is', 'my', 'for', 'of', 'it', 'if', 'in', 'we', 'but', 'you', 'are', 'have', 'not', 'it\'s', 'I\'m', 'am', 'at', 'so', 'will', 'be']
for word in stopwords:
	try:
		del output[word]
	except:
		pass 

words_keys = sorted(output, key=output.get, reverse=True)[:10]
words_vals = [output[words_key] for words_key in words_keys]

fig =  plt.figure(0, figsize = (10, 5))

plt.bar(words_keys, words_vals, color ='maroon',
        width = 0.4)

plt.xlabel("Common spoken words")
plt.ylabel("No. of times spoken")
plt.title("Words commonly used in Speech:")
plt.savefig("CommonWords.pdf")
# # plt.show()

# words_freq = dict()
# for key in words_key: 
# 	= output




# ### Filler Words ### 

filler_words = {'like','um', 'umm', 'totally', 'hmm', 'hmmm', 'literally', 'really', 'uh', 'actually', 'so'}
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





from PyPDF2 import PdfFileMerger
pdfs = ['TranscriptionReport.pdf', 'CommonWords.pdf','UserAmplitudePlot.pdf', 'SentimentPlot.pdf', 'FillerWords.pdf']

merger = PdfFileMerger()
for pdf in pdfs:
	merger.append(pdf)
merger.write("Carvis Report1.pdf")
merger.close()
print("............")
print("Preparing your Report!")
path = 'Carvis Report1.pdf'
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



