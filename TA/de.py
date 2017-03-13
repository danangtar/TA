import math

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
        vtemp = 2 * math.floor(v / 2) + b
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
        return 0

    def getlm(self):
        return self.lm