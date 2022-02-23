#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 10:56:26 2021

@author: kamil
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn import datasets

wine = pd.read_csv(r'/home/kamil/Documents/ML - Mobilo/Data/winequality-red.csv',
                   sep=';')
columns = ['alcohol']
X = wine[columns]
y = wine['quality'].astype(float)


#n_samples = 500
#X, y, coef = datasets.make_regression(n_samples=n_samples, n_features=1, 
#                                      n_informative=1, noise=10, coef=True, 
#                                     random_state=0)

scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

y_pred_mean = np.full((len(y)), np.mean(y))

plt.figure(figsize=(5,5))
plt.scatter(X, y)
plt.plot((X.min(), X.max()), (np.mean(y), np.mean(y)))

from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y, y_pred_mean)
mae

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

lr = LinearRegression()
lr.fit(X_train, y_train)

y_pred_train = lr.predict(X_train)
y_pred_test = lr.predict(X_test)

mae_train = mean_absolute_error(y_train, y_pred_train)
mae_test = mean_absolute_error(y_test, y_pred_test)
print('MAE: train: {} test {}'.format(mae_train, mae_test))


from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y, y_pred_mean)
mse

mse_train = mean_squared_error(y_train, y_pred_train)
mse_test = mean_squared_error(y_test, y_pred_test)
print('MSE: train: {} test {}'.format(mse_train, mse_test))


from sklearn.metrics import r2_score
r2 = r2_score(y, y_pred_mean)
r2

r2_train = r2_score(y_train, y_pred_train)
r2_test = r2_score(y_test, y_pred_test)
print('R2: train: {} test {}'.format(r2_train, r2_test))



































