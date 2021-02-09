import matplotlib.pyplot as plt
import numpy as np
import sys

f   = 400.0;                  # frecuencia de la senal
A   = 2;                      # amplitud de la senal
phi = np.pi/4;                # fase
fs  = 8000.0;                 # frecuencia de muestreo
Ts  = 1/fs;                   # periodo de muestreo
T   = 100.0*Ts;               # rango de tiempo
t   = np.arange(0,T,Ts)       # rango de tiempo
x   = A*np.sin(2*np.pi*f*t + phi);

plt.plot(t, x)
plt.title('funcion seno')
plt.show()