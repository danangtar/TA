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

pair = head.reshape((-1, 4))
y = pair.size
pair = pair.tolist()
x = 0
lm = []

teks = TA.pesan.Pesan()
teks = teks.getBinary()
panjangteks = len(teks)
print(teks)
print(pair)

def expandable(v, m, b, rde, location_map):
    vtemp = 2 * v + b
    if 128 <= m <= 255:
        if abs(vtemp) <= 2 * (255 - m):
            if rde:
                if location_map:
                    lm.append(0)
                else:
                    lm.append(1)
            else:
                lm.append(2)
            return vtemp
        else:
            return changeable(v, m, b)
    elif 0 <= m <= 127:
        if abs(vtemp) <= 2 * m + 1:
            if rde:
                if location_map:
                    lm.append(0)
                else:
                    lm.append(1)
            else:
                lm.append(2)
            return vtemp
        else:
            return changeable(v, m, b)


def changeable(v, m, b):
    vtemp = 2 * np.floor(v / 2) + b
    if 128 <= m <= 255:
        if abs(vtemp) <= 2 * (255 - m):
            lm.append(3)
            return vtemp
        else:
            return unchangeable()
    elif 0 <= m <= 127:
        if abs(vtemp) <= 2 * m + 1:
            lm.append(3)
            return vtemp
        else:
            return unchangeable()


def unchangeable():
    lm.append(4)
    return "aduh"

lx = []
j = 0
uaksen = []

for isiquad in pair:
    rde = False
    location_map = False
    i = 0
    if j < panjangteks:
        while i < 3:
            v = int(isiquad[i + 1]) - int(isiquad[0])
            if -2 < v < 2:
                vr = v
                rde = False
            elif v <= -2:
                vr = v + 2 ** (np.floor(np.log2(np.absolute(v))) - 1)
                rde = True
            elif v >= 2:
                vr = v - 2 ** (np.floor(np.log2(np.absolute(v))) - 1)
                rde = True

            if rde:
                if 2 ** (np.floor(np.log2(np.absolute(vr)))) == 2 ** (np.floor(np.log2(np.absolute(v)))):
                    location_map = True

            m = np.floor((int(isiquad[i]) + int(isiquad[i + 1])) / 2)
            b = int(teks[j])
            # v.append(vtemp)
            vtemp = expandable(vr, m, b, rde, location_map)
            if vtemp != 0:
                lx.append([b, teks[j], j, vtemp, x])
            # print(v, m, b, vtemp, j)
            if vtemp != "aduh":
                if i == 0:
                    uaksen[i] = int(isiquad[0])
                else:
                    uaksen[i] = vtemp + int(isiquad[0])

                # pair[x] = [uaksen1, uaksen2]
                # if b == 1:
                #     lx.append([pair[x], x])
                j += 1
            i += 1
            x += 1
            # print(x, y)
        pair[x] = [uaksen[0], uaksen]
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
write('testrde.wav', 44100, tulis)

# with open('lm', 'wb') as lmfile:
#     pickle.dump(lm, lmfile)
#
# lmfile = open('lmun.txt', 'w')
# for item in lm:
#   lmfile.write("%s\n" % item)
#
# lmfile.close()

LMFile = open("lmrde", "wb")
LMFileByteArray = bytes(lm)
# print(LMFileByteArray)
# print(list(LMFileByteArray))
LMFile.write(LMFileByteArray)
LMFile.close()

# print(len(lm), panjangteks, lm.count(0), lm.count(1), lm.count(2), lx[:6])
print(head.reshape((-1, 2)))
# # print(head)
# print(lm.count(2))