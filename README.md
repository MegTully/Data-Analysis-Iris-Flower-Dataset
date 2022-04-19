# pands-project

This Project is based off a dataset created by R.A Fisher which contains information about three types of iris plants. There are 4 attributes used to differentiate each plant class, they are petal length, petal width, sepal length and sepal width. The three iris flower types are iris setosa, iris versicolor and iris virginica[1].

# Iris Dataset
The dataset was downloaded from the UCI website [1] and column headings were added to the .txt file in notepad ++. The dataset was then read into the analysis.py file using the pandas package. Pandas allows the csv file to be analysed as a dataframe with columns and rows[2].

# Summary of Variables
A statistical summary of each variable was printed to a text file called "Variable Summaries"[4]. For each of the 4 variables the mean was calculated using .mean() which had a lot of decimal places so the round() function was used to round it to 2 decimal places inside the print() function. The mean is the average value of all the attributes in a set. Then .median() was used to calculated the "middle" value which is the most common value. The .min() and .max() functions were used to calculate the maximum and minimum values in each set of variables[2]. A package called Numpy, denoted as np, was used to calculate the standard deviation and the variance with the functions np.std() and np.var() [4]. The standard deviation measures how spread out the data is i.e how close each measurement is to the mean/average measurement [12]. The variance is similar to the standard deviation but calculates the spread of the data using a different formula[13].

# Sepal Length
The average measurement for the length of all three iris flower's sepals was 5.8cm. This mean value was also the same as the median so 5.8cm was the centre/middle value in all the recorded sepal lengths in the iris dataset when in ascending order. The shortest sepal length amongst all the flowers was 4.3cm and the longest was 7.9cm. This is quite a big difference, the smallest sepal length is not far off half the length of the longest sepal. The standard deviation was 0.83cm this means that the individual sepal length measurements are all within a 0.83cm distance from the mean. The variance was 0.68cm which along with standard deviation is small enough which means the data is unlikely to have any outliers.

# Sepal Width
The values for sepal width statistics are much smaller than sepal length with the average width measurement being 3.1cm which is very small. The median is very close with a value of 3.0cm. The maximum value the sepal width reaches is 4.4cm and the minimum value is 2.0cm so as with the sepal length theres quite a big difference in size between the smallest sepal width and the largest. However the measurements don't spread too far from the mean value which is shown by the calculates standard deviation of 0.43cm and variance of 0.19cm.

# Petal Length
The mean petal length of the iris flowers is 3.8cm which shows they have short petals on average. Unlike the sepal measurements the centre value of this data column is a bit off from the mean with a value of 4.35cm. Suprisingly the smallest petal length is 1cm which is very short. The longest petal of the flowers in the dataset is 6.9cm. All of these values are noticeably smaller than the sepal length values which shows the sepals are longer than the petals on these iris flowers. The standard deviation was 1.76cm and the variance was 3.06cm. These values are quite large which shows there is a large spread and variance amongst the petal length of the iris flowers. There are clearly a wide variety of petal lengths in the dataset.

# Petal Width
The average petal width is very skinny with a measurement of 1.2cm. The median is very close to the mean with a value of 1.3cm. Interestingly the minimum width recorded was an extremely small value of 0.1cm and the widest petal was 2.5cm. Given the small range of width measurements, the standard deviation at 0.76cm and variance at 0.58cm are quite big statistics. Just like the petal lengths, the petal widths of all the flowers vary alot.

# Species
For the sepal length of each species of flower all statistics were very similar to each other therefore I think it would be difficult to tell them apart based off of their sepal length. The average sepal length was shortest for the iris-setosa at 5.0cm, then the iris-versicolor was 5.9cm and the longest was the iris-virginica at 6.6cm. The medians were the same as the means except for iris-virginica which was only 0.1cm less than it's mean. Both the iris-versicolor and iris-virginica had the same minimum value of 4.9cm and iris-setosa had the smallest sepal length in the dataset with a value of 4.3cm. The longest sepal recorded was an iris-virginica at 7.9cm. The max values of the iris-setosa and iris-versicolor were 5.8cm and 7.0cm respectively.

The sepal widths of each species would also make it a challenge to diffrentiate between the 3 flowers. The average width of the iris-setosa, iris-versicolor and iris-virginica sepals are 3.4cm,2.8cm and 3.0cm respectively. The medians are exactly the same as the means. The iris-versicolor has the smallest width of 2.0cm recorded in the dataset. The iris-setosa has the largest sepal width recorded which is 4.4cm.







# References
[1] https://archive.ics.uci.edu/ml/datasets/iris
[2]https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
[3]https://www.w3schools.com/python/python_ml_standard_deviation.asp
[4]https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
[5]https://stackoverflow.com/questions/71207177/how-to-calculate-mean-of-specific-rows-in-python-dataframe
[6]https://mode.com/example-gallery/python_histogram/
[7]https://dataindependent.com/pandas/pandas-histogram-dataframe-hist/
[8]https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
[9]https://stackabuse.com/rotate-axis-labels-in-matplotlib/
[10]https://www.w3schools.com/colors/colors_mixer.asp?colorbottom=00FF00&colortop=FFFFFF
[11]https://chartio.com/resources/tutorials/how-to-save-a-plot-to-a-file-using-matplotlib/
[12]https://www.statisticshowto.com/probability-and-statistics/standard-deviation/
[13]https://www.investopedia.com/ask/answers/021215/what-difference-between-standard-deviation-and-variance.asp