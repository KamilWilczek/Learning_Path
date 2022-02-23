#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:27:58 2021

@author: kamil
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing   import StandardScaler
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
 
 
cols = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
        'RAD','TAX','PTRATIO','B','LSTAT','MEDV']
 
data = pd.read_csv(r"/home/kamil/Documents/ML - Mobilo/Data/housing/housing.data",
                   sep=' +', engine='python', header=None, 
                   names=cols)



data = data.loc[:,['LSTAT', 'MEDV']]
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
outlier_condition = (data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))
data = data[~outlier_condition.any(axis=1)]

X = data['LSTAT'].values.reshape(-1,1)
y = data['MEDV'].values.reshape(-1,1)
plt.scatter(X, y, color='green')

scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)
scaler.fit(y)
y = scaler.transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

lr = LinearRegression()
lr.fit(X_train, y_train)

mae_train = mean_absolute_error(y_train, lr.predict(X_train))
mae_test = mean_absolute_error(y_test, lr.predict(X_test))
print('MAE train {} test {}'.format(mae_train, mae_test))

mse_train = mean_squared_error(y_train, lr.predict(X_train))
mse_test = mean_squared_error(y_test, lr.predict(X_test))
print('MSE train {} test {}'.format(mse_train, mse_test))

r2_train = r2_score(y_train, lr.predict(X_train))
r2_test = r2_score(y_test, lr.predict(X_test))
print('R2 train {} test {}'.format(r2_train, r2_test))
#___________________________________________________________________________

cols = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
        'RAD','TAX','PTRATIO','B','LSTAT','MEDV']
 
data = pd.read_csv(r"/home/kamil/Documents/ML - Mobilo/Data/housing/housing.data",
                   sep=' +', engine='python', header=None, 
                   names=cols)
 
data = data.loc[:,['LSTAT','MEDV']]
 
X = data['LSTAT'].values.reshape(-1,1)
y = data['MEDV'].values.reshape(-1,1)
 
plt.figure(figsize=(5,5))
plt.scatter(X, y)
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
 
lr = LinearRegression()
lr.fit(X_train, y_train)                
 
mae_train = mean_absolute_error(y_train, lr.predict(X_train))
mae_test = mean_absolute_error(y_test, lr.predict(X_test))
print("MAE TRAIN {}, TEST {}".format(round(mae_train,2), round(mae_test,2)))
 
mse_train = mean_squared_error(y_train, lr.predict(X_train))
mse_test = mean_squared_error(y_test, lr.predict(X_test))
print("MSE TRAIN {}, TEST {}".format(round(mse_train,2), round(mse_test,2)))
 
r2_train = r2_score(y_train, lr.predict(X_train))
r2_test = r2_score(y_test, lr.predict(X_test))
print("R2  TRAIN {}, TEST {}".format(round(r2_train,2), round(r2_test,2)))

#___________________________________________________________________________

cols = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
        'RAD','TAX','PTRATIO','B','LSTAT','MEDV']
 
data = pd.read_csv(r"/home/kamil/Documents/ML - Mobilo/Data/housing/housing.data",
                   sep=' +', engine='python', header=None, 
                   names=cols)
 
 
# detecting outliers with IQR method
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
 
## removing outliers
outlier_condition = ((data < (Q1 - 1.5 * IQR)) | (data > (Q3 +1.5 * IQR)))
data = data[~outlier_condition.any(axis=1)]
 
X = data.loc[:, data.columns!='MEDV']
y = data['MEDV'].values.reshape(-1,1)
 
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)
 
scaler = StandardScaler()
scaler.fit(y)
y = scaler.transform(y)
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
 
lr = LinearRegression()
lr.fit(X_train, y_train)                
 
 
mae_train = mean_absolute_error(y_train, lr.predict(X_train))
mae_test = mean_absolute_error(y_test, lr.predict(X_test))
print("MAE TRAIN {}, TEST {}".format(round(mae_train,2), round(mae_test,2)))
 
mse_train = mean_squared_error(y_train, lr.predict(X_train))
mse_test = mean_squared_error(y_test, lr.predict(X_test))
print("MSE TRAIN {}, TEST {}".format(round(mse_train,2), round(mse_test,2)))
 
r2_train = r2_score(y_train, lr.predict(X_train))
r2_test = r2_score(y_test, lr.predict(X_test))
print("R2  TRAIN {}, TEST {}".format(round(r2_train,2), round(r2_test,2)))

#___________________________________________________________________________


cols = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
        'RAD','TAX','PTRATIO','B','LSTAT','MEDV']
 
data = pd.read_csv(r"/home/kamil/Documents/ML - Mobilo/Data/housing/housing.data",
                   sep=' +', engine='python', header=None, 
                   names=cols)
 
# prepare for residual plot
X = data.loc[:, data.columns!='MEDV']
y = data['MEDV'].values.reshape(-1,1)
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
 
lr = LinearRegression()
lr.fit(X_train, y_train)                
 
mae_train = mean_absolute_error(y_train, lr.predict(X_train))
mae_test = mean_absolute_error(y_test, lr.predict(X_test))
print("MAE TRAIN {}, TEST {}".format(round(mae_train,2), round(mae_test,2)))
 
mse_train = mean_squared_error(y_train, lr.predict(X_train))
mse_test = mean_squared_error(y_test, lr.predict(X_test))
print("MSE TRAIN {}, TEST {}".format(round(mse_train,2), round(mse_test,2)))
 
 
r2_train = r2_score(y_train, lr.predict(X_train))
r2_test = r2_score(y_test, lr.predict(X_test))
print("R2  TRAIN {}, TEST {}".format(round(r2_train,2), round(r2_test,2)))











