#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 09:22:33 2021

@author: kamil
"""

import numpy as np

a = np.arange(20)
a

a.shape

a[0]
a[3]

a = a.reshape(2,10)
a.shape
a

a[0]
a[3]
a[0][3]

a = a.reshape(2,5,2)

a.shape
a

a[0]
a[0][3]
a[0][3][1]

b = np.arange(0,40,2).reshape(4,5)
b

# a_python_list =  [2**x for x in range(10)]
c = [2**x for x in range(10)]

zero_array = np.zeros(10)
one_array = np.ones(10)
empty_array = np.empty(100)
lucky_array = np.full((5,5),13)
diagonal_array = np.eye(5,5)
random_array = np.random.random(10)
linspace_array = np.linspace(100,200,5)
