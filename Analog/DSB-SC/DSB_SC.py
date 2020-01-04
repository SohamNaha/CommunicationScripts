'''
This is a script to demonstrate a DSB-SC signal with user provided carrier and message signal frequency.
In case of DSB-SC the carrier is suppressed. Thus, the output waveform is of the form:
s(t) = cos(2*pi*fc*t)*cos(2*pi*fm*t)
'''
import matplotlib.pyplot as plt
import math

t = int(input("Enter the time duration to view : "))
tc = int(input("Enter the carrier wave time period: "))
tm = int(input("Enter the message signal time period : "))
fc,fm = 1/tc,1/tm
time = [i for i in range(t)]
carrier = [math.cos(2*math.pi*fc*i) for i in time]
msg = [math.sin(2*math.pi*fm*i) for i in time]
output = [i*j for i,j in zip(carrier,msg)]

plt.suptitle("DSB-SC MODULATION")
plt.subplot(221)
plt.plot(carrier)
plt.title("Carrier Signal")
plt.xlabel("Time(s)"),plt.ylabel("Amplitude")
plt.subplot(222)
plt.plot(msg)
plt.title("Message Signal")
plt.xlabel("Time(s)"),plt.ylabel("Amplitude")
plt.subplot(212)
plt.plot(output)
plt.title("Modulated Signal")
plt.xlabel("Time(s)"),plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()