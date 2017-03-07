import numpy as np
import wave
import TA.pesan

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
y = pair.size
pair = pair.tolist()
x = 0
lm = []


teks = TA.pesan.Pesan()
teks = teks.getBinary()
panjangteks = len(teks)
print(teks)
print(pair)

def expandable(v, m, b):
    vtemp = 2 * v + b
    if (128 <= m <= 255):
        if (abs(vtemp) <= 2 * (255 - m)):
            lm.append(0)
        else:
            changeable(v, m, b)
    elif (0 <= m <= 127):
        if (abs(vtemp) <= 2 * m + 1):
            lm.append(0)
        else:
            changeable(v, m, b)

def changeable(v, m, b):
    vtemp = 2 * abs(v / 2) + b
    if (128 <= m <= 255):
        if (abs(vtemp) <= 2 * (255 - m)):
            lm.append(1)
    elif (0 <= m <= 127):
        if (abs(vtemp) <= 2 * m + 1):
            lm.append(1)
    else:
        unchangeable()

def unchangeable():
    lm.append(2)


j = 0
for isiquad in pair:
    i = 0
    if(j < panjangteks):
        while i < 1:
            v = float(isiquad[i+1]) - float(isiquad[i])
            m = v / 2
            b = float(teks[j])
            # v.append(vtemp)
            expandable(v, m, b)
            i += 1
            x += 1
            print(x, y)
    else:
        break

print(v)