
import numpy                 as     np
import pandas                as     pd
import sys

# define nombre de archivo
datafile = '.\\data\\E04.xlsx'

# lee datos
dataset  = pd.read_excel(datafile)  # lee dataset

# tipos de datos
print('tipos de datos')
print(dataset.dtypes)

# Identificando todas las columnas con null
print('nulls por columna')
print(dataset.isnull().sum())

# Identificando todas los valores únicos
print('valores únicos')
print(dataset.nunique())

# identifica valores duplicados
print(dataset.duplicated())

# extrae duplicados
print(dataset[dataset.duplicated()])

# describe los datos
print(dataset.describe())

print(dataset.skew())