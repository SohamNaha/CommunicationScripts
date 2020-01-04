"""
This is a program used to visualize amplitude modulation in python.
For an amplitude modulated wave, the carrier wave given by c(t) = Ac*cos(wc*t)
is modulated w.r.t. the amplitude of the modulating wave (or message signal)
given by m(t) = Am*cos(wm*t).
The modulated signal is given by : s(t) = c(t)[1 + mu * cos(wm * t)]
where mu = modualtion index = Am/Ac
if mu > 1 : overmodulation --- leads to distortion in reconstructed wave
   mu = 1 : critical modulation --- perfect reconstruction possible
   mu < 1 : undermodulation --- aliasing can be removed.

"""
from matplotlib import pyplot as plt
from math import pi
import numpy as np


fs = 2000  # sampling frequency
fc = int(input("Enter the carrier frequency (in Hz) : "))
fm = int(input("Enter the carrier frequency (in Hz) : "))
Ac = float(input("Enter the amplitude of carrier signal : "))
Am = float(input("Enter the amplitude of message signal : "))
modulations = ["Over", "Critical", "Under"]

# X-axis for plot and time series data
t = np.arange(0, 2, 1 / fs)

# calculations of message signal, carrier signal and modulated signal
msg_signal = Am * np.cos(2 * pi * fm * t)
carrier_signal = Ac * np.cos(2 * pi * fc * t)
modulated_signal = carrier_signal * (1 + msg_signal / Ac)


mod = ""
mu = Am / Ac
if mu > 1:
    mod = modulations[0]
elif mu < 1:
    mod = modulations[2]
else:
    mod = modulations[1]

s = " ".join([mod, "-Modulation with modulation index, mu = ", str(mu)])

# plots
plt.suptitle(s)

plt.subplot(3, 1, 1)
plt.plot(t, carrier_signal, "r")
plt.title("Carrier Signal")
plt.xlabel("Time (in seconds)")
plt.ylabel("Amplitude (in volts)")

plt.subplot(3, 1, 2)
plt.plot(t, msg_signal, "g")
plt.title("Message Signal")
plt.xlabel("Time (in seconds)")
plt.ylabel("Amplitude (in volts)")

plt.subplot(3, 1, 3)
plt.plot(t, modulated_signal, "b")
plt.title("Modulated Signal")
plt.xlabel("Time (in seconds)")
plt.ylabel("Amplitude (in volts)")

plt.tight_layout()
plt.subplots_adjust(top = 0.88)
plt.show()