import myprosody as mysp
import pickle
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pyaudio
import wave
import threading
import sys
import shutil
import os
import matplotlib.pyplot as plt
import numpy as np

#10/29/23 - had to adjust myprosody.py to output actual numbers instead of printing out strings

# Set up PyAudio
audio = pyaudio.PyAudio()

# Configure recording parameters
sample_format = pyaudio.paInt16  # Sample format (16-bit)
channels = 1  # Number of audio channels (1 for mono, 2 for stereo)
sample_rate = 44100  # Sample rate (samples per second)
chunk = 1024  # Buffer size
output_folder = "myprosody/dataset/audioFiles"
filename = "test.wav"  # Name of the output audio file

frames = []  # To store recorded audio frames

# Create a flag to indicate whether recording should continue
recording = True

# Define a function for the audio recording thread
def record_audio():
    global frames
    global recording

    # Open the audio stream for recording
    stream = audio.open(format=sample_format,
                       channels=channels,
                       rate=sample_rate,
                       frames_per_buffer=chunk,
                       input=True)

    print("Recording...")

    while recording:
        data = stream.read(chunk)
        frames.append(data)

    print("Stopped recording.")
    stream.stop_stream()
    stream.close()

# Start the audio recording thread
print("Do you want to record a new file? If yes, press y. Otherwise, any other keypress will go with what is already present.")
if input().lower() == 'y':
    recording_thread = threading.Thread(target=record_audio)
    recording_thread.start()
    try:
        print("Press 'q' and Enter to stop recording and save audio...")
        while True:
            user_input = input()
            if user_input.lower() == 'q':
                recording = False
                break
        recording_thread.join()
        audio.terminate()

        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(audio.get_sample_size(sample_format))
            wf.setframerate(sample_rate)
            wf.writeframes(b''.join(frames))

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        output_path = os.path.join(output_folder, filename)
        shutil.move(filename, output_path)

        print(f"Audio file moved to: {output_path}")
        audio.terminate()
    except KeyboardInterrupt:
        pass


p="passage 1"
c=r"C:\Users\rener\Documents\GitHub\Voice-Project\myprosody"



percentages, numbers, column = mysp.myprosody(p,c)
print("")
list = [percentages]
df = pd.read_csv(r"C:\Users\rener\Documents\GitHub\Voice-Project\myprosody\dataset\stats.csv")

percent = pd.DataFrame(list, columns=column)
list = [numbers]
num = pd.DataFrame(list, columns=column)
#num = pd.DataFrame(numbers, columns=column)
#print(list)
mean_values = df.loc[1]
mean_values = pd.DataFrame(mean_values)

num = num.T

num = num.drop(labels=["No._long_pause", "speaking_time", "No._words_in_minutes", "No._detected_vowel", "no._of_words", "no._of_pauses", "ave_No._of_words_in_minutes"], axis=0)
print("")
mean_values = mean_values.drop(labels=["No._long_pause", "speaking_time", "No._words_in_minutes", "No._detected_vowel", "no._of_words", "no._of_pauses", "ave_No._of_words_in_minutes"], axis=0)
mean_values = mean_values.iloc[1:, :]

print(mean_values)