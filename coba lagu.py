import numpy as np
import wave
from scipy.io.wavfile import write

spf = wave.open('Bruno_Mars_Versace_On_The_Floor.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'uint8')

size = signal.size

mod = divmod(size,4)
headlen = size-mod[1]
# print(size)
# print(mod)

head = signal[:headlen]
tail = signal[headlen:]

pair = head.reshape((-1, 2))
tulis = pair.reshape(1, -1)
tulis = np.append(tulis, tail)
tulis.astype(np.int8)
# print(tulis)

write('test.wav', 44100, tulis)