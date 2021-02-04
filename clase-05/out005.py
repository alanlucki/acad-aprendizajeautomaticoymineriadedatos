
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
#cols.remove('capacidad contratacion')
col      = 'capacidad contratacion'
cols     = [col]
dataset = dataset[cols]

dataset.boxplot()
plt.show()

q10 = dataset[col].quantile(0.10)
q90 = dataset[col].quantile(0.90)
print('-----------------')
print(dataset[col].skew())
print(q10)
print(q90)

dataset[col] = np.where(dataset[col] < q10, q10, dataset[col])
dataset[col] = np.where(dataset[col] > q90, q90, dataset[col])

q10 = dataset[col].quantile(0.10)
q90 = dataset[col].quantile(0.90)
print('-----------------')
print(dataset[col].skew())
print(q10)
print(q90)

dataset.boxplot()
plt.show()
