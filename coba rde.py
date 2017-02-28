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
# print(quad.size)
x = 0
y = len(quad)
print(y)
vstrip = np.array([])
# print(v)

for isiquad in quad:
    i = 0
    while i < 3:
        vtemp = int(isiquad[i+1]) - int(isiquad[i])
        if(vtemp < -2):
            # vtemp = vtemp +
        v = np.append(v, vtemp)
        i += 1
        x += 1
        print(int((x/y)*100))

print(v)