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

#print out the results and round the mean to one decimal place to a text file [3]
print("Sepal Length Statistics","\nMean:", round(mean_SL,1), "\nMedian:",median_SL, "\nMin:", min_SL, "\nMax:", max_SL, file=open("Variable Summaries.txt", "a"))

#Using numpy to get standard deviation and variance rounded to 2 decimal places[2]
std_SL = np.std(data["SepalLength"])
var_SL = np.var(data["SepalLength"])

print("Standard Deviation:",round(std_SL,2), "\nVariance:",round(var_SL, 2), file=open("Variable Summaries.txt", "a") )

#Summary of Variable SepalWidth[1]
mean_SW = data["SepalWidth"].mean()
median_SW = data["SepalWidth"].median()
min_SW = data["SepalWidth"].min()
max_SW = data["SepalWidth"].max()

#print out the results and round the mean to one decimal place
print("Sepal Width Statistics ","\nMean:", round(mean_SW,1), "\nMedian:",median_SW, "\nMin:", min_SW, "\nMax:", max_SW, file=open("Variable Summaries.txt", "a"))

#Using numpy to get standard deviation and variance rounded to 2 decimal places[2]
std_SW = np.std(data["SepalWidth"])
var_SW = np.var(data["SepalWidth"])

print("Standard Deviation:",round(std_SW,2), "\nVariance:",round(var_SW, 2),file=open("Variable Summaries.txt", "a") )

#Summary of Variable PetalLength[1]
mean_PL = data["PetalLength"].mean()
median_PL = data["PetalLength"].median()
min_PL = data["PetalLength"].min()
max_PL = data["PetalLength"].max()

#print out the results and round the mean to one decimal place
print("Petal Length Statistics ","\nMean:", round(mean_PL,1), "\nMedian:",median_PL, "\nMin:", min_PL, "\nMax:", max_PL, file=open("Variable Summaries.txt", "a"))

#Using numpy to get standard deviation and variance rounded to 2 decimal places[2]
std_PL = np.std(data["PetalLength"])
var_PL = np.var(data["PetalLength"])

print("Standard Deviation:",round(std_PL,2), "\nVariance:",round(var_PL, 2), file=open("Variable Summaries.txt", "a") )

#Summary of Variable PetalWdth[1]
mean_PW = data["PetalWidth"].mean()
median_PW = data["PetalWidth"].median()
min_PW = data["PetalWidth"].min()
max_PW = data["PetalWidth"].max()

#print out the results and round the mean to one decimal place
print("Petal Width Statistics ","\nMean:", round(mean_PW,1), "\nMedian:",median_PW, "\nMin:", min_PW, "\nMax:", max_PW, file=open("Variable Summaries.txt", "a"))

#Using numpy to get standard deviation and variance rounded to 2 decimal places[2]
std_PW = np.std(data["PetalWidth"])
var_PW = np.var(data["PetalWidth"])

print("Standard Deviation:",round(std_PW,2), "\nVariance:",round(var_PW, 2), file=open("Variable Summaries.txt", "a") )



 
#print(data.shape)


#References:
#[1]https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
#[2]https://www.w3schools.com/python/python_ml_standard_deviation.asp
#[3]https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file