import matplotlib.pyplot as plt
import numpy as np
import sys
import pylab

x    = np.arange(1, 100, 1/100.0)    # dominio del tiempo
x    = 2*np.pi*x                     # dominio del tiempo
sig  = np.sin(x)                     # vector de la senal

plt.plot(x, sig)
plt.show()