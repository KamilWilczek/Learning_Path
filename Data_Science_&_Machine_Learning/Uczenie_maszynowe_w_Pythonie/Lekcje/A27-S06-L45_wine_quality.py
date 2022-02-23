#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:15:08 2021

@author: kamil
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

wine = pd.read_csv(r'/home/kamil/Documents/ML - Mobilo/Data/winequality-red.csv', 
                   sep=';')

wine.head()
wine.info()

wine.describe()
wine.columns

for i in wine.columns:
    print(wine[i].describe())
    
plt.figure()
sns.boxplot(x=wine['quality'], y=wine['alcohol'])
plt.plot()

for i in wine.columns[:-1]:
    plt.figure()
    sns.boxplot(x=wine['quality'], y=wine[i])
    plt.plot()
    
    
    
    
plt.figure()
sns.barplot(x=wine['quality'], y=wine['alcohol'])
plt.plot()

for i in wine.columns[:-1]:
    plt.figure()
    sns.barplot(x=wine['quality'], y=wine[i])
    plt.plot()



corr_matrix = np.corrcoef(wine.values.T)

fig, ax = plt.subplots(figsize=(11,11))
sns.set(font_scale=1.1)
sns.heatmap(data=corr_matrix, square=True, cbar=True, annot=True, fmt='.2f', 
            annot_kws={'size':10}, xticklabels=wine.columns, 
            yticklabels=wine.columns)


sns.pairplot(wine, height=1.5)

columns = ['alcohol', 'volatile acidity', 'sulphates', 'citric acid', 
           'total sulfur dioxide', 'density', 'quality']

sns.pairplot(wine[columns], size=1.5)