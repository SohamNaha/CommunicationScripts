from scipy.fftpack import fft,fftshift
import matplotlib.pyplot as plt
import numpy as np
import math

freq1 = 692
freq2 = 1200
fs = 1000
t = np.linspace(0,1,fs)
wave = [(np.sin(2*math.pi*freq1*i)+np.sin(2*math.pi*freq2*i)) for i in t]
plt.plot(wave)
plt.show()

N = 2048
mag1 = abs(fftshift(fft(wave,N)))
time_axis = [i*(fs/N) for i in range(-1024,1024)]
plt.plot(time_axis,mag1)
plt.show()
