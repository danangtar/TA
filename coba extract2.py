import numpy as np
from scipy.io.wavfile import write
import wave
import binascii
import bitarray

ba = bitarray.bitarray()

spf = wave.open('testde.wav', 'r')

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

with open("lmde", mode='rb') as file: # b is important -> binary
    fileContent = file.read()

fileContent = list(fileContent)

message = []

lx = []
j = 0
for isiquad in pair:
    i = 0
    if j < len(fileContent):
        while i < 1:
            v = int(isiquad[i]) - int(isiquad[i + 1])
            m = np.floor((int(isiquad[i]) + int(isiquad[i + 1])) / 2)
            b = v & 1
            if fileContent[j] == 0:
                v = np.floor(v / 2)
                lx.append(0)
            else:
                if 0 <= v <= 1:
                    v = 1
                    lx.append(1)
                elif -2 <= v <= -1:
                    v = -2
                    lx.append(2)
                else:
                    v = 2 * np.floor(v / 2) + b
                    lx.append(3)

            # print(pair[j], m, v, "before")
            pair[j] = [m + np.floor((v + 1) / 2), m - np.floor(v / 2)]
            # print(pair[j], "after")
            message.append(b)

            j += 1
            i += 1

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
write('returnde.wav', 44100, tulis)

# print(message)

message = np.array(message, dtype=bool)
message = message.tolist()

n = int(bitarray.bitarray(message).tostring(),2)

write = binascii.unhexlify('%x' % n)

# print(write)

f = open('hasyilde.txt', 'wb')
f.write(write)
f.close()

print(lx.count(0), lx.count(1), lx.count(2), lx.count(3))