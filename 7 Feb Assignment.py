#!/usr/bin/env python
# coding: utf-8

# In[1]:


string = "Hello, World!"

# Using lambda function and startswith() method
starts_with_letter = lambda s, letter: s.startswith(letter)
result = starts_with_letter(string, "H")
print(result)  # Output: True


# In[2]:


string = "12345"

# Using lambda function and isnumeric() method
is_numeric = lambda s: s.isnumeric()
result = is_numeric(string)
print(result)  # Output: True


# In[3]:


fruits = [("mango", 99), ("orange", 80), ("grapes", 1000)]

# Using lambda function and sorted() function
sorted_fruits = sorted(fruits, key=lambda x: x[1])
print(sorted_fruits)
# Output: [('orange', 80), ('mango', 99), ('grapes', 1000)]


# In[4]:


# Using list comprehension and lambda function
squares = [x**2 for x in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# In[5]:


import math

# Using list comprehension and lambda function
cube_roots = [math.pow(x, 1/3) for x in range(1, 11)]
print(cube_roots)  # Output: [1.0, 1.2599210498948732, 1.4422495703074083, 1.5874010519681994, 1.7099759466766968, 1.8171205928321397, 1.912931182772389, 2.0, 2.080084356959949, 2.154434690031884]


# In[6]:


number = 6

# Using lambda function and modulo operator
is_even = lambda n: n % 2 == 0
result = is_even(number)
print(result)  # Output: True


# In[7]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter() function and lambda function
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # Output: [1, 3, 5, 7, 9]


# In[8]:


numbers = [1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, 0]

# Using list comprehension and lambda function
positive_numbers = [x for x in numbers if x > 0]
negative_numbers = [x for x in numbers if x < 0]

print(positive_numbers)  # Output: [1, 2, 3, 4, 5, 6]
print(negative_numbers)  # Output: [-1, -2, -3, -4,


# In[9]:


import re

def validate_password(password):
    # Check length of the password
    if len(password) != 10:
        return "Invalid Password"
    
    # Count uppercase and lowercase letters
    uppercase_count = sum(1 for char in password if char.isupper())
    lowercase_count = sum(1 for char in password if char.islower())
    
    # Check the count of uppercase and lowercase letters
    if uppercase_count < 2 or lowercase_count < 2:
        return "Invalid Password"
    
    # Check if the password contains a number
    if not any(char.isdigit() for char in password):
        return "Invalid Password"
    
    # Check if the password contains at least three special characters
    special_chars = re.findall(r'[!@#$%^&*]', password)
    if len(special_chars) < 3:
        return "Invalid Password"
    
    # If all conditions are satisfied, the password is valid
    return "Valid Password"


# In[12]:


password1 = "ABCdef!£$"
password2 = "Password123"

print(validate_password(password1))  # Output: Valid Password
print(validate_password(password2))  # Output: Invalid Password


#Facing error in validation


# In[ ]:




