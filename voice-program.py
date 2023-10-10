mysp = __import__("myprosody")
import pickle

#p="Walkers"  Audio File title
#c=r"C:\Users\rener\Documents\GitHub\Voice-Project\myprosody" Path to the Prosody folder (Python 3.7)

p="PPAP"
c=r"C:\Users\rener\Documents\GitHub\Voice-Project\myprosody"

mysp.myspsyl(p,c)
mysp.myspgend(p,c)

p="passage 2 slow"
mysp.myspatc(p,c)
mysp.myspgend(p,c)

p="passage 2 normal"
mysp.myspatc(p,c)
mysp.myspgend(p,c)

p="passage 2 fast"
mysp.myspatc(p,c)
mysp.myspgend(p,c)

p="fast 2 channel"
mysp.myspatc(p,c)
mysp.myspgend(p,c)
