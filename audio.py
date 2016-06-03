import pyaudio
import math

PyAudio = pyaudio.PyAudio

#See http://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 16000 #number of frames per second/frameset.

FREQUENCY = 700 #Hz, waves per second, 261.63=C4-note.
LENGTH = 1 #seconds to play sound

if FREQUENCY > BITRATE:
    BITRATE = FREQUENCY+100

NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''

for x in range(0,NUMBEROFFRAMES):
 WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))

for x in range(0,RESTFRAMES):
 WAVEDATA = WAVEDATA+chr(128)

p = PyAudio()
