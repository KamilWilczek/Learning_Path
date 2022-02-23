#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:04:57 2021

@author: kamil
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

wine = pd.read_csv(r'/home/kamil/Documents/ML - Mobilo/Data/winequality-red.csv',
                   sep=';')

columns = ['fixed acidity', 'volatile acidity', 'citric acid', 
           'residual sugar', 'chlorides', 'free sulfur dioxide', 'density', 
           'pH', 'sulphates', 'alcohol']

X = wine[columns]

y = wine['quality'].astype(float)

scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)

plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred, s=80, facecolors='none', edgecolors='r')

lr.score(X_test, y_test)

good_counter = np.count_nonzero(y_test == np.rint(y_pred))
total_counter = len(y_test)
print(good_counter / total_counter)
