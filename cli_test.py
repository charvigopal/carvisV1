from subprocess import Popen
import gtts
from playsound import playsound
# from GazeTracking_master import prototype_milestone

print("Hi there! Welcome to Carvis.")
tts = gtts.gTTS("Hi there! Welcome to Carvis.")
tts.save("welcome_to_carvis.mp3")
playsound("welcome_to_carvis.mp3")
tts = gtts.gTTS("For the gaze task, would you like me to play sounds when you are not looking straight at the camera? Please type Y or N.")
print("For the gaze task, would you like me to play sounds when you are not looking straight at the camera? Please type Y or N.")
tts.save("playsound_prompt.mp3")
playsound("playsound_prompt.mp3")
entry = input('in> ')
while entry not in ["Y", "N"]:
    print("For the gaze task, would you like me to play sounds when you are not looking straight at the camera? Please type Y or N.")
    entry = input('in> ')
if entry == "Y":
    tts = gtts.gTTS("Thanks for letting me know. I will play a sound when you aren't looking straight at the camera. Happy presenting!")
    print("Thanks for letting me know. I will play a sound when you aren't looking straight at the camera. Happy presenting!")
    tts.save("will_play_sound.mp3")
    playsound("will_play_sound.mp3")
    Popen('GazeTracking_master/implementation_milestone_with_sound.py')
if entry == "N":
    tts = gtts.gTTS("Thanks for letting me know. I will not play a sound during the session, but I will show you a graph of where you looked afterwards. Happy presenting!")
    print("Thanks for letting me know. I will not play a sound during the session, but I will show you a graph of where you looked afterwards. Happy presenting!")
    tts.save("wont_play_sound.mp3")
    playsound("wont_play_sound.mp3")
    Popen('GazeTracking_master/implementation_milestone_without_sound.py')


