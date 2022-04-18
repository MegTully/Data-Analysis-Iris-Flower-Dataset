#Need to use package pandas
import pandas as pd
import numpy as np

#read in the iris dataset and assign it a avariable name data [2]
data = pd.read_csv("C:/Users/Owner/Desktop/pands-project/pands-project/pands-project/iris.txt")

#Summary of Variable SepalLenth[2]
mean_SL = data["SepalLength"].mean()
median_SL = data["SepalLength"].median()
min_SL = data["SepalLength"].min()
max_SL = data["SepalLength"].max()

#print out the results and round the mean to one decimal place to a text file [4]
print("Sepal Length Statistics","\nMean:", round(mean_SL,1), "\nMedian:",median_SL, "\nMin:", min_SL, "\nMax:", max_SL, file=open("Variable Summaries.txt", "a"))

#Using numpy to get standard deviation and variance rounded to 2 decimal places[2]
std_SL = np.std(data["SepalLength"])
var_SL = np.var(data["SepalLength"])

print("Standard Deviation:",round(std_SL,2), "\nVariance:",round(var_SL, 2), file=open("Variable Summaries.txt", "a") )

#Summary of Variable SepalWidth[2]
mean_SW = data["SepalWidth"].mean()
median_SW = data["SepalWidth"].median()
min_SW = data["SepalWidth"].min()
max_SW = data["SepalWidth"].max()

#print out the results and round the mean to one decimal place
print("Sepal Width Statistics ","\nMean:", round(mean_SW,1), "\nMedian:",median_SW, "\nMin:", min_SW, "\nMax:", max_SW, file=open("Variable Summaries.txt", "a"))

#Using numpy to get standard deviation and variance rounded to 2 decimal places[3]
std_SW = np.std(data["SepalWidth"])
var_SW = np.var(data["SepalWidth"])

print("Standard Deviation:",round(std_SW,2), "\nVariance:",round(var_SW, 2),file=open("Variable Summaries.txt", "a") )

#Summary of Variable PetalLength[2]
mean_PL = data["PetalLength"].mean()
median_PL = data["PetalLength"].median()
min_PL = data["PetalLength"].min()
max_PL = data["PetalLength"].max()

#print out the results and round the mean to one decimal place
print("Petal Length Statistics ","\nMean:", round(mean_PL,1), "\nMedian:",median_PL, "\nMin:", min_PL, "\nMax:", max_PL, file=open("Variable Summaries.txt", "a"))

#Using numpy to get standard deviation and variance rounded to 2 decimal places[3]
std_PL = np.std(data["PetalLength"])
var_PL = np.var(data["PetalLength"])

print("Standard Deviation:",round(std_PL,2), "\nVariance:",round(var_PL, 2), file=open("Variable Summaries.txt", "a") )

#Summary of Variable PetalWdth[2]
mean_PW = data["PetalWidth"].mean()
median_PW = data["PetalWidth"].median()
min_PW = data["PetalWidth"].min()
max_PW = data["PetalWidth"].max()

#print out the results and round the mean to one decimal place
print("Petal Width Statistics ","\nMean:", round(mean_PW,1), "\nMedian:",median_PW, "\nMin:", min_PW, "\nMax:", max_PW, file=open("Variable Summaries.txt", "a"))

#Using numpy to get standard deviation and variance rounded to 2 decimal places[3]
std_PW = np.std(data["PetalWidth"])
var_PW = np.var(data["PetalWidth"])

print("Standard Deviation:",round(std_PW,2), "\nVariance:",round(var_PW, 2), file=open("Variable Summaries.txt", "a") )

#Summary of Variable Species
mean_SpecSL= data.groupby('Species')['SepalLength'].mean().reset_index()
median_SpecSL = data.groupby('Species')['SepalLength'].median().reset_index()
min_SpecSL = data.groupby('Species')['SepalLength'].min().reset_index()
max_SpecSL = data.groupby('Species')['SepalLength'].max().reset_index()
mean_SpecSW= data.groupby('Species')['SepalWidth'].mean().reset_index()
median_SpecSW = data.groupby('Species')['SepalWidth'].median().reset_index()
min_SpecSW = data.groupby('Species')['SepalWidth'].min().reset_index()
max_SpecSW = data.groupby('Species')['SepalWidth'].max().reset_index()
mean_SpecPL= data.groupby('Species')['PetalLength'].mean().reset_index()
median_SpecPL = data.groupby('Species')['PetalLength'].median().reset_index()
min_SpecPL = data.groupby('Species')['PetalLength'].min().reset_index()
max_SpecPL = data.groupby('Species')['PetalLength'].max().reset_index()
mean_SpecPW= data.groupby('Species')['PetalWidth'].mean().reset_index()
median_SpecPW = data.groupby('Species')['PetalWidth'].median().reset_index()
min_SpecPW = data.groupby('Species')['PetalWidth'].min().reset_index()
max_SpecPW = data.groupby('Species')['PetalWidth'].max().reset_index()

#print out the results and round the mean to one decimal place
print("Species Sepal Length Statistics ","\nMean:\n", round(mean_SpecSL,1), "\nMedian:\n",median_SpecSL, "\nMin:\n", min_SpecSL, "\nMax:\n", max_SpecSL, file=open("Variable Summaries.txt", "a"))
print("Species Sepal Width Statistics ","\nMean\n:", round(mean_SpecSW,1), "\nMedian:\n",median_SpecSW, "\nMin:\n", min_SpecSW, "\nMax:\n", max_SpecSW, file=open("Variable Summaries.txt", "a"))
print("Species Petal Length Statistics ","\nMean\n:", round(mean_SpecPL,1), "\nMedian:\n",median_SpecPL, "\nMin:\n", min_SpecPL, "\nMax:\n", max_SpecPL, file=open("Variable Summaries.txt", "a"))
print("Species Petal Width Statistics ","\nMean\n:", round(mean_SpecPW,1), "\nMedian:\n",median_SpecPW, "\nMin:\n", min_SpecPW, "\nMax:\n", max_SpecPW, file=open("Variable Summaries.txt", "a"))

#Histograms
import matplotlib as plt
xs= np.data["Species"]
ys= np.data["SepalLength"]

plt.hist(xs,ys)
plt.show()
#graph = data.plot.hist(column=["SepalLength"], by="Species", figsize=(10, 8))


#References:
#[2]https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
#[3]https://www.w3schools.com/python/python_ml_standard_deviation.asp
#[4]https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
#[5] https://stackoverflow.com/questions/71207177/how-to-calculate-mean-of-specific-rows-in-python-dataframe