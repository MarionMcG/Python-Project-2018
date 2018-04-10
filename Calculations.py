#Marion McGowan

#Statistical analysis of Iris Dataset 1 
#Measures of Central Tendency and Spread

import numpy as np
#Referred to numpy references to perform many of these calculations
#https://docs.scipy.org/doc/numpy-1.12.0/reference/routines.statistics.html


data=np.genfromtxt('data/iris-data.csv', delimiter=',')

print()
first = data[:,0]
print("Results for Sepal Length Data")
firstmin=np.min(data[:,0])
firstmax=np.max(data[:,0])
firstmean=np.mean(data[:,0])
firstmed=np.median(data[:,0])
firstsd = np.std(data[:,0])
print("Minimum Value: ", firstmin)
print("Maximum Value: ", firstmax)
print ("Mean:","{0:.4f}".format(round(firstmean,4)))
#Refered to this site when rounding to 4dps
#https://www.quora.com/In-Python-how-can-I-round-a-float-off-at-two-decimal-places
print ("Median: ", firstmed)
print ("Standard Deviation: ","{0:.4f}".format(round(firstsd,4)))
print()

print("Results for Sepal Width Data")
secmean=np.mean(data[:,1])
secmed=np.median(data[:,1])
secsd = np.std(data[:,1])
print ("Mean:","{0:.4f}".format(round(secmean,4)))
print("Median:", secmed)
print ("Standard Deviation: ","{0:.4f}".format(round(secsd,4)))
print()

print("Results for Petal Length Data")
thirdmean=np.mean(data[:,2])
thirdmed=np.median(data[:,2])
thirdsd = np.std(data[:,2])
print ("Mean:","{0:.4f}".format(round(thirdmean,4)))
print("Median:", thirdmed)
print ("Standard Deviation: ","{0:.4f}".format(round(thirdsd,4)))
print()

print("Results for Petal Width Data")
fourmean=np.mean(data[:,3])
fourmed=np.median(data[:,3])
foursd = np.std(data[:,3])
print ("Mean:","{0:.4f}".format(round(fourmean,4)))
print("Median:", fourmed)
print ("Standard Deviation: ","{0:.4f}".format(round(foursd,4)))
print()