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

# pair = head.reshape((-1, 4))
# y = pair.size
# pair = pair.tolist()

teks = TA.pesan.Pesan()
teks = teks.getBinary()
panjangteks = len(teks)
print(panjangteks)
# print(pair)


def expandable(v, b, u0, rde, location_map):
    vtemp = 2 * v + b
    if 0 <= vtemp + u0 <= 255:
        if rde:
            if location_map:
                lm.append(0)
            else:
                lm.append(1)
        else:
            lm.append(2)
        return vtemp
    else:
        return changeable(v, b, u0)


def changeable(v, b, u0):
    vtemp = 2 * np.floor(v / 2) + b
    if 0 <= vtemp + u0 <= 255:
        lm.append(3)
        return vtemp
    else:
        return unchangeable()


def unchangeable():
    lm.append(4)
    return "aduh"

# x = hitung sample
x = 0

# j = hitung bit pesan
j = 0

lm = []
# lx = []

avg = head[0]
i = 0
k = 0
while j < panjangteks:
    rde = False
    location_map = False

    if k == 4:
        avg = head[i]
        k = 0

    v = int(head[i + 1]) - avg

    if -2 < v < 2:
        vr = v
        rde = False
    elif v <= -2:
        vr = v + 2 ** (np.floor(np.log2(np.absolute(v))) - 1)
        rde = True
    elif v >= 2:
        vr = v - 2 ** (np.floor(np.log2(np.absolute(v))) - 1)
        rde = True

    if rde and 2 ** (np.floor(np.log2(np.absolute(vr)))) == 2 ** (np.floor(np.log2(np.absolute(v)))):
        location_map = True

    if j < panjangteks:
        b = int(teks[j])
    else:
        b = 0

    vtemp = expandable(vr, b, avg, rde, location_map)

    head[i+1] = vtemp + avg

    i += 1
    j += 1
    k += 1


# for isiquad in pair:
#     rde = False
#     location_map = False
#     i = 0
#     uaksen = [int(isiquad[0])]
#     if j < panjangteks:
#         while i < 3:
#             rde = False
#             location_map = False
#             v = int(isiquad[i + 1]) - int(isiquad[0])
#
#             if -2 < v < 2:
#                 vr = v
#                 rde = False
#             elif v <= -2:
#                 vr = v + 2 ** (np.floor(np.log2(np.absolute(v))) - 1)
#                 rde = True
#             elif v >= 2:
#                 vr = v - 2 ** (np.floor(np.log2(np.absolute(v))) - 1)
#                 rde = True
#
#             if rde and 2 ** (np.floor(np.log2(np.absolute(vr)))) == 2 ** (np.floor(np.log2(np.absolute(v)))):
#                 location_map = True
#
#             if j < panjangteks:
#                 b = int(teks[j])
#             else:
#                 b = 0
#
#             vtemp = expandable(vr, b, int(isiquad[0]), rde, location_map)
#
#             if vtemp != "aduh":
#                 uaksen.append(vtemp + int(isiquad[0]))
#                 j += 1
#             else:
#                 uaksen.append(0)
#                 j += 1
#
#             i += 1
#
#         # print(j, panjangteks)
#         if 4 in lm[-3:]:
#             j -= i
#             while i > 0:
#                 lm[-i] = 4
#                 i -= 1
#         else:
#             pair[x] = [uaksen[0], uaksen[1], uaksen[2], uaksen[3]]
#
#         x += 1
#
#     else:
#         break


pair = np.asarray(head, dtype=np.uint8)
# print(pair)

tulis = pair.reshape(1, -1)
# print(tulis.size, head.size)
# if tulis.size == head.size:
#     print("ok")
tulis = np.append(tulis, tail)
tulis.astype(np.uint8)
# print(tulis.size, size)
# print(tulis)
#
write('testoverlap.wav', 44100, tulis)

# with open('lmpickle', 'wb') as lmfile:
#     pickle.dump(lm, lmfile)
#
# lmfile = open('lmungrde.txt', 'w')
# str1 = ''.join(str(e) for e in lm)
# # str1 = bz2.compress(str1.encode("utf-8"))
# for item in str1:
#     lmfile.write("%s" % item)
#
# lmfile.close()

LMFile = open("lmgoverlap", "wb")
LMFileByteArray = bytes(lm)
# print(LMFileByteArray)
# print(list(LMFileByteArray))
LMFile.write(LMFileByteArray)
LMFile.close()

# print(len(lm), panjangteks, lm.count(0), lm.count(1), lm.count(2), lx[:6])
# print(head.reshape((-1, 2)))
# # print(head)
# print(lm.count(2))
