#Finding the correlation between variables Pearson's correlation coefficient[19]
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/Owner/Desktop/pands-project/pands-project/pands-project/iris.txt")

#want to get the correlation coefficient, need to specify groupby to get correlation for each species[20][2]
correlation=data.groupby("Species").corr(method='pearson')
#print the output to a .txt file[4]
print(correlation,file=open("Correlation_Tables.txt", "w"))

#correlation coefficients of the dataset not including or grouping by species
corr2=data.corr(method='pearson')
#print the output to a .txt file[4]
print(corr2,file=open("Correlation_Tables.txt", "a"))

#sb.heatmap(data.corr(method='pearson').drop(
 # ['Id'], axis=1).drop(['Id'], axis=0),
 #           annot = True);
  
#plt.show()
