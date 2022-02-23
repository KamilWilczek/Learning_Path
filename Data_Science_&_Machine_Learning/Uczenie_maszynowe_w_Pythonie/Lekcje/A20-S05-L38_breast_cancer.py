#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:29:47 2021

@author: kamil
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

 
class Perceptron:
    
    def __init__(self, eta=0.10, epochs=50, is_verbose = False):
        
        self.eta = eta
        self.epochs = epochs
        self.is_verbose = is_verbose
        self.list_of_errors = []
        
    
    def predict(self, x):
        
        ones = np.ones((x.shape[0],1))
        x_1 = np.append(x.copy(), ones, axis=1)
        #activation = self.get_activation(x_1)
        #y_pred = np.where(activation >0, 1, -1)
        #return y_pred
        return np.where(self.get_activation(x_1) > 0, 1, -1)
        
    
    def get_activation(self, x):
        
        activation = np.dot(x, self.w)
        return activation
     
    
    def fit(self, X, y):
        
        self.list_of_errors = []
        
        ones = np.ones((X.shape[0], 1))
        X_1 = np.append(X.copy(), ones, axis=1)
 
        self.w = np.random.rand(X_1.shape[1])
        
        for e in range(self.epochs):
 
            error = 0
            
            activation = self.get_activation(X_1)
            delta_w = self.eta * np.dot((y - activation), X_1)
            self.w += delta_w
                
            error = np.square(y - activation).sum()/2.0
                
            self.list_of_errors.append(error)
            
            if(self.is_verbose):
                print("Epoch: {}, weights: {}, error {}".format(
                        e, self.w, error))
                
                
diag = pd.read_csv(r'/home/kamil/Documents/ML - Mobilo/Data/breast_cancer.csv')

X = diag[['area_mean', 'area_se', 'texture_mean', 'concavity_worst', 
          'concavity_mean']]
X

y = diag['diagnosis']
y = y.apply(lambda d:1 if d == 'M' else -1)      
y                

p = Perceptron(eta=0.00001, epochs=100)
p.fit(X, y)
plt.scatter(range(p.epochs), p.list_of_errors)

p = Perceptron(eta=0.001, epochs=100)
p.fit(X, y)
plt.scatter(range(p.epochs), p.list_of_errors)
                
p = Perceptron(eta=0.00000001, epochs=100)
p.fit(X, y)
plt.scatter(range(p.epochs), p.list_of_errors)
                
p = Perceptron(eta=0.000000001, epochs=100)
p.fit(X, y)
plt.scatter(range(p.epochs), p.list_of_errors)
                
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(X)
X_std = scaler.transform(X)
                
p = Perceptron(eta=0.01, epochs=100)
p.fit(X_std, y)
plt.scatter(range(p.epochs), p.list_of_errors)

p = Perceptron(eta=0.001, epochs=100)
p.fit(X_std, y)
plt.scatter(range(p.epochs), p.list_of_errors)

p = Perceptron(eta=0.000000001, epochs=100)
p.fit(X_std, y)
plt.scatter(range(p.epochs), p.list_of_errors)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_std, y, test_size=0.2)

p = Perceptron(eta=0.001, epochs=100)
p.fit(X_train, y_train)
plt.scatter(range(p.epochs), p.list_of_errors)

y_pred = p.predict(X_test)

good = y_test[y_test == y_pred].count()
total = y_test.count()
print('result: {}'.format(100*good/total))























