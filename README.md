# Pands-Project
## Author Megan Tully

This Project is based off a dataset created by R.A Fisher which contains information about three types of iris plants. There are 4 attributes used to differentiate each plant class, they are petal length, petal width, sepal length and sepal width. The three iris flower types are iris setosa, iris versicolor and iris virginica[1].

# Iris Dataset
The dataset was downloaded from the UCI website [1] and column headings were added to the .txt file in notepad ++. The dataset was then read into the analysis.py file using the pandas package. Pandas allows the csv file to be analysed as a dataframe with columns and rows[2].

# Summary of Variables
A statistical summary of each variable was printed to a text file called "Variable Summaries"[4]. For each of the four variables the mean was calculated using .mean() which had a lot of decimal places so the round() function was used to round it to 2 decimal places inside the print() function. The mean is the average value of all the attributes in a set. Then .median() was used to calculated the "middle" value which is the most common value. The .min() and .max() functions were used to calculate the maximum and minimum values in each set of variables[2]. A package called Numpy, denoted as np, was used to calculate the standard deviation and the variance with the functions np.std() and np.var() [4]. The standard deviation measures how spread out the data is i.e how close each measurement is to the mean/average measurement [12]. The variance is similar to the standard deviation but calculates the spread of the data using a different formula[13].

## Sepal Length
The average measurement for the length of all three iris flower's sepals was 5.8cm. This mean value was also the same as the median so 5.8cm was the centre/middle value in all the recorded sepal lengths in the iris dataset when in ascending order. The shortest sepal length amongst all the flowers was 4.3cm and the longest was 7.9cm. This is quite a big difference, the smallest sepal length is not far off half the length of the longest sepal. The standard deviation was 0.83cm this means that the individual sepal length measurements are all within a 0.83cm distance from the mean. The variance was 0.68cm which along with standard deviation is small enough which means the data is unlikely to have any outliers.

## Sepal Width
The values for sepal width statistics are much smaller than sepal length with the average width measurement being 3.1cm which is very small. The median is very close with a value of 3.0cm. The maximum value the sepal width reaches is 4.4cm and the minimum value is 2.0cm so as with the sepal length theres quite a big difference in size between the smallest sepal width and the largest. However the measurements don't spread too far from the mean value which is shown by the calculates standard deviation of 0.43cm and variance of 0.19cm.

## Petal Length
The mean petal length of the iris flowers is 3.8cm which shows they have short petals on average. Unlike the sepal measurements the centre value of this data column is a bit off from the mean with a value of 4.35cm. Suprisingly the smallest petal length is 1cm which is very short. The longest petal of the flowers in the dataset is 6.9cm. All of these values are noticeably smaller than the sepal length values which shows the sepals are longer than the petals on these iris flowers. The standard deviation was 1.76cm and the variance was 3.06cm. These values are quite large which shows there is a large spread and variance amongst the petal length of the iris flowers. There are clearly a wide variety of petal lengths in the dataset.

## Petal Width
The average petal width is very skinny with a measurement of 1.2cm. The median is very close to the mean with a value of 1.3cm. Interestingly the minimum width recorded was an extremely small value of 0.1cm and the widest petal was 2.5cm. Given the small range of width measurements, the standard deviation at 0.76cm and variance at 0.58cm are quite big statistics. Just like the petal lengths, the petal widths of all the flowers vary alot.

## Species
For the sepal length of each species of flower all statistics were very similar to each other therefore I think it would be difficult to tell them apart based off of their sepal length. The average sepal length was shortest for the Iris-Setosa at 5.0cm, then the Iris-Versicolor was 5.9cm and the longest was the Iris-Virginica at 6.6cm. The medians were the same as the means except for Iris-Virginica which was only 0.1cm less than it's mean. Both the Iris-Versicolor and Iris-Virginica had the same minimum value of 4.9cm and Iris-Setosa had the smallest sepal length in the dataset with a value of 4.3cm. The longest sepal recorded was an Iris-Virginica at 7.9cm. The max values of the Iris-Setosa and Iris-Versicolor were 5.8cm and 7.0cm respectively.

The sepal widths of each species would also make it a challenge to diffrentiate between the 3 flowers. The average width of the Iris-Setosa, Iris-Versicolor and Iris-Virginica sepals are 3.4cm,2.8cm and 3.0cm respectively. The medians are exactly the same as the means. The Iris-Versicolor has the smallest width of 2.0cm recorded in the dataset. The Iris-Setosa has the largest sepal width recorded which is 4.4cm.

The petal lengths could be used to diffrentiate between the three types of flower. The shortest average petal length of 1.5cm was in the Iris-Setosa species group, then the Iris-Versicolor flowers had a mean of 5.6cm and the Iris-Virginica had the longest average petal length of 5.6cm. The values in the centre of the datasets were the same as the means. The flower with the max petal length recorded was the Iris-Virginica at 6.9cm. The longest petal found amongst the Iris-Setosa and Iris-Versicolor was a length of 1.9cm and 5.1cm respectively. The min petal length in the dataset was the Iris-Setosa at 1cm and the Iris-Versicolor had a shortest petal of length 3cm and Iris-Virginica was 4.5cm.

The average and median width of the petals on the Iris-Setosa were very small at 0.2cm. Then not too far off them was the Iris-Versicolor with a mean and median of 1.3cm and then the Iris-Virginica with mean and median of 2cm. The Iris-Virginica has the max value recorded for the petal width at 2.5cm and the Iris-Setosa has the thinnest width of 0.1cm out of the 150 iris flower samples.

After analysing these statistics it appears that out of the three iris species that in general Iris-Setosa's have the smallest petals and Iris-Virginica's have largest petals. It is also evident that Iris-Setosa's have the shortest sepal length of the three species but also have the widest sepal widths in the recorded data. The Iris-Virginica's have the longest recorded sepal lengths and Iris-Versicolor's have smallest sepal widths of all the flowers. 

# Histograms- Coding
Next I displayed the dataset using histograms. The following packages were imported and used for this section of code, Pandas as pd, Numpy as np and matplotlib.pyplot as plt. The iris dataset was read in as variable name "data". I used the .hist() function to create a histogram [6][7] and assigned the plot a variable name "graph". For each variable sepal length, sepal width, petal length and petal width I plotted three subplots showing the variables prroperites for each species. The first set of histograms, "Histogram_SepalLength", had "column" parameter equal to "SepalLength" so the x-axis represents the measurements recorded for each flower then the "by" parameter was equal to species to group each histogram based on which type of species the measurements correspond to. The next parameter in the .hist() function is "bins" which is the amount of clusters you want to put the data into so I chose 50 because I want to see each of the 50 measurements plotted separaretly instead of being joined with measurements near each other, this makes it easier to read and inspect the graph. The "legend" parameter was set to true so the it is clear what the bars on the graph represent with the legend in to top right corner of the graph. "grid" is set to True to show the axes grid lines. "figsize" sets the size of the graph, I just played with these numbers until a nice size was found and then "layout()" parameter set the layout for the three subplots in which I set it to be three rows and one on top of another. The colour of the bars were set to "m" which represents a pinky magenta colour. The next line of code sets the title of the x-axis to "Sepal Length(cm)" using the plt.xlabel function. I created a for loop to set the title of the y-axis in all the subplots to be "Count" using the ".set(ylabel="")" function and also to rotate the ticks along the x-axis to 0degrees to make the graph look neater, the ".tick_params(axis='x', labelrotation = 0)" function did this. Lastly I used the plt.savefig() function to output the histograms to a png file [11][15]. I used the same code for each group of subplots.

# Histograms - Analysis
Sepal Length Histograms: 
These three histograms for each species appear to be normally distributed as they have a bell shaped curve.

-After observering the histogram subplots I saw that the measurement recorded most amount of times for the    Iris-Setosa was both 5.0cm and 5.1cm which both had 8 recordings each. The least frequent measurements only  recorded once were 4.3cm,4.5cm,5.3cm and 5.8cm which is also the longest sepal length.

-For the Iris-Versicolor the most frequent measurements for sepal length all occuring five times each were 5.5cm,5.6cm and 5.7cm. There are 10 measurements in this set that were only recorded once

-For the Iris-Virginica the majority of the sepal lengths were around 6.3cm.

Sepal Width Histograms:
-The Iris-Setosa had 8 occurences of the measurement 3.4cm which explains why it is also it's mean and that the graph is normally distributed.

-The Iris-Versicolor also had 8 recorded measurements of 3.0cm, although these is the most frequent measurement it is larger than it's mean which means we get a graph that is skewed right.

-Close to a quarter of the 50 measurements recorded for Iris-Virginica were 3.0cm which is also it's mean so this graph was normally distributed.

Petal Length Histograms:
-14 out of 50 of the petal length recordings for Iris-Setosa were 1.5cm which is also clearly the mean.

-The Iris-Versicolor and Iris-Virginica both had a highest count of 7 for the respective measurements 4.5cm and 5.1cm.

Petal Width Histograms:
-The tallest bar seen out of all the histograms was for Iris-Setosa for petal width of 0.2cm. 58% of Iris-Setosa's petal widths recorded were 0.2cm.

-Iris-Versicolor had a count of 13 for it's most common measurement of 1.3cm.

-Iris-Virginica had 1.8cm as it's most frequent measurement.

# Scatterplots For Each Pair Of Variables Showing The Correlation Between Variables
When analysing this dataset I was curious to see if there was any relationship between the lengths and widths of the sepals and the lengths and widths of the petals. For example if the sepal lengths are long then so are the petals or if the sepal widths are small then sepal lengths are large. I used the seaborn package to carry out this analysis[16]. For the code I researched how to use seaborn for multivariate data plots[18] and I decided to use the "seaborn.pairplot" function as I think it displays the relationships between the variables well. Within this function I read in the dataset under the variable name data, set the hue parameter to "Species" because I wanted to look at the relationships of each variable based on the type of species and set the parameter kind equal to "scatter" because after trying a few plots the scatterplot proved to be easiest read and understand as you can clearly see the distance between the clusters of data which shows the closeness of their relationships with each other i.e how similar each flower is to another. Then I set the markers parameters to dots, stars and squares to represent the Iris-Setosa's, Iris-Versicolor's and Iris-Virginica's respectively so that aswell as the different colours this helps distinguish between species and lastly I set the height of the graphs equal to 3cm because when I set it abover 3cm all the information didn't print to the screen[16]. I then displayed the graph [17] and saved it as a png file [11].

## Analysing The Pairplot
The diagonal in the pairplot represents univariate data so like our histograms they just show the count for each variable but are displayed using density plots. The scatterplots are divided into two trianges separated by the diagonal with the density plots, both the upper and lower triangle contain the same information except the x and y axes are swapped so if sepal width is the y-axis and sepal length is the x-axis in lower triangle then in its corresponding plot in the upper triangle will have sepal length on the y-axis and sepal width on the x-axis. For my analysis I will just look at the lower triangle. 

The first pairplot in the lower triangle is the second row first column. This plot shows there is a positive correlation between the sepal length and sepal width of all three flowers but it is especially evident in the Iris-Setosa(represented by blue dots) as you can see a steep incline which translates to the sepal length increases as the sepal length increase. For the Iris-Versicolor(represented by orange stars) and Iris-Virginica(represented by green squares) the incline is alot more suble because there are a few outliers, it is also noticeable for these two flowers that they are almost the same in similarities with regards to sepal lengths and widths as their data points are on top of each other in this plot. This would make it hard to distinguish between them in a field when looking these properties but it would be easier to point out an Iris-Setosa as it appears to have smaller sepals.

The next pairplot is directly under the previous one displaying petal length and sepal length. There is clearly no correlation between these two variables in the Iris-Setosa group as the points create a stright horizonal line so the petal lengths stay the same even as the sepal lengths increase slightly. There is a strong positive correlation evident for both the other two flowers. For the similarities the Iris-Setosa as before is most disimilar which is shown by the distance of it's data points to the other sets of points. The Iris-Versicolor and Iris-Virginica have close proximity but not as close as the previous graph but still have some points overlapping so they are not the same but very similar. 

To the right of the previous plot is another displaying petal length vs sepal width. This graph represents much the same information as the previous one except for sepal width but the correlations and similarities have the same pattern so the same can be said as was for petal length vs sepal length.

The first pairplot on the next row, which is also the bottom of the lower triangle, shows petal width vs sepal length. Even though there are a few points in Iris-Setosa that appear to be inclining as a slope the majority of the points appear to be moving in a horizontal line so I would interpret them as not having any correlation between the two variables. The other two species have a positive slope so it appears their sepal lengths increase as their petal widths do. As for similarities Iris-setosas have much smaller petal widths which sets them down the bottom of the graph away from the other two flowers. The Iris-Versicolor and Iris-Virginica have almost the same sepal length measurements but their petal width ranges help separate the two sets of data.

The next pairplot to the right of the previous one displays petal width against sepal width. This graph shows a very similar pattern amongst the data as the previous one. The only noticeable difference is the sepal widths are lower down the measurement scale than sepal lengths as expected.

The last pairplot in the lower triangles demonstrates petal length vs petal width. For all three species this graph shows the strongest correlation between any two variables, all of the flowers have points sitting on or very close to the straight diagonal line x=y. This means that you can be certain that as petal widths increase then so do petal lengths at the same increase rate, they have a linear relationship. The similarities are the same as all our previous plots therefore it can be said that for all sepal and petal properties the Iris-Setosa has most dissimilarities and the other two flowers are very similar.

# Further analysis
Sometimes graphs can be difficult to read accurately and therefore are misinterpretted. For example I might think two clusters of data are very dissimilar if there is a good distance between them but the scale of the distances could be very small so they are not as far as it appears so to check my analysis for my pairplots I decided to calculate the correlation coefficient for each subplot. The correlation coefficient [19] is a number calculated the shows how strong a relationship two variables have with each other i.e does one variable influence the growth of the other variable and if so is it a negative influence or a positive one. The correlation coefficients is between 1 and -1 where 1 indicates a strong positive relationship, 0 represents no relationship and -1 represents a strong negative relationship. I used Pearson's correlation coefficient method in my code because it's the most popular [19]. The function I used in the code was ".corr(method="pearson")" [2], this created a table with all the correlation coefficients that I printed to a .txt file called "Correlation_Tables.txt" so it can be easily accessed[4]. I added in the code "groupby("Species")" to specify the correlation coefficient for each species[20].

## Analysis of correlation coefficients for species
The diagonal in the three tables is equal to 1 because it is measuring the the relationship between each variable and itself which is obviously the strongest relationship they can get. For the Iris-Setosa it only has one strong positive correlation coefficient of 0.75 for sepal width and sepal length which is close to 1. The rest of it's correlation coefficients are close to 0 showing no/very weak relationships. In comparison to my analysis of the pairplots it confirms my interpretations were accurate except for the reltionship between petal lengths and widths. This surprised me because I expected the correlation to be close to one but it has a weak correlation coefficient of 0.31. After taking another look at this pairplot I can see that if the points were plotted on a magnified scale between 0cm and 2cm then it may look like less of an incline.

The correlation coefficients for Iris-Versicolor are all positive and above 0.5 so there is a correlation there between each relationship but the strongest are between sepal length and petal length and between petal width and length. This confirms I accurately interpretted the pairplots for this species.

For the Iris-Verginica I was most surprised as I had interpretted it to have the same correlations as the Iris-Versicolor but it is evident that other than petal width vs sepal width and sepal length vs petal length, the rest of the relationships have a weak positive relationship. Just as in the Iris-Setosa calculations I was most inaccurate when interpretting petal length and width as it only has correlation coefficient of 0.32.

## Further analysis on the correlation coefficients
When first carrying out the above calculations for correlation coefficients I forgot that I needed to group by species and I printed a table of correlation coefficients for each variable not including species and I noticed alot of negative correlation coefficients. I was confused at first but then found it very interesting that even though for all three individual species there was no negative relationships but when you look at the dataset as a whole and analyse the sepals and petals properties in general there are negative influences in some cases.

After having another look at the pairplots I saw that the correlation coefficients do match up. There is a very weak negative correlation for petal length vs sepal width. The negative relationship between sepal width and length and between petal width and sepal width is more evident. They both have a moderate negative slope, this means that as sepal length increases sepal width decreases and as sepal width increases petal width decreases and vice versa. 

After researching the factors that affect the correlation [21] I have come to the conclusion the reason the correlation may have changed from positive to negative when analysing the dataset overall vs grouping by species could be because of the difference in some distribution shapes as some are skewed distributions aswell as normal distributions. It could also be due to outliers in the dataset but I don't think this is the reason as there are not that many outliers. I think the most viable reason is because of the variability in the dataset because the measurements for each type of flower are within different scale ranges. For example if you have three clusters of data placed in the plot in a position that appears to be a declining slope but within the clusters the data displays an increasing slope. After discovering this I believe it is more accurate to analyse the data grouped by type or else normalise the scales so that the size of measurements recorded don't affect the results.











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
[18]https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166
[19]https://www.statisticshowto.com/probability-and-statistics/correlation-coefficient-formula/
[20]https://www.statology.org/pandas-groupby-correlation/
[21]https://www.tandfonline.com/doi/abs/10.3200/JEXE.74.3.249-266