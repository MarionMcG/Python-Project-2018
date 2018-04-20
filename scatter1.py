#Marion McGowan, 16/04/2018
#Graphical Analysis of Iris Dataset

#This program geaphs measurements against one another on a scatter graph. 
#There are six graphs in totalagainst the Petal Length and Sepal.
#The Correlation Co-eff is calculated for each graph.

import numpy as np
import matplotlib.pyplot as pl


data = np.genfromtxt('data/iris-data.csv', delimiter=',')
firstcol = data[:,0]
seccol =  data[:,1]
thirdcol= data[:,2]
fourcol= data[:,3]

#Finding the Correlation Coefficent
corr1 = np.corrcoef(firstcol, seccol) [0, 1]
a= "{0:.4f}".format(round(corr1, 4))
print("The correlation coefficient for Sepal Length and Sepal Width is ", a) 

corr2 = np.corrcoef(thirdcol, fourcol) [0, 1]
b= "{0:.4f}".format(round(corr2, 4))
print("The correlation coefficient for Petal Length and Petal Width is ", b)

corr3 = np.corrcoef(seccol, fourcol) [0, 1]
c= "{0:.4f}".format(round(corr3, 4))
print("The correlation coefficient for Sepal Width and Petal Width is ", c)

corr4 = np.corrcoef(firstcol, thirdcol) [0, 1]
d= "{0:.4f}".format(round(corr4, 4))
print("The correlation coefficient for Sepal Length and Petal Length is ", d)

corr5 = np.corrcoef(firstcol, fourcol) [0, 1]
e= "{0:.4f}".format(round(corr5, 4))
print("The correlation coefficient for Sepal Length and Petal Width is ", e)

corr6 = np.corrcoef(seccol, thirdcol) [0, 1]
f= "{0:.4f}".format(round(corr6, 4))
print("The correlation coefficient for Sepal Width and Petal Length is ", f)



#Plotting the scatter diagrams with their lines of best fit will show us a graphical representation of correlation
pl.scatter(firstcol, seccol, s = 20, color = 'dimgrey', marker='8')
pl.title('Sepal Length vs. Sepal Width')
pl.xlabel('Sepal Length')
pl.ylabel('Sepal Width')
pl.plot(np.unique(firstcol), np.poly1d(np.polyfit(firstcol, seccol, 1))(np.unique(firstcol)), color = 'salmon')
#Code from https://stackoverflow.com/questions/22239691/code-for-line-of-best-fit-of-a-scatter-plot-in-python
pl.yticks([0, 0.5, 1, 1.5,  2, 2.5, 3, 3.5, 4, 4.5])
pl.xticks([0, 1, 2, 3,  4, 5, 6, 7])
pl.show()

pl.scatter(thirdcol,fourcol, s=20, color='dimgrey', marker = '8')
pl.title('Petal Length vs. Petal Width')
pl.xlabel('Petal Length')
pl.ylabel('Petal Width')
pl.plot(np.unique(thirdcol), np.poly1d(np.polyfit(thirdcol, fourcol, 1))(np.unique(thirdcol)), color = 'salmon')
pl.xticks([0, 1, 2, 3,  4, 5, 6, 7])
pl.show()

pl.scatter(seccol, fourcol, s = 20, color = 'dimgrey', marker = '8')
pl.title('Sepal Width vs.Petal Width')
pl.xlabel('Sepal Width')
pl.ylabel('Petal Width')
pl.plot(np.unique(seccol), np.poly1d(np.polyfit(seccol, fourcol, 1))(np.unique(seccol)), color = 'salmon')
pl.xticks([0, 0.5, 1, 1.5,  2, 2.5, 3, 3.5, 4, 4.5])
pl.show()

pl.scatter(firstcol, thirdcol, s = 20, color='dimgrey', marker = '8')
pl.title('Sepal Length vs.Petal Length')
pl.xlabel('Sepal Length')
pl.ylabel('Petal Length')
pl.plot(np.unique(firstcol), np.poly1d(np.polyfit(firstcol, thirdcol, 1))(np.unique(firstcol)), color = 'salmon')
pl.xticks([0, 1, 2, 3,  4, 5, 6, 7, 8])
pl.yticks([0, 1, 2, 3,  4, 5, 6, 7, 8])
pl.show()

pl.scatter(firstcol, fourcol, s = 20, color='dimgrey', marker = '8')
pl.title('Sepal Length vs.Petal Width')
pl.xlabel('Sepal Length')
pl.ylabel('Petal Width')
pl.plot(np.unique(firstcol), np.poly1d(np.polyfit(firstcol, fourcol, 1))(np.unique(firstcol)), color = 'salmon')
pl.xticks([0, 1, 2, 3,  4, 5, 6, 7, 8])
pl.yticks([0, 1, 2, 3,  4, 5, 6, 7, 8])
pl.show()

pl.scatter(seccol, thirdcol, s = 20, color='dimgrey', marker = '8')
pl.title('Sepal Width vs.Petal Length')
pl.xlabel('Sepal Width')
pl.ylabel('Petal Length')
pl.plot(np.unique(seccol), np.poly1d(np.polyfit(seccol, thirdcol, 1))(np.unique(seccol)), color = 'salmon')
pl.xticks([0, 1, 2, 3,  4, 5, 6, 7, 8])
pl.yticks([0, 1, 2, 3,  4, 5, 6, 7, 8])
pl.show()

#Referred to the following Youtube videos when customising my scatter diagrams
#https://www.youtube.com/watch?v=WbTOutpwPHs

#Refered to Mathplotlibs named colors list and markers list
#https://matplotlib.org/examples/color/named_colors.html
#http://sparkandshine.net/en/draw-with-matplotlib-colors-markers-and-line-styles/
