import myprosody as mysp
import pickle

#p="Walkers"  Audio File title
#c=r"C:\Users\rener\Documents\GitHub\Voice-Project\myprosody" Path to the Prosody folder (Python 3.7)

p="french"
c=r"C:\Users\rener\Documents\GitHub\Voice-Project\myprosody"

mysp.myprosody(p,c)
mysp.myspsyl(p,c)
mysp.mysppaus(p,c)
mysp.mysplev(p,c)

#ratio = syllable_count/pauses
#print(f"The ratio between syllable count and pauses is {ratio}")