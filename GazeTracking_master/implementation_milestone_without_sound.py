#!/usr/bin/env python

"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
from playsound import playsound
import time
from threading import Thread
import matplotlib.pyplot as plt

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
time_start = time.time()

def playSound():
    playsound('airplane_ding.wav')

horizontal_frequencies = {'left': 0, 'right': 0, 'center at camera': 0, 'up': 0, 'down': 0}
total = 0

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        pass 
        # text = "Blinking"
    else:
        # cv2.putText(frame, str(gaze.vertical_ratio()), (600, 120), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
        total += 1 
        if gaze.is_right():
            text = "<-- "
            cv2.putText(frame, text, (600, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
            horizontal_frequencies['right'] += 1
        if gaze.is_left():
            text = "-->"
            cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
            horizontal_frequencies['left'] += 1
        if gaze.is_up():
            text= ""
            cv2.putText(frame, text, (400, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
            horizontal_frequencies['up'] += 1
        if gaze.is_down():
            text= "^"
            cv2.putText(frame, text, (400, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
            horizontal_frequencies['down'] += 1
        if gaze.is_center():
            text= "looking center"
            cv2.putText(frame, text, (400, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
            horizontal_frequencies['center at camera'] += 1

    # left_pupil = gaze.pupil_left_coords()
    # right_pupil = gaze.pupil_right_coords()
    # cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    # cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
   
time_end = time.time()
webcam.release()
cv2.destroyAllWindows()

fig =  plt.figure(1, figsize = (10, 5))

for freq in horizontal_frequencies:
    horizontal_frequencies[freq] = (horizontal_frequencies[freq]/total) * (time_end - time_start)

plt.bar(horizontal_frequencies.keys(), horizontal_frequencies.values(), color ='blue',
        width = 0.4)

plt.xlabel("Direction")
plt.ylabel("Time (s)")
plt.title("Time Looked in Each Direction")
plt.show()
