#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle
# Create a Vehicle object
car = Vehicle("Car", 200, 50)

# Access the instance variables
print(car.name_of_vehicle)  # Output: Car
print(car.max_speed)        # Output: 200
print(car.average_of_vehicle)  # Output: 50


# In[2]:


class Car(Vehicle):
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        super().__init__(name_of_vehicle, max_speed, average_of_vehicle)
    
    def seating_capacity(self, capacity):
        return f"{self.name_of_vehicle} - Seating Capacity: {capacity} passengers"

car = Car("Sedan", 180, 4)
print(car.seating_capacity(5))


# In[3]:


class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def drive(self):
        print(f"{self.name} is being driven.")

class Flyable:
    def fly(self):
        print("Flying...")

class Car(Vehicle):
    def honk(self):
        print("Honk!")

class FlyingCar(Car, Flyable):
    pass

# Create a FlyingCar object
my_car = FlyingCar("FlyingCar1")

# Access methods from the base classes
my_car.drive()
my_car.honk()  
my_car.fly()   


# In Python, getter and setter methods are used to access and modify the values of class attributes (variables). They provide a way to encapsulate the access to the attributes and allow controlled access and modification.
# 
# 

# In[6]:


class Person:
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        self._name = new_name

# Create a Person object
person = Person("John Doe")

# Use the getter method to retrieve the name
name = person.get_name()
print(name)  # Output: John Doe

# Use the setter method to update the name
person.set_name("Jane Doe")
new_name = person.get_name()
print(new_name)  # Output: Jane Doe


# In[5]:


class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Create objects of Dog and Cat
dog = Dog()
cat = Cat()

# Call the make_sound method on Dog and Cat objects
dog.make_sound()  # Output: Woof! Woof!
cat.make_sound()  # Output: Meow!


# In[ ]:




