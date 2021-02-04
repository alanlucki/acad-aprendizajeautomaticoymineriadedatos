#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.linear_model    import LinearRegression
from sklearn.model_selection import train_test_split
import numpy                 as     np
import pandas                as     pd
import sys

np.set_printoptions(threshold=sys.maxsize)

# define nombre de archivo
datafile = './data/E004.xlsx'

# lee datos
dataset_ori  = pd.read_excel(datafile, index_col=0)  # lee dataset

# describe dataset
dataset_ori.describe()
dataset  = dataset_ori.to_numpy()                # numpy
# print(dataset)

# separa los datos en X y target
X = dataset[:, :-1]
y = dataset[:, -1:]
# print('X', X)
# print('y', y)

# separa los datos para entrenamiento y para pruebas
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# entrena regresion lineal
regressor = LinearRegression()
rl = regressor.fit(X_train, y_train)
print(regressor)

print('inter:', regressor.intercept_, 'coef:', regressor.coef_)

# haciendo predicciones
y_test_pred = regressor.predict(X_test)
print('X_test     ', X_test)
print('y_test_pred', y_test_pred)

# concatena
test = np.concatenate((y_test, y_test_pred), axis=1)
print('yreal, ypred')
print(test)


