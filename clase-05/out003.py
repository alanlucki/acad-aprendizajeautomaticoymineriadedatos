
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

# Calculate 1st and 3rd percentiles, and IQR
Q1 = dataset.quantile(0.25)
Q3 = dataset.quantile(0.75)
IQR= Q3 - Q1

# Filter out the rows that fall outside the 1.5 threshold in each column
filtro = ((dataset < (Q1 - 1.5 * IQR)) | (dataset > (Q3 + 1.5 * IQR))).any(axis=1)
outliers    = dataset[filtro]
dataset_new = dataset[~filtro]

outliers.boxplot()
plt.show()

dataset_new.boxplot()
plt.show()

