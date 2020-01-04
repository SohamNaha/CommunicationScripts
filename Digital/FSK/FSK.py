'''
This script is used to generate FSK modulated output of a random digital waveform.
For +ve inputs the FSK output is a sinusoid of frequency f1
and for -ve wave the output is a sinusoid of frequency f2
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


#FSK modulation
t = [i for i in range(total_length)]
fc = 1/(0.5*bit_length)
f = [(fc/2)*i for i in input_stream]
output = []
for i,j in zip(f,t):
	output.append(math.sin(2*math.pi*(fc+i)*j))

plt.suptitle("FSK MODULATION")
plt.subplot(211)
plt.title("Random digital waveform")
plt.plot(input_stream),plt.grid()
plt.subplot(212)
plt.title("FSK modulated waveform")
plt.plot(output),plt.grid()
plt.tight_layout(),plt.show()