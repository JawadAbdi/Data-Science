#!/usr/bin/env python
# coding: utf-8

# Q1. Characteristics of tuples:-
# -> Both heterogeneous and homogeneous data are stored in tuples.
# -> In nature, tuples are immutable.
# -> To navigate a tuple, use an index.
# -> Tuples are ordered.
# -> They can contain duplicate items
# Tuples are immutable in nature

# Q2. There are 2 tuple methods in python:
#     -> count()- This method returns the number of times a specific value occurs                 in a tuple.
#     -> index()- This method searches the tuple for a specific value after which                 it returns the position of the specific value.
# 
# Examples 
# tuple = (1, 2, 3, 1, 2, 3, 1, 2, 3)
# tuple.count(3)   
# tuple = (1, 2, 3, 1, 2, 3, 1, 2, 3)
# tuple.index(3)   
# 
# There are only two built-in methods that can be used on a tuple. This is because methods that can add or remove items are not available in the tuple.
# Since tuple() is immutable, therefore, it does not change after the initial assigning of items. The methods used on a tuple are count() and index().

# Q3. Set is a collection which is unordered and unindexed. No duplicate members.

# In[12]:


# Write a code using a set to remove  duplicates from the given list. 
List = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4] 
set1 = set(List)
print(set1)


# Q4. union() and update() are both methods in Python's built-in set class that allow you to combine sets. However, they differ in their behavior.
# 
# The union() method returns a new set that contains all the unique elements from both the original set and another set that you pass as an argument. It does not modify the original set or the other set that you pass as an argument.
# 
# On the other hand, the update() method modifies the original set by adding all the unique elements from another set that you pass as an argument.
# 
# So, the main difference between the union() and update() methods is that union() returns a new set without modifying the original set, while update() modifies the original set by adding the unique elements from another set.

# In[16]:


#Examples

#Union

set1 = {1, 2, 3}
set2 = {2, 3, 4}
union_set = set1.union(set2)
print(union_set)

#Update

set1 = {1, 2, 3}
set2 = {2, 3, 4}
update_set = set1.update(set2)
print(update_set)


# Q5. A dictionary is a built-in data structure that allows you to store a collection of key-value pairs. The keys are unique identifiers that map to corresponding values. Dictionaries are also sometimes referred to as associative arrays, maps, or hash tables in other programming languages.
# A dictionary is created using a pair of braces {} and defining the key-value pairs within it, separated by colons :.
# 
# Dictionaries are unordered collections, meaning that the order in which the key-value pairs are defined in the dictionary is not preserved.

# In[19]:


# Dictionary Example

student = {'name': 'Alice', 'age': 22, 'major': 'Computer Science'}


# Q6. Yes we can create a nested dictionary.

# In[22]:


# Nested dictionary example

employee = {'name': 'John','age': 30,'department': {'name': 'IT','location': 'New York'}}
print(employee['department']['name'])


# In[24]:


# Program(7)

dict1 = {'language' : 'Python', 'course': 'Data Science Masters'}
dict1.setdefault('topics', ['Python', 'Machine Learning', 'Deep Learning'])
print(dict1)


# Q8. In Python, a dictionary has three view objects that allow you to view the keys, values, and key-value pairs of a dictionary:
# 
# dict.keys(): Returns a view object that contains the keys of the dictionary.
# dict.values(): Returns a view object that contains the values of the dictionary.
# dict.items(): Returns a view object that contains the key-value pairs of the dictionary as tuples.

# In[26]:


#Example

dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']} 

print(dict1.keys())
print(dict1.values())
print(dict1.items())


# In[ ]:




