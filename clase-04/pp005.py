#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy                 as     np
import pandas                as     pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns

numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

# define nombre de archivo
datafile = './data/E02.xls'

# lee datos
dataset_ori  = pd.read_excel(datafile, index_col=0)  # lee dataset

print('columns')
print(dataset_ori.describe().to_string())

ax1 = dataset_ori.plot(kind='scatter', x='monto_perdida', y='seguro',        color='r'        )    
ax2 = dataset_ori.plot(kind='scatter', x='monto_perdida', y='recuperacion',  color='g', ax=ax1)    
ax3 = dataset_ori.plot(kind='scatter', x='monto_perdida', y='perdida_bruta', color='b', ax=ax1)    

ax1.set_xlabel("monto_perdida")
ax1.set_ylabel("seguro, recuperacion, perdida_bruta")
plt.show()
