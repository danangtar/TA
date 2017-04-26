import hashlib
import numpy as np
import wave

before = hashlib.md5()
with open('testttt.wav', 'rb') as afile:
    buf = afile.read()
    before.update(buf)

after = hashlib.md5()
with open('returnrde.wav', 'rb') as afile:
    buf = afile.read()
    after.update(buf)

before = before.hexdigest()
after = after.hexdigest()
print(before)
print(after)

if before == after:
    print('sama')

# spf = wave.open('returngrde.wav', 'r')
#
# # Extract Raw Audio from Wav File
# after = spf.readframes(-1)
# after = np.fromstring(after, 'uint8')
#
# spf = wave.open('testgrde.wav', 'r')
#
# # Extract Raw Audio from Wav File
# test = spf.readframes(-1)
# test = np.fromstring(test, 'uint8')
#
# spf = wave.open('testttt.wav','r')
#
# #Extract Raw Audio from Wav File
# before = spf.readframes(-1)
# before = np.fromstring(before, 'uint8')
#
# diffff = after - before
#
# diffff = diffff.tolist()
#
# x = 0
# while x < len(diffff):
#     if diffff[x] != 0:
#         i = divmod(x, 4)
#         j = i[1]
#         k = x - j + 4
#         print(x, i[0], before[x], before[x-j], test[x], test[x-j], after[x], after[x-j])
#     x += 1
#
# # print(diffff)
#
# print(len(before), len(after))