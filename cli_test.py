import subprocess 
from subprocess import Popen
import gtts
from playsound import playsound
# from GazeTracking_master import prototype_milestone

print("Hi there! Welcome to Carvis. Let's start with Gaze Mode, to help you practice looking straight at the camera when you are speaking.")
tts = gtts.gTTS("Hi there! Welcome to Carvis. Let's start with Gaze Mode, to help you practice looking straight at the camera when you are speaking.")
tts.save("welcome_to_carvis.mp3")
playsound("welcome_to_carvis.mp3")


# entry = input('in> ')
# while entry.lower() not in ["y", "n"]:
#     print("Would you like to see detailed instructions again?")
#     entry = input('in> ')
# if entry.lower() == "y":
#     pass 
# if entry.lower() == "n":
#     pass 


prompt = "Would you like me to play sounds when you are not looking straight at the camera? Please type Y or N."
tts = gtts.gTTS(prompt)
print(prompt)
tts.save("playsound_prompt.mp3")
playsound("playsound_prompt.mp3")
entry = input('in> ')
while entry.lower() not in ["y", "n"]:
    print("Would you like me to play sounds when you are not looking straight at the camera? Please type Y or N.")
    entry = input('in> ')
if entry.lower() == "y":
    tts = gtts.gTTS("Thanks for letting me know. I will play a sound when you aren't looking straight at the camera.")
    print("Thanks for letting me know. I will play a sound when you aren't looking straight at the camera.")
    tts.save("will_play_sound.mp3")
    playsound("will_play_sound.mp3")
    presentation_prompt = "Okay, now here's your task. I want you to imagine a project you really like. It could be your thesis project or your favorite personal project. Imagine meeting the president of MIT over a video call and explaining this project to them in one minute. Happy presenting!"
    tts = gtts.gTTS(presentation_prompt)
    print(presentation_prompt)
    tts.save("presentation_prompt.mp3")
    playsound("presentation_prompt.mp3")
    gaze_opening = "I am opening Gaze Mode now! Have fun, and press Escape to come back here!"
    tts = gtts.gTTS(gaze_opening)
    print(gaze_opening)
    tts.save("gaze_opening.mp3")
    playsound("gaze_opening.mp3")
    Popen('GazeTracking_master/implementation_milestone_with_sound.py')
    print('Now, let\'s try Speech Mode. Please enter the following command: python3 audio_record.py')
if entry.lower() == "n":
    tts = gtts.gTTS("Thanks for letting me know. I will not play a sound during the session, but I will show you a graph of where you looked afterwards.")
    print("Thanks for letting me know. I will not play a sound during the session, but I will show you a graph of where you looked afterwards.")
    tts.save("wont_play_sound.mp3")
    playsound("wont_play_sound.mp3")
    presentation_prompt = "Okay, now here's your task. I want you to imagine a project you really like. It could be your thesis project or your favorite personal project. Imagine meeting the president of MIT over a video call and explaining this project to them in one minute. Happy presenting!"
    tts = gtts.gTTS(presentation_prompt)
    print(presentation_prompt)
    tts.save("presentation_prompt.mp3")
    playsound("presentation_prompt.mp3")
    gaze_opening = "I am opening Gaze Mode now! Have fun, and press Escape to come back here!"
    tts = gtts.gTTS(gaze_opening)
    print(gaze_opening)
    tts.save("gaze_opening.mp3")
    playsound("gaze_opening.mp3")
    Popen('GazeTracking_master/implementation_milestone_without_sound.py')
    subprocess.call(['python', 'audio_record.py']) 
    print('Now, let\'s try Speech Mode. Please enter the following command: python3 audio_record.py')


