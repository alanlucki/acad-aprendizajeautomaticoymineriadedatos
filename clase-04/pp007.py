#!/usr/bin/env 
# -*- coding: utf-8 -*- 
import numpy                 as     np
import pandas                as     pd
import sys
import matplotlib.pyplot as plt

np.set_printoptions(threshold=sys.maxsize)

# define nombre de archivo
datafile = './data/E04.xls'

# lee datos
dataset_ori  = pd.read_excel(datafile, index_col=0)  # lee dataset

# datos balanceados
filter1 = dataset_ori["Class"]=="grupo1"
filter2 = dataset_ori["Class"]=="grupo2"
g1 = dataset_ori.loc[filter1]
g2 = dataset_ori.loc[filter2]
g1 = g1.sample(n=1354, replace=False, random_state=1)
g2 = g2.sample(n=1354, replace=False, random_state=1)
balanceado = pd.concat([g1, g2], axis= 0)

ax1 = balanceado.V1[balanceado.Class == 'grupo1'].hist(bins= 20, alpha=0.5)
ax1 = balanceado.V1[balanceado.Class == 'grupo2'].hist(bins= 20, alpha=0.5)
ax1.set_title('V1')
ax1.plot(kind='bar')

plt.show()

ax1 = balanceado.V2[balanceado.Class == 'grupo1'].hist(bins= 20, alpha=0.5)
ax1 = balanceado.V2[balanceado.Class == 'grupo2'].hist(bins= 20, alpha=0.5)
ax1.set_title('V2')
ax1.plot(kind='bar')

plt.show()

sys.exit()
