#Marion McGowan 
#Distribution of four data sets: Sepal Length, Sepal Width, Petal Length and Petal Width

import numpy as np
import matplotlib.pyplot as pl
data = np.genfromtxt('data/iris-data.csv', delimiter=',')
firstcol = data[:,0]
seccol =  data[:,1]
thirdcol= data[:,2]
fourcol= data[:,3]


pl.hist(data[:,0], edgecolor='k', linewidth=1.2, color ='salmon')
pl.title('Sepal Length')
pl.xlabel('Length in cm')
pl.ylabel('Number')
pl.show()

pl.hist(data[:,1], edgecolor='k', linewidth=1.2, color ='salmon')
pl.title('Sepal Width')
pl.xlabel('Length in cm')
pl.ylabel('Number')
pl.show()

pl.hist(data[:,2], edgecolor='k', linewidth=1.2, color ='salmon')
pl.title('Petal Length')
pl.xlabel('Length in cm')
pl.ylabel('Number')
pl.show()

pl.hist(data[:,3], edgecolor='k', linewidth=1.2, color ='salmon')
pl.title('Petal Width')
pl.xlabel('Length in cm')
pl.ylabel('Number')
pl.show()

#Now taking the same distributions, I want to graph them along the same interval of the xaxis
pl.hist(data[:,0], edgecolor='k', linewidth=1.2, color ='salmon')
pl.title('Sepal Length')
pl.xlabel('Length in cm')
pl.ylabel('Number')
pl.xticks([0,2, 4,6, 8, 10])
pl.show()


pl.hist(data[:,1], edgecolor='k', linewidth=1.2, color ='salmon')
pl.title('Sepal Width')
pl.xlabel('Length in cm')
pl.ylabel('Number')
pl.xticks([0,2, 4,6, 8, 10])
pl.show()

pl.hist(data[:,2], edgecolor='k', linewidth=1.2, color ='salmon')
pl.title('Petal Length')
pl.xlabel('Length in cm')
pl.ylabel('Number')
pl.xticks([0,2, 4,6, 8, 10])
pl.show()

pl.hist(data[:,3], edgecolor='k', linewidth=1.2, color ='salmon')
pl.title('Petal Width')
pl.xlabel('Length in cm')
pl.ylabel('Number')
pl.xticks([0,2, 4,6, 8, 10])
pl.show()

#Refered to this webpage: 
#https://stackoverflow.com/questions/42741687/python-histogram-outline