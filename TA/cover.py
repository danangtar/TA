import wave
import numpy as np
from .pesan import Pesan

class Cover:

    head = np.array()
    tail = np.array()

    def __init__(self):
        self.fileName = "cover.wav"

    def __init__(self, fileName):
        self.fileName = fileName

    def buka(self):
        spf = wave.open(self.fileName, 'r')

        signal = spf.readframes(-1)
        signal = np.fromstring(signal, 'uint8')

        size = signal.size
        mod = divmod(size, 4)
        headlen = size - mod[1]

        self.head = signal[:headlen]
        tail = signal[headlen:]

        pair = self.head.reshape((-1, 2))
        y = pair.size
        pair = pair.tolist()
        x = 0
        lm = []

        teks = Pesan()
        teks = teks.getBinary()
        panjangteks = len(teks)
