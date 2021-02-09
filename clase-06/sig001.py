import numpy as np
import sys


def createArray():
    # Crear un array 1D, 2D, 3D
    a = np.array([1, 2, 3])           # Crea un vector
    # print(a)
    b = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float)  # Crea una matriz
    # print(b)
    c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]], dtype=int)
    # print(c)
    # sys.exit(0)
    return c


def dimensionesArray(m):
    # Dimensiones, tamanos
    print('----------------')
    print('ndim ', m.ndim)    # dimensiones
    print('shape', m.shape)    # tamano de las dimensiones
    print('size ', m.size)    # elementos en el array
    print('dtype', m.dtype)    # tipo de dato del array
    print('item ', m.itemsize)  # bytes por c/elemento
    # sys.exit(0)


def initialValues():
    # valores iniciales
    # x = np.empty((3,2))                 # Crea un array vacio
    # print(x)
    # x = np.zeros((3,4))                 # Crea un array de zeros
    # print(x)
    # x = np.ones((2,3,4),dtype=np.int16) # Crea un array de unos
    # print(x)
    # x = np.random.random((2,2))         # Crea un array aleatorio
    # print(x)
    # Crea un array aleatorio enteros
    x = np.random.randint(0, 100, (4, 4))
    print(x)
    # sys.exit(0)

# generacion de secuencias
# x = np.arange(10)                 # Crea un array de tamano 10, iniciando en 0
# print(x)
# x = np.arange(10,26)              # Crea un array de 10 a 25, sin el ultimo
# print(x)
# x = np.arange(10,26,5)            # Crea un array de 10 a 25, separado de 5 e 5
# print(x)
# sys.exit(0)

# generacion de secuencias
# x = np.linspace(0,2,9)              # divide el espacio de 0 a 2, en 9 valores, incluye el extremo derecho
# print(x)
# x = np.full((2,2),7)                # Crea una constante
# print(x)
# x = np.eye(2)                       # Crea una matriz identidad de 2X2
# print(x)

# operaciones de matrices
# x1 = np.arange(0, 10)            # Crea un array de 10 a 25, separado de 5 e 5
# x2 = np.arange(5, 15)            # Crea un array de 10 a 25, separado de 5 e 5
# print(x1)
# print(x2)
# print(x1 + x2)
# print(x1 * x2)


def sig001():

    v = createArray()
    dimensionesArray(v)
    initialValues()

    return
    x1 = np.random.randint(0, 100, (2, 4))
    x2 = np.random.randint(0, 100, (4, 3))

    print(x1)
    print(x2)
    print(np.dot(x1, x2))


sig001()
