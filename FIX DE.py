import numpy as np
from TA import cover, pesan, de

cvr = cover.Cover("testttt.wav")

pair = cvr.getHead()
tail = cvr.getTail()

psn = pesan.Pesan()
teks = psn.getBinary()
panjangteks = teks.panjang()

expand = de.DE()

x = 0
j = 0

for isiquad in pair:
    i = 0
    if j < panjangteks:
        while i < 1:
            v = int(isiquad[i]) - int(isiquad[i + 1])
            m = np.floor((int(isiquad[i]) + int(isiquad[i + 1])) / 2)
            b = int(teks[j])
            vtemp = expand.expandable(v, m, b)
            if vtemp != "aduh":
                uaksen1 = m + np.floor((vtemp + 1) / 2)
                uaksen2 = m - np.floor(vtemp / 2)

                pair[x] = [uaksen1, uaksen2]
                j += 1
            i += 1
            x += 1
    else:
        break

cvr.setHead(pair)

cvr.writeStego()

expand.writelm()