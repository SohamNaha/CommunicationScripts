'''
This program is used to generate ASK modulation output for a certain frequency. In case of ASK, the output of the modulator produces a sine wave when the amplitude of the
input signal is +ve and produces "0" when the input is -ve.
'''

import matplotlib.pyplot as plt
from random import random
import numpy as np
import math

chip_length = int(input("Enter the duration of each input bit: "))
total_length = int(input("Enter the total duratio of input bits ;"))
num_symbols = math.ceil(total_length/chip_length)
symbols = [random()-0.5 for _ in range(num_symbols)]

inp = [1 if i>=0 else 0 for i in symbols]
input_bitstream = []

for i in inp:
    for _ in range(chip_length):
        input_bitstream.append(i)
        
f = 1/(0.5*chip_length)
t = [i for i in range(total_length)]
c = [np.sin(2*math.pi*f*i) for i in t]

out = [i*j for i,j in zip(c,input_bitstream)]

plt.suptitle("ASK MODULATION")    
plt.subplot(211)
plt.plot(input_bitstream)
plt.ylabel("Amplitude"),plt.xlabel("Time --->")
plt.title("Input Bitstream"),plt.grid()
plt.subplot(212)
plt.plot(out)
plt.ylabel("Amplitude"),plt.xlabel("Time --->")
plt.title("Modulated Output"),plt.grid()
plt.tight_layout()
plt.show()
