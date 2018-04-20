#Marion McGowan, 18/04/2018
#Comparison of Species using subplots

#For this task, I copied and pasted my iris data into 3 seperate csv files, one for each species.
#I hope to find a more efficient way of performing this task in the future. 
#UPDATED (20/04/2018): To better compare across species I plotted all 3 subplots on 1 coordinate graph.
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

#Refered to the following webpages to learn about how to use subplots:
#https://stackoverflow.com/questions/33713034/plotting-multiple-graph-from-a-csv-file-and-output-to-a-single-pdf-svg
#https://matplotlib.org/examples/pylab_examples/subplots_demo.html

f, ax=pl.subplots(1)
ax.scatter(set1,set2, color='r', s =20, label='Iris-Setosa')
ax.scatter(virg1,virg2, color='g', s = 20, label='Iris-Virginica')
ax.scatter(vers1,vers2, color='b', s=20, label='Iris-Versicolor')
ax.set_title('Sepal Length vs. Sepal Width')
f.text(0.5, 0.02, 'Sepal Length', ha='center')
f.text(0.03, 0.5, 'Sepal Width', va='center', rotation='vertical')
#Refered to https://stackoverflow.com/questions/16150819/common-xlabel-ylabel-for-matplotlib-subplots
f.legend(loc=1, fontsize='small', shadow=True)
#Refered to https://matplotlib.org/api/legend_api.html
pl.show()

f, ax=pl.subplots(1)
ax.scatter(set1,set3, color='r', s =20, label='Iris-Setosa')
ax.scatter(virg1,virg3, color='g', s = 20, label='Iris-Virginica')
ax.scatter(vers1,vers3, color='b', s=20, label='Iris-Versicolor')
ax.set_title('Sepal Length vs. Petal Length')
f.text(0.5, 0.02, 'Sepal Length', ha='center')
f.text(0.03, 0.5, 'Petal Length', va='center', rotation='vertical')
f.legend(loc=1, fontsize='small', shadow=True)
pl.show()

f, ax=pl.subplots(1)
ax.scatter(set1,set4, color='r', s =20, label='Iris-Setosa')
ax.scatter(virg1,virg4, color='g', s = 20, label='Iris-Virginica')
ax.scatter(vers1,vers4, color='b', s=20, label='Iris-Versicolor')
ax.set_title('Sepal Length vs. Petal Width')
f.text(0.5, 0.02, 'Sepal Length', ha='center')
f.text(0.03, 0.5, 'Petal Width', va='center', rotation='vertical')
f.legend(loc=1, fontsize='small', shadow=True)
pl.show()

f, ax=pl.subplots(1)
ax.scatter(set3,set4, color='r', s =20, label='Iris-Setosa')
ax.scatter(virg3,virg4, color='g', s = 20, label='Iris-Virginica')
ax.scatter(vers3,vers4, color='b', s=20, label='Iris-Versicolor')
ax.set_title('Petal Length vs. Petal Width')
f.text(0.5, 0.02, 'Petal Length', ha='center')
f.text(0.03, 0.5, 'Petal Width', va='center', rotation='vertical')
f.legend(loc=1, fontsize='small', shadow=True)

pl.show()


