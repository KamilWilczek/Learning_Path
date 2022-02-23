#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 13:05:07 2021

@author: kamil
"""

import numpy as np

X = np.arange(-25, 25).reshape(10, 5)

ones = np.ones(X.shape)

X_1 = np.append(X, ones, axis=1)

w = np.random.rand(X_1.shape[1])

def predict(x, w):
    total_simulation = np.dot(x, w)
    y_pred = 1 if total_simulation > 0 else -1
    return y_pred

print(predict(X_1[0], w))

for x in X_1:
    y_pred = predict(x, w)
    print(y_pred)