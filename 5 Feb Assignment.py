#!/usr/bin/env python
# coding: utf-8

# Q1. Class:
# 
# In OOP, a class is a blueprint or a template that defines the structure and behavior of objects. It serves as a blueprint for creating objects of a particular type.
# A class encapsulates data (in the form of attributes or properties) and functions (in the form of methods) that operate on that data.
# It defines the common characteristics and behaviors that the objects of that class will possess.
# You can think of a class as a blueprint for creating multiple instances (objects) that share the same structure and behavior.
# Object:
# 
# An object is an instance of a class. It is a concrete entity that is created based on the blueprint provided by a class.
# An object represents a specific instance of a class and can have its own unique data and behavior.
# Objects can interact with each other, communicate, and perform operations based on the methods defined in the class.
# Objects are created from a class by using the new keyword or by calling the class name as a constructor.
# 
# 4 pillars are:
# Encapsulation
# Abstraction
# Inheritence
# Polymorphism

# In[2]:


#Example

# Define a Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started for {} {} {}".format(self.make, self.model, self.year))


car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2023)

car1.start_engine() 
car2.start_engine()


# Q2. The __init__() function is a special method in Python classes that is used to initialize the attributes or properties of an object when it is created. It is also known as the constructor method.
# 
# Here's why the __init__() function is used:
# 
# Object Initialization: The __init__() function allows you to specify how an object should be initialized and what initial values its attributes should have. It is called automatically when an object is created from a class and allows you to set the initial state of the object.
# 
# Attribute Assignment: Within the __init__() function, you can assign values to the attributes of the object using the self keyword, which represents the instance of the object being created. This allows each object to have its own unique attribute values.
# 
# Parameter Passing: The __init__() function can accept parameters that allow you to pass values to the object's attributes during initialization. These parameters can be used to customize the initial state of the object based on the provided values.
# 
# Code Reusability: By defining the __init__() function in a class, you can reuse it to initialize multiple objects of the same class with different attribute values. This promotes code reuse and helps in creating objects efficiently.

# Q3. n Object-Oriented Programming (OOP), self is used as a convention to refer to the instance of a class within the class itself. It is a special parameter that represents the object or instance that the method is being called on. 

# Q4. Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class to inherit properties and behaviors from another class. The class that is being inherited from is called the base class, parent class, or superclass, while the class that inherits is called the derived class, child class, or subclass.

# In[4]:


#Examples

#Single

class Animal:
    def sound(self):
        print("Making sound...")


class Dog(Animal):
    def bark(self):
        print("Barking...")


dog = Dog()
dog.sound()
dog.bark()

#Multiple

class Car:
    def drive(self):
        print("Driving...")


class Boat:
    def sail(self):
        print("Sailing...")


class AmphibiousVehicle(Car, Boat):
    def operate(self):
        print("Operating...")

amphibious_vehicle = AmphibiousVehicle()
amphibious_vehicle.drive()
amphibious_vehicle.sail() 
amphibious_vehicle.operate()

#Multilevel

class Vehicle:
    def drive(self):
        print("Driving...")


class Car(Vehicle):
    def start(self):
        print("Starting...")


class SportsCar(Car):
    def race(self):
        print("Racing...")



sports_car = SportsCar()
sports_car.drive()
sports_car.start()  
sports_car.race()   

#Hierarchical

class Animal:
    def sound(self):
        print("Making sound...")


class Dog(Animal):
    def bark(self):
        print("Barking...")


class Cat(Animal):
    def meow(self):
        print("Meowing...")


dog = Dog()
cat = Cat()
dog.sound()  
dog.bark() 
cat.sound() 
cat.meow()  


# In[ ]:




