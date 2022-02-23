#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 15:16:11 2021

@author: kamil
"""

# CRIM - współczynnik przestępczości w mieście
# ZN - odsetek "dużych działek" - powyzej 2500m2
# INDUS - odsetek terenów industrialnych w mieście
# CHAS - jeśli teren znajduje się przy rzece Charles -1, w pozostałych przypadkach 0
# NOX - stężenie tlenków azotu
# RM - średnia ilość pomieszczeń w budynku
# AGE - odsetek "starych budynków" - powstałych prez 1940 r.
# DIS - ważona odległość od urzędów pracy w Bostonie
# RAD - wskaźnik dostępności do głównych dróg
# TAX - wartość podatku od nieruchomości liczona od 10 tys. dolarów
# PTRATIO - stosunek liczby uczniów na nauczycieli w mieście
# B - odsetek osób pochodzenia afroamerykańskiego
# LSTAT - odsetek mieszkańców zaliczany do ubogich
# MEDV - mediana wartości domów z danego terenu (w tys. dolarów)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


cols = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
        'RAD','TAX','PTRATIO','B','LSTAT','MEDV']
 
data = pd.read_csv(r"/home/kamil/Documents/ML - Mobilo/Data/housing/housing.data",
                   sep=' +', engine='python', header=None, 
                   names=cols)

plt.figure()
sns.boxplot(x=data['CHAS'], y=data['MEDV'])
plt.plot()

plt.figure()
sns.barplot(x=data['CHAS'], y=data['MEDV'])
plt.plot()

sns.barplot(x=data['CRIM'], y=data['MEDV'])

corr_matrix = np.corrcoef(data.values.T)
fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(data=corr_matrix,
            annot=True,
            square = True,
            fmt='.2f',
            xticklabels=cols,
            yticklabels=cols)

sns.pairplot(data[cols])
plt.show()

cols = ['LSTAT', 'RM', 'PTRATIO', 'INDUS','TAX','NOX','MEDV']
 
fig, ax = plt.subplots(figsize=(12,12))
sns.pairplot(data[cols])
plt.show()

