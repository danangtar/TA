import numpy as np
import wave
import math

spf = wave.open('test.wav', 'r')

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'uint8')

size = signal.size

mod = divmod(size, 4)
headlen = size - mod[1]
# print(size)
# print(mod)

head = signal[:headlen]
tail = signal[headlen:]

pair = head.reshape((-1, 2))
y = pair.size
pair = pair.tolist()
x = 0
lm = []

def expandable(v, m, b):
    vtemp = 2 * v + b
    if 128 <= m <= 255:
        if abs(vtemp) <= 2 * (255 - m):
            lm.append(0)
            return vtemp
        else:
            return changeable(v, m, b)
    elif 0 <= m <= 127:
        if abs(vtemp) <= 2 * m + 1:
            lm.append(0)
            return vtemp
        else:
            return changeable(v, m, b)


def changeable(v, m, b):
    vtemp = 2 * math.floor(v / 2) + b
    if 128 <= m <= 255:
        if abs(vtemp) <= 2 * (255 - m):
            lm.append(1)
            return vtemp
    elif 0 <= m <= 127:
        if abs(vtemp) <= 2 * m + 1:
            lm.append(1)
            return vtemp
    else:
        return unchangeable()


def unchangeable():
    lm.append(2)
    return 0

j = 0
for isiquad in pair:
    i = 0
    while i < 1:
        v = float(isiquad[i + 1]) - float(isiquad[i])
        m = math.floor((float(isiquad[i + 1]) + float(isiquad[i])) / 2)
        b = float(teks[j])
        # v.append(vtemp)
        vtemp = expandable(v, m, b)
        # print(v, m, b, vtemp, j)
        if vtemp != 0:
            uaksen1 = m + math.floor((vtemp + 1) / 2)
            uaksen2 = m - math.floor(vtemp / 2)

            pair[x] = [uaksen1, uaksen2]
            j += 1
        i += 1
        x += 1