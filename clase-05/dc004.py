#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy                 as     np
import pandas                as     pd
import sys
import matplotlib.pyplot     as plt

# Making a list of missing value types
missing_values = ["n/a", "na", "--", "null", "??"]

np.set_printoptions(threshold=sys.maxsize)

# define nombre de archivo
datafile = './data/E03.xls'

# lee datos
dataset  = pd.read_excel(datafile, index_col=0, na_values = missing_values)  # lee dataset

print(dataset.shape)
sys.exit(0)
print(dataset.columns)


print('nulls por columna-----------')
print(dataset.isnull().sum())

# existe algún null
print('existe nulls----------------')
print(dataset.isnull().values.any())

# null en una columna
print('nulls por columna-----------')
print(dataset['MathSAT'].isna().sum())

# nulls en todo el dataframe
print('nulls en todo el dataframe--')
print(dataset.isna().sum().sum())

# nulls por cada fila
print(dataset.isnull().sum(axis=1).tolist())
