#Marion McGowan, 16/04/2018
#Graphical Analysis of Iris Dataset

#This program geaphs measurements against one another on a scatter graph. 
#There are six graphs in totalagainst the Petal Length and Sepal.
#The correlation coefficient, r^2 value, p value and slope of line of best fit are found for each. 

import numpy as np
import matplotlib.pyplot as pl
import scipy.stats as stats

data = np.genfromtxt('data/iris-data.csv', delimiter=',')
firstcol = data[:,0]
seccol =  data[:,1]
thirdcol= data[:,2]
fourcol= data[:,3]

print()

#Sepal Length vs.Sepal Width
print("Sepal Length vs. Sepal Width")
#Plotting the scatter diagrams 
pl.scatter(firstcol, seccol, s = 20, color = 'dimgrey', marker='8')
pl.title('Sepal Length vs. Sepal Width')
pl.xlabel('Sepal Length')
pl.ylabel('Sepal Width')
#Plotting the line of best fit
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(firstcol, seccol)
pl.plot(firstcol, intercept + slope*(firstcol), 'r')
#Determining Correlations, calculating r value, r squared, m(slope) and p value
print ("Slope: " + str(np.round(slope, 4)))
print ("Y-intercept:" + str(intercept))
print('y =','%.2f' %slope,' + ','%.2f' %intercept,' x')
print ("Correlation Coefficient: "+ str(np.round(r_value, 4)))
y=np.round((r_value**2), 4)
print ("R-squared Value: " + str(y))
print ("P Value: " + str(p_value))
z=np.round((p_value), 10)
print ("Rounded P Value: " + str(z))
#Referenes for Scipy.Stats
#I switched from numpy to scipy.stats, because coming from Maths background I find scipy.stats more intuitive.
#https://stackoverflow.com/questions/24130922/how-to-print-equation-of-line-using-scipy-stats]
#https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.linregress.html
pl.show()
print()

#Petal Length vs. Petal Width
print('Petal Length vs. Petal Width')
#Plotting the scatter diagram
pl.scatter(thirdcol,fourcol, s=20, color='dimgrey', marker = '8')
pl.title('Petal Length vs. Petal Width')
pl.xlabel('Petal Length')
pl.ylabel('Petal Width')
#Plotting the line of best fit
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(thirdcol, fourcol)
pl.plot(thirdcol, intercept + slope*(thirdcol), 'r')
#Determining Correlations: calculating r value, r squared, m(slope) and p value
print ("Slope: " + str(np.round(slope, 4)))
print ("Y-intercept:" + str(intercept))
print('y =','%.2f' %slope,' + ','%.2f' %intercept,' x')
print ("Correlation Coefficient: "+ str(np.round(r_value, 4)))
y=np.round((r_value**2), 4)
print ("R-squared Value: " + str(y))
print ("P Value: " + str(p_value))
z=np.round((p_value), 10)
print ("Rounded P Value: " + str(z))

pl.show()
print()

#Sepal Width vs. Petal Width
print('Sepal Width vs. Petal Width')
pl.scatter(seccol, fourcol, s = 20, color = 'dimgrey', marker = '8')
pl.title('Sepal Width vs.Petal Width')
pl.xlabel('Sepal Width')
pl.ylabel('Petal Width')
#Plotting the line of best fit
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(seccol, fourcol)
pl.plot(seccol, intercept + slope*(seccol), 'r')
#Determining Correlations: calculating r value, r squared, m(slope) and p value
print ("Slope: " + str(np.round(slope, 4)))
print ("Y-intercept:" + str(intercept))
print('y =','%.2f' %slope,' + ','%.2f' %intercept,' x')
print ("Correlation Coefficient: "+ str(np.round(r_value, 4)))
y=np.round((r_value**2), 4)
print ("R-squared Value: " + str(y))
print ("P Value: " + str(p_value))
z=np.round((p_value), 10)
print ("Rounded P Value: " + str(z))
pl.show()
print()

#Sepal Length vs. Petal Length
print('Sepal Length vs. Petal Length')
pl.scatter(firstcol, thirdcol, s = 20, color='dimgrey', marker = '8')
pl.title('Sepal Length vs.Petal Length')
pl.xlabel('Sepal Length')
pl.ylabel('Petal Length')
#Plotting the line of best fit
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(firstcol, thirdcol)
pl.plot(firstcol, intercept + slope*(firstcol), 'r')
#Determining Correlations: calculating r value, r squared, m(slope) and p value
print ("Slope: " + str(np.round(slope, 4)))
print ("Y-intercept:" + str(intercept))
print('y =','%.2f' %slope,' + ','%.2f' %intercept,' x')
print ("Correlation Coefficient: "+ str(np.round(r_value, 4)))
y=np.round((r_value**2), 4)
print ("R-squared Value: " + str(y))
print ("P Value: " + str(p_value))
z=np.round((p_value), 10)
print ("Rounded P Value: " + str(z))
pl.show()
print()

#Sepal Length vs. Petal Width
print('Sepal Length vs. Petal Width')
pl.scatter(firstcol, fourcol, s = 20, color='dimgrey', marker = '8')
pl.title('Sepal Length vs.Petal Width')
pl.xlabel('Sepal Length')
pl.ylabel('Petal Width')
#Plotting the line of best fit
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(firstcol, fourcol)
pl.plot(firstcol, intercept + slope*(firstcol), 'r')
#Determining Correlations: calculating r value, r squared, m(slope) and p value
print ("Slope: " + str(np.round(slope, 4)))
print ("Y-intercept:" + str(intercept))
print('y =','%.2f' %slope,' + ','%.2f' %intercept,' x')
print ("Correlation Coefficient: "+ str(np.round(r_value, 4)))
y=np.round((r_value**2), 4)
print ("R-squared Value: " + str(y))
print ("P Value: " + str(p_value))
z=np.round((p_value), 10)
print ("Rounded P Value: " + str(z))
pl.show()
print()

#Sepal Width vs. Petal Length
print ('Sepal Width vs. Petal Length')
pl.scatter(seccol, thirdcol, s = 20, color='dimgrey', marker = '8')
pl.title('Sepal Width vs.Petal Length')
pl.xlabel('Sepal Width')
pl.ylabel('Petal Length')
#Plotting the line of best fit:
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(seccol, thirdcol)
pl.plot(seccol, intercept + slope*(seccol), 'r')
#Determining Correlations: calculating r value, r squared, m(slope) and p value
print ("Slope: " + str(np.round(slope, 4)))
print ("Y-intercept:" + str(intercept))
print('y =','%.2f' %slope,' + ','%.2f' %intercept,' x')
print ("Correlation Coefficient: "+ str(np.round(r_value, 4)))
y=np.round((r_value**2), 4)
print ("R-squared Value: " + str(y))
print ("P Value: " + str(p_value))
z=np.round((p_value), 10)
print ("Rounded P Value: " + str(z))
pl.show()
print()
#Referred to the following Youtube video when customising my scatter diagrams
#https://www.youtube.com/watch?v=WbTOutpwPHs
#Refered to Mathplotlibs named colors list and markers list
#https://matplotlib.org/examples/color/named_colors.html
#http://sparkandshine.net/en/draw-with-matplotlib-colors-markers-and-line-styles/
