#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing   import OrdinalEncoder
import numpy as np

# define nombre de archivo
datafile = './data/E003.xlsx'

# lee los datos, con id = paciente
dataset_ori  = pd.read_excel(datafile, index_col=0)  # lee dataset, con index
# print(dataset_ori.shape)
# print(dataset_ori)
dataset_ori  = dataset_ori.to_numpy()                # numpy
# print(dataset_ori)

enc = OrdinalEncoder()
enc.fit(dataset_ori)

# codifica resultados
dataset = enc.transform(dataset_ori)

print(dataset)
print(dataset.shape)

# separa los datos en X y target
X = dataset[:, :-1]
y = dataset[:, -1:]

print(X)
print(y)

# # Split the data into a training and a testing set
train_X, test_X, train_y, test_y = train_test_split(X, y, train_size=0.75)

print(train_X)
print(test_X)
print(train_y)
print(test_y)

# decodifica resultados
train = np.concatenate((train_X, train_y), axis=1)
print(train)

train = enc.inverse_transform(train)
print(train)

