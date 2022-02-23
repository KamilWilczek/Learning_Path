#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 12:25:36 2021

@author: kamil
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
 
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
        
cols = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
        'RAD','TAX','PTRATIO','B','LSTAT','MEDV']
 
data = pd.read_csv(r"/home/kamil/Documents/ML - Mobilo/Data/housing/housing.data",
                   sep=' +', engine='python', header=None, 
                   names=cols)
 
X = data.drop('MEDV', axis=1)
y = data['MEDV'].values


scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)


X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2)


lasso_df = pd.DataFrame({'param_value': np.arange(start = 0, stop = 10.1, step = 0.1),
                      'r2_result': 0.,
                      'number_of_features':0})

for i in range(lasso_df.shape[0]):
    
    alpha = lasso_df.at[i, 'param_value']
    model = Lasso(alpha=alpha)
    model.fit(X_train, y_train)
    
    lasso_df.at[i, 'r2_result'] = r2_score(y_test, model.predict(X_test))
    lasso_df.at[i, 'number_of_features'] = len(model.coef_[ model.coef_ > 0])
 
ridge_df = pd.DataFrame({'param_value': np.arange(start = 0, stop = 10.1, step = 0.1),
                      'r2_result': 0.,
                      'number_of_features':0})
 
for i in range(ridge_df.shape[0]):
    
    alpha = ridge_df.at[i, 'param_value']
    model = Ridge(alpha=alpha)
    model.fit(X_train, y_train)
    
    ridge_df.at[i, 'r2_result'] = r2_score(y_test, model.predict(X_test))
    ridge_df.at[i, 'number_of_features'] = len(model.coef_[ model.coef_ > 0])
 
 
elastic_df = pd.DataFrame({'param_value': np.arange(start = 0, stop = 10.1, step = 0.1),
                      'r2_result': 0.,
                      'number_of_features':0})
 
for i in range(elastic_df.shape[0]):
    
    alpha = elastic_df.at[i, 'param_value']
    model = ElasticNet(alpha=alpha)
    model.fit(X_train, y_train)
    
    elastic_df.at[i, 'r2_result'] = r2_score(y_test, model.predict(X_test))
    elastic_df.at[i, 'number_of_features'] = len(model.coef_[ model.coef_ > 0])
 
 
fig, axs = plt.subplots(3, figsize=(10,10))
axs[0].title.set_text('Lasso')
axs[0].scatter(x = lasso_df['param_value'], y=lasso_df['r2_result']*10)
axs[0].scatter(x = lasso_df['param_value'], y=lasso_df['number_of_features'])
axs[0].legend(loc='center right')
axs[1].title.set_text('Ridge')
axs[1].scatter(x = ridge_df['param_value'], y=ridge_df['r2_result']*10)
axs[1].scatter(x = ridge_df['param_value'], y=ridge_df['number_of_features'])
axs[1].legend(loc='center right')
axs[2].title.set_text('Elastic Net')
axs[2].scatter(x = elastic_df['param_value'], y=elastic_df['r2_result']*10)
axs[2].scatter(x = elastic_df['param_value'], y=elastic_df['number_of_features'])
axs[2].legend(loc='center right')
fig.show()

