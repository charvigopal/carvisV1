from subprocess import Popen
import gtts
from playsound import playsound
# from GazeTracking_master import prototype_milestone

print("Hi there! Welcome to Carvis.")
tts = gtts.gTTS("Hi there! Welcome to Carvis.")
tts.save("welcome_to_carvis.mp3")
playsound("welcome_to_carvis.mp3")
print("For the gaze task, would you like to play sound? Please type Y or N.")
tts = gtts.gTTS("For the gaze task, would you like to play sound? Please type Y or N.")
tts.save("playsound_prompt.mp3")
playsound("playsound_prompt.mp3")
entry = ""
while entry not in ["Y", "N"]:
    entry = input('in> ')
if entry == "Y":
    Popen('GazeTracking_master/prototype_milestone.py')
if entry == "N":
    Popen('GazeTracking_master/prototype_milestone.py')


