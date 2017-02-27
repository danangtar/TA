import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open('Bruno_Mars_Versace_On_The_Floor.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'uint8')
fs = spf.getframerate()

#If Stereo
if spf.getnchannels() == 2:
    print('Just mono files')
    sys.exit(0)


Time=np.linspace(0, len(signal)/fs, num=len(signal))

plt.rcParams['agg.path.chunksize'] = 10000
plt.figure(1)
plt.title('Signal Wave...')
plt.plot(Time,signal)
plt.show()