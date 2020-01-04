'''
this python script is written to generate FM modulated random digital waveform
fc = carrier wave frequency
fm = message signal frequency
FM modulated signal = cos(2*pi*fc*n + 2*pi*kf*sin(2*pi*fm*n))
'''

import matplotlib.pyplot as plt
import numpy as np
import math
from random import random


time = int(input("Enter the time span for which the wave is to be shown : "))
kf = float(input("Enter the modulation index for the FM modulation : "))
tm = int(input("Enter the time period of the message signal : "))
tc = int(input("Enter the time period of the carrier signal : "))
fm = 1/tm
fc = 1/tc
n = [i for i in range(1,time)]
carrier = [np.cos(2*math.pi*fc*i) for i in n]
msg = [np.cos(2*math.pi*fm*i) for i in n]
fm_modulated = [np.cos(2*math.pi*(fc*i + kf*np.sin(2*math.pi*fm*i))) for i in n]

s = "FM Modulation with kf ="+str(kf)
plt.suptitle(s)
plt.subplot(311)
plt.plot(carrier),plt.title(("Carrier Signal"))
plt.xlabel("Time(s) ---->"),plt.ylabel("Amplitude ---->")
plt.subplot(312)
plt.plot(msg),plt.title(("Message Signal"))
plt.xlabel("Time(s) ---->"),plt.ylabel("Amplitude ---->")
plt.subplot(313)
plt.plot(fm_modulated),plt.title("FM Modulated Signal")
plt.xlabel("Time(s) ---->"),plt.ylabel("Amplitude ---->")
plt.tight_layout()
plt.show()