import numpy as np
import zlib

# v = -47
# # vr = -1
# vr = v - 2 ** (np.floor(np.log2(np.absolute(v))) - 1)
# vr = v + 2 ** (np.floor(np.log2(np.absolute(v))) - 1)
# # powers = np.floor(np.log2(v))-1
# # print(powers)
# # print(2**-1)
# # print(2**(np.floor(np.log2(vr))-1))
# # # print(np.absolute(-3))
# # print(vr)
# print(vr + 2**(np.floor(np.log2(np.absolute(vr)))-1))
# print(vr + 2**np.floor(np.log2(np.absolute(vr))))
#
# print(vr - 2**(np.floor(np.log2(np.absolute(vr)))-1))
# print(vr - 2**np.floor(np.log2(np.absolute(vr))))

# if -3 < -2:
#     print("yes")
#
# v=1
# while v<30:
#     vr = v - 2 ** (np.floor(np.log2(np.absolute(v))) - 1)
#     if 2 ** (np.floor(np.log2(np.absolute(vr)))) == 2 ** (np.floor(np.log2(np.absolute(v)))):
#         print(v, vr + 2 ** (np.floor(np.log2(np.absolute(vr))) - 1), " ", 2 ** (np.floor(np.log2(np.absolute(vr)))), 2 ** (np.floor(np.log2(np.absolute(v)))))
#     else:
#         print(v, vr + 2**np.floor(np.log2(np.absolute(vr))), " ", 2 ** (np.floor(np.log2(np.absolute(vr)))), 2 ** (np.floor(np.log2(np.absolute(v)))))
#     v += 1

# i = 0
# while i < 3:
#     print(i+1, i)
#     i += 1
#
# i = 1
# while i > 0:
#     print(i)
#     i -= 1
# print(i)

# a = []
# b = [3, 4]
#
# a.append([1, 2])
# a.append(b)
#
# a[-1] = [5, 6]
#
# a[-1] = [0, 0]
#
# a.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
#
# i = 3
# if 0 in a[2][-3:]:
#     while i > 0:
#         a[2][-i] = 11
#         i -= 1
#
# print(a[2][-4:])
# pair = np.asarray(a, dtype=np.uint8)
# print(pair)
# pair = pair.reshape(1, -1)
# print(pair)

# a = '1111111111111111111111111111111111111111111'
# # a = zlib.compress(a.encode("utf-8"))
# print(a.encode("utf-8"))

a = [True, True, False, [1, 2, 3]]

print(a.count(False))
print(a[3][2])