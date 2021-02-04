
import numpy                 as     np
import pandas                as     pd
import sys
import matplotlib.pyplot as     plt
from scipy.stats import zscore

# define nombre de archivo
datafile = '.\\data\\E04.xlsx'

# lee datos
dataset  = pd.read_excel(datafile)  # lee dataset

print(dataset.columns)
columns = dataset.columns

# columnas numericas
numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
cols     = [c for c in dataset.columns if dataset[c].dtype in numerics]
#cols    = ['dias tecnico', 'dias verificacion', 'dias total', 'devuelto linea', 'subsanado']
cols.remove('capacidad contratacion')

dataset = dataset[cols]

dataset.boxplot()
plt.show()

# Filter out the rows
dataset_new = dataset[(z < 3).all(axis=1)]

dataset_new.boxplot()
plt.show()

