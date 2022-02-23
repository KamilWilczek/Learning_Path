#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 10:35:08 2021

@author: kamil
"""

import numpy as np

arr = np.arange(5,29,2)

boolArr = arr < 10

newArr = arr[boolArr]
newArr1 = arr[arr<20]
newArr2 = arr[arr % 3 == 0]
newArr3 = arr[(arr > 10) & (arr < 20)]

arr = np.arange(24).reshape(4,6)
arr[1]
arr[1][2]
arr[1][2:4]
arr[1][2:5]
arr[1][:]
arr[:][2]
arr[0:3][2]
arr[:3][2]
arr[:3][2:4]
arr[:][-1]
arr[:][:-1]

arr = np.arange(50).reshape(10,5)
split_level = 0.2
num_rows = arr.shape[0]
split_border = split_level * num_rows
arr[:round(split_border)][:]
arr[round(split_border):][:]
np.random.shuffle(arr)
arr[:round(split_border)][:]
arr[round(split_border):][:]

data = np.arange(500).reshape(100,5)
np.random.shuffle(data)
split_level = 0.2
num_rows = data.shape[0]
split_border = split_level * num_rows
X_train = data[round(split_border):,:-1]
X_test  = data[:round(split_border),:-1]
y_train = data[round(split_border):,-1]
y_test  = data[:round(split_border),-1]

data.shape
X_train.shape
X_test.shape
y_train.shape
y_test.shape

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        data[:, :-1], data[:, -1], test_size=0.2, shuffle = True)

X_train.shape
X_test.shape
y_train.shape
y_test.shape
