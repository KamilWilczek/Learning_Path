#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:57:54 2021

@author: kamil
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.linear_model import LinearRegression
from scipy import stats

cols = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
        'RAD','TAX','PTRATIO','B','LSTAT','MEDV']
 
data = pd.read_csv(r"/home/kamil/Documents/ML - Mobilo/Data/housing/housing.data",
                   sep=' +', engine='python', header=None, 
                   names=cols)


data1 = data.loc[:,['LSTAT', 'MEDV']]
len(data1)

plt.figure()
sns.boxplot(x = data1['LSTAT'])
plt.plot()

lr = LinearRegression()
X = data1['LSTAT'].values.reshape(-1,1)
y = data1['MEDV'].values.reshape(-1,1)
lr.fit(X, y)
lr.score(X,y)





z = np.abs(stats.zscore(data1))
treshold = 3
data1_o_z = data1[(z<treshold).all(axis=1)]
len(data1_o_z)

plt.figure()
sns.boxplot(x=data1_o_z['LSTAT'])
plt.plot()

lr1_o_z = LinearRegression()
X = data1_o_z['LSTAT'].values.reshape(-1,1)
y = data1_o_z['MEDV'].values.reshape(-1,1)
lr1_o_z.fit(X, y)
lr1_o_z.score(X, y)




Q1 = data1.quantile(0.25)
Q3 = data1.quantile(0.75)
IQR = Q3 - Q1

outlier_condition = ((data1 < (Q1 - 1.5 * IQR)) | (data1 > (Q3 + 1.5 * IQR)))
data1_o_iqr = data1[~outlier_condition.any(axis=1)]
len(data1_o_iqr)

plt.figure()
sns.boxplot(x=data1_o_iqr['LSTAT'])
plt.plot()

lr1_o_iqr = LinearRegression()
X = data1_o_iqr['LSTAT'].values.reshape(-1,1)
y = data1_o_iqr['MEDV'].values.reshape(-1,1)
lr1_o_iqr.fit(X, y)
lr1_o_iqr.score(X, y)