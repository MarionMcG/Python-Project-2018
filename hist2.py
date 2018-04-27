#Marion McGowan, 25/04/2018

import numpy as np
import matplotlib.pyplot as pl

data = np.genfromtxt('data/setosa.csv', delimiter=',')
set1= data[:,0]
set2 =  data[:,1]
set3= data[:,2]
set4= data[:,3]

data = np.genfromtxt('data/virginica.csv', delimiter=',')
virg1= data[:,0]
virg2 =  data[:,1]
virg3= data[:,2]
virg4= data[:,3]

data = np.genfromtxt('data/versicolor.csv', delimiter=',')
vers1= data[:,0]
vers2=data[:,1]
vers3= data[:,2]
vers4= data[:,3]


pl.subplot(311)
pl.title('Sepal Length')
pl.hist(set1, color='r',edgecolor='k', linewidth=0.2, label='Iris-Setosa')
pl.xticks([3, 4, 5, 6, 7])
pl.yticks([0, 5, 10, 15])
pl.subplot(312)
pl.hist(virg1, color='g',edgecolor='k', linewidth=0.2, label='Iris-Virginica')
pl.xticks([3, 4, 5, 6, 7])
pl.yticks([0, 5, 10, 15])
pl.subplot(313)
pl.hist(vers1, color='b',edgecolor='k', linewidth=0.2, label='Iris-Versicolor')
pl.xticks([3, 4, 5, 6, 7])
pl.yticks([0, 5, 10, 15])
pl.show()

pl.subplot(311)
pl.title('Sepal Width')
pl.hist(set2, color='r',edgecolor='k', linewidth=0.2, label='Iris-Setosa')
pl.xticks([1, 2, 3, 4, 5])
pl.yticks([0, 5, 10, 15])
pl.subplot(312)
pl.hist(virg2, color='g',edgecolor='k', linewidth=0.2, label='Iris-Virginica')
pl.xticks([ 1, 2, 3, 4, 5])
pl.yticks([0, 5, 10, 15])
pl.subplot(313)
pl.hist(vers2, color='b',edgecolor='k', linewidth=0.2, label='Iris-Versicolor')
pl.xticks([ 1, 2, 3, 4, 5])
pl.yticks([0, 5, 10, 15])
pl.show()

pl.subplot(311)
pl.title('Petal Length')
pl.hist(set3, color='r',edgecolor='k', linewidth=0.2, label='Iris-Setosa')
pl.xticks([0, 1, 2, 3, 4, 5, 6, 7])
pl.yticks([0, 5, 10, 15])
pl.subplot(312)
pl.hist(virg3, color='g',edgecolor='k', linewidth=0.2, label='Iris-Virginica')
pl.xticks([0, 1, 2, 3, 4, 5, 6, 7])
pl.yticks([0, 5, 10, 15])
pl.subplot(313)
pl.hist(vers3, color='b',edgecolor='k', linewidth=0.2, label='Iris-Versicolor')
pl.xticks([0, 1, 2, 3, 4, 5, 6, 7])
pl.yticks([0, 5, 10, 15])
pl.show()

pl.subplot(311)
pl.title('Petal Width')
pl.hist(set4, color='r',edgecolor='k', linewidth=0.2, label='Iris-Setosa')
pl.xticks([0, 1, 2, 3])
pl.yticks([0, 10, 20, 30])
pl.subplot(312)
pl.hist(virg4, color='g',edgecolor='k', linewidth=0.2, label='Iris-Virginica')
pl.xticks([0, 1, 2, 3])
pl.yticks([0, 10, 20, 30])
pl.subplot(313)
pl.hist(vers4, color='b',edgecolor='k', linewidth=0.2, label='Iris-Versicolor')
pl.xticks([0, 1, 2, 3])
pl.yticks([0, 10, 20, 30])
pl.show()
