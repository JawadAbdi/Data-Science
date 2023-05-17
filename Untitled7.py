#!/usr/bin/env python
# coding: utf-8

# In[11]:


def calculate_product(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, (list, tuple, set)):
            flat_list.extend(calculate_product(item))
        elif isinstance(item, dict):
            flat_list.extend(calculate_product(list(item.keys())))
            flat_list.extend(calculate_product(list(item.values())))
        elif isinstance(item, (int, float)):
            flat_list.append(item)
    
    product = 1
    for num in flat_list:
        product *= num
    
    return product


# In[15]:


lst = [1, 2, 3, 4, [44, 55, 66, True], False, (34, 56, 78, 89, 34), {1, 2, 3, 3, 2, 1}, {1: 34, "key2": [55, 67, 78, 89], 4: (45, 22, 61, 34)}, [56, 'data science'], 'Machine Learning']
result = calculate_product(lst)
print(result)  # Output: 121,170,176,384


# In[16]:


def encrypt_message():
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(219 - ord(char))  # Mapping the characters to their encrypted counterparts
            else:
                encrypted_char = chr(219 - ord(char.lower())).upper()  # Converting uppercase characters to lowercase encrypted counterparts
        elif char.isspace():
            encrypted_char = '$'  # Replacing whitespace with a dollar sign
        else:
            encrypted_char = char  # Keeping punctuation marks unchanged
        encrypted_message += encrypted_char
    return encrypted_message

# Input sentence
input_sentence = "I want to become a Data Scientist."

# Convert the input sentence to lowercase
lowercase_sentence = input_sentence.lower()

# Encrypt the lowercase sentence
encrypted_sentence = encrypt_message(lowercase_sentence)

print("Encrypted Sentence:", encrypted_sentence)


# In[17]:


def get_product(lst):
    product = 1
    for element in lst:
        if isinstance(element, (int, float)):
            product *= element
        elif isinstance(element, list):
            product *= get_product(element)
        elif isinstance(element, dict):
            product *= get_product(element.values())
    return product

# Test list
list1 = [1, 2, 3, 4, [44, 55, 66, True], False, (34, 56, 78, 89, 34), {1, 2, 3, 3, 2, 1}, {1: 34, "key2": [55, 67, 78, 89], 4: (45, 22, 61, 34)}, [56, 'data science'], 'Machine Learning']

result = get_product(list1)
print("Product of all numbers in the list:", result)


# In[ ]:




