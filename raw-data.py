#Marion McGowan 03/03/2018
#Iris Dataset RAW
#I wrote this program for my own use, it doesn't provide any relevant information.
#But listing data in this form allowed me to easily copy and paste raw data into online calculators, in order to verify my results.
#I'm new to Python and wanted to make sure I wasn't getting incorrect results. 

print("Sepal Length Raw Data")
with open ("data/iris-data.csv") as f:
    for line in f:
        print(", ",line.split(',')[0],end="")
print()
print("Sepal Width Raw Data")
with open ("data/iris-data.csv") as f:
    for line in f:
        print(", ", line.split(',')[1],end="")
print()
print("Petal Length Raw Data")
with open ("data/iris-data.csv") as f:
    for line in f:
        print(", ", line.split(',')[2],end="")
print()
print("Petal Width Raw Data")
with open ("data/iris-data.csv") as f:
    for line in f:
        print(", " , line.split(',')[3],end="")
        
