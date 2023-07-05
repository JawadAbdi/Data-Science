#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2, 3, 6, 4]

df = pd.DataFrame(data={'course_name': course_name, 'duration': duration})

# Print the data present in the second row using iloc
second_row = df.iloc[1]
print(second_row)


# In Pandas, the loc and iloc are both indexer functions used to access data in a DataFrame. However, they have different methods of indexing and selecting data:
# 
# loc: The loc indexer is label-based and is used to select data based on labels or boolean arrays along both the row and column axes.
# Syntax: df.loc[row_indexer, column_indexer]
# 
# iloc: The iloc indexer is integer-based and is used to select data based on integer positions along both the row and column axes.
# Syntax: df.iloc[row_indexer, column_indexer]

# In[10]:


import pandas as pd

course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2, 3, 6, 4]

df = pd.DataFrame(data={'course_name': course_name, 'duration': duration})

# Define the reindex order
reindex = [3, 0, 1, 2]

# Reindex the DataFrame
new_df = df.reindex(reindex)

# Print the new_df
print(new_df)

# Access row using loc
print(new_df.loc[2])

# Access row using iloc
print(new_df.iloc[2])


# The difference in the outputs arises because loc and iloc use different indexing methods:
# 
# new_df.loc[2] accesses the row with index label 2. In this case, after reindexing, the row with index label 2 corresponds to the course "Big Data" with a duration of 6. So, new_df.loc[2] returns the row with the label 2, which includes the values 'Big Data' and 6.
# 
# new_df.iloc[2] accesses the row with index position 2. After reindexing, the row with index position 2 corresponds to the course "Machine Learning" with a duration of 3. So, new_df.iloc[2] returns the row with the index position 2, which includes the values 'Machine Learning' and 3.
# 
# The difference is due to the fact that loc uses label-based indexing, whereas iloc uses integer-based indexing. Therefore, loc and iloc may return different results depending on the index labels and positions.
# 
# In summary, the difference in the outputs is because loc and iloc access the data based on different indexing methods: label-based indexing for loc and integer-based indexing for iloc.

# In[12]:


import pandas as pd
import numpy as np

columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1, 2, 3, 4, 5, 6]

# Creating a DataFrame
df1 = pd.DataFrame(np.random.rand(6, 6), columns=columns, index=indices)

# Calculate the mean of each column
column_means = df1.mean()
print("Mean of each column:")
print(column_means)
print()

# Calculate the standard deviation of 'column_2'
column_2_std = df1['column_2'].std()
print("Standard deviation of 'column_2':", column_2_std)


# In pandas, the "window functions" refer to a group of operations that are applied over a sliding window of data in a DataFrame or Series. These functions allow you to perform calculations and transformations on a specified window of data, such as rolling averages, cumulative sums, and more. Window functions are particularly useful for time series data and can provide insights into trends, patterns, and rolling statistics.
# 
# There are several types of window functions available in pandas, including:
# 
# Rolling Functions: These functions operate on a specified window of consecutive rows in the data. The window size can be defined using a fixed number of rows or a time-based offset. Some common rolling functions include:
# 
# rolling(): Provides access to various rolling window computations, such as mean, sum, min, max, etc.
# rolling().apply(): Applies a custom function to the rolling window.
# Expanding Functions: These functions calculate statistics that accumulate over time as more data points become available. The window size expands with each new row. Some common expanding functions include:
# 
# expanding(): Provides access to various expanding window computations, such as mean, sum, min, max, etc.
# expanding().apply(): Applies a custom function to the expanding window.
# EWM (Exponentially Weighted Moving) Functions: These functions assign weights to each data point based on its age or position within the window. Recent data points have higher weights than older data points, allowing for calculations that give more importance to recent observations. Some common EWM functions include:
# 
# ewm(): Provides access to various exponentially weighted moving window computations, such as mean, sum, min, max, etc.
# ewm().apply(): Applies a custom function to the exponentially weighted moving window.
# These window functions can be applied to both DataFrame columns and Series objects in pandas, providing powerful tools for analyzing and transforming data over specified windows. They offer flexibility in handling time series data and enable various calculations and aggregations to be performed efficiently.

# In[23]:


import pandas as pd
from datetime import datetime

# Get the current date and time
current_date = datetime.now()

# Extract the month and year
current_month = current_date.month
current_year = current_date.year

# Create a pandas datetime object
pandas_datetime = pd.to_datetime(f"{current_year}-{current_month}")

# Print the current month and year
print("Current Month:", pandas_datetime.strftime("%B"))
print("Current Year:", current_year)


# In[25]:


import pandas as pd

# Prompt the user to enter the dates
date1 = input("Enter the first date (YYYY-MM-DD): ")
date2 = input("Enter the second date (YYYY-MM-DD): ")

# Convert the input dates to Pandas datetime objects
date1 = pd.to_datetime(date1)
date2 = pd.to_datetime(date2)

# Calculate the time difference
time_diff = date2 - date1

# Extract the difference in days, hours, and minutes
days_diff = time_diff.days
hours_diff = time_diff.seconds // 3600
minutes_diff = (time_diff.seconds % 3600) // 60

# Display the result
print("Time difference: {} days, {} hours, {} minutes.".format(days_diff, hours_diff, minutes_diff))


# In[29]:


import pandas as pd

# Prompt the user to enter the file path
file_path = input("Enter the file path: ")

# Prompt the user to enter the column name
column_name = input("Enter the column name: ")

# Prompt the user to enter the category order
category_order = input("Enter the category order (comma-separated): ").split(",")

# Read the CSV file
df = pd.read_csv(file_path)

# Convert the specified column to categorical data type with specified category order
df[column_name] = pd.Categorical(df[column_name], categories=category_order, ordered=True)

# Sort the data based on the specified column
sorted_data = df.sort_values(by=column_name)

# Display the sorted data
print(sorted_data)


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt

# Prompt the user to enter the file path
file_path = input("Enter the file path: ")

# Read the CSV file
df = pd.read_csv(file_path)

# Convert the 'Date' column to datetime data type
df['Date'] = pd.to_datetime(df['Date'])

# Group the data by product category and date, and calculate the sum of sales
grouped_data = df.groupby(['Product Category', 'Date'])['Sales'].sum().reset_index()

# Pivot the data to have product categories as columns and dates as index
pivot_data = grouped_data.pivot(index='Date', columns='Product Category', values='Sales')

# Plot the stacked bar chart
pivot_data.plot(kind='bar', stacked=True)

# Set the labels and title
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales of Product Categories over Time')

# Show the chart
plt.show()


# In[ ]:


import pandas as pd
from tabulate import tabulate

# Prompt the user to enter the file path
file_path = input("Enter the file path of the CSV file containing the student data: ")

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Calculate the mean, median, and mode of the test scores
mean_score = df['Test Score'].mean()
median_score = df['Test Score'].median()
mode_scores = df['Test Score'].mode()

# Format the mode scores as a string
mode_scores_str = ', '.join(map(str, mode_scores))

# Create a table to display the results
table = [['Statistic', 'Value'],
         ['Mean', mean_score],
         ['Median', median_score],
         ['Mode', mode_scores_str]]

# Display the table
print(tabulate(table, headers='firstrow', tablefmt='grid'))


# In[ ]:




