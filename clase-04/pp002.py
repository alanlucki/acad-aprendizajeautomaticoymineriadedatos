#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy                 as     np
import pandas                as     pd
import sys

np.set_printoptions(threshold=sys.maxsize)

# define nombre de archivo
datafile = './data/E02.xls'

# lee datos
dataset_ori  = pd.read_excel(datafile, index_col=0)  # lee dataset

#print de las primeras líneas
print('primeras filas')
print(dataset_ori.head().to_string())
#sys.exit()

# tipos de datos
print('tipos de datos')
print(dataset_ori.dtypes)
#sys.exit()

# estadísticas de los datos
print('descripción de datos numéricos')
print(dataset_ori.describe())
#sys.exit()

print('descripción de datos categóricos')
print('business_line_level_1')
print(dataset_ori['business_line_level_1'].value_counts())
#sys.exit()

print('business_line_level_2')
print(dataset_ori['business_line_level_2'].value_counts())
#sys.exit()

# Datos agrupados
print(dataset_ori.groupby('business_line_level_1').describe())
print(dataset_ori.groupby('business_line_level_1').count())
#sys.exit()

# valores null
print('valores null')
print(dataset_ori.isna().sum())
sys.exit()

