# pands-project

This Project is based off a dataset created by R.A Fisher which contains information about three types of iris plants. There are 4 attributes used to differentiate each plant class, they are petal length, petal width, sepal length and sepal width. The three iris flower types are iris setosa, iris versicolor and iris virginica[1].

# Iris Dataset
The dataset was downloaded from the UCI website [1] and column headings were added to the .txt file in notepad ++. The dataset was then read into the analysis.py file using the pandas package. Pandas allows the csv file to be analysed as a dataframe with columns and rows[2].

# Summary of Variables
A statistical summary of each variable was printed to a text file called "Variable Summaries"[4]. For each of the 4 variables the mean was calculated using .mean() which had a lot of decimal places so the round() function was used to round it to 2 decimal places inside the print() function. The mean is the average value of all the attributes in a set. Then .median() was used to calculated the "middle" value which is the most common value. The .min() and .max() functions were used to calculate the maximum and minimum values in each set of variables[2]. A package called Numpy, denoted as np, was used to calculate the standard deviation and the variance with the functions np.std() and np.var() [4]. The standard deviation and variance measure the spread of the data.

# Sepal Length




# References
[1] https://archive.ics.uci.edu/ml/datasets/iris
[2]https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
[3]https://www.w3schools.com/python/python_ml_standard_deviation.asp
[4]https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
[5]https://stackoverflow.com/questions/71207177/how-to-calculate-mean-of-specific-rows-in-python-dataframe