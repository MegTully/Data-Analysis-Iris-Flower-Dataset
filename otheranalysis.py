#Finding the correlation between variables Pearson's correlation coefficient[19]
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("C:/Users/Owner/Desktop/pands-project/pands-project/pands-project/iris.txt")

#want to get the correlation coefficient, need to specify groupby to get correlation for each species[20][2]
correlation=data.groupby("Species").corr(method='pearson')
#print the output to a .txt file[4]
print(correlation,file=open("Correlation_Tables.txt", "w"))

#correlation coefficients of the dataset not including or grouping by species
corr2=data.corr(method='pearson')
#print the output to a .txt file[4]
print(corr2,file=open("Correlation_Tables.txt", "a"))

from sklearn import preprocessing
SepalLength = np.array(data['SepalLength'])
normalized_arr = preprocessing.normalize([SepalLength])
print(normalized_arr)

SepalWidth = np.array(data['SepalWidth'])
normalized_arr2 = preprocessing.normalize([SepalWidth])
print(normalized_arr2)

PetalLength = np.array(data['PetalLength'])
normalized_arr3 = preprocessing.normalize([PetalLength])
print(normalized_arr3)

PetalWidth = np.array(data['PetalWidth'])
normalized_arr4 = preprocessing.normalize([PetalWidth])
print(normalized_arr4)

print(np.corrcoef(normalized_arr,normalized_arr2))
print(np.corrcoef(normalized_arr3,normalized_arr2))
print(np.corrcoef(normalized_arr4,normalized_arr2))


scaler = preprocessing.MinMaxScaler()
names=["SepalLength","SepalWidth","PetalLength","PetalWidth"]
df_scaled = pd.DataFrame(scaler.fit_transform(data["PetalLength"]), columns=data.columns)
np.reshape(df_scaled, (-1,1))
df_scaled


#sb.heatmap(data.corr(method='pearson').drop(
 # ['Id'], axis=1).drop(['Id'], axis=0),
 #           annot = True);
  
#plt.show()
