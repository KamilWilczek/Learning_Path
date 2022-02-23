#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 15:06:04 2021

@author: kamil
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron

diag = pd.read_csv(r'/home/kamil/Documents/ML - Mobilo/Data/breast_cancer.csv')

X = diag[['area_mean', 'area_se', 'texture_mean' ,'concavity_worst', 
          'concavity_mean']]
y = diag['diagnosis']
y = y.apply(lambda d:1 if d == 'M' else -1)

X
y

sc = StandardScaler()
sc.fit(X)
X_std = sc.transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_std, y, test_size=0.2)

perceptron = Perceptron(max_iter=100, eta0=0.01)

perceptron.fit(X_train, y_train)

y_pred = perceptron.predict(X_test)

print(perceptron.score(X_test, y_test))

good = y_test[y_test == y_pred].count()
total = y_test.count()
print('result: {}'.format(100*good/total))
