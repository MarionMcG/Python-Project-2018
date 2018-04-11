#Marion McGowan 03/03/2018
#Iris Dataset RAW

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