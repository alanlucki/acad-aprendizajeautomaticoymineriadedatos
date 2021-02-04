#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy                 as     np
import pandas                as     pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns

def my_function():

    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

    # define nombre de archivo
    datafile = './data/E02.xls'

    # lee datos
    dataset_ori  = pd.read_excel(datafile, index_col=0)  # lee dataset

    print('columns')
    print(dataset_ori.describe().to_string())

    print('selecciona columnas numérico')
    dataset_ori = dataset_ori.select_dtypes(include=numerics)

    dataset_ori = dataset_ori[["seguro", "monto_perdida"]]

    sns.boxplot(x="variable", y="value", data=pd.melt(dataset_ori))

    plt.show()
    sys.exit()


my_function()
