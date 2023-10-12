mysp = __import__("myprosody")
import pickle

#p="Walkers"  Audio File title
#c=r"C:\Users\rener\Documents\GitHub\Voice-Project\myprosody" Path to the Prosody folder (Python 3.7)

p="passage 1"
c=r"C:\Users\rener\Documents\GitHub\Voice-Project\myprosody"

mysp.myprosody(p,c)

mysp.mysplev(p,c)
