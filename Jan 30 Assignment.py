#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Program (1) to display according to %

perc = int(input('Enter Percentage of student: '))

if perc > 90:
    print('A Grade')
elif perc > 80 and perc <=90:
    print('B Grade')
elif perc >=60 and perc <=80:
    print('C Grade')
else:
    print('D Grade')        


# In[20]:


#Program (2) to display road tax to be paid according to criteria

price = int(input('Price of Bike: '))

if price > 100000:
    print('Tax to be paid:',price*0.15)
elif price >50000 and price <=100000:
    print('Tax to be paid:',price*0.10)
else:
    print('Tax to be paid:',price*0.05)


# In[30]:


#Program (3) to display monuments of cities

city = input('Enter City: ')
if city == 'Delhi':
    print('Red Fort')
elif city == 'Agra':
    print('Taj Mahal')
elif city == 'Jaipur':
    print('Jal Mahal')
else:
    print()


# In[70]:


#Program (4) to check how many times a given number can be dvided by 3 before it is less than or equals to 10

num = int(input('Enter a number: '))
count = 0

while num >= 10:
    num /= 3
    count += 1
print('Number can be divided by 3 is:',count,',before it is less than or equals to 10.')


# #Program (5) When and why to use while loop with example
# 
# While loop falls under the category of indefinite iteration. Indefinite iteration means that the number of times the loop is executed isn’t specified explicitly in advance. 
# 
# Statements represent all the statements indented by the same number of character spaces after a programming construct are considered to be part of a single block of code. Python uses indentation as its method of grouping statements. When a while loop is executed, expr is first evaluated in a Boolean context and if it is true, the loop body is executed. Then the expr is checked again, if it is still true then the body is executed again and this continues until the expression becomes false.

# In[72]:


#Program (5) while loop example

num=1

while num <=10:
    print('12 x',num,'=',12*num )
    num+=1


# In[75]:


#Program (6) nested while to print 3 different patterns

# Pattern 1
print("Pattern 1:")
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print()
    row += 1

# Pattern 2
print("\nPattern 2:")
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print('+', end="")
        col += 1
    print()
    row += 1

# Pattern 3
print("\nPattern 3:")
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print('-', end="")
        col += 1
    print()
    row += 1


# In[76]:


#Program(7) reverse while loop to display number 10 to 1

number = 10

while number >= 1:
    print(number)
    number -= 1

