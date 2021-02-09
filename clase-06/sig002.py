def generar():

    import numpy as np

    x    = np.arange(100)         # dominio del tiempo
    t1   = 2.0*np.pi*(2/100.0)*x  # vector de angulos 1
    t2   = 2.0*np.pi*(4/100.0)*x  # vector de angulos 2
    sin1 = np.sin(t1)             # vector de senos 1
    sin2 = np.sin(t2)             # vector de senos 2
    sig  = sin1 + sin2            # suma de senos    
    return x , sig

def plot( x , sig):
    
    import matplotlib.pyplot as plt

    plt.plot(x, sig)
    plt.title('funcion seno')
    plt.grid()
    plt.show()    

def sig002():
    
    gen = generar()
    plot( gen[0]  , gen[1])


sig002()