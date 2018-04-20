#Marion McGowan, 16/04/2018
#Graphical Analysis of Iris Dataset

#This program graphs Sepal Length against Sepal Wisth, and Petal Length against Petal Width, 
# calculating the Correlation Coefficient for both.
#It also graphs Sepal Length against the Petal Length and Sepal Width against Petal Width,
# calculating the Correlation Coefficient for both.

import numpy as np
import matplotlib.pyplot as pl


data = np.genfromtxt('data/iris-data.csv', delimiter=',')
firstcol = data[:,0]
seccol =  data[:,1]
thirdcol= data[:,2]
fourcol= data[:,3]

#Finding the Correlation Coefficent
Corr12 = np.corrcoef(firstcol, seccol) [0, 1]
a= "{0:.4f}".format(round(Corr12, 4))
print("The correlation coefficient for Sepal Length and Sepal Width is ", a) 

Corr34 = np.corrcoef(thirdcol, fourcol) [0, 1]
b= "{0:.4f}".format(round(Corr34, 4))
print("The correlation coefficient for Petal Length and Petal Width is ", b)

Widthcorr = np.corrcoef(firstcol, thirdcol) [0, 1]
c= "{0:.4f}".format(round(Widthcorr, 4))
print("The correlation coefficient for Sepal Width and Petal Width is ", c)

Lengthcorr = np.corrcoef(seccol, fourcol) [0, 1]
d= "{0:.4f}".format(round(Lengthcorr, 4))
print("The correlation coefficient for Sepal Length and Petal Length is ", d)

#Plotting the scatter diagrams with their lines of best fit will show us a graphical representation of correlation
pl.scatter(firstcol, seccol, s = 10, color = 'dimgrey', marker='8')
pl.title('Sepal Length vs. Sepal Width')
pl.xlabel('Sepal Length')
pl.ylabel('Sepal Width')
pl.plot(np.unique(firstcol), np.poly1d(np.polyfit(firstcol, seccol, 1))(np.unique(firstcol)), color = 'salmon')
#Code from https://stackoverflow.com/questions/22239691/code-for-line-of-best-fit-of-a-scatter-plot-in-python
pl.yticks([0, 0.5, 1, 1.5,  2, 2.5, 3, 3.5, 4, 4.5])
pl.xticks([0, 1, 2, 3,  4, 5, 6, 7])
pl.show()

pl.scatter(firstcol, thirdcol, s = 10, color='dimgrey', marker = '8')
pl.title('Sepal Length vs.Petal Length')
pl.xlabel('Sepal Length')
pl.ylabel('Petal Length')
pl.plot(np.unique(firstcol), np.poly1d(np.polyfit(firstcol, thirdcol, 1))(np.unique(firstcol)), color = 'salmon')
pl.xticks([0, 1, 2, 3,  4, 5, 6, 7, 8])
pl.yticks([0, 1, 2, 3,  4, 5, 6, 7, 8])
pl.show()

pl.scatter(seccol, fourcol, s = 10, color = 'dimgrey', marker = '8')
pl.title('Sepal Width vs.Petal Width')
pl.xlabel('Sepal Width')
pl.ylabel('Petal Width')
pl.plot(np.unique(seccol), np.poly1d(np.polyfit(seccol, fourcol, 1))(np.unique(seccol)), color = 'salmon')
pl.xticks([0, 0.5, 1, 1.5,  2, 2.5, 3, 3.5, 4, 4.5])
pl.show()

pl.scatter(thirdcol,fourcol, s=10, color='dimgrey', marker = '8')
pl.title('Petal Length vs. Petal Width')
pl.xlabel('Petal Length')
pl.ylabel('Petal Width')
pl.plot(np.unique(thirdcol), np.poly1d(np.polyfit(thirdcol, fourcol, 1))(np.unique(thirdcol)), color = 'salmon')
pl.xticks([0, 1, 2, 3,  4, 5, 6, 7])
pl.show()
#Referred to the following Youtube videos when customising my scatter diagrams
#https://www.youtube.com/watch?v=WbTOutpwPHs

#Refered to Mathplotlibs named colors list and markers list
#https://matplotlib.org/examples/color/named_colors.html
#http://sparkandshine.net/en/draw-with-matplotlib-colors-markers-and-line-styles/
