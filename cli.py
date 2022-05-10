import subprocess 
from subprocess import Popen
import gtts
from playsound import playsound
# from GazeTracking_master import prototype_milestone

print("Hi there! Welcome (back) to Carvis. Press 1 for Gaze Mode, 2 for Speech Mode, 3 for Presentation Mode.")
tts = gtts.gTTS("Hi there! Welcome to Carvis. Press 1 for Gaze Mode, 2 for Speech Mode, 3 for Presentation Mode.")
tts.save("welcome_to_carvis.mp3")
playsound("welcome_to_carvis.mp3")


entry = input('in> ')
while entry not in ["1", "2", "3"]:
    print("Press 1 for Gaze Mode, 2 for Speech Mode, 3 for Presentation Mode.")
    entry = input('in> ')
if entry == "1":
    subprocess.call(['python', 'gaze_cli.py'])  
if entry == "2":
    subprocess.call(['python', 'audio_record.py'])
if entry == "3":
    subprocess.call(['python', 'make_presentation.py'])


