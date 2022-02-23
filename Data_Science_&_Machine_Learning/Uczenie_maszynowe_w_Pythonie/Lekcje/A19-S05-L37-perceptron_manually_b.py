#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 12:44:38 2021

@author: kamil
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.array([2., 7., 8., 10.])
zeros = np.zeros(data.shape[0])

plt.figure(figsize=(10,2))
plt.scatter(x = data, y=zeros, marker='o', s=50, c='b')
plt.scatter(x = [data.mean()], y=0, marker='d', s=100, c='r')
plt.scatter(x = [data.mean() - data.std(), data.mean() + data.std()],
            y = [0,0], marker ='s', s=70, c='y', alpha=0.5)

mean = data.mean()
data_stand = data - mean
data_stand

plt.figure(figsize=(10,2))
plt.scatter(x = data_stand, y=zeros, marker='o', s=50, c='b')
plt.scatter(x = [data_stand.mean()], y=0, marker='d', s=100, c='r')
plt.scatter(x = [data_stand.mean() - data_stand.std(), 
                 data_stand.mean() + data_stand.std()],
            y = [0,0], marker ='s', s=70, c='y', alpha=0.5)

std = data.std()
data_stand = data_stand / std
data_stand

plt.figure(figsize=(10,2))
plt.scatter(x = data_stand, y=zeros, marker='o', s=50, c='b')
plt.scatter(x = [data_stand.mean()], y=0, marker='d', s=100, c='r')
plt.scatter(x = [data_stand.mean() - data_stand.std(), 
                 data_stand.mean() + data_stand.std()],
            y = [0,0], marker ='s', s=70, c='y', alpha=0.5)