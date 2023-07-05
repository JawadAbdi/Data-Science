#!/usr/bin/env python
# coding: utf-8

# Yes, there is a difference in the data type of the variables list_ and array_list.
# 
# The variable list_ is a Python list, while the variable array_list is a NumPy array.
# 
# To print the data types of both variables, you can use the type() function:

# In[3]:


import numpy as np

list_ = ['1', '2', '3', '4', '5']
array_list = np.array(object=list_)

print("Data type of list_:", type(list_))
print("Data type of array_list:", type(array_list))


# In[6]:


import numpy as np

list_ = ['1', '2', '3', '4', '5']
array_list = np.array(object=list_)

# Print data types of elements in list_
print("Data types of elements in list_:")
for element in list_:
    print(type(element))

# Print data types of elements in array_list
print("\nData types of elements in array_list:")
for element in array_list:
    print(type(element))


# Yes, there will be a difference in the data type of the elements present in list_ and array_list after applying the dtype=int parameter.
# 
# The dtype=int parameter specifies that the elements in the array_list should have an integer data type.
# 
# To print the data types of each element in both list_ and array_list, you can use a loop and the type() function. Here's an example code:

# In[7]:


import numpy as np

list_ = ['1', '2', '3', '4', '5']
array_list = np.array(object=list_, dtype=int)

# Print data types of elements in list_
print("Data types of elements in list_:")
for element in list_:
    print(type(element))

# Print data types of elements in array_list
print("\nData types of elements in array_list:")
for element in array_list:
    print(type(element))


# In[8]:


import numpy as np

num_list = [[1, 2, 3], [4, 5, 6]]
num_array = np.array(object=num_list)

# (i) Shape of the num_array
print("Shape of num_array:", num_array.shape)

# (ii) Size of the num_array
print("Size of num_array:", num_array.size)


# In[20]:


import numpy as np

# Create a 3x3 matrix of zeros
array = np.arange(2,11).reshape(3,3)
# Print the zeros array
print(array)


# In[21]:


import numpy as np

# Create a 5x5 identity matrix
identity_matrix = np.eye(5)

# Print the identity matrix
print(identity_matrix)


# In[ ]:




