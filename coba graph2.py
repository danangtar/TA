import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open('returngrde2.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'uint8')
signal = signal[:114441]
fs = spf.getframerate()

#If Stereo
if spf.getnchannels() == 2:
    print('Just mono files')
    sys.exit(0)


Time=np.linspace(0, len(signal)/fs, num=len(signal))

plt.rcParams['agg.path.chunksize'] = 10000
plt.figure(1)
plt.title('After')
plt.plot(Time,signal)
plt.show()