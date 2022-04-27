#Finding the correlation between each pair of variables using seaborn package[16]
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

#Read in the dataset under variable name data
data = pd.read_csv("C:/Users/Owner/Desktop/pands-project/pands-project/pands-project/iris.txt")

#plot multivariate graph and specify the parameters[18]
#kind=scatter because want the pairplots to be scatterplots[18]
#markers the represent the data points set to diff shapes, height of graph is 3cm
sb.pairplot(data, hue= "Species",kind="scatter", markers=["o","*","s"], height= 3)

#Save pairplot as png file[11]
plt.savefig('Pairplots.png')#Need to use package pandas

