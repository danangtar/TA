import hashlib
import numpy as np
import wave

before = hashlib.md5()
with open('testttt.wav', 'rb') as afile:
    buf = afile.read()
    before.update(buf)

after = hashlib.md5()
with open('returngrde.wav', 'rb') as afile:
    buf = afile.read()
    after.update(buf)

before = before.hexdigest()
after = after.hexdigest()
print(before)
print(after)

if before == after:
    print('sama')

spf = wave.open('returngrde.wav', 'r')

# Extract Raw Audio from Wav File
after = spf.readframes(-1)
after = np.fromstring(after, 'int8')

spf = wave.open('testttt.wav','r')

#Extract Raw Audio from Wav File
before = spf.readframes(-1)
before = np.fromstring(before, 'int8')

diffff = after - before

diffff = diffff.tolist()

x = 0
while x < len(diffff):
    if diffff[x] != 0:
        i = divmod(x, 4)
        j = i[1]
        k = x - j + 4
        print(x, before[x], after[x], before[x-j]-before[x], after[x-j]-after[x])
    x += 1

# print(diffff)

print(len(before), len(after))