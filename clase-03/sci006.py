#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.neural_network  import MLPClassifier
from sklearn.datasets        import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics         import confusion_matrix
from sklearn.metrics         import plot_confusion_matrix
import numpy                 as     np
import sys
import matplotlib.pyplot     as     plt  # doctest: +SKIP

np.set_printoptions(threshold=sys.maxsize)

# prepara datos para clasificacion
X, y = make_classification(n_samples=100, random_state=1)
print(X)
print(y)
print('lenX', X.shape)
print('lenY', y.shape)
# sys.exit(0)
# separa los datos para entrenamiento y para pruebas
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=1)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# entrena clasificador
clf = MLPClassifier(random_state=1, max_iter=300).fit(X_train, y_train)
print(clf)

# calcula probabilidades, solo el primero
y_test_prob = clf.predict_proba(X_test[:1])
#print('X_test     ', X_test[:1])
#print('y_test_prob', y_test_prob)
#sys.exit(0)
# predice resultados, solo el primero
#y_test_pred = clf.predict(X_test)
#print('X_test    ', X_test)
#print('y_test    ', y_test)
#print('y_test_prd', y_test_pred)

# # score
# score = clf.score(X_test, y_test)
# print(score)

# # matriz de confusion
# cmatrix = confusion_matrix(y_test, y_test_pred)
# print(cmatrix)

# plot_confusion_matrix(clf, X_test, y_test)  # doctest: +SKIP
# plt.show()                                  # doctest: +SKIP