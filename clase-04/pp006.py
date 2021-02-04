#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy                 as     np
import pandas                as     pd
import sys
import matplotlib.pyplot as plt

np.set_printoptions(threshold=sys.maxsize)

# define nombre de archivo
datafile = './data/E04.xls'

# lee datos
dataset_ori  = pd.read_excel(datafile, index_col=0)  # lee dataset

# Datos agrupados
print(dataset_ori.describe())
print(dataset_ori.groupby('Class').describe())
print(dataset_ori.groupby('Class').count())
sys.exit()

# # descripción de los datos
# print('tipos de datos')
# print(dataset_ori.dtypes)

# print('descripción de datos numéricos')
# print(dataset_ori.describe())

# print('descripción de datos categóricos')
# print(dataset_ori['Class'].value_counts())

# datos balanceados
filter1 = dataset_ori["Class"]=="grupo1"
filter2 = dataset_ori["Class"]=="grupo2"

g1 = dataset_ori.loc[filter1]
g2 = dataset_ori.loc[filter2]
# print('g1')
# print(g1['Class'].value_counts())

# print('g2')
# print(g2['Class'].value_counts())

g1 = g1.sample(n=1354, replace=False, random_state=1)
g2 = g2.sample(n=1354, replace=False, random_state=1)

# print('g1')
# print(g1['Class'].value_counts())
# print('g2')
# print(g2['Class'].value_counts())

balanceado = pd.concat([g1, g2], axis= 0)

print('balanceado . . . .')
print(balanceado.dtypes)
print(balanceado.describe())
print(balanceado['Class'].value_counts())
