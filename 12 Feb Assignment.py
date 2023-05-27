#!/usr/bin/env python
# coding: utf-8

# In Python, an exception is an event that occurs during the execution of a program, which disrupts the normal flow of the program's instructions. When an exceptional condition arises, an exception object is created, and the normal flow of the program is interrupted. The program then jumps to a predefined exception handling code block, known as an exception handler, to deal with the exception.
# 
# Exceptions are used to handle errors and exceptional situations that can occur during program execution, such as invalid input, file not found, division by zero, or network errors. They provide a way to gracefully handle such situations and prevent the program from crashing.
# 
# On the other hand, syntax errors are a different type of error in Python. They occur when the code violates the rules of the Python language syntax. Syntax errors are detected by the Python interpreter during the parsing phase, before the program is executed. These errors usually result from misspelled keywords, missing punctuation, or incorrect indentation.

# When an exception is not handled, it propagates up the call stack until it reaches an appropriate exception handler or, if none is found, terminates the program. This behavior is known as "unhandled exception" or "exception propagation."
# 
# Let's consider an example in Python to understand this better:

# In[4]:


#Example

def divide_numbers(a, b):
    return a / b

def main():
    try:
        result = divide_numbers(10, 0)
        print("The result is:", result)
    except ValueError:
        print("Caught a ValueError.")
    finally:
        print("This will always execute.")

main()


# In Python, the try and except statements are used to catch and handle exceptions. The try block is used to enclose the code that might raise an exception, and the except block is used to specify the actions to be taken if a specific exception occurs.

# In[5]:


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        if result < 0:
            raise ValueError("Result is negative.")
        print("The result is:", result)
    finally:
        print("This will always execute.")

divide_numbers(10, 2)  # No exception occurs, output: The result is: 5.0 \n This will always execute.
divide_numbers(10, 0)  # ZeroDivisionError occurs, output: Error: Division by zero is not allowed. \n This will always execute.
divide_numbers(10, -2)  # ValueError occurs, output: Error: Result is negative. \n This will always execute.


# In Python, custom exceptions are user-defined exceptions that inherit from the base Exception class or any of its derived classes. Custom exceptions allow you to define and raise your own exception types to handle specific exceptional scenarios in your code.
# 
# Here are a few reasons why custom exceptions are useful:
# 
# Specific error handling: Custom exceptions allow you to create exception types that represent specific errors or exceptional conditions in your application. This enables you to handle those specific errors differently from generic exceptions.
# 
# Code organization and readability: By defining custom exceptions, you can provide meaningful and self-explanatory names for specific errors in your code. This improves code organization and makes your code more readable and maintainable.
# 
# Hierarchy and inheritance: Custom exceptions can be organized in a hierarchy by creating exception classes that inherit from each other. This allows you to capture different levels of errors or exceptional situations and handle them accordingly.
# 
# Exception customization: Custom exceptions provide the flexibility to add additional attributes or methods to the exception class. This allows you to include relevant information or behavior specific to the exception type, making it easier to handle and provide meaningful error messages.
# 
# Here's an example that demonstrates the use of a custom exception:

# In[6]:


class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Insufficient funds. Cannot withdraw {amount}. Available balance: {balance}.")

def withdraw(amount, balance):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    else:
        print("Withdrawal successful.")

try:
    withdraw(1000, 500)
except InsufficientFundsError as e:
    print(str(e))


# In[7]:


class InvalidInputError(Exception):
    def __init__(self, input_value):
        self.input_value = input_value
        super().__init__(f"Invalid input: {input_value}")

def process_input(input_value):
    if not isinstance(input_value, int):
        raise InvalidInputError(input_value)
    else:
        print("Input processing successful.")

try:
    process_input("abc")
except InvalidInputError as e:
    print(str(e))


# In[ ]:




