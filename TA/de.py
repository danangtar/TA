import numpy as np

class DE:
    def __init__(self):
        self.lm = []

    def expandable(self, v, m, b):
        vtemp = 2 * v + b
        if 128 <= m <= 255:
            if abs(vtemp) <= 2 * (255 - m):
                self.lm.append(0)
                return vtemp
            else:
                return self.changeable(v, m, b)
        elif 0 <= m <= 127:
            if abs(vtemp) <= 2 * m + 1:
                self.lm.append(0)
                return vtemp
            else:
                return self.changeable(v, m, b)

    def changeable(self, v, m, b):
        vtemp = 2 * np.floor(v / 2) + b
        if 128 <= m <= 255:
            if abs(vtemp) <= 2 * (255 - m):
                self.lm.append(1)
                return vtemp
        elif 0 <= m <= 127:
            if abs(vtemp) <= 2 * m + 1:
                self.lm.append(1)
                return vtemp
        else:
            return self.unchangeable()

    def unchangeable(self):
        self.lm.append(2)
        return "aduh"

    def getlm(self):
        return self.lm

    def writelm(self):
        LMFile = open("lmde", "wb")
        LMFileByteArray = bytes(self.lm)
        LMFile.write(LMFileByteArray)
        LMFile.close()

    # def expands(self, pair, panjangteks):
    #     j = 0
    #     for isiquad in pair:
    #         i = 0
    #         if j < panjangteks:
    #             while i < 1:
    #                 v = int(isiquad[i]) - int(isiquad[i + 1])
    #                 m = np.floor((int(isiquad[i]) + int(isiquad[i + 1])) / 2)
    #                 b = int(teks[j])
    #
    #                 vtemp = self.expandable(v, m, b)
    #
    #                 if vtemp != "aduh":
    #                     uaksen1 = m + np.floor((vtemp + 1) / 2)
    #                     uaksen2 = m - np.floor(vtemp / 2)
    #
    #                     pair[x] = [uaksen1, uaksen2]
    #                     # if b == 1:
    #                     #     lx.append([pair[x], x])
    #                     j += 1
    #                 i += 1
    #                 x += 1
    #                 # print(x, y)
    #         else:
    #             break
    #
    # def expand(self, isiquad, teks):
    #     v = int(isiquad[i]) - int(isiquad[i + 1])
    #     m = np.floor((int(isiquad[i]) + int(isiquad[i + 1])) / 2)
    #     b = int(teks[j])
    #
    #     vtemp = self.expandable(v, m, b)
    #
    #     return vtemp
    #
    # def embed(self, m, vtemp):
    #     uaksen1 = m + np.floor((vtemp + 1) / 2)
    #     uaksen2 = m - np.floor(vtemp / 2)
    #
    #     return [uaksen1, uaksen2]