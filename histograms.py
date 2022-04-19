#Histograms
#Need to use package pandas, numpy,matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read in the iris dataset and assign it a avariable name data [2]
data = pd.read_csv("C:/Users/Owner/Desktop/pands-project/pands-project/pands-project/iris.txt")

#create histogram the counts the flowers with same sepal length and group by species and set parameters[6][7]
graph = data.hist(column='SepalLength', by='Species', bins=50, legend=True, grid=True, figsize=(8,9), 
layout=(3,1), color='m')

#Set x-axis label that represents x-axis for all subplots[7]
plt.xlabel("Sepal Length (Cm)")

#create a for loop to set y-axis labels and rotate the x-axis labels to 0 degrees for all subplots[8][9]
for ax in graph.flat:
    ax.set(ylabel='Count')
    ax.tick_params(axis='x', labelrotation = 0)
    
#create histogram the counts the flowers with same sepal Width and group by species and set parameters[6][7]
graph1 = data.hist(column='SepalWidth', by='Species', bins=50, legend=True, grid=True, figsize=(8,9), 
layout=(3,1), color='y')
#Set x-axis label that represents x-axis for all subplots[7]
plt.xlabel("Sepal Width (Cm)")

#create a for loop to set y-axis labels and rotate the x-axis labels to 0 degrees for all subplots[8][9]
for ax in graph1.flat:
    ax.set(ylabel='Count')
    ax.tick_params(axis='x', labelrotation = 0)

#create histogram the counts the flowers with same sepal Width and group by species and set parameters[6][7]
graph2 = data.hist(column='PetalLength', by='Species', bins=50, legend=True, grid=True, figsize=(8,9), 
layout=(3,1), color='c')
#Set x-axis label that represents x-axis for all subplots[7]
plt.xlabel("Petal Length (Cm)")

#create a for loop to set y-axis labels and rotate the x-axis labels to 0 degrees for all subplots[8][9]
for ax in graph2.flat:
    ax.set(ylabel='Count')
    ax.tick_params(axis='x', labelrotation = 0)

#create histogram the counts the flowers with same sepal Width and group by species and set parameters[6][7]
graph3 = data.hist(column='PetalWidth', by='Species', bins=50, legend=True, grid=True, figsize=(8,9), 
layout=(3,1), color='#00FF00')
#Set x-axis label that represents x-axis for all subplots[7]
plt.xlabel("Petal Width (Cm)")

#create a for loop to set y-axis labels and rotate the x-axis labels to 0 degrees for all subplots[8][9]
for ax in graph3.flat:
    ax.set(ylabel='Count')
    ax.tick_params(axis='x', labelrotation = 0)
    
#Display Graphs
plt.show()

#References
#[6]https://mode.com/example-gallery/python_histogram/
#[7]https://dataindependent.com/pandas/pandas-histogram-dataframe-hist/
#[8]https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
#[9]https://stackabuse.com/rotate-axis-labels-in-matplotlib/
#[10]https://www.w3schools.com/colors/colors_mixer.asp?colorbottom=00FF00&colortop=FFFFFF