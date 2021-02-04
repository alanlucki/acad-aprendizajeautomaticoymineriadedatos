
import numpy                 as     np
import pandas                as     pd
import sys
import matplotlib.pyplot as     plt

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

dataset.boxplot(cols)
plt.show()

for c in cols:
    dataset[c] = np.log10(np.abs(dataset[c])+1)

dataset.boxplot(cols)
plt.show()

sys.exit(0)
