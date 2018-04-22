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
pl.plot(np.unique(firstcol), np.poly1d(np.polyfit(firstcol, seccol, 1))(np.unique(firstcol)), color = 'salmon')
#Code from https://stackoverflow.com/questions/22239691/code-for-line-of-best-fit-of-a-scatter-plot-in-python
#Determining Correlations, calculating r value, r squared, m(slope) and p value
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(firstcol, seccol)
print ("Slope: " + str(np.round(slope, 4)))
print ("Correlation Coefficient: "+ str(np.round(r_value, 4)))
y=np.round((r_value**2), 4)
print ("R-squared Value: " + str(y))
print ("P Value: " + str(p_value))
z=np.round((p_value), 10)
print ("Rounded P Value: " + str(z))
#https://stackoverflow.com/questions/24130922/how-to-print-equation-of-line-using-scipy-stats
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
pl.plot(np.unique(thirdcol), np.poly1d(np.polyfit(thirdcol, fourcol, 1))(np.unique(thirdcol)), color = 'salmon')
#Determining Correlations: calculating r value, r squared, m(slope) and p value
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(thirdcol, fourcol)
print ("Slope: " + str(np.round(slope, 4)))
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
pl.plot(np.unique(seccol), np.poly1d(np.polyfit(seccol, fourcol, 1))(np.unique(seccol)), color = 'salmon')
#Determining Correlations: calculating r value, r squared, m(slope) and p value
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(seccol, fourcol)
print ("Slope: " + str(np.round(slope, 4)))
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
pl.plot(np.unique(firstcol), np.poly1d(np.polyfit(firstcol, thirdcol, 1))(np.unique(firstcol)), color = 'salmon')
#Determining Correlations: calculating r value, r squared, m(slope) and p value
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(firstcol, thirdcol)
print ("Slope: " + str(np.round(slope, 4)))
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
pl.plot(np.unique(firstcol), np.poly1d(np.polyfit(firstcol, fourcol, 1))(np.unique(firstcol)), color = 'salmon')
#Determining Correlations: calculating r value, r squared, m(slope) and p value
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(firstcol, fourcol)
print ("Slope: " + str(np.round(slope, 4)))
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
#Plotting the line of best fit
pl.plot(np.unique(seccol), np.poly1d(np.polyfit(seccol, thirdcol, 1))(np.unique(seccol)), color = 'salmon')
#Determining Correlations: calculating r value, r squared, m(slope) and p value
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(seccol, thirdcol)
print ("Slope: " + str(np.round(slope, 4)))
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
