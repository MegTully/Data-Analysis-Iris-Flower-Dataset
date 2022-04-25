#Finding the correlation between variablesusing seaborn package[16]
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

#Read in the dataset under variable name data
data = pd.read_csv("C:/Users/Owner/Desktop/pands-project/pands-project/pands-project/iris.txt")

#plot multivariate graph and specify the parameters
sb.pairplot(data, hue= "Species",kind="scatter", markers=["o","*","s"], height= 3)

#Displey the graph
plt.show()

#Save pairplot as png file[11]
plt.savefig('Multivariate_Pairplot.png', format="png")

