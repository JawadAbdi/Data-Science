#!/usr/bin/env python
# coding: utf-8

# Matplotlib is a popular data visualization library for Python. It provides a wide range of functions and tools for creating various types of plots and charts. Matplotlib is widely used in fields such as data analysis, scientific research, and machine learning.
# 
# Here are five types of plots that can be created using the Pyplot module of Matplotlib:
# 
# Line Plot: Line plots are used to visualize the relationship between two variables by connecting data points with straight lines. They are commonly used to show trends or changes over time.
# 
# Scatter Plot: Scatter plots display the relationship between two variables as individual data points. Each point represents a single observation, and the position of the point on the plot corresponds to the values of the variables.
# 
# Bar Plot: Bar plots represent data using rectangular bars. They are often used to compare and display categorical data or to show the distribution of a variable across different categories.
# 
# Histogram: Histograms are used to represent the distribution of a continuous variable. They display the frequencies or counts of data points within specific intervals, known as bins.
# 
# Pie Chart: Pie charts are circular plots divided into sectors, where each sector represents a category or a proportion of the whole. They are commonly used to visualize proportions or percentages.

# A scatter plot is a type of plot used to visualize the relationship between two variables. It represents individual data points as dots on a graph, with the position of each dot corresponding to the values of the variables. Scatter plots are useful for identifying patterns, trends, or correlations between the variables.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3)
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))

# Plotting the scatter plot
plt.scatter(x, y)

# Adding title, xlabel, and ylabel
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')

# Displaying the plot
plt.show()


# The subplot() function in Matplotlib is used to create multiple plots within a single figure. It allows you to arrange plots in a grid-like structure, specifying the number of rows, number of columns, and the index of the current plot.

# In[2]:


import numpy as np
import matplotlib.pyplot as plt

# Data for line 1
x1 = np.array([0, 1, 2, 3, 4, 5])
y1 = np.array([0, 100, 200, 300, 400, 500])

# Data for line 2
x2 = np.array([0, 1, 2, 3, 4, 5])
y2 = np.array([50, 20, 40, 20, 60, 70])

# Data for line 3
x3 = np.array([0, 1, 2, 3, 4, 5])
y3 = np.array([10, 20, 30, 40, 50, 60])

# Data for line 4
x4 = np.array([0, 1, 2, 3, 4, 5])
y4 = np.array([200, 350, 250, 550, 450, 150])

# Creating the subplots
plt.subplot(2, 2, 1)  # 2 rows, 2 columns, subplot 1
plt.plot(x1, y1)
plt.title('Line 1')

plt.subplot(2, 2, 2)  # 2 rows, 2 columns, subplot 2
plt.plot(x2, y2)
plt.title('Line 2')

plt.subplot(2, 2, 3)  # 2 rows, 2 columns, subplot 3
plt.plot(x3, y3)
plt.title('Line 3')

plt.subplot(2, 2, 4)  # 2 rows, 2 columns, subplot 4
plt.plot(x4, y4)
plt.title('Line 4')

# Adjusting the layout
plt.tight_layout()

# Displaying the plots
plt.show()


# A bar plot, also known as a bar chart, is a type of plot used to represent categorical data with rectangular bars. Each bar represents a category, and the length or height of the bar corresponds to the magnitude of the data or a specific value associated with the category. Bar plots are useful for comparing and visualizing the distribution, frequency, or magnitude of different categories or groups.

# In[3]:


import numpy as np
import matplotlib.pyplot as plt

company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])

# Creating a bar plot
plt.figure(figsize=(8, 6))  # Adjusting the figure size
plt.bar(company, profit)

# Adding title, xlabel, and ylabel to the bar plot
plt.title('Company Profits')
plt.xlabel('Company')
plt.ylabel('Profit (in millions)')

# Displaying the bar plot
plt.show()


# In[4]:


import numpy as np
import matplotlib.pyplot as plt

company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])

# Creating a horizontal bar plot
plt.figure(figsize=(8, 6))  # Adjusting the figure size
plt.barh(company, profit)

# Adding title, xlabel, and ylabel to the horizontal bar plot
plt.title('Company Profits')
plt.xlabel('Profit (in millions)')
plt.ylabel('Company')

# Displaying the horizontal bar plot
plt.show()


# A box plot, also known as a box-and-whisker plot, is a type of statistical plot used to display the distribution and summary statistics of a dataset. It provides a visual representation of the minimum, first quartile (25th percentile), median (50th percentile), third quartile (75th percentile), and maximum values of the dataset, along with any outliers.

# In[5]:


import numpy as np
import matplotlib.pyplot as plt

box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)

# Combine the data into a single list
data = [box1, box2]

# Creating the box plot
plt.figure(figsize=(8, 6))  # Adjusting the figure size
plt.boxplot(data)

# Adding title and labels to the box plot
plt.title('Box Plot')
plt.xlabel('Box')
plt.ylabel('Value')

# Displaying the box plot
plt.show()


# In[ ]:




