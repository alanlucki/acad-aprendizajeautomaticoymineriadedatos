#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import sys
# define nombre de archivo
import platform

def loadData():
    
    import pandas as pd
    import platform

    datafile = '.\\data\\E000.xlsx'

    if platform.system() == 'Linux':datafile = datafile.replace("\\", "/")
    
    return pd.read_excel(datafile, index_col=0)  # lee dataset

def sci001():
    # lee los datos, con id = paciente
    dataset_ori  = loadData()
    # print('dataset_ori')
    # print(dataset_ori)
    # print(dataset_ori.shape)
    # print(dataset_ori)
    dataset  = dataset_ori.to_numpy()                # numpy
    
    #print('dataset')
    #print(dataset)
    #print(dataset.shape)

    # separa los datos en X y target
    x = dataset[:, :-1]
    y = dataset[:, -1:]


    print('x')
    print(x)

    #print('y')
    #print(y)

    
sci001()