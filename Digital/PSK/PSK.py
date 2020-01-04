'''
This script is used to generate PSK modulated waveform from random generated digital signal.
In case of PSK the output waveform has 180 degree phase shift when input bit is -ve 
and 0 degree phase shift when the input bit is +ve. 
'''


import math
import matplotlib.pyplot as plt
import numpy as np
from random import random

#random signal generation
bit_length = int(input("Enter the bit duration : "))
total_length = int(input("Enter the total duration : "))
n_sym = math.ceil(total_length/bit_length)
input_bits = [random()-0.5 for i in range(n_sym)]
syms = [1 if i>=0 else -1 for i in input_bits]
input_stream = []
for i in syms:
	for _ in range(bit_length):
		input_stream.append(i)

#PSK modulation
t = [i for i in range(total_length)]
fc = 1/(0.5*bit_length)
c = [math.sin(2*math.pi*fc*i) for i in t]
psk = [i*j for i,j in zip(c,input_stream)]

plt.suptitle("PSK MODULATION")
plt.subplot(211)
plt.title("Random digital waveform")
plt.plot(input_stream),plt.grid()
plt.xlabel("Time(s)"),plt.ylabel("Amplitude")
plt.subplot(212)
plt.title("PSK modulated waveform")
plt.plot(psk),plt.grid()
plt.xlabel("Time(s)"),plt.ylabel("Amplitude")
plt.tight_layout(),plt.show()