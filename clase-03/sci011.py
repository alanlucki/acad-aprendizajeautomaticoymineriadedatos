#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import seaborn as sns

def percentage_error(actual, predicted):
    res = np.empty(actual.shape)
    for j in range(actual.shape[0]):
        if actual[j] != 0:
            res[j] = (actual[j] - predicted[j]) / actual[j]
        else:
            res[j] = predicted[j] / np.mean(actual)
    return res

def mean_absolute_percentage_error(y_true, y_pred): 
    return np.mean(np.abs(percentage_error(np.asarray(y_true), np.asarray(y_pred)))) 

# define nombre de archivo
datafile = './data/E011.xlsx'

# lee los datos, con id = paciente
dataset  = pd.read_excel(datafile)  # lee dataset, con index
dataset  = dataset.to_numpy()                # numpy

# separa los datos en X y target
y = dataset[:, -2:]
print(y)

y_real = y[:,0] # real
y_pred = y[:,1] # predecido

# matriz de confusion
mape = mean_absolute_percentage_error(y_real, y_pred)
print(mape)

