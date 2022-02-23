#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 14:36:39 2021

@author: kamil
"""

import numpy as np

rand_a = np.random.rand()
rand_a

rand_a = np.random.rand(2,5)
rand_a

rand_b = np.random.rand(1,5)

rand_b = rand_b * 100

rand_c = np.vstack((rand_a, rand_b))

rand_b = np.random.rand(2,1)

rand_c = np.hstack((rand_a, rand_b))

X = rand_c[:,1]

a = 3
b = 8

y = a * X + b

X = np.random.randint(0, 10, size=10)

X = X * 10

Z = np.random.choice(10, size=3, replace=False)

W = np.random.choice(X, size=3, replace=True)

idx = np.random.choice(X.shape[0], size=3, replace=False)
print(X)
print(idx)
print(X[idx])

X.shape[0]
X.shape
