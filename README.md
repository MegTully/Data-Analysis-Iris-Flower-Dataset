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

The petal lengths could be used to diffrentiate between the three types of flower. The shortest average petal length of 1.5cm was in the iris-setosa species group, then the iris-versicolor flowers had a mean of 5.6cm and the iris-virginica had the longest average petal length of 5.6cm. The values in the centre of the datasets were the same as the means. The flower with the max petal length recorded was the iris-virginica at 6.9cm. The longest petal found amongst the iris-setosa and iris-versicolor was a length of 1.9cm and 5.1cm respectively. The min petal length in the dataset was the iris-setosa at 1cm and the iris-versicolor had a shortest petal of length 3cm and iris-virginica was 4.5cm.

The average and median width of the petals on the iris-setosa were very small at 0.2cm. Then not too far off them was the iris-versicolor with a mean and median of 1.3cm and then the iris-virginica with mean and median of 2cm. The iris-virginica has the max value recorded for the petal width at 2.5cm and the iris-setosa has the thinnest width of 0.1cm out of the 150 iris flower samples.

After analysing these statistics it appears that out of the three iris species that in general iris-setosa's have the smallest petals and iris-virginica's have largest petals. It is also evident that iris-setosa's have the shortest sepal length of the three species but also have the widest sepal widths in the recorded data. The iris-virginica's have the longest recorded sepal lengths and iris-versicolor's have smallest sepal widths of all the flowers. 

# Histograms
Next I displayed the dataset using histograms. The following packages were imported and used for this section of code, Pandas as pd, Numpy as np and matplotlib.pyplot as plt. The iris dataset was read in as variable name "data". I used the .hist() function to create a histogram [6][7] and assigned the plot a variable name "graph". For each variable sepal length, sepal width, petal length and petal width I plotted 3 subplots showing the variables prroperites for each species. The first set of histograms, "Histogram_SepalLength", had "column" parameter equal to "SepalLength" so the x-axis represents the measurements recorded for each flower then the "by" parameter was equal to species to group each histogram based on which type of species the measurements correspond to. The next parameter in the .hist() function is "bins" which is the amount of clusters you want to put the data into so I chose 50 because I want to see each of the 50 measurements plotted separaretly instead of being joined with measurements near each other, this makes it easier to read and inspect the graph. The "legend" parameter was set to true so the it is clear what the bars on the graph represent with the legend in to top right corner of the graph. "grid" is set to True to show the axes grid lines. "figsize" sets the size of the graph, I just played with these numbers until a nice size was found and then "layout()" parameter set the layout for the 3 subplots in which I set it to be 3 rows and 1 on top of another. The colour of the bars were set to "m" which represents a pinky magenta colour.

# Correlation Between Variables
When analysing this dataset I was curious to see if there was any relationship between the lengths and widths of the sepals and the lengths and widths of the petals. For example if they sepal lengths are long then so are the petals or if the sepal widths are small then sepal lengths are large. I used the seaborn package to carry out this analysis[16]. For the code I researched how to use seaborn for multivariate data plots and I decided to use the "seaborn.pairplot" function as I think it displays the relationships between the variables well. Within this function I read in the dataset under the variable name data, set the hue parameter to "Species" because I wanted to look at the relationships of each variable based on the type of species and set the parameter kind equal to "scatter" because after trying a few plots the scatterplot proved to be easiest read and understand as you can clearly see the distance between the clusters of data which shows the closeness of their relationships with each other. Then I set the markers parameters to dots, stars and squares to represent the iris-setosa's, iris-versicolor's and iris-virginica's respectively so that aswell as the different colours this helps distinguish between species and lastly I set the height of the graphs equal to 3cm because when I set it abover 3cm all the information didn't print to the screen[16]. I then displayed the graph [17] and saved it as a png file [11].

# Analysing The Pairplot
The diagonal in the pairplot represents univariate data so like our histograms they just show the count for each variable but are displayed using density plots.







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
[14]https://datavizpyr.com/how-to-color-scatterplot-by-a-variable-in-matplotlib/
[15]https://datavizpyr.com/add-legend-to-scatterplot-colored-by-a-variable-with-matplotlib-in-python/
[16]https://seaborn.pydata.org/generated/seaborn.pairplot.html
[17]https://www.adamsmith.haus/python/answers/how-to-display-a-seaborn-plot-in-python