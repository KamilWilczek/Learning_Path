#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 15:19:57 2021

@author: kamil
"""

import pandas as pd
import matplotlib.pyplot as plt
#--------------------------------------------------------------------------
from sklearn.linear_model import LinearRegression
#--------------------------------------------------------------------------
auto = pd.read_csv(r"/home/kamil/Documents/ML - Mobilo/Data/auto-mpg.csv")
auto.head()
auto.shape
#--------------------------------------------------------------------------
X = auto.iloc[:, 1:-1]
X = X.drop('horsepower', axis=1)
#--------------------------------------------------------------------------
y = auto.loc[:, 'mpg']
#--------------------------------------------------------------------------
X.head()
y.head()
#--------------------------------------------------------------------------
lr = LinearRegression()
lr.fit(X, y)
lr.score(X, y)
#--------------------------------------------------------------------------
my_car1 = [4, 160, 190, 12, 90, 1]
my_car2 = [4, 200, 260, 15, 83, 1]
 
cars = [my_car1, my_car2]
#--------------------------------------------------------------------------
car_predict = lr.predict(cars)
print(car_predict)
