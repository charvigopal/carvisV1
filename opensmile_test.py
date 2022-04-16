import opensmile
import matplotlib.pyplot as plt
import numpy as np
import wave, sys

smile = opensmile.Smile(
feature_set=opensmile.FeatureSet.ComParE_2016,
feature_level=opensmile.FeatureLevel.Functionals,
)

# the result is a pandas.DataFrame containing the features
# y = smile.process_file("demo.wav")
# print(y)
 
# shows the sound waves
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
    plt.title("User Presentation Audio Waves") 

    plt.xlabel("Time")

    plt.plot(time, signal)

    plt.show()
 
    # Can also save
    # the plot using
    # plt.savefig('filename')
 
 
visualize("demo.wav")


