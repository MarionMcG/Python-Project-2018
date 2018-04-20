# Python-Project-2018


## Background Information on the Iris Dataset
**The Iris Dataset** is a multivariate data set. 
There are three species included in the Iris set; Iris Setosa, Iris Versicolour and Iris Virginica. 
Each species has a total of 50 samples measured, leading to 150 samples in total. 
In each sample, four measurements were taken; sepal length, sepal width, petal length and petal width. There are no missing data points and all the data is measured in centimetres. 

## Project Plan

My aim in analyzing the Iris Dataset is to determine if there is any relationship between the four different measurements and the three different species. I am looking for nice patterns that may indicate a relationship between variables, or distinguish between species. 

I intend to calculate various measures of central tendency and spread within the four data sets: sepal length, sepal width, petal length and petal width. I also plan to compare pairs of measurements on scatter diagrams to determine if there is any relationship between them. Calculating the correlation coefficient would give me a definitive answer without a graphical representation. However I hope to get a better understanding of how the relationship between variables differs, or not, across species. This comparison would be best done on scatter diagrams.  

As this is my first statistical analysis project, I did not have any concrete goals in mind, beyond determining correlation. As I worked my way through this project, I went on several tangents that gave me a better understanding of the limitations of my initial plan. 

**Tangents**

In the process of my analysis, my results often meant I reconsidered my approach to get the most accurate view of my data. 
* After running my program Calculations.py, I have a number of different measures for the average and spread but could not get a good idea of the distribution or how these values related to one another. 
I placed all 150 data points for each measurement into a histogram to get a graph of the distribution of data. I then viewed these distributions along the same intervals of the x and y axes.

* After running my program Scatter.py, it was clear that petal length and petal width correlate strongly. I began to consider if it would be possible to get an equation for length with respect to width. 

* After running my program Scatter2.py, it was clear that the relationship between petal length and petal width was also a good indicator of species. 

## How to Run my Code
* **Calculations.py -**
The first program I wrote is designed to perform statistical analysis on each of the four measurements in the Iris Dataset. It will list the minimum value, maximum value, range, interquartile range, mean, median, mode, standard deviation and variance for these measurements. 

* **Hist.py -**

* **Scatter1.py -**
This program looks at the relationship between the four measurements, graphing two variables against one another on a scatter diagram and calculating the correlation co-efficient for each graph. 


* **Scatter2.py -**
This program looks at the relationship between the three different species, graphing two variable for each species against one another. Subplots were used to better compare these three different species side by side. 

## My Analysis of the Iris Dataset

**Central Tendency and Distribution**
<table>
 <tr>
  <th>Sepal Length</th>
  <th>Sepal Width</th>
  <th>Petal Length</th>
  <th>Petal Width</th></tr>
 <tr>
   <td><img src='img/hist1.png'></td>
   <td><img src='img/hist2.png'></td>
   <td><img src='img/hist3.png'></td>
   <td><img src='img/hist4.png'></td></tr>
 <tr>
  <td> Minimum Value:  4.3<br> 
     Maximum Value:  7.9<br> 
     Range:  3.6<br>
     Interquartile Range:  1.3<br> 
     Mean: 5.8433<br>
     Median:  5.8<br> 
     Mode:  5.0 <br> 
     Standard Deviation:  0.8253<br>   
     Variance:  0.6811</td>
  <td> Minimum Value:  2.0<br>
     Maximum Value:  4.4<br>
     Range:  2.4<br>
     Interquartile Range:  0.5<br>
     Mean: 3.0540<br> 
     Median: 3.0<br> 
     Mode:  3.0<br>
     Standard Deviation:  0.4321<br>   
     Variance:  0.1868<br></td> 
<td>
  Minimum Value:  1.0<br>
  Maximum Value:  6.9<br>
  Range:  5.9<br>
  Interquartile Range:  3.5<br>
  Mean: 3.7587<br>
  Median: 4.35<br>
  Mode:  1.5<br>
  Standard Deviation:  1.7585<br>
  Variance:  3.0924<br></td>
<td>
  Minimum Value:  0.1<br>
  Maximum Value:  2.5<br>
  Range:  2.4<br>
  Interquartile Range:  1.5<br>
  Mean: 1.1987<br>
  Median: 1.3<br>
  Mode:  0.2<br>
  Standard Deviation:  0.7606<br>
  Variance:  0.5785<br></td>
</tr>
  <td><img src='img/hist5.png'></td>
  <td><img src='img/hist6.png'></td>
  <td><img src='img/hist7.png'></td>
  <td><img src='img/hist8.png'></td></tr>
 </table>
 

<table>
 <tr>
  <th>Sepal Length vs. Sepal Width</th>
   <td><img src='img/scatter1.png'></td>
   <td><img src='img/updtsubplot1.png'></td>
   <td>Correlation Co=efficient: -0.1094</td></tr>
 <tr>
  <th>Petal Length vs.Petal Width</th>
   <td><img src='img/scatter2.png'></td>
   <td><img src='img/updtsubplot2.png'></td>
    <td>Correlation Co=efficient: 0.9628</td></tr>
 <tr>
  <th>Sepal Width vs. Petal Width</th>
   <td><img src='img/scatter4.png'></td>
   <td></td>
   <td>Correlation Co=efficient: 0.8718</td></tr>
 <tr>
  <th>Sepal Length vs. Petal Length </th>
   <td><img src='img/scatter3.png'></td>
   <td><img src='img/updtsubplot3.png'></td><td> 
   <td>Correlation Co=efficient: -0.3565</td></tr>
 </table>
 
## References

* Fisher, R.A. [The use of multiple measurements in taxonomic problems.](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x)Annals of Eugenics. 7 (2): 179–188. (1936) Accessed on 10/04/2018.
* Hoey, Patrick S. [Statistical Analysis of the Iris Flower Dataset](http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf). University of Massachusetts At Lowell. Accessed on 10/04/2018.
* [The Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set), Wikipedia. Accessed on 10/04/2018.
* 
