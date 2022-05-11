# Carvis


# Getting Started:
Clone this repo:
       https://github.com/charvigopal/carvisV1.git
cd carvisV1
Install the following dependencies:
 pip install -r requirements.txt

Following are the installations you would need to run: 

pip install reportlab 
pip language_tool_python 
pip install text2emotion
pip install PyPDF2
pip install opencv-python 
conda install pyaudio
pip install gtts
pip install fitz 
pip install PyMuPDF==1.18.9 
pip install textstat 
pip install audioread
pip install python-pptx 
pip install fake_useragent
pip install youtube_dl
pip install pytube
pip install cmake 
pip install dlib  


#OS requirements: 
Supports any OS. The project was tested on Windows as well as Mac OS. Recommended Python version >= 3.7

#Key functions in Carvis Breakdown:
cli.py
The starting point for Carvis is running: python cli.py in terminal. So this is the main file that calls which allows users to select from 3 modes: i) Gaze Mode
ii)  Speech Mode iii) Presentation Mode. 

audio_record.py
This is where the Speech mode begins. The user enters this mode when the user selects Speech mode in the CLI. This is where the user is given a prompt and the user can specify how long of a recording session they want. We use a speech recognition library for recording the audio and we save it in the user specified file.

video_transcript.py
This is where the Carvis report is prepared. It can work with both audio and video files.
 Once the recording is done, user can run python video_transcript.py which performs the transcription splitting audio to smaller chunks and performing transcription, detecting filler words

 make_presentation.py
This is where the presentation mode begins. Use can specify keywords and the program generates a presentation based on these keywords.

pick_any_video.py
The user can automatically download videos using this file which can then be used by other files.

gaze_cli.py
This file is where we enter gaze mode. We enter gaze mode when a user selects to enter gaze model while running cli.py. This is where we ask the user if they like to have the ding sound playing while they are speaking and generate a gaze report. We would like to credit open source project https://github.com/antoinelame/GazeTracking
for the detecting gaze. We essentially build on the work of this project and generate plots based on different directions the user looked into while talking/presenting.
















