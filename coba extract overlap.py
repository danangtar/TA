import numpy as np
from scipy.io.wavfile import write
import wave
import binascii
import bitarray
import TA.pesan

ba = bitarray.bitarray()

spf = wave.open('testoverlap.wav', 'r')

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
# print(signal[10467])
# pair = head.reshape((-1, 4))


with open("lmgoverlap", mode='rb') as file:  # b is important -> binary
    fileContent = file.read()

fileContent = list(fileContent)

message = []

# x = hitung sample
x = 0

# j = hitung bit pesan
j = 0

lx = []

avg = head[0]
i = 0
k = 0
while j < len(fileContent):
    if k == 4:
        avg = head[i]
        k = 0
    v = int(head[i + 1]) - avg
    b = v & 1

    vr = np.floor(v / 2)

    if fileContent[j] == 0:
        if vr > 0:
            v = vr + 2 ** (np.floor(np.log2(np.absolute(vr))) - 1)
            lx.append(0)
        elif vr < 0:
            v = vr - 2 ** (np.floor(np.log2(np.absolute(vr))) - 1)
            lx.append(1)

    elif fileContent[j] == 1:
        if vr > 0:
            v = vr + 2 ** np.floor(np.log2(np.absolute(vr)))
            lx.append(2)
        elif vr < 0:
            v = vr - 2 ** np.floor(np.log2(np.absolute(vr)))
            lx.append(3)

    elif fileContent[j] == 2:
        v = vr
        lx.append(4)
    else:
        if 0 <= v <= 1:
            v = 1
            lx.append(5)
        elif -2 <= v <= -1:
            v = -2
            lx.append(6)
        else:
            v = 2 * np.floor(v / 2) + b
            lx.append(7)

    head[i + 1] = v + avg

    # if fileContent[j] != 4:
    message.append(b)

    i += 1
    j += 1
    k += 1

# for isiquad in pair:
#     i = 0
#     uaksen = [int(isiquad[0])]
#     if j < len(fileContent):
#         while i < 3:
#             v = int(isiquad[i + 1]) - int(isiquad[0])
#             b = v & 1
#
#             vr = np.floor(v / 2)
#
#             if fileContent[j] == 0:
#                 if vr > 0:
#                     v = vr + 2 ** (np.floor(np.log2(np.absolute(vr))) - 1)
#                     lx.append(0)
#                 elif vr < 0:
#                     v = vr - 2 ** (np.floor(np.log2(np.absolute(vr))) - 1)
#                     lx.append(1)
#
#             elif fileContent[j] == 1:
#                 if vr > 0:
#                     v = vr + 2 ** np.floor(np.log2(np.absolute(vr)))
#                     lx.append(2)
#                 elif vr < 0:
#                     v = vr - 2 ** np.floor(np.log2(np.absolute(vr)))
#                     lx.append(3)
#
#             elif fileContent[j] == 2:
#                 v = vr
#                 lx.append(4)
#             else:
#                 if 0 <= v <= 1:
#                     v = 1
#                     lx.append(5)
#                 elif -2 <= v <= -1:
#                     v = -2
#                     lx.append(6)
#                 else:
#                     v = 2 * np.floor(v / 2) + b
#                     lx.append(7)
#
#             uaksen.append(v + int(isiquad[0]))
#
#             # if fileContent[j] != 4:
#             message.append(b)
#             j += 1
#             i += 1
#
#         pair[x] = [uaksen[0], uaksen[1], uaksen[2], uaksen[3]]
#         x += 1
#
#     else:
#         break

pair = np.asarray(head, dtype=np.uint8)

tulis = pair.reshape(1, -1)

# print(tulis.size, head.size)
# if tulis.size == head.size:
#     print("ok")
tulis = np.append(tulis, tail)
tulis.astype(np.uint8)
print(tulis[10467])
write('returnoverlap.wav', 44100, tulis)

# print(message)

message = np.array(message, dtype=bool)
message = message.tolist()
lenmes = len(message)
print(lenmes)

# teks = TA.pesan.Pesan()
# teks = teks.getBinary()

# print((teks > message)-(teks < message))

# lmfile = open('compare.txt', 'w')
# # str1 = bz2.compress(str1.encode("utf-8"))
# for item in message:
#     lmfile.write("%s," % item)
#
# lmfile.write("aduh")
#
# for item in teks:
#     lmfile.write("%s," % item)
#
# lmfile.close()

# print(lenmes % 8)

n = int(bitarray.bitarray(message).tostring(), 2)

write = binascii.unhexlify('%x' % n)

print(write)

f = open('hasyiloverlap.txt', 'wb')
f.write(write)
f.close()

print(lx.count(0), lx.count(1), lx.count(2), lx.count(3), lx.count(4), lx.count(5), lx.count(6), lx.count(7))
