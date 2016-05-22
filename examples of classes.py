# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 20:07:42 2014

Examples of using classes

@author: Hugo Sarrazin
"""

#class Employee:
#    '''Common base class for all employees'''
#
#    #empCount is a class variable whose value would be shared among all instances of a this class.
#    empCount = 0
#
#    def __init__(self, name, salary):
#        self.name = name
#        self.salary = salary
#        Employee.empCount += 1  # Updates the class variable
#
#    def displayCount(self):
#        print "Total Employee %d" % Employee.empCount
#
#    def displayEmployee(self):
#        print "Name : ", self.name, ", Salary: ", self.salary


""" Test Harness """
#==============================================================================
#emp1 = Employee("Zara", 2000)
#emp1.displayEmployee()
#emp1.displayCount()
#
#emp2 = Employee("Manni", 5000)
#emp2.displayEmployee()
#emp2.displayCount()
#
#emp1.age = 7 # Add an 'age' attribute.
#emp1.age = 8 # Modify 'age' attribute.
##del emp1.age # Delete 'age' attribute.
#
#
#hasattr(emp1, 'age') # Returns true if 'age' attribute exists
#getattr(emp1, 'age') # Returns value of 'age' attribute
#setattr(emp1, 'age', 8) # Set attribute 'age' at 8
#delattr(emp1, 'age') # Delete attribute 'age'
#
#
## Printing built-in capabilities
#print "Employee.__doc__:", Employee.__doc__
#print "Employee.__name__:", Employee.__name__
#print "Employee.__module__:", Employee.__module__
#print "Employee.__bases__:", Employee.__bases__
#==============================================================================
#print "Employee.__dict__:", Employee.__dict__


""" Overloading an operator for a tuple vector
"""
#class Vector:
#    """ Vectors are tuples of two elements"""
#    def __init__(self, a, b):
#        self.a, self.b = (a,b) # Decomposes a tuple
#        
#    def __str__(self):
#        return 'Vector (%d, %d)' % (self.a, self.b)
#        
#    def __add__(self,other):
#        """ Defines a new way to do tuple additions """
#        return Vector(self.a + other.a, self.b + other.b)
#
#v1 = Vector(2,10)
#v2 = Vector(5,-2)     
#print v1 + v2

""" Creating a class with getter and setter using Properties.
    This will allow each of the properties to be updated 
    when attribute is changed.
    In python 2.7 important to have object as an argument for class
"""
#class Circle(object):
#    def __init__(self, input_radius):
#        self.__radius = input_radius
#    def __str__(self):
#        return "Radius : " + str(self.__radius)
#    @property
#    def radius(self):
#        # print "Inside the getter"
#        return self.__radius
#        
#    @radius.setter
#    def radius(self, value):
#        #print "Inside the setter"
#        self.__radius = value
#           
#    @property
#    def diameter(self):
#        return 2 * self.__radius
#    
#    @property    
#    def area(self):
#        return 3.14159 * self.__radius**2  
#        
#  # Test harnest
#c = Circle(5)
#print "radius =", c.radius
#print "diameter =", c.diameter
#c.radius = 6
#print "radius =", c.radius
#print "diameter =", c.diameter

""" Uses class attributes and instance attributes
    In python 2.7 important to have object as an argument for class
"""
#class Celsius(object):
#    
#    count = 0   # Class attribute
#    def __init__(self, temperature = 0):
#        """ Using __temperature we are hidding the variable temperature"""
#        self.__temperature = temperature
#        Celsius.count += 1  # Increment the class attribute
#        
#    def to_farh(self):
#        ' Convert Celsius to Farheneit'
#        return (self.temperature * 1.8) + 32 
#
#    @property   
#    def temperature(self):
#        print "Getting value"
#        return self.__temperature   # Uses the private name
#
#    @temperature.setter
#    def temperature(self, value):
#        if value <-273:
#            raise ValueError("Temperature below -273 is not possible")
#        print "Setting value"
#        self.__temperature = value  # Setting private name
#        
#    @classmethod
#    def printCountInstances(cls):
#        print "Celsius has,", cls.count, "objects"
#
## Test harness
#c = Celsius(55)
#
#print  c.temperature  # answer is 55 and uses the getter function
#
#c.temperature = 66  
#
#print c.temperature   
#b = Celsius(30)
#a = Celsius(80)
#Celsius.printCountInstances()

"""Atomic element class with there own getter/setter
   Basic exception testing for atomic number
"""
class Element(object):
    'Atomic element class with private attributes'
    
    def __init__(self, name= None, symbol= None, number=0):
        'Include default names'
        self.__name = name
        self.__symbol = symbol
        if number <0:
          raise ValueError("Negative atomic number is not possible")
        self.__number = number
        
    def __str__(self):
        return "Name : "+ str(self.__name) \
        + ", Symbol : " + str(self.__symbol)\
        + ", Number : " +  str(self.__number)
        
    # Getter and setter for name    
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, value):
        self.__name = value
        
    # Getter and setter for symbol    
    @property
    def symbol(self):
        return self.__symbol
        
    @symbol.setter
    def symbol(self, value):
        self.__symbol = value
        
    # Getter and setter for atomic number    
    @property
    def number(self):
        return self.__number
        
    @number.setter
    def number(self, value):
        if value <0:
          raise ValueError("Negative atomic number is not possible")
        self.__number = value
        
    def __add__(self, other):
       """ Defines an overload for addition"""
       newAtomicNumber = self.__number + other.__number
       newElement = Element(number = newAtomicNumber)
       return newElement  # returns an object that is an Element
       
    def __eq__(self, other):
       """ Defines an overload for equality"""
       if self.__number != other.__number:
           print "1st"
           return False
       elif self.__name != other.__name:
               print "2nd"
               return False
       elif self.__symbol != other.__symbol:
                   print "3rd"
                   return False
       else:
           print "4th"
           return True
       
    def __mul__(self, other):
       """ Defines an overload for multiplication"""
       newAtomicNumber = other.__number * self.__number
       newElement = Element(number = newAtomicNumber)
       return newElement  # returns an object that is an Element

# Test harness
hydrogen = Element("Hydrogen", "H", 1)
oxygen = Element()
print hydrogen
print oxygen
oxygen.name = "Oxygen"
oxygen.symbol = "O"
oxygen.number = 16
print oxygen
nE = hydrogen + oxygen
print nE

nE2 = hydrogen * oxygen
print nE2
        
print "H == H?", hydrogen == hydrogen
print "H == O?", hydrogen == oxygen