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

teks = TA.pesan.Pesan()
teks = teks.getBinary()
panjangteks = len(teks)
print(teks)
print(pair)


def expandable(v, b):
    vtemp = 2 * v + b
    return vtemp


def changeable(v, b):
    vtemp = 2 * np.floor(v / 2) + b
    return vtemp


def is_expandable(v0, vtemp):
    vtemps = np.floor((vtemp[0]+vtemp[2]+vtemp[4])/4)
    ex = [6, 0, 2, 4]
    is_ex = []
    i = 0
    while i < 3:
        if i == 0:
            if 0 <= v0 - vtemps <= 255:
                is_ex.append(True)
                i += 1
            else:
                is_ex.append(False)
                i += 1
        else:
            if 0 <= vtemp[ex[i]] + v0 - vtemps <= 255:
                is_ex.append(True)
                i += 1
            else:
                is_ex.append(False)
                i += 1

    if is_ex.count(False) == 0:
        return [0, vtemps, ex]
    else:
        return if_changeable(v0, vtemp)

def if_changeable(v0, vtemp):
    vtemps = np.floor((vtemp[0] + vtemp[2] + vtemp[4]) / 4)
    ex = [6, 1, 3, 5]
    is_ch = []
    i = 0
    while i < 3:
        if i == 0:
            if 0 <= v0 - vtemps <= 255:
                is_ch.append(True)
                i += 1
            else:
                is_ch.append(False)
                i += 1
        else:
            if 0 <= vtemp[ex[i]] + v0 - vtemps <= 255:
                is_ch.append(True)
            else:
                is_ch.append(False)
                i += 1

    if is_ch.count(False) == 0:
        return [1, vtemps, ex]
    else:
        return 2

def unchangeable():


# x = hitung sample
x = 0

# j = hitung bit pesan
j = 0

lm = []
# lx = []

for isiquad in pair:
    rde = []
    location_map = []
    i = 0
    vs = [np.floor((int(isiquad[0]) + int(isiquad[1]) + int(isiquad[2]) + int(isiquad[3])) / 4)]
    vtemp = []
    uaksen = []
    w_vs = -1
    if j < panjangteks:
        while i < 3:
            v = int(isiquad[i + 1]) - int(isiquad[0])

            if -2 < v < 2:
                vr = v
                rde.append(False)
            elif v <= -2:
                vr = v + 2 ** (np.floor(np.log2(np.absolute(v))) - 1)
                rde.append(True)
            elif v >= 2:
                vr = v - 2 ** (np.floor(np.log2(np.absolute(v))) - 1)
                rde.append(True)

            if rde[i]:
                if 2 ** (np.floor(np.log2(np.absolute(vr)))) == 2 ** (np.floor(np.log2(np.absolute(v)))):
                    location_map.append(0)
                else:
                    location_map.append(1)
            else:
                location_map.append(2)

            if j < panjangteks:
                b = int(teks[j])
            else:
                b = 0

            vs.append(vr)
            vtemp.append(expandable(vr, b))
            vtemp.append(changeable(vr, b))

            i += 1
            j += 1

        # if is_expandable(vs[0], vtemp):
        #     lm.append(0)

        vtemps = is_expandable(vs[0], vtemp)

        # w_vs = np.floor((vs[0] + vs[1] + vs[2] + vs[3]) / 4)

        k = 0
        while k < 3:
            if k == 0:
                if vtemps != "aduh":
                    uaksen[0] = vs[0] - vtemps[1]
                    k += 1
                else:
                    break
            else:
                uaksen[k] = vtemp[vtemps[2][k]] + uaksen[0]
                k += 1

        # print(j, panjangteks)
        if 4 in lm[-3:]:
            j -= i
            while i > 0:
                lm[-i] = 4
                i -= 1
        else:
            pair[x] = [uaksen[0], uaksen[1], uaksen[2], uaksen[3]]
            x += 1
    else:
        break


pair = np.asarray(pair, dtype=np.uint8)
print(pair)

tulis = pair.reshape(1, -1)
# print(tulis.size, head.size)
# if tulis.size == head.size:
#     print("ok")
tulis = np.append(tulis, tail)
tulis.astype(np.uint8)
print(tulis.size, size)
print(tulis)
#
write('testgrde.wav', 44100, tulis)

# with open('lmpickle', 'wb') as lmfile:
#     pickle.dump(lm, lmfile)
#
lmfile = open('lmungrde.txt', 'w')
str1 = ''.join(str(e) for e in lm)
# str1 = bz2.compress(str1.encode("utf-8"))
for item in str1:
    lmfile.write("%s" % item)

lmfile.close()

LMFile = open("lmgrde", "wb")
LMFileByteArray = bytes(lm)
# print(LMFileByteArray)
# print(list(LMFileByteArray))
LMFile.write(LMFileByteArray)
LMFile.close()

# print(len(lm), panjangteks, lm.count(0), lm.count(1), lm.count(2), lx[:6])
print(head.reshape((-1, 2)))
# # print(head)
# print(lm.count(2))
