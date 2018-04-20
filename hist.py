#Marion McGowan, 18/04/2017
#Distribution of four data sets: Sepal Length, Sepal Width, Petal Length and Petal Width

import numpy as np
import matplotlib.pyplot as pl
data = np.genfromtxt('data/iris-data.csv', delimiter=',')
firstcol = data[:,0]
seccol =  data[:,1]
thirdcol= data[:,2]
fourcol= data[:,3]

#Graphing each measurement as a histogram to get an indication of their distribution
pl.hist(data[:,0], edgecolor='k', linewidth=1.2, color ='lightcoral')
#Refered to this webpage to get a border line around the bars of the histogram.
#https://stackoverflow.com/questions/42741687/python-histogram-outline
pl.title('Sepal Length', fontsize = '20')
pl.xlabel('Length in cm')
pl.ylabel('Number')
pl.show()

pl.hist(data[:,1], edgecolor='k', linewidth=1.2, color ='gold')
pl.title('Sepal Width',  fontsize = '20')
pl.xlabel('Length in cm')
pl.ylabel('Number')
pl.show()

pl.hist(data[:,2], edgecolor='k', linewidth=1.2, color ='lightgreen')
pl.title('Petal Length',  fontsize = '20')
pl.xlabel('Length in cm')
pl.ylabel('Number')
pl.show()

pl.hist(data[:,3], edgecolor='k', linewidth=1.2, color ='lightskyblue')
pl.title('Petal Width',  fontsize = '20')
pl.xlabel('Length in cm')
pl.ylabel('Number')
pl.show()

#Taking the same distributions, I willnow graph them along the same interval of the xaxis
#This will give us a better idea of how their distributions compare to one another
pl.hist(data[:,0], edgecolor='k', linewidth=1.2, color ='lightcoral')

pl.title('Sepal Length',  fontsize = '20')
pl.xlabel('Length in cm')
pl.ylabel('Number')
pl.xticks([0,2, 4,6, 8, 10])
pl.show()


pl.hist(data[:,1], edgecolor='k', linewidth=1.2, color ='gold')
pl.title('Sepal Width',  fontsize = '20')
pl.xlabel('Length in cm')
pl.ylabel('Number')
pl.xticks([0,2, 4,6, 8, 10])
pl.show()

pl.hist(data[:,2], edgecolor='k', linewidth=1.2, color ='lightgreen')
pl.title('Petal Length',  fontsize = '20')
pl.xlabel('Length in cm')
pl.ylabel('Number')
pl.xticks([0,2, 4,6, 8, 10])
pl.show()

pl.hist(data[:,3], edgecolor='k', linewidth=1.2, color ='lightskyblue')
pl.title('Petal Width',  fontsize = '20')
pl.xlabel('Length in cm')
pl.ylabel('Number')
pl.xticks([0,2, 4,6, 8, 10])
pl.show()