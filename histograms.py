#Histograms
#Need to use package pandas, numpy,matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read in the iris dataset and assign it a avariable name data [2]
data = pd.read_csv("C:/Users/Owner/Desktop/pands-project/pands-project/pands-project/iris.txt")

#create histogram the counts the flowers with same sepal length and group by species and set parameters[6][7]
graph = data.hist(column='SepalLength', by='Species', bins= 50 , legend=True, grid=True, figsize=(8,9), 
layout=(3,1), color='m')

#Set x-axis label that represents x-axis for all subplots[7]
plt.xlabel("Sepal Length (Cm)")

#create a for loop to set y-axis labels and rotate the x-axis labels to 0 degrees for all subplots[8][9]
for ax in graph.flat:
    ax.set(ylabel='Count')
    ax.tick_params(axis='x', labelrotation = 0)

#Save histogram as png file[11][15]
plt.savefig('Histogram_SepalLength.png',format="png")
    
#create histogram the counts the flowers with same sepal Width and group by species and set parameters[6][7]
graph1 = data.hist(column='SepalWidth', by='Species', bins=50, legend=True, grid=True, figsize=(8,9), 
layout=(3,1), color='y')
#Set x-axis label that represents x-axis for all subplots[7]
plt.xlabel("Sepal Width (Cm)")

#create a for loop to set y-axis labels and rotate the x-axis labels to 0 degrees for all subplots[8][9]
for ax in graph1.flat:
    ax.set(ylabel='Count')
    ax.tick_params(axis='x', labelrotation = 0)

#Save histogram as png file[11][15]
plt.savefig('Histogram_SepalWidth.png',format="png")

#create histogram the counts the flowers with same petal length and group by species and set parameters[6][7]
graph2 = data.hist(column='PetalLength', by='Species', bins=50, legend=True, grid=True, figsize=(8,9), 
layout=(3,1), color='c')
#Set x-axis label that represents x-axis for all subplots[7]
plt.xlabel("Petal Length (Cm)")

#create a for loop to set y-axis labels and rotate the x-axis labels to 0 degrees for all subplots[8][9]
for ax in graph2.flat:
    ax.set(ylabel='Count')
    ax.tick_params(axis='x', labelrotation = 0)

#Save histogram as png file[11][15]
plt.savefig('Histogram_petalLength.png', format="png")

#create histogram the counts the flowers with same Petal Width and group by species and set parameters[6][7]
graph3 = data.hist(column='PetalWidth', by='Species', bins=50, legend=True, grid=True, figsize=(8,9), 
layout=(3,1), color='#00FF00')
#Set x-axis label that represents x-axis for all subplots[7]
plt.xlabel("Petal Width (Cm)")

#create a for loop to set y-axis labels and rotate the x-axis labels to 0 degrees for all subplots[8][9]
for ax in graph3.flat:
    ax.set(ylabel='Count')
    ax.tick_params(axis='x', labelrotation = 0)

#Save histogram as png file[11][15]
plt.savefig('Histogram_PetalWidth.png',format="png")
    
#Display Graphs
plt.show()
