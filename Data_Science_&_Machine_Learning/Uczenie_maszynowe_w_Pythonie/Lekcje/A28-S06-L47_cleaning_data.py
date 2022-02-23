#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 09:07:47 2021

@author: kamil
"""

import numpy as np
import pandas as pd


diam_org = pd.read_csv(r'/home/kamil/Documents/ML - Mobilo/Data/diamonds.csv', 
                       usecols=['color', 'price'])
diam = diam_org.copy()
diam.head()


diam_mean_original = diam.groupby(by='color').mean()


import random
missing_data = random.sample(range(0, diam.shape[0]), 5)
diam.loc[missing_data]
diam.loc[missing_data, 'price'] = np.NAN
diam.loc[missing_data]


diam_mean_start = diam.groupby(by='color').mean()
diam_mean_original
diam_mean_start
diam_mean_original - diam_mean_start


filter_nan = diam['price'].isnull()
diam.loc[filter_nan, ]
diam.loc[filter_nan, 'color'].map(diam_mean_start['price'])
diam.loc[filter_nan, 'price'] = diam.loc[filter_nan, 'color'].map(diam_mean_start['price'])
diam.loc[filter_nan, 'price']


diam_mean_repair = diam.groupby(by = 'color').mean()
diam_mean_start - diam_mean_repair
diam_mean_original - diam_mean_start
diam_mean_original - diam_mean_repair


diam2= diam_org.copy()
mean_price = diam2['price'].mean()
diam2.loc[missing_data, 'price'] = np.NaN
diam_mean_start2 = diam2.groupby(by = 'color').mean()
filter_nan2 = diam2['price'].isnull()
diam2.loc[filter_nan2, 'price'] = mean_price
diam_mean_repair2 = diam2.groupby(by = 'color').mean()
 

diam_mean_original - diam_mean_start
diam_mean_start2 - diam_mean_repair2
diam_mean_original - diam_mean_start2
diam_mean_original - diam_mean_repair2