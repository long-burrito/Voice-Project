import myprosody as mysp
import pickle
import pandas as pd

#p="Walkers"  Audio File title
#c=r"C:\Users\rener\Documents\GitHub\Voice-Project\myprosody" Path to the Prosody folder (Python 3.7)

p="passage 2 normal"
c=r"C:\Users\rener\Documents\GitHub\Voice-Project\myprosody"



percentages, numbers, column = mysp.myprosody(p,c)


print(percentages)
print("")
print(numbers)
print("")
print(column)
print("")

list = [percentages]
df = pd.read_csv(r"C:\Users\rener\Documents\GitHub\Voice-Project\myprosody\dataset\stats.csv")
print(df)

percent = pd.DataFrame(list, columns=column)
list = [numbers]
num = pd.DataFrame(list, columns=column)
#num = pd.DataFrame(numbers, columns=column)
#print(list)
print(percent)
print(num)
print(df.loc[1])
mean_values = df.loc[1]


#print(num)
#ratio = syllable_count/pauses
#print(f"The ratio between syllable count and pauses is {ratio}")

