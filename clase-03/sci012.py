#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
N = 1


def desplaza1(data):
    cifrado = ""
    # Iteramos por cada letra del mensaje
    for l in data:
        # Si la letra está en el abecedario se reemplaza
        if l in abc:
            pos_letra = abc.index(l)
            # Sumamos para movernos a la derecha del abc
            nueva_pos = (pos_letra + N) % len(abc)
            cifrado += abc[nueva_pos]
        else:
            # Si no está en el abecedario sólo añadelo
            cifrado += l

    return cifrado


def desplaza2(data):
    return map(lambda c: chr(ord(c)+N) if(c != "z") else "a", data)


def desplaza3(data):

    data2 = ''
    for car in data:
        num = ord(car) + N
        data2 += chr(num)

    return data2


def plot(data):
    ts = pd.Series(data).value_counts()
    ts = ts.sort_index(ascending=True)
    ts.plot(kind='bar')
    plt.show()


char = [[' ', ''], ['"', ''], ['&', ''], ['/', ''], ['(', ''], [')', ''], ['-', ''], ['.', ''], ['\n', ''],
        [',', ''], [':', ''], ['Á', 'A'], ['É', 'E'], [
            'Í', 'I'], ['Ó', 'O'], ['Ú', 'U'],
        ['0', ''], ['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', ''], ['8', ''], ['9', '']]

# lee los datos
datafile = './data/E012.txt'
#f = open(datafile, "r", encoding = 'utf-8')
f = open(datafile, "r")
data = f.read()
data = data.upper()

# reemplaza
for c in char:
    data = data.replace(c[0], c[1])

# extrae frecuencia y plotea
plot(list(data))

# corrimiento
plot(list(desplaza1(data)))  # Pacherres

plot(desplaza2(list(data)))  # Guerra

plot(list(desplaza3(data)))  # Quispe
