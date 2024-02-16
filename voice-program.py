import myprosody as mysp
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import jaccard_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error
import pyaudio
import wave
import threading
import sys
import shutil
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from sklearn.metrics import confusion_matrix, classification_report

#10/29/23 - had to adjust myprosody.py to output actual numbers instead of printing out strings

# Set up PyAudio
audio = pyaudio.PyAudio()

# Configure recording parameters
sample_format = pyaudio.paInt16  # Sample format (16-bit)
channels = 1  # Number of audio channels (1 for mono, 2 for stereo)
sample_rate = 44000  # Sample rate (samples per second)
chunk = 1024  # Buffer size
output_folder = "myprosody/dataset/audioFiles"
filename = "lycci.wav"  # Name of the output audio file

#frames = [*]  # To store recorded audio frames

# Create a flag to indicate whether recording should continue
recording = True

# Define a function for the audio recording thread
# def record_audio():
#     global frames
#     global recording

#     # Open the audio stream for recording
#     stream = audio.open(format=sample_format,
#                        channels=channels,
#                        rate=sample_rate,
#                        frames_per_buffer=chunk,
#                        input=True)

#     print("Recording...")

#     while recording:
#         data = stream.read(chunk)
#         frames.append(data)

#     print("Stopped recording.")
#     stream.stop_stream()
#     stream.close()

# # Start the audio recording thread
# print("Do you want to record a new file? If yes, press y. Otherwise, any other keypress will go with what is already present.")
# if input().lower() == 'y':
#     recording_thread = threading.Thread(target=record_audio)
#     recording_thread.start()
#     try:
#         print("Press 'q' and Enter to stop recording and save audio...")
#         while True:
#             user_input = input()
#             if user_input.lower() == 'q':
#                 recording = False
#                 break
#         recording_thread.join()
#         audio.terminate()

#         with wave.open(filename, 'wb') as wf:
#             wf.setnchannels(channels)
#             wf.setsampwidth(audio.get_sample_size(sample_format))
#             wf.setframerate(sample_rate)
#             wf.writeframes(b''.join(frames))

#         if not os.path.exists(output_folder):
#             os.makedirs(output_folder)

#         output_path = os.path.join(output_folder, filename)
#         shutil.move(filename, output_path)

#         print(f"Audio file moved to: {output_path}")
#         audio.terminate()
#     except KeyboardInterrupt:
#         pass
#name_list = ["kalyn main", "may barnett backup", "grace ann", "greg cochran", "lycci", "thor seay", "jakku edited"]
master_list = []
#jack and eli's audio unusable, due to separate reasons
#use may barnett backup, grace ann good, greg cochran good, kalyn main good, lycci good, thor good
eli = "eli final"
c=r"C:\Users\Rene Ramirez\Documents\GitHub\Voice-Project\myprosody"
#uncomment when data analysis needed
def data_analysis(file_name, file_directory):
    percentages, numbers, column = mysp.myprosody(file_name,file_directory)
    print(f"File name: {file_name} has been read and analyzed")
    df = pd.read_csv(r"C:\Users\Rene Ramirez\Documents\GitHub\Voice-Project\myprosody\dataset\stats.csv")
    list = [numbers]
    percent = pd.DataFrame(list, columns=column)
    num = pd.DataFrame(list, columns=column)
    print("list is printed")
    print(list)
    print("-"*25)
    mean_values = df.loc[1]
    mean_values = pd.DataFrame(mean_values)

    num = num.T
    num.to_csv("values7.csv", index=True)

    print("transposed list: \n")
    print("-"*25)
    print(num)
    master_list.append([file_name, num])
# data_analysis(eli,c)
# # data_analysis(jack, c)
# print("master list below: should be multiple file names detected")
# print(name_list[6])
# for name,numbers in master_list:
#     print(f"file name: {name}")
#     print("-"*25)
#     print(numbers)

data = [{'Gender': 'Female','Educated': 'True','average_syll_pause_duration': 0.791158562, 'No._long_pause': 4.872787879, 'speaking_time': 52.83, 'ave_No._of_words_in_minutes': 2.897686087, 'articulation_rate': 5.041973792, 'No._words_in_minutes': 92.9393141, 'formants_index': 346.5907851, 'f0_index': 0.907811693, 'f0_quantile_25_index': 0.91546632, 'f0_quantile_50_index': 180.7314206, 'f0_quantile_75_index': 0.867854897, 'f0_std': 37.53711111, 'f0_max': 410.1670479, 'f0_min': 70.40981874, 'No._detected_vowel': 150, 'perc%._correct_vowel': 0.788888889, '(f2/f1)_mean': 2.866466309, '(f2/f1)_std': 0.733308493, 'no._of_words': 113, 'no._of_pauses': 43, 'intonation_index': 9, '(voiced_syll_count)/(no_of_pause)': 4.581395349, 'TOEFL_Scale_Score': 25, 'Score_Shannon_index': 3.26, 'speaking_rate': 2.695240109}
       ,{'Gender': 'Female','Educated': 'True','average_syll_pause_duration': 0.751524793, 'No._long_pause': 12.88984848, 'speaking_time': 69.78, 'ave_No._of_words_in_minutes': 2.29675059, 'articulation_rate': 3.996346027, 'No._words_in_minutes': 108.3450846, 'formants_index': 392.3115556, 'f0_index': 1.085337655, 'f0_quantile_25_index': 1.162979236, 'f0_quantile_50_index': 228.3916159, 'f0_quantile_75_index': 1.05000377, 'f0_std': 39.22652523, 'f0_max': 394.1238061, 'f0_min': 76.97042625, 'No._detected_vowel': 69, 'perc%._correct_vowel': 0.425531915, '(f2/f1)_mean': 2.245555946, '(f2/f1)_std': 0.563378762, 'no._of_words': 140, 'no._of_pauses': 22, 'intonation_index': 7, '(voiced_syll_count)/(no_of_pause)': 11.04545455, 'TOEFL_Scale_Score': 22, 'Score_Shannon_index': 2.85, 'speaking_rate': 3.142007452}
       ,{'Gender': 'Female','Educated': 'False','average_syll_pause_duration': 0.511238095, 'No._long_pause': 36.43681818, 'speaking_time': 71.96, 'ave_No._of_words_in_minutes': 2.478739095, 'articulation_rate': 4.313006025, 'No._words_in_minutes': 126.8137528, 'formants_index': 382.7220862, 'f0_index': 0.997426255, 'f0_quantile_25_index': 1.055650123, 'f0_quantile_50_index': 207.0790832, 'f0_quantile_75_index': 0.946128793, 'f0_std': 33.85279892, 'f0_max': 386.9533886, 'f0_min': 75.83354076, 'No._detected_vowel': 64, 'perc%._correct_vowel': 0.5, '(f2/f1)_mean': 2.355953775, '(f2/f1)_std': 0.563287177, 'no._of_words': 154, 'no._of_pauses': 21, 'intonation_index': 7, '(voiced_syll_count)/(no_of_pause)': 12.76190476, 'TOEFL_Scale_Score': 26, 'Score_Shannon_index': 3.325, 'speaking_rate': 3.677598832}
       ,{'Gender': 'Female','Educated': 'False','average_syll_pause_duration': 0.96389899, 'No._long_pause': 6.287967914, 'speaking_time': 77.8, 'ave_No._of_words_in_minutes': 2.614797765, 'articulation_rate': 4.549748111, 'No._words_in_minutes': 93.22676332, 'formants_index': 352.5222684, 'f0_index': 1.052614895, 'f0_quantile_25_index': 1.051144236, 'f0_quantile_50_index': 213.9151717, 'f0_quantile_75_index': 1.015303252, 'f0_std': 46.0913287, 'f0_max': 410.2389958, 'f0_min': 77.98204959, 'No._detected_vowel': 158, 'perc%._correct_vowel': 0.765957447, '(f2/f1)_mean': 3.034725322, '(f2/f1)_std': 0.830764424, 'no._of_words': 166, 'no._of_pauses': 45, 'intonation_index': 7, '(voiced_syll_count)/(no_of_pause)': 6.422222, 'TOEFL_Scale_Score': 21, 'Score_Shannon_index': 2.64, 'speaking_rate': 2.703576136}
       ,{'Gender': 'Male','Educated': 'False','average_syll_pause_duration': 0.581216783, 'No._long_pause': 64.45181818, 'speaking_time': 64.45, 'ave_No._of_words_in_minutes': 2.737400282, 'articulation_rate': 4.76307649, 'No._words_in_minutes': 144.9893556, 'formants_index': 345.5568367, 'f0_index': 0.995849641, 'f0_quantile_25_index': 1.096416793, 'f0_quantile_50_index': 114.1299734, 'f0_quantile_75_index': 0.869507896, 'f0_std': 20.8929885, 'f0_max': 392.5738872, 'f0_min': 79.68625882, 'No._detected_vowel': 43, 'perc%._correct_vowel': 0.766666667, '(f2/f1)_mean': 2.570604226, '(f2/f1)_std': 0.609004977, 'no._of_words': 156, 'no._of_pauses': 13, 'intonation_index': 7, '(voiced_syll_count)/(no_of_pause)': 20.84615385, 'TOEFL_Scale_Score': 28, 'Score_Shannon_index': 3.74, 'speaking_rate': 4.204691313}
       ,{'Gender': 'Male','Educated': 'False','average_syll_pause_duration': 0.4224, 'No._long_pause': 68.27727273, 'speaking_time': 68.28, 'ave_No._of_words_in_minutes': 2.753467197, 'articulation_rate': 4.791032923, 'No._words_in_minutes': 160.0977023, 'formants_index': 372.024, 'f0_index': 0.99799637, 'f0_quantile_25_index': 0.990869867, 'f0_quantile_50_index': 109.4735468, 'f0_quantile_75_index': 0.911921912, 'f0_std': 36.08700187, 'f0_max': 367.3343059, 'f0_min': 73.11446379, 'No._detected_vowel': 14, 'perc%._correct_vowel': 0.5, '(f2/f1)_mean': 2.392975674, '(f2/f1)_std': 0.863794268, 'no._of_words': 182, 'no._of_pauses': 5, 'intonation_index': 10, '(voiced_syll_count)/(no_of_pause)': 63.4, 'TOEFL_Scale_Score': 29, 'Score_Shannon_index': 3.94, 'speaking_rate': 4.642833367}
       ,{'Gender': 'Male','Educated': 'True','average_syll_pause_duration': 0.658789773, 'No._long_pause': 60.76315909, 'speaking_time': 60.76, 'ave_No._of_words_in_minutes': 2.484644789, 'articulation_rate': 4.323281932, 'No._words_in_minutes': 145.8460866, 'formants_index': 327.06, 'f0_index': 0.965660306, 'f0_quantile_25_index': 1.008895857, 'f0_quantile_50_index': 107.9623772, 'f0_quantile_75_index': 0.863012413, 'f0_std': 28.11364924, 'f0_max': 395.5182046, 'f0_min': 81.33573907, 'No._detected_vowel': 8, 'perc%._correct_vowel': 0.714285714, '(f2/f1)_mean': 2.00545451, '(f2/f1)_std': 1.022014283, 'no._of_words': 148, 'no._of_pauses': 2, 'intonation_index': 7, '(voiced_syll_count)/(no_of_pause)': 128.5, 'TOEFL_Scale_Score': 25, 'Score_Shannon_index': 3.285, 'speaking_rate': 4.229536513}
       ,{'Gender': 'Male','Educated': 'True','average_syll_pause_duration': 0.538741004, 'No._long_pause': 63.85956818, 'speaking_time': 62.31, 'ave_No._of_words_in_minutes': 2.877524944, 'articulation_rate': 5.006893403, 'No._words_in_minutes': 137.6943769, 'formants_index': 386.4601833, 'f0_index': 0.907211079, 'f0_quantile_25_index': 0.913901278, 'f0_quantile_50_index': 98.49206804, 'f0_quantile_75_index': 0.775403262, 'f0_std': 41.39462327, 'f0_max': 400.2554582, 'f0_min': 79.0226986, 'No._detected_vowel': 72, 'perc%._correct_vowel': 0.470588235, '(f2/f1)_mean': 2.365648269, '(f2/f1)_std': 0.774679953, 'no._of_words': 147, 'no._of_pauses': 24, 'intonation_index': 9, '(voiced_syll_count)/(no_of_pause)': 10.625, 'TOEFL_Scale_Score': 29, 'Score_Shannon_index': 3.9, 'speaking_rate': 3.993136929}
]

df = pd.DataFrame(data)
print(df)
#one hot encoding for gender
encoder_gender = OneHotEncoder(sparse_output=False)
encoded_gender = encoder_gender.fit_transform(df[['Gender']])
encoded_df_gender = pd.DataFrame(encoded_gender, columns = encoder_gender.get_feature_names_out(['Gender']))

#one hot encoding for education
encoder_ed = OneHotEncoder(sparse_output=False)
encoded_ed = encoder_ed.fit_transform(df[['Educated']])
encoded_df_ed = pd.DataFrame(encoded_ed, columns = encoder_ed.get_feature_names_out(['Educated']))

df_encoded = pd.concat([df.drop(['Gender', 'Educated'], axis=1), encoded_df_gender, encoded_df_ed], axis=1)


df = df_encoded

df = df.drop(['ave_No._of_words_in_minutes', 'Score_Shannon_index', 'TOEFL_Scale_Score', 'No._detected_vowel', 'perc%._correct_vowel', '(voiced_syll_count)/(no_of_pause)', 'formants_index', 'intonation_index', '(f2/f1)_mean', '(f2/f1)_std', 'No._long_pause', 'f0_quantile_25_index', 'f0_quantile_75_index', 'no._of_pauses', 'f0_index'],axis=1)

print(df)

