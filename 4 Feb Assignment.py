#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Q1.

data = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)] 
sorted_data = sorted(data, key=lambda x: x[0])

for item in sorted_data:
    print(item)


# In[4]:


#Q2.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
squared_numbers = list(map(lambda x: x**2, numbers))

print(squared_numbers)


# In[5]:


#Q3.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
string_tuple = tuple(map(lambda x: str(x), numbers))

print(string_tuple)


# In[6]:


#Q4.

from functools import reduce
numbers = list(range(1, 26))
product = reduce(lambda x, y: x * y, numbers)

print(product)


# In[7]:


#Q5.

numbers = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46] 
filtered_numbers = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, numbers))

print(filtered_numbers)


# In[8]:


#Q6.

strings = ['python', 'php', 'aba', 'radar', 'level'] 
palindromes = list(filter(lambda x: x == x[::-1], strings))

print(palindromes)


# In[ ]:




