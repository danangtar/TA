import numpy as np
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

if -3 < -2:
    print("yes")

v=1
while v<30:
    vr = v - 2 ** (np.floor(np.log2(np.absolute(v))) - 1)
    if 2 ** (np.floor(np.log2(np.absolute(vr)))) == 2 ** (np.floor(np.log2(np.absolute(v)))):
        print(v, vr + 2 ** (np.floor(np.log2(np.absolute(vr))) - 1), " ", 2 ** (np.floor(np.log2(np.absolute(vr)))), 2 ** (np.floor(np.log2(np.absolute(v)))))
    else:
        print(v, vr + 2**np.floor(np.log2(np.absolute(vr))), " ", 2 ** (np.floor(np.log2(np.absolute(vr)))), 2 ** (np.floor(np.log2(np.absolute(v)))))
    v += 1