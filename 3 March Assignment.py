#!/usr/bin/env python
# coding: utf-8

# Seaborn is a popular Python data visualization library built on top of Matplotlib. It provides a high-level interface for creating attractive and informative statistical graphics. Here are five commonly used plots that can be created using Seaborn:
# 
# Scatter Plot:
# 
# Uses: Scatter plots are used to visualize the relationship between two continuous variables. They can help identify patterns, correlations, or clusters in the data.
# Line Plot:
# 
# Uses: Line plots are suitable for displaying trends or changes in a variable over time or other continuous domains. They are often used to visualize time series data or trends in experimental results.
# Bar Plot:
# 
# Uses: Bar plots are effective for comparing categories or groups. They can show the distribution or magnitude of a variable across different categories or display aggregated values such as means or sums.
# Histogram:
# 
# Uses: Histograms are used to understand the distribution of a single variable. They group data into bins and display the frequency or count of observations in each bin, providing insights into the data's shape and central tendencies.
# Heatmap:
# 
# Uses: Heatmaps are particularly useful for visualizing correlation matrices or matrices of numerical values. They use color intensity to represent values, allowing you to identify patterns, clusters, or relationships between variables.

# In[5]:


import seaborn as sns
import matplotlib.pyplot as plt

# Load the "fmri" dataset
fmri_data = sns.load_dataset("fmri")

# Plot the line plot
sns.lineplot(data=fmri_data, x="timepoint", y="signal", hue="event", style="region")

# Set the title and labels
plt.title("FMRI Signal over Time")
plt.xlabel("Timepoint")
plt.ylabel("Signal")

# Show the plot
plt.show()


# In[4]:


import seaborn as sns
import matplotlib.pyplot as plt

# Load the "titanic" dataset
titanic_data = sns.load_dataset("titanic")

# Create the first box plot (pclass vs age)
plt.subplot(1, 2, 1)  # Create a subplot for the first box plot
sns.boxplot(data=titanic_data, x="pclass", y="age")
plt.title("Pclass vs Age")  # Set title for the first box plot

# Create the second box plot (pclass vs fare)
plt.subplot(1, 2, 2)  # Create a subplot for the second box plot
sns.boxplot(data=titanic_data, x="pclass", y="fare")
plt.title("Pclass vs Fare")  # Set title for the second box plot

# Adjust the layout
plt.tight_layout()

# Show the plot
plt.show()


# In[6]:


import seaborn as sns
import matplotlib.pyplot as plt

# Load the "diamonds" dataset
diamonds_data = sns.load_dataset("diamonds")

# Plot the histogram
sns.histplot(data=diamonds_data, x="price", hue="cut", multiple="stack")

# Set the title and labels
plt.title("Histogram of Diamond Prices")
plt.xlabel("Price")
plt.ylabel("Count")

# Show the plot
plt.show()


# In[7]:


import seaborn as sns

# Load the "iris" dataset
iris_data = sns.load_dataset("iris")

# Plot the pair plot
sns.pairplot(data=iris_data, hue="species")

# Show the plot
plt.show()


# In[8]:


import seaborn as sns

# Load the "flights" dataset
flights_data = sns.load_dataset("flights")

# Reshape the data into a pivot table format
flights_pivot = flights_data.pivot("month", "year", "passengers")

# Plot the heatmap
sns.heatmap(data=flights_pivot, annot=True, fmt="d", cmap="YlGnBu")

# Set the title and labels
plt.title("Passenger Count by Year and Month")
plt.xlabel("Year")
plt.ylabel("Month")

# Show the plot
plt.show()


# In[ ]:




