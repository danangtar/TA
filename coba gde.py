import numpy as np
from scipy.io.wavfile import write
import wave
import TA.pesan
import pickle

spf = wave.open('testttt.wav', 'r')

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

teks = TA.pesan.Pesan()
teks = teks.getBinary()
panjangteks = len(teks)
print(teks)
print(pair)

def expandable(v, m, b):
    vtemp = 2 * v + b
    if 128 <= m <= 255:
        if abs(vtemp) <= 2 * (255 - m):
            lm.append(0)
            print(vtemp)
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
    vtemp = 2 * np.floor(v / 2) + b
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
    return "aduh"

lx = []
j = 0
for isiquad in pair:
    i = 0
    if j < panjangteks:
        while i < 1:
            v = int(isiquad[i]) - int(isiquad[i + 1])
            m = np.floor((int(isiquad[i]) + int(isiquad[i + 1])) / 2)
            b = int(teks[j])
            # v.append(vtemp)
            vtemp = expandable(v, m, b)
            if vtemp != 0:
                lx.append([b, teks[j], j, vtemp, x])
            # print(v, m, b, vtemp, j)
            if vtemp != "aduh":
                uaksen1 = m + np.floor((vtemp + 1) / 2)
                uaksen2 = m - np.floor(vtemp / 2)

                pair[x] = [uaksen1, uaksen2]
                # if b == 1:
                #     lx.append([pair[x], x])
                j += 1
            i += 1
            x += 1
            # print(x, y)
    else:
        break

pair = np.asarray(pair, dtype=np.uint8)

tulis = pair.reshape(1, -1)
# print(tulis.size, head.size)
# if tulis.size == head.size:
#     print("ok")
tulis = np.append(tulis, tail)
tulis.astype(np.uint8)
print(tulis.size, size)
print(tulis)
#
write('test4.wav', 44100, tulis)

# with open('lm', 'wb') as lmfile:
#     pickle.dump(lm, lmfile)
#
# lmfile = open('lmun.txt', 'w')
# for item in lm:
#   lmfile.write("%s\n" % item)
#
# lmfile.close()

LMFile = open("lm4", "wb")
LMFileByteArray = bytes(lm)
# print(LMFileByteArray)
# print(list(LMFileByteArray))
LMFile.write(LMFileByteArray)
LMFile.close()

# print(len(lm), panjangteks, lm.count(0), lm.count(1), lm.count(2), lx[:6])
print(head.reshape((-1, 2)))
# # print(head)
# print(lm.count(2))