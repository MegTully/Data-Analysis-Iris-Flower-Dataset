#Need to use package pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read in the iris dataset and assign it a avariable name data [2]
data = pd.read_csv("C:/Users/Owner/Desktop/pands-project/pands-project/pands-project/iris.txt")

#create two arrays of x and y values which are the sepal lengths and sepal widths respectively
xs= data["SepalLength"]
ys=data["SepalWidth"]

#plot a scatter plot with its colour defining the class of species and outlining the edge of the data points with the colour black(k) [5][14]
plot=plt.scatter(xs,ys,label = "Sepal Length vs Sepal Width $", c = data.Species.astype("category").cat.codes,edgecolors="k") 
#create an array of the types of iris flowers for the legend
flowerNames=["Iris Setosa","Iris Versicolor","Iris Virginica"]
#label the x and y axes accordingly
plt.xlabel("x-Axis")
plt.ylabel("y-Axis")
#Create a legend showing which of the species each colour of the data points represents[15] 
plt.legend(handles=plot.legend_elements()[0], labels=flowerNames, 
           title="Species")
#display plot
plt.show()
#Save histogram as png file[11][15]
plt.savefig('ScatterPlot_SepalWidth_VS_SepalLength.png', format="png")

#create two new arrays with x values as petal lengths and y values as petal widths
x2s=data["PetalLength"]
y2s=data["PetalWidth"]

#plot another scatter plot for the petal lengths and widths with stars as data points
plot2=plt.scatter(x2s,y2s,label = "Petal Length vs Petal Width $", c = data.Species.astype("category").cat.codes, marker="*")
#label the x and y axes
plt.xlabel("x-Axis")
plt.ylabel("y-Axis")
#Create a legend showing which of the species each colour of the data points represents[15] 
plt.legend(handles=plot.legend_elements()[0], labels=flowerNames, 
           title="Species")
#display plot           
plt.show()
#Save histogram as png file[11][15]
plt.savefig('ScatterPlot_PetalWidth_VS_PetalLength.png',format="png")