# -*- coding: utf-8 -*-
"""
Created on Fri Jan 02 13:18:56 2015

@author: Hugo Sarrazin
"""

# Define functions inside other functions
def greet(name):
    def get_msg():
        return "Hello "
    return get_msg() + name

print greet("john")     # Output : Hello John

# Passing functions as parameters to functions
def greet(name):
    return "Hello " + name
    
def call_func(func):  # Passing a function called func
    other_name = "Bob"
    return func(other_name)  # It is returning the output of func()

print call_func(greet)  # Calling the function with greet as a functional arg
                        # Outoput : Hello Bob

# Functions can return other functions
def compose_greet_func():
    def get_msg(name):
        return "Hello there!" + name
    return get_msg    # returning a function get_msg
    
# assigning a function to greet. 
# greet becomes a function that behaves like the get_msg function
greet = compose_greet_func()  

print greet("julie")       # Print Hello there! julie