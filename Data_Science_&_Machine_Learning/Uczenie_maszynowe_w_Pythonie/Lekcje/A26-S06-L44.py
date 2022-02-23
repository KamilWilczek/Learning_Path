#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 12:08:18 2021

@author: kamil
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv(r'/home/kamil/Documents/ML - Mobilo/Data/high_school_sat_gpa.csv',
                   sep=' ', usecols=['math_SAT', 'verb_SAT', 'high_GPA'])
data.head()
data.dtypes

plt.figure(figsize=(10,6))
plt.scatter(data['math_SAT'], data['high_GPA'], color='red')
plt.show()

lr_math = LinearRegression()
lr_math.fit(data['math_SAT'].values.reshape(-1,1), 
            data['high_GPA'].values.reshape(-1,1))

x_min = data['math_SAT'].min()
x_max = data['math_SAT'].max()

plt.figure(figsize=(10,6))
plt.scatter(data['math_SAT'], data['high_GPA'], color='red')
plt.plot([x_min, x_max], lr_math.predict([[x_min],[x_max]]), color='red')
plt.show()


plt.figure(figsize=(10,6))
plt.scatter(data['verb_SAT'], data['high_GPA'], color='blue')
plt.show()

lr_verb = LinearRegression()
lr_verb.fit(data['verb_SAT'].values.reshape(-1,1), 
            data['high_GPA'].values.reshape(-1,1))

x_min = data['verb_SAT'].min()
x_max = data['verb_SAT'].max()

plt.figure(figsize=(10,6))
plt.scatter(data['verb_SAT'], data['high_GPA'], color='red')
plt.plot([x_min, x_max], lr_math.predict([[x_min],[x_max]]), color='blue')
plt.show()


lr = LinearRegression()
lr.fit(data[['math_SAT','verb_SAT']].values, data['high_GPA'].values.reshape(-1,1))
 
student_john = np.array([600,650]).reshape(1,2)
lr.predict(student_john)
