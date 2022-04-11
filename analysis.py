#Need to use package pandas
import pandas as pd
import numpy as np

#read in the iris dataset and assign it a avariable name data [1]
data = pd.read_csv("C:/Users/Owner/Desktop/pands-project/pands-project/pands-project/iris.txt")

#Summary of Variable SepalLenth[1]
mean_SL = data["SepalLength"].mean()
median_SL = data["SepalLength"].median()
min_SL = data["SepalLength"].min()
max_SL = data["SepalLength"].max()

#print out the results and round the mean to one decimal place
print("Mean:", round(mean_SL,1), "\nMedian:",median_SL, "\nMin:", min_SL, "\nMax:", max_SL)

#Using numpy to get standard deviation and variance rounded to 2 decimal places[2]
std_SL = np.std(data["SepalLength"])
var_SL = np.var(data["SepalLength"])

print("Standard Deviation:",round(std_SL,2), "\nVariance:",round(var_SL, 2) )




 
#print(data.shape)


#References:
#[1]https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
#[2]https://www.w3schools.com/python/python_ml_standard_deviation.asp