'''
This script is used to generate random digital wave signal of given bit length and total bit duration
'''
import matplotlib.pyplot as plt
from random import random
import math

chip_length = int(input("Enter the bit length of the bit streams : "))
total_length = int(input("Enter the total duration of the bit streams : "))
num_symbols = math.ceil(total_length/chip_length)

sym = [random()-0.5 for _ in range(num_symbols)]
inp = [1 if i>=0 else 0 for i in sym]
output = []
for i in inp:
    for _ in range(chip_length):
        output.append(i)        

plt.plot(output)
plt.grid(),plt.title("Random Digital Waveform")
plt.show()
