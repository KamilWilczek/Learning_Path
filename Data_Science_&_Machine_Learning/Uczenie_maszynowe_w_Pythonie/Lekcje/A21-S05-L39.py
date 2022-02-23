#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:54:41 2021

@author: kamil
"""

import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


iris = datasets.load_iris()

X = iris.data[:]
y = iris.target[:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

sc = StandardScaler()
sc.fit(X)

X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

perceptron = Perceptron(max_iter=20, eta0=0.1)
perceptron.fit(X_train_std, y_train)

y_pred = perceptron.predict(X_test_std)

y_test
y_pred

[(a,b) for (a, b) in zip(y_pred[y_pred != y_test], y_test[y_pred != y_test])]

bad_results = [(a,b) for (a, b) in zip(y_pred[y_pred != y_test], y_test[y_pred != y_test])]
good_results = [(a,b) for (a, b) in zip(y_pred[y_pred == y_test], y_test[y_pred == y_test])]
bad_results
good_results
print(len(good_results) / len(y_test))

print(perceptron.score(X_test_std, y_test))

print(perceptron.coef_)
print(perceptron.intercept_)
print(perceptron.n_iter_)
print(perceptron.t_)

