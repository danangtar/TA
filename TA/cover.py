import wave
import numpy as np
from scipy.io.wavfile import write

class Cover:

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

        head = signal[:headlen]
        self.tail = signal[headlen:]

        self.head = head.reshape((-1, 2))

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    def setHead(self, head):
        self.head = head

    def writeStego(self):
        pair = np.asarray(self.head, dtype=np.uint8)

        tulis = pair.reshape(1, -1)

        tulis = np.append(tulis, self.tail)
        tulis.astype(np.uint8)

        write('testde.wav', 44100, tulis)