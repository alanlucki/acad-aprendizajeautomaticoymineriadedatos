import matplotlib.pyplot as plt
import numpy as np
import sys

f1  = 100.0;                  # frecuencia de la senal
f2  = 300.0;                  # frecuencia de la senal
f3  = 600.0;                  # frecuencia de la senal
A   = 3;                      # amplitud de la senal
phi = 0;                      # fase
fs  = 8000.0;                 # frecuencia de muestreo
Ts  = 1/fs;                   # periodo de muestreo
t   = np.arange(0,0.1, Ts)      # rango de tiempo de muestreo
x1  = A*np.sin(2*np.pi*f1*t + phi);
x2  = A*np.sin(2*np.pi*f2*t + phi);
x3  = A*np.sin(2*np.pi*f3*t + phi);

x   = x1+x2+x3

# plt.plot(t, x)
# plt.title('funcion seno')
# plt.show()


# Frequency domain representation
tf = np.fft.fft(x)/len(x)           # Normalize amplitude
tf = tf[range(int(len(x)/2))] # Exclude sampling frequency

tpCount     = len(x)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/fs
frequencies = values/timePeriod

plt.title('Fourier transform depicting the frequency components')
plt.plot(frequencies, abs(tf))
plt.xlabel('Frequency')
plt.ylabel('Amplitude')

plt.show()