#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 10:52:55 2021

@author: kamil
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv(r"/home/kamil/Documents/ML - Mobilo/Data/Airbnb listings in Ottawa (May 2016).csv")
df.shape
df.head()

coordinates = df.loc[:,['longitude','latitude']]
coordinates.shape

plt.scatter(df.loc[:,'longitude'], df.loc[:,'latitude'])

# losujemy centroidy, dzielimy na grupy obliczajac odleglosc i wybierajac grupę
# tego bliżej, robimy to tak długo jak trzeba.
# Dla każdego centrum można obliczyc sume odleglosci punktow ktore zostaly do niego przypisane
# suma kwadratow odległości podzielona przez ilosc punktow
# within-cluster-sum-of-squares

WCSS = []
# obliczanie wcss dla racjonalnej liczby klastrow (1-15)
for k in range(1, 15):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(coordinates)
    WCSS.append(kmeans.inertia_)
    
plt.plot(range(1,15),WCSS)
plt.xlabel("Number of K Value(Cluster)")
plt.ylabel("WCSS")
plt.grid()
plt.show()

# wybrana liczba klastrów = 5, wartość ta znajduje się w punkcie przegięcia wykresu

kmeans = KMeans(n_clusters = 4, max_iter=300, random_state=1)
clusters = kmeans.fit_predict(coordinates)
# tablica-dla kazdej probki numer klastra do ktorego zostala zakwalifikowana
labels = kmeans.labels_
# centralne punkty kazdego klastra
centroids = kmeans.cluster_centers_


# dokladnosc
h = 0.001
# granice fragmentu plaszczyzny
x_min, x_max = coordinates['longitude'].min(), coordinates['longitude'].max()
y_min, y_max = coordinates['latitude'].min(), coordinates['latitude'].max()
# macierz wszystkich punktow wykresu
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
# wynik predykcji dla wszystkich punktow z calej plaszczyzny (xx,yy)
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

plt.figure(1, figsize=(10, 4))
plt.clf()
Z = Z.reshape(xx.shape)
# rysowanie granic decyzyjnych
plt.imshow(Z, interpolation='nearest',
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap = plt.cm.Pastel1,
           origin='lower')

plt.scatter(x=coordinates['longitude'], 
            y=coordinates['latitude'],
            c=labels, 
            s=100)

plt.scatter(x=centroids[:,0],
            y=centroids[:,1],
            s=300,
            c='red')

plt.ylabel('Long(y)'), plt.xlabel('Lat(x)')
plt.grid()
plt.title("Clustering")
plt.show()
