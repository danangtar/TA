import numpy as np
import wave
import binascii
import bitarray

ba = bitarray.bitarray()

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

with open("lm", mode='rb') as file: # b is important -> binary
    fileContent = file.read()

fileContent = list(fileContent)

message = []

j = 0
for isiquad in pair:
    i = 0
    if j < len(fileContent):
        while i < 1:
            v = int(isiquad[i + 1]) - int(isiquad[i])

            message.append(v & 1)

            j += 1
            i += 1

    else:
        break

print(message)

message = np.array(message, dtype=bool)
message = message.tolist()

n = int(bitarray.bitarray(message).tostring(),2)

write = binascii.unhexlify('%x' % n)

print(write)

f = open('hasyil.txt', 'wb')
f.write(write)
f.close()