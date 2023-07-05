#!/usr/bin/env python
# coding: utf-8

# Certainly! Here are five commonly used functions in the pandas library along with their execution:
# 
# read_csv(): This function is used to read data from a CSV file and create a DataFrame.
# 
# head(): This function returns the first n rows of a DataFrame. By default, it returns the first 5 rows.
# 
# groupby(): This function is used to group data based on one or more columns and perform aggregation or analysis on the grouped data.
# 
# fillna(): This function is used to fill missing values in a DataFrame with specified values or strategies.
# 
# to_csv(): This function is used to save a DataFrame to a CSV file.

# In[9]:


file_path = r'C:\Users\razaj\Downloads\services.csv'

df = pd.read_csv(file_path)

# Perform operations on the DataFrame as needed
# ...

# Print a preview of the DataFrame
print(df)


# In[10]:



print(df.head(2))


# In[13]:


grouped = df.groupby('id')['location_id'].mean()
print(grouped)


# In[19]:


fill = df.fillna(df.mean(), inplace=True)
print(fill)


# In[20]:


cv=df.to_csv(file_path, index=False)
print(cv)


# In[ ]:




