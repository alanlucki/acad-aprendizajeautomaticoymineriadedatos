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
#datafile = '.\\data\\E02.xls'
datafile = './data/E02.xls'

# lee datos
dataset  = pd.read_excel(datafile, index_col=0, na_values = missing_values)  # lee dataset

# existe algún null
print(dataset.isnull().values.any())

# reemplaza valores a null
dataset.loc[dataset.Variable_3 == 'aa', 'Variable_3'] = np.nan
dataset["Variable_3"] = pd.to_numeric(dataset["Variable_3"])

# Identificando todas las columnas con null
print('nulls por columna')
print(dataset.isnull().sum())


# Replace missing values with a number
dataset['Variable_1'].fillna(0,  inplace=True)
dataset['Variable_2'].fillna('', inplace=True)
dataset['Variable_3'].fillna(0,  inplace=True)

# Identificando todas las columnas con null
print('nulls por columna')
print(dataset.isnull().sum())

# existe algún null
print(dataset.isnull().values.any())
