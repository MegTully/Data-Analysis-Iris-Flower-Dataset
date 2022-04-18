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

#create a for loop to set y-axis labels and rotate the x-axis labels to 0 degrees for all subplots[8]
for ax in graph.flat:
    ax.set(ylabel='Count')
    ax.tick_params(axis='x', labelrotation = 0)
    
#Display Graph
plt.show()

#References
#[6]https://mode.com/example-gallery/python_histogram/
#[7]https://dataindependent.com/pandas/pandas-histogram-dataframe-hist/
#[8]https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html