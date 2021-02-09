#!/usr/bin/env python
# -*- coding: utf-8 -*-

def loadData():

    import pandas as pd
    import platform

    datafile = '.\\data\\E000.xlsx'

    if platform.system() == 'Linux':datafile = datafile.replace("\\", "/")
    
    return pd.read_excel(datafile)

def listColumns(x):

    print("------------------------------------------------------------------")
    print("Listar Columnas")
    print("------------------------------------------------------------------")

    for i in range(0, len(x.columns)):
        print i, ' - ', x.columns[i]

    print("")

def describeData(x):

    print("------------------------------------------------------------------")
    print("Data Describe")
    print("------------------------------------------------------------------")
    print(x.describe().to_string())

    print("")

def histogramData(x):
    
    print("------------------------------------------------------------------")
    print("Historgrama  ")
    print("------------------------------------------------------------------")

    import matplotlib.pyplot as plt

    # histograma de los datos
    x.drop(['Title', 'url','comments','Images_video','Elapsed_days','Shares'], 1).hist()
    plt.show()
    plt.scatter(x['Word_count'].values, x['Links'].values)
    plt.show()

def linearRegression(x):

    print("------------------------------------------------------------------")
    print("Linear Regresion  ")
    print("------------------------------------------------------------------")

    import numpy as np
    from sklearn import linear_model
    from sklearn.metrics import mean_squared_error, r2_score

    # regresión
    X_train = x[["Word_count", "Links"]].values
    Y_train = x['Shares'].values
    regr = linear_model.LinearRegression()

    # Entrenamos nuestro modelo
    regr.fit(X_train, Y_train)
    # Consulta
    Y_pred = regr.predict(X_train)
    result = np.concatenate(
        ([Y_train], [Y_pred], [np.absolute(Y_train - Y_pred)])).T

    #print result.astype(int)
    print("------------------------------------------------------------------")
    print("Resultado")
    print("------------------------------------------------------------------")
 
    print 'Coefficients         :   ', regr.coef_[0]  ,'\t',  regr.coef_[1]
    print 'Independent term     :   ', regr.intercept_
    print "Mean squared error   :    %.4f" % mean_squared_error(Y_train, Y_pred)
    print 'Variance score       :    %.4f' % r2_score(Y_train, Y_pred) 

def sci000():

    print("------------------------------------------------------------------")
    print("sci000")
    print("------------------------------------------------------------------")

    data = loadData()
    #listColumns(data)
    #describeData(data)
    linearRegression(data)
    histogramData(data)
    
    print("------------------------------------------------------------------")

sci000()
