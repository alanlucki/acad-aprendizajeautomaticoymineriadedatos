
import numpy                 as     np
import pandas                as     pd
import sys
import matplotlib.pyplot     as plt

# Making a list of missing value types
missing_values = ["n/a", "na", "--", "null", "??"]

#np.set_printoptions(threshold=sys.maxsize)

# define nombre de archivo
datafile = './data/E02.xls'

# lee datos
dataset  = pd.read_excel(datafile, index_col=0, na_values = missing_values)  # lee dataset

# reemplaza valores a null
dataset.loc[dataset.Variable_1 <= 0, 'Variable_3'] = np.nan
dataset.loc[dataset.Variable_3 == 'aa', 'Variable_3'] = np.nan
dataset.astype({'Variable_3': 'float64'}).dtypes

# tipos de datos
print('tipos de datos')
print(dataset.dtypes)

# Identificando todas las columnas con null
print('nulls por columna')
print(dataset.isnull().sum())

#print(dataset.to_string())
