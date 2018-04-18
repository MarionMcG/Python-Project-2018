#Marion McGowan, 18/04/2018
#Comparison of Species using subplots

#For this task, I copied and pasted my iris data into 2 seperate csv files, one for each species.
# I hope to find a more efficient way of performing this task in the future.

import numpy as np
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
import matplotlib.pyplot as pl

f, ((ax1, ax2, ax3)) = pl.subplots(3, 1, sharex='all', sharey='all')
ax1.scatter(set1,set2, color='r', s =10)
ax2.scatter(virg1,virg2, color='g', s = 10)
ax3.scatter(vers1,vers2, color='b', s=10)
ax1.set_title('Sepal Length vs. Width')
pl.show()

f, ((ax1, ax2, ax3)) = pl.subplots(3, 1, sharex='all', sharey='all')
ax1.scatter(set1,set3, color='r', s =10)
ax2.scatter(virg1,virg3, color='g', s = 10)
ax3.scatter(vers1,vers3, color='b', s=10)
ax1.set_title('Sepal Length vs. Petal Length')
pl.show()

f, ((ax1, ax2, ax3)) = pl.subplots(3, 1, sharex='all', sharey='all')
ax1.scatter(set1,set4, color='r', s =10)
ax2.scatter(virg1,virg4, color='g', s = 10)
ax3.scatter(vers1,vers4, color='b', s=10)
ax1.set_title('Sepal Length vs. Petal Width')
pl.show()

f, ((ax1, ax2, ax3)) = pl.subplots(3, 1, sharex='all', sharey='all')
ax1.scatter(set3,set4, color='r', s =10)
ax2.scatter(virg3,virg4, color='g', s = 10)
ax3.scatter(vers3,vers4, color='b', s=10)
ax1.set_title('Petal Length vs. Width')
pl.show()
