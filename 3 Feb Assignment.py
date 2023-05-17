#!/usr/bin/env python
# coding: utf-8

# Q1. def keyword is used to create a function.

# In[21]:


#List creation

def num(*args):
    l=[]
    for i in (args):
        if type(i)==list:
            for j in (i):
                if j%2==1:
                    print(args)
                    l.append(j)


# In[23]:


num([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])


# In[37]:


def num():
    l = []
    for num in range(1, 26):
        if num % 2 != 0:
            l.append(num)
    return l


# In[38]:


num()


# Q2. In Python, *args and **kwargs are used to pass a variable number of arguments to a function.
# 
# The *args parameter allows a function to accept any number of positional arguments. It collects all the additional positional arguments passed to the function into a tuple.
# 
# On the other hand, **kwargs allows a function to accept any number of keyword arguments. It collects the additional keyword arguments passed to the function into a dictionary.

# In[59]:


#Examples

def string(*args):
    result = ""
    for arg in args:
        result += arg
    return result


def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# In[60]:


string('mohd', ' ','jawad',' ','raza',' ', 'abdi')


# In[61]:


info(name='jawad', age=22, course='bca')


# Q3. In Python, an iterator is an object that implements the iterator protocol, which consists of the __iter__ and __next__ methods. Iterators are used to iterate over a sequence of elements, such as a list, without the need to store the entire sequence in memory.
# 
# The __iter__ method is used to initialize the iterator object and returns the iterator itself. The __next__ method is used for iteration and returns the next element in the sequence. When there are no more elements to iterate over, it raises the StopIteration exception.

# In[62]:


#Example

def list_iterator(data):
    index = 0
    while index < len(data):
        yield data[index]
        index += 1
my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
my_iterator = list_iterator(my_list)

for _ in range(5):
    print(next(my_iterator))


# Q4. In Python, a generator function is a special type of function that uses the yield keyword instead of the return keyword to return values. It allows you to define an iterator in a more concise and elegant way. When a generator function is called, it returns an iterator object that can be iterated over using a for loop or by calling the next() function.
# 
# The yield keyword is used in a generator function to produce a value without terminating the function's execution. When the yield statement is encountered, the function's state is saved, and the yielded value is returned. The function's execution is then suspended, and it can be resumed from where it left off when the next value is requested.

# In[70]:


#Example

def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


# In[71]:


for i in fib(10):
    print(i)


# In[73]:


#Q5.

def prime():
    primes = []
    num = 2
    while True:
        is_prime = True
        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
            yield num
        num += 1
prime()


# In[74]:


prime_sequence = prime_generator()

for _ in range(20):
    print(next(prime_sequence))


# In[ ]:




