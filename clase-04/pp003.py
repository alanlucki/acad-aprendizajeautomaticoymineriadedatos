#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy                 as     np
import pandas                as     pd
import sys
import matplotlib.pyplot as plt

np.set_printoptions(threshold=sys.maxsize)

# define nombre de archivo
datafile = './data/E02.xls'

# lee datos
dataset_ori  = pd.read_excel(datafile, index_col=0)  # lee dataset

print('descripción de datos numéricos')
ts = dataset_ori['evento_mes'].hist(bins=12)
ts.plot(kind='bar')
plt.show()
sys.exit()

print('descripción de datos categóricos')
print('business_line_level_1')
ts = dataset_ori['business_line_level_1'].value_counts()
ts.plot(kind='bar')
plt.show()
sys.exit()

print('business_line_level_12')
ts = dataset_ori['business_line_level_2'].value_counts()
ts.plot(kind='bar')
plt.show()
sys.exit()


