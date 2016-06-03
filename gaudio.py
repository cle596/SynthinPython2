import pyaudio
import math

PyAudio = pyaudio.PyAudio

bitrate = 16000

freq = 880
LENGTH = 1  

if freq > bitrate:
    bitrate = freq + 100

NUMBEROFFRAMES = int(bitrate * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % bitrate
WAVEDATA = ''

for x in range(0, NUMBEROFFRAMES):
    WAVEDATA = WAVEDATA + \
        chr(int(math.sin(x / ((bitrate / freq) / math.pi)) * 127 + 128))

for x in range(0, RESTFRAMES):
    WAVEDATA = WAVEDATA + chr(128)

p = PyAudio()
