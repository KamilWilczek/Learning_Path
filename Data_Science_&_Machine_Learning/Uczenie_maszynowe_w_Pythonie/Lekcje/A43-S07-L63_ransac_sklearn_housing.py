#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 11:07:10 2021

@author: kamil
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing   import StandardScaler
from sklearn.linear_model import RANSACRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
 
cols = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
        'RAD','TAX','PTRATIO','B','LSTAT','MEDV']
 
data = pd.read_csv(r"/home/kamil/Documents/ML - Mobilo/Data/housing/housing.data",
                   sep=' +', engine='python', header=None, 
                   names=cols)
 
X = data.loc[:, 'LSTAT'].values.reshape(-1,1)
y = data['MEDV'].values



scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


ransac = RANSACRegressor()
ransac.fit(X_train, y_train)
r2_ransac = r2_score(y_test, ransac.predict(X_test))
print("Ransac regression result: {}".format(r2_ransac))


lr = LinearRegression()
lr.fit(X_train, y_train)
r2_lr = r2_score(y_test, lr.predict(X_test))
print("Linear regression result: {}".format(r2_lr))


the_best_r2 = 0

for tmp_threshold in range(10,40):
    tmp_ransac = RANSACRegressor(residual_threshold=tmp_threshold)
    tmp_ransac.fit(X_train, y_train)
    tmp_r2 = r2_score(y_test, tmp_ransac.predict(X_test))
    
    print("Threshold {} - R2 {}".format(tmp_threshold, tmp_r2))
    
    if tmp_r2 > the_best_r2:
        the_best_r2 = tmp_r2
        ransac = tmp_ransac
        

line_X = np.arange(X.min(), X.max())[:, np.newaxis]
line_y_ransac = ransac.predict(line_X)
line_y_lr = lr.predict(line_X)
 
plt.scatter(X_train[ransac.inlier_mask_], y_train[ransac.inlier_mask_], color='green', marker='.',
            label='Inliers')
plt.scatter(X_train[~ransac.inlier_mask_], y_train[~ransac.inlier_mask_], color='gold', marker='.',
            label='Outliers')
 
plt.plot(line_X, line_y_ransac, color='red', linewidth=2, label='RANSAC regressor')
plt.plot(line_X, line_y_lr, color='blue', linewidth=2, label='Linear regression')
 
plt.legend(loc='lower right')
plt.xlabel("Input")
plt.ylabel("Response")
plt.show()
 
r2_ransac = r2_score(y_test, ransac.predict(X_test))
print("Ransac regression result: {}".format(r2_ransac))
print("Linear regression result: {}".format(r2_lr))
































