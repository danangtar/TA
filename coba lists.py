import numpy as np
import wave

spf = wave.open('Bruno_Mars_Versace_On_The_Floor.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'uint8')

size = signal.size

mod = divmod(size,4)
headlen = size-mod[1]
print(size)
print(mod)

head = signal[:headlen]
tail = signal[headlen:]

quad = head.reshape((-1, 4))
# print(quad)

quadavg = np.mean(quad, axis=1, dtype=np.float64)

quadavgsize = quadavg.size
quadavgmod = divmod(quadavgsize, 4)
print(quadavgmod)
print(quadavgsize)

quadavgheadlen = quadavgsize - quadavgmod[1]
quadavghead = quadavg[:quadavgheadlen]
quadavgtail = quadavg[quadavgheadlen:]

smooth = quadavghead.reshape((-1, 4))
smoothness = np.var(smooth, axis=1, dtype=np.float64)
# print(smoothness)

for item in smoothness:
    print(item)