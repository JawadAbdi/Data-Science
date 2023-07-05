#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = [4, 8, 15, 16, 23, 42]
series = pd.Series(data)

print(series)


# In[2]:


import pandas as pd

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
series = pd.Series(my_list)

print(series)


# In[3]:


import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Claire'],
    'Age': [25, 30, 27],
    'Gender': ['Female', 'Male', 'Female']
}

df = pd.DataFrame(data)

print(df)


# In Pandas, a DataFrame is a two-dimensional labeled data structure that represents a table of data with rows and columns. It is one of the most commonly used data structures in Pandas and provides a flexible and efficient way to work with structured data.
# 
# On the other hand, a Series in Pandas is a one-dimensional labeled array-like object that can hold any data type. It can be considered as a single column of data from a DataFrame. A Series consists of two main components: an index and the corresponding data values.

# Pandas provides a wide range of functions and methods to manipulate data in a DataFrame. Here are some common functions and methods you can use:
# 
# head() and tail(): These functions allow you to retrieve the first few rows (head()) or the last few rows (tail()) of a DataFrame. They are useful for quickly inspecting the structure and content of the DataFrame.
# 
# info(): This function provides a concise summary of a DataFrame, including the data types, column names, and the number of non-null values. It helps in understanding the overall structure and data types of the DataFrame.
# 
# describe(): This function computes various summary statistics of the numerical columns in a DataFrame, such as count, mean, standard deviation, minimum, maximum, and quartiles. It provides a quick overview of the distribution and central tendency of the data.
# 
# sort_values(): This method allows you to sort a DataFrame by one or more columns. You can specify the column(s) to sort by and the sort order (ascending or descending). Sorting is useful when you want to arrange the data in a specific order.
# 
# groupby(): This method enables grouping of data based on one or more columns. It allows you to perform aggregation, transformation, or filtering operations on the grouped data. It is useful when you want to analyze data based on certain categories or variables.
# 
# fillna(): This method is used to fill missing values in a DataFrame with specified values or using specific strategies, such as filling with the mean or median of the column. It helps in handling missing data and making the DataFrame complete.
# 
# apply() and map(): These methods allow you to apply a custom function or a built-in function to manipulate the data in a column or DataFrame. They are useful when you need to perform element-wise operations or transform the data based on specific conditions.
# 
# These are just a few examples of common functions and methods in Pandas for data manipulation. Pandas provides a rich set of functions that can handle various data manipulation tasks efficiently and effectively.

# In[4]:


# Retrieve the first 5 rows of a DataFrame
df.head(5)

# Display summary information about the DataFrame
df.info()

# Generate descriptive statistics of the DataFrame
df.describe()

# Sort the DataFrame by the 'Age' column in descending order
df.sort_values('Age', ascending=False)

# Group the DataFrame by the 'Gender' column and calculate the average age for each group
df.groupby('Gender')['Age'].mean()


# Fill missing values in the 'Age' column with the mean age
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Apply a lambda function to calculate the square of values in the 'Age' column
df['Age'].apply(lambda x: x ** 2)


# Map the values in the 'Gender' column to numerical codes
gender_mapping = {'Male': 0, 'Female': 1}
df['Gender'] = df['Gender'].map(gender_mapping)


# In Pandas, the Series and DataFrame objects are mutable, while the Panel object is not mutable.

# In[5]:


import pandas as pd

# Creating Series objects
name_series = pd.Series(['Alice', 'Bob', 'Claire'])
age_series = pd.Series([25, 30, 27])
gender_series = pd.Series(['Female', 'Male', 'Female'])

# Creating a DataFrame using the Series
data = {'Name': name_series, 'Age': age_series, 'Gender': gender_series}
df = pd.DataFrame(data)

# Printing the DataFrame
print(df)


# In[ ]:




