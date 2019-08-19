# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:29:01 2018

https://www.computerhope.com/issues/ch001721.htm
"""
in_file = open("lorem.txt", "rt")   # open file. 'rt' means read text data."
contents = in_file.read()           # read the entire file into a string variable
in_file.close()                     # close the file
# print(contents)  		             # print contents


"""To create efficient program, important to close your open files 
   as soon as possible.A great way to do this is with the 
   with open... as compound statement. It opens, operates on it, & closes the file, 
   All in one easy-to-read block of code. The file is automatically closed 
   when the code block completes. 
"""
print("\n")
with open ('lorem.txt', 'rt') as in_file:  # Open file lorem.txt for reading of text data.
    contents = in_file.read()              # Read the entire file into a variable named contents.
    print('\n', contents, '\n')            # Print contents.


""" The file object is an iterator. An iterator is a type of Python 
    object which behaves in certain ways when operated on repeatedly. 
    For instance, you can use a for loop to operate on a file object 
    repeatedly, and each time the same operation is performed, you'll 
    receive a different, or next, result. """
    
    
with open ('lorem.txt', 'rt') as in_file:  # Open file lorem.txt for reading of text data.
    for line in in_file:    # Store each line in a string variable "line"
        print(line)         # prints that line    

""" To remove the line separator, use append() but now we have a list.
    The whole thing is contained in brackets. 
    Its individual elements are enclosed in single-quotes, and delimited 
    with commas. Also, note that each element is a string, and that the 
    line breaks (\n) are preserved at the end of each string."""
    
print("\n")
lines = []                                  # Declare an empty list named "lines"
with open ('lorem.txt', 'rt') as in_file:   # Open file lorem.txt for reading of text data.
    for line in in_file:                    # Store each line in a string variable "line"
        lines.append(line)                  # add that line to our list of lines
    print(lines)                            # prints that line
    

""" We can print each elements and special version of print to remove the EOL
    The current examples tells print to but nothing instead of \n"""
print("\n")   
for element in lines:
    print(element, end='')    
    
    
""" But what if we want to remove the line breaks that exist in our data? 
    We can strip them. String objects have many useful methods for operating 
    on their data, including a method called rstrip(), which strips 
    characters from the end of a string."""
print("\n")    
lines = []                  # Declare an empty list named "lines"
with open ('lorem.txt', 'rt') as in_file:  # Open file lorem.txt for reading of text data.
    for line in in_file:  # For each line of text in in_file, where the data is named "line",
        lines.append(line.rstrip('\n'))   # add that line to our list of lines, stripping newlines.
    for element in lines:            # For each element in our list,
        print(element)                   
    
""" read data by iterating over file object"""    
print("\n")
filein = 'weight-data.txt'
weight = []     # empty list to hold data
with open(filein, 'r') as f:
    for i, line in enumerate(f):  # counter i is included in for loop
        if i == 0:
            pass # skips header
        else:
            data = line.split(',')          # Splits line
            weight.append(float(data[-1]))  #data[-1] ensures we take last value in line
print(weight)   

""" read data using readlines()""" 
filein = 'weight-data.txt'
weight = []     # empty list to hold data
with open(filein, 'r') as f:
    file_data = f.readlines()
    for line in file_data[1:]: # Skips head by doing [1:]
        data = line.split(',') # Splits line
        weight.append(float(data[-1]))
        
print(weight)

""" read data using CSV Reader """
import csv
filein = 'weight-data.txt'
weight = []         # empty list
with open(filein, 'r') as f:
    w = csv.reader(f, delimiter = ',')  # CVS reader object
    for i, line in enumerate(w):
        if i == 0:
            pass # Skip first row
        else:
            weight.append(float(line[-1]))
            
print(weight)
print(type(weight))

""" read data using numpy.loadtxt() 
    weight is a ndarray. 
    Note comma on usecols (needed if only one column is used)"""
import numpy as np
filein = 'weight-data.txt'
# Use loadtxt skipping 1 row and only using second column
weight = np.loadtxt(filein, dtype = np.float_, delimiter = ',', skiprows = 1,\
usecols = (1,))
print(weight)