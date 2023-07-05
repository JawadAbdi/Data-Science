#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import plotly.express as px

# Load the "titanic" dataset
titanic_data = sns.load_dataset("titanic")

# Create the scatter plot using Plotly Express
scatter_plot = px.scatter(titanic_data, x="age", y="fare")

# Show the scatter plot
scatter_plot.show()


# In[2]:


import plotly.express as px

# Load the "tips" dataset from Plotly
tips_data = px.data.tips()

# Create the box plot using Plotly Express
box_plot = px.box(tips_data, x="day", y="total_bill", color="time", notched=True)

# Show the box plot
box_plot.show()


# In[3]:


import plotly.express as px

# Load the "tips" dataset from Plotly
tips_data = px.data.tips()

# Create the histogram using Plotly Express
histogram = px.histogram(
    tips_data,
    x="sex",
    y="total_bill",
    color="day",
    pattern_shape="smoker",
    barmode="group",
    nbins=10
)

# Show the histogram
histogram.show()


# In[6]:


import plotly.express as px

# Load the "iris" dataset from Plotly
iris_data = px.data.iris()

# Create the scatter matrix plot using Plotly Express
scatter_matrix = px.scatter_matrix(
    iris_data,
    dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
    color="species"
)

# Show the scatter matrix plot
scatter_matrix.show()


# Distplot, short for "Distribution Plot," is a plot used to visualize the distribution of a univariate dataset. It combines a histogram with a kernel density estimation (KDE) plot, providing a smooth estimate of the underlying distribution.
# 
# To plot a distplot using Plotly Express, you can use the distplot() function from the plotly.figure_factory module. However, please note that the distplot() function is deprecated in Plotly and is not recommended for new code. Instead, it is recommended to use the histogram() function from Plotly Express for histogram plots and the kdeplot() function for KDE plots.

# In[8]:


import plotly.subplots as sp
import plotly.graph_objects as go
import plotly.express as px

# Load an example dataset
data = px.data.tips()

# Create a subplot with a distribution plot
fig = sp.make_subplots(rows=1, cols=2)

# Add the histogram
fig.add_trace(go.Histogram(x=data["total_bill"], nbinsx=30), row=1, col=1)

# Add the KDE plot


# In[ ]:




