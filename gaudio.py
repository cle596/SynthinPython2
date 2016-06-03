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
        chr(int(math.sin(x / ((bitrate / freq) / (2 * math.pi))) * 127 + 128))

for x in range(0, restframes):
    wavedata = wavedata + chr(127)

p = PyAudio()

def play():
    stream = p.open(format=p.get_format_from_width(1),
                    channels=1,
                    rate=bitrate,
                    output=True)
    stream.write(wavedata)
    stream.stop_stream()
    stream.close()
    p.terminate()
