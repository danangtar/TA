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
# smoothness = np.reshape(smoothness, smoothness.size)

new_smooth = np.array_split(smooth, smoothness.size)
print("----")
new_list_smooth = []
for i in range(smoothness.size):
    temp = new_smooth[i].tolist()[0]
    temp.append(smoothness[i])
    new_list_smooth.append(temp)

new_list_smooth.sort(key=lambda x: x[4]) #reverse=True if descending
print(new_list_smooth)
#smoothness = np.array([np.array(i) for i in new_list_smooth])

#print(smooth.size)
#print(smoothness.size)

#print(np.concatenate((smooth, [smoothness.T]), axis=1))

# print(np.sort(smoothness))
# for item in smoothness:
#     print(item)