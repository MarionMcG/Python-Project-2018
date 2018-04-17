#Marion McGowan, 10/04/2018

#Statistical analysis of Iris Dataset 1 
#Measures of Central Tendency and Spread
#Program to calculate mean, median, mode, range, interquartile range, 
#max, min, standard deviation and variance of data for four measurements
#in the Iris Dataset 
import time
start_time = time.time()
import numpy as np
#Referred to numpy references to perform many of these calculations
#https://docs.scipy.org/doc/numpy-1.12.0/reference/routines.statistics.html
import statistics as s
#Stackoverflow Reference:
#https://stackoverflow.com/questions/10797819/finding-the-mode-of-a-list?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

data=np.genfromtxt('data/iris-data.csv', delimiter=',')

print()
first = data[:,0]
print("Results for Sepal Length Data")
firstmin=np.min(data[:,0])
firstmax=np.max(data[:,0])
firstmean=np.mean(data[:,0])
firstmed=np.median(data[:,0])
firstmode=s.mode(data[:,0])
firstsd = np.std(data[:,0])
firstvar= np.var(data[:,0])
firstiqr=np.percentile(data[:,0],75) - np.percentile(data[:,0], 25)
#Refered to this site to calculate the IQR
#https://stackoverflow.com/questions/23228244/how-do-you-find-the-iqr-in-numpy
print("Minimum Value: ", firstmin)
print("Maximum Value: ", firstmax)
print("Range: ", firstmax - firstmin)
print("Interquartile Range: ", firstiqr)
print ("Mean:","{0:.4f}".format(round(firstmean,4)))
#Refered to this site when rounding to 4dps
#https://www.quora.com/In-Python-how-can-I-round-a-float-off-at-two-decimal-places
print ("Median: ", firstmed)
print("Mode: ", firstmode)
print ("Standard Deviation: ","{0:.4f}".format(round(firstsd,4)))
print("Variance: ","{0:.4f}".format(round(firstvar,4)))
print()

print("Results for Sepal Width Data")
secmin=np.min(data[:,1])
secmax=np.max(data[:,1])
secmean=np.mean(data[:,1])
secmed=np.median(data[:,1])
secmode=s.mode(data[:,1])
secsd = np.std(data[:,1])
secvar= np.var(data[:,1])
seciqr=np.percentile(data[:,1],75) - np.percentile(data[:,1], 25)
print("Minimum Value: ", secmin)
print("Maximum Value: ", secmax)
print("Range: ", secmax - secmin)
print("Interquartile Range: ", seciqr)
print ("Mean:","{0:.4f}".format(round(secmean,4)))
print("Median:", secmed)
print("Mode: ", secmode)
print ("Standard Deviation: ","{0:.4f}".format(round(secsd,4)))
print("Variance: ","{0:.4f}".format(round(secvar,4)))
print()

print("Results for Petal Length Data")
thirdmin=np.min(data[:,2])
thirdmax=np.max(data[:,2])
thirdmean=np.mean(data[:,2])
thirdmed=np.median(data[:,2])
thirdmode=s.mode(data[:,2])
thirdsd = np.std(data[:,2])
thirdvar= np.var(data[:,2])
thirdiqr=np.percentile(data[:,2],75) - np.percentile(data[:,2], 25)
print("Minimum Value: ", thirdmin)
print("Maximum Value: ", thirdmax)
print("Range: ", thirdmax - thirdmin)
print("Interquartile Range: ", thirdiqr)
print ("Mean:","{0:.4f}".format(round(thirdmean,4)))
print("Median:", thirdmed)
print("Mode: ", thirdmode)
print ("Standard Deviation: ","{0:.4f}".format(round(thirdsd,4)))
print("Variance: ","{0:.4f}".format(round(thirdvar,4)))
print()

print("Results for Petal Width Data")
fourmin=np.min(data[:,3])
fourmax=np.max(data[:,3])
fourmean=np.mean(data[:,3])
fourmed=np.median(data[:,3])
fourmode=s.mode(data[:,3])
foursd = np.std(data[:,3])
fourvar= np.var(data[:,3])
fouriqr=np.percentile(data[:,3],75) - np.percentile(data[:,3], 25)
print("Minimum Value: ", fourmin)
print("Maximum Value: ", fourmax)
print("Range: ", fourmax - fourmin)
print("Interquartile Range: ", fouriqr)
print ("Mean:","{0:.4f}".format(round(fourmean,4)))
print("Median:", fourmed)
print("Mode: ", fourmode)
print ("Standard Deviation: ","{0:.4f}".format(round(foursd,4)))
print("Variance: ","{0:.4f}".format(round(fourvar,4)))
print()

print("My program took %.2fs seconds to run" % (time.time() - start_time))
#Timed my program with reference to the following stackoverflow page
#https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
