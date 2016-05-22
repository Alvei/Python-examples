# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 13:47:08 2014

Simple function to read input with some error checking

@author: Hugo Sarrazin
"""
def readInt():
    """ Function to ask for integer with basic error handling
    Input: None
    Retun: Int or error
    """
    while True:
        val = raw_input('Enter an integer: ')
        try:
            val = int(val)
            return val
        except ValueError:
            print val, 'is not an integer'
            
def readVal(valType, requestMsg, errorMsg, maxTries = 4):
    """ Function to test the input with error handling
    Input:
        valtype: is the type of value expected (eg., int)
        requestMsg: str defining the input question
        errorMsg: str to be displayed to user when error happens
    """
    
    numTries = 0
    while numTries < maxTries:
        val = raw_input(requestMsg)
        try:
            val = valType(val)
            return val
        except ValueError:  # Handler for the exception
            print(errorMsg)
            numTries += 1
            
    raise TypeError('Number of tries exceeded')

""" ##Test Harness"""
##print readVal(int, "Enter int: ", "Not an int.")
##print readVal(str, "Enter string: ", "Not an string.")

# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError, Argument:
      print "The argument does not contain numbers\n", Argument

# Call above function here.
#temp_convert("xyz");
