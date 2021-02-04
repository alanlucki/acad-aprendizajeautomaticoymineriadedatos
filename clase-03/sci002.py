#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from   sklearn.model_selection import train_test_split
from   sklearn.preprocessing   import OrdinalEncoder
import numpy as np
import sys
import platform

if platform.system() == 'Linux':
    # define nombre de archivo
    datafile = './data/E002.xlsx'

# lee los datos, con id = paciente
dataset_ori  = pd.read_excel(datafile)  # lee dataset
# print('dataset_ori')
# print(dataset_ori)
# print(dataset_ori.shape)
dataset  = dataset_ori.to_numpy()                # numpy
# print('dataset')
# print(dataset)
# print(dataset.shape)

# separa los datos en X y target
X = dataset[:, :-1]
y = dataset[:, -1:]

print('X')
print(X)
print('y')
print(y)
# sys.exit(0)

# Split the data into a training and a testing set
train_X, test_X, train_y, test_y = train_test_split(X, y, train_size=0.75)

# print(train_X.shape, train_X)
# print(test_X.shape,  test_X)
# print(train_y.shape, train_y)
# print(test_y.shape,  test_y)

# concatenar resultados
train = np.concatenate((train_X, train_y), axis=1)
print(train.round(4))
test  = np.concatenate((test_X, test_y), axis=1)
print(test.round(4))