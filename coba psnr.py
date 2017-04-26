import matplotlib.pyplot as plt
import numpy as np
import wave

spf = wave.open('testttt.wav', 'r')
# Extract Raw Audio from Wav File
read = spf.readframes(-1)
A = np.fromstring(read, 'uint8')

spf = wave.open('testgrde.wav', 'r')
# Extract Raw Audio from Wav File
read = spf.readframes(-1)
B = np.fromstring(read, 'uint8')


mse = ((A - B) ** 2).mean(axis=None)

print(mse)

psnr = 20 * np.log10(255 / np.sqrt(mse))

print(psnr)