df.to_csv("collection.csv", index=True)

educated_group = df[df['Educated_True'] == 1].drop(['Gender_Female', 'Gender_Male', 'Educated_False', 'Educated_True'], axis=1)
not_educated_group = df[df['Educated_True'] == 0].drop(['Gender_Female', 'Gender_Male', 'Educated_False', 'Educated_True'], axis=1)
print(educated_group)
print(not_educated_group)

euclidean_dist = euclidean_distances(educated_group, not_educated_group)
cosine_sim = cosine_similarity(educated_group, not_educated_group)
print("Euclidean Distance Matrix:")
print(euclidean_dist)
print("Cosine Similarity Matrix:")
print(cosine_sim)

vmin = 0.95  # Set the minimum value to be close to 1
vmax = 1.0   # Set the maximum value to 1

# Plot the heatmap with a red colormap
# sns.heatmap(euclidean_dist, annot=True, cmap="Reds", fmt=".2f",
#             xticklabels=['Sample 1', 'Sample 2', 'Sample 3', 'Sample 4'],
#             yticklabels=['Educated 1', 'Educated 2', 'Educated 3', 'Educated 4'])
# plt.title("Euclidean Distance Heatmap")
# plt.show()

X = df.drop(['Educated_True', 'Educated_False'], axis=1)
y = df['Educated_True']

# Stratified train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, stratify=df['Educated_True'], random_state=42)

# Model training
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)

# Convert y_test and y_pred to binary for Jaccard Score
y_test_binary = y_test
y_pred_binary = (y_pred > 0.5).astype(int)

# Calculate Jaccard Score
jaccard_similarity = jaccard_score(y_test_binary, y_pred_binary)

# Calculate Mean Squared Error and R-squared
mse = mean_squared_error(y_test, y_pred)
r_squared = r2_score(y_test, y_pred)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Print the results
print(f"Accuracy on the entire test set: {accuracy}")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r_squared*-1}")
print(f"Jaccard Similarity: {jaccard_similarity}")