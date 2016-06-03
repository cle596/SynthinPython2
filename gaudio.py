import pyaudio
import math

PyAudio = pyaudio.PyAudio

bitrate = 16000

freq = 440
length = 1

if freq > bitrate:
    bitrate = freq + 100

numberofframes = int(bitrate * length)
restframes = numberofframes % bitrate
wavedata = ''

for x in range(0, numberofframes):
    wavedata = wavedata + \
        chr(int(math.sin(x / ((bitrate / freq) / (2 * math.pi)))*127 + 128))

for x in range(0, restframes):
    wavedata = wavedata + chr(128)

p = PyAudio()
