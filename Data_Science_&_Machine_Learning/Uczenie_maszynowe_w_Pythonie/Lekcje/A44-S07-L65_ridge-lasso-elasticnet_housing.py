#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:02:29 2021

@author: kamil
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
 
 
# importing data - variant 1 with housing example
cols = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
        'RAD','TAX','PTRATIO','B','LSTAT','MEDV']
 
data = pd.read_csv(r"/home/kamil/Documents/ML - Mobilo/Data/housing/housing.data",
                   sep=' +', engine='python', header=None, 
                   names=cols)
 
# transforming data - add column with '1' as first column
data['Ones'] = 1
 
X = data[['Ones']+cols[:-1]].values
X
y = data['MEDV'].values.reshape(-1,1)
y
 
 
# importing data - variant 1 with IRIS
#data = pd.read_csv(r"C:\data\iris.data", header = None)
#
#data.insert(0,'Ones', value=1)
#data[4] = data[4].apply(lambda x: 1 if x == 'Iris-setosa' else 
#                        2 if x == 'Iris-versicolor' else 3)
#data
#
#X = data.iloc[:,:-1].values
#X
#y = data.iloc[:,-1].values.reshape(-1,1)
#y
 
#scaling data
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)
 
scaler = StandardScaler()
scaler.fit(y)
y = scaler.transform(y)
 
 
 
# init weights to some small numbers. Intentionally avoiding random values
weights = np.ones((1,X.shape[1])).T/1000
weights
 
 
# function used to predict values
def predict(X, weights):
        predictions = np.dot(X,weights)
        return predictions.reshape(-1,1)
 
 
# initaiating hyperparameters
eta =   0.01
lmbda =   0.1
epochs = 100
N = X.shape[0] 
 
 
# learning model
for e in range(epochs):
    
    y_pred = predict(X, weights)
    error_pred = np.sum(np.square(y - y_pred)) + lmbda*np.sum(np.square(weights))    
    delta_weight = np.zeros(weights.shape[0]).reshape(-1,1)    
    
    for j in range(weights.shape[0]):
    
        lin_delta_weights = -2 * np.sum(np.dot(X[:,j], (y - y_pred))) / N
        
        if j ==0:
            weights[j] = weights[j] - eta * lin_delta_weights
        else:
            weights[j] = (1-2*eta*lmbda) * weights[j] - eta * lin_delta_weights 
 
    print(e, error_pred, np.square(weights).sum())
 
 
# creating models from scikit learn - just to compare the results
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X,y)
 
from sklearn.linear_model import Ridge
ridge = Ridge(alpha = lmbda)
ridge.fit(X,y)
 
 
# calculating R2
from sklearn.metrics import r2_score
r2_my_ridge = r2_score(y, predict(X, weights))
r2_lr = r2_score(y, lr.predict(X))
r2_ridge = r2_score(y, ridge.predict(X))
 
 
# showing coefficients
print(weights.reshape(1,-1))
print(lr.coef_)
print(ridge.coef_)
 
 
# printing results
print('R2\t','My Ridge\t', r2_my_ridge, 
      '\tLINREG\t', r2_lr, '\tRIDGE\t', r2_ridge)
print('W \t','My Ridge\t', np.square(weights).sum(), 
      '\tLINREG\t', np.square(lr.coef_).sum(), 
      '\tRIDGE\t', np.square(ridge.coef_).sum())
 




































