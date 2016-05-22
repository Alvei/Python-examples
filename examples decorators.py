# -*- coding: utf-8 -*-
"""
Created on Fri Jan 02 09:10:38 2015

Examples of decorators

@author: Hugo Sarrazin
"""

def document_it(func):
    """ First decorator function"""
    def new_function(*args, **kwargs):
        print "Running function: ", func.__name__
        print "Positional arguments: ", args
        print "Keywords arguments: ", kwargs
        result = func(*args, **kwargs)
        print "Result: ", result
        
        return result
    return new_function

def square_it(func):
    """ Second decorator function"""
    def new_function(*args, **kwargs):
        print "Running function: ", func.__name__
        print "Positional arguments: ", args
        print "Keywords arguments: ", kwargs
        result = func(*args, **kwargs)
        print "Result Square_it: ", result
        
        return result * result
    return new_function
    
def add_ints(a,b):
    return a+b
    
## Test harness
#add_ints(3,5)
#cooler_add_ints = document_it(add_ints) # Manual decorator assignments

#cooler_add_ints(3,5)       

#@document_it  # use @ to make the implicit assignment
#def substract_ints(a,b):
#    return a-b
    
#substract_ints(5,3)

@document_it
@square_it
def mult_int(a,b):
    return a*b
    
mult_int(5,3)