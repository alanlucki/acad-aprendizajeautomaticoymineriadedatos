import matplotlib.pyplot as plt
import numpy as np
import sys

Ts = lambda fs : 1/fs
t  = lambda Ts : np.arange(1,4, Ts)
x  = lambda A , f , t , phi : A * np.sin( 2 * np.pi * f * t + phi )

grid  = lambda : plt.grid()
show  = lambda : plt.show()

f   = 1.0;                      # frecuencia de la senal
A   = 1;                        # amplitud de la senal
phi = 0;                        # fase
fs  = 100.0;                    # frecuencia de muestreo
Ts  = Ts(fs);                   # periodo de muestreo
t   = t(Ts)                     # rango de tiempo de muestreo
x   = x(A , f , t , phi)



plt.plot(t, x)
plt.title('funcion seno')

grid()
show()