#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing   import OrdinalEncoder
import numpy as np
import seaborn as sns

# define nombre de archivo
datafile = './data/E010.xlsx'

# lee los datos, con id = paciente
dataset_ori  = pd.read_excel(datafile)  # lee dataset, con index
dataset_ori  = dataset_ori.to_numpy()                # numpy

# codifica la data
enc = OrdinalEncoder()
enc.fit(dataset_ori)
dataset = enc.transform(dataset_ori)
# print(dataset)
# print(dataset.shape)

# separa los datos en X y target
X = dataset[:, :-2]
y = dataset[:, -2:]
# print(X)
# print(y)

y_real = y[:,0] # real
y_pred = y[:,1] # predecido

# matriz de confusion
cmatrix = confusion_matrix(y_real, y_pred)
print(cmatrix)

# plot
#sns.heatmap(confusion_matrix(y_real, y_pred))



