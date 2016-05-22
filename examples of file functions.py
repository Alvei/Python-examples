# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 07:45:23 2014

Examples of I/O

@author: Hugo Sarrazin
"""



def num_words(file_name):
    ''' function to count the words in a file
    Input: filename is a string
    Output: int'''
    with open(file_name, 'r') as f:
        total = 0
        for line in f:
            count = len(line.split())
            total += count
         #   print "total =", total, "count =", count
        return total
    
#print "number of word is: ", num_words('course_description.txt')

def most_common(file_name):
    ''' Function to returns the most common word in a file.
    Input: str for the filename
    Output: dict with the word and word count pairs
    '''
    
    with open(file_name, 'r') as f:
        words = {}
        for line in f:                  # Loop of each line
            line_words = line.split()   # Creates a list of words for that line
            
            for word in line_words:     # Loop over the list of words
                if word in words:       # Check to see if in dictionary
                    words[word] += 1    # Add to the counter
                else:
                    words[word] = 1     # Create a new word in dict with count 1
        #print "list of items: ", words.items()           
        #return sorted(words.items(), key=lambda x: x[1], reverse=True)[0]
        return words                    # Unsorted dict

#print "Most common word is: ", most_common(file_name)

def getKey(item):
    """ Simple function to return the 2nd item from a list.
    This is a list of tuples (word, word_count)
    """
    return item[1]  # return the 2nd item of the list on which we will sort

''' Test harnest'''
file_name = "course_description.txt"    
D = most_common(file_name)
listWords = D.items()   # Create a list of tuples (word, word_count)

# replaces the lambda function, 
# uses getKey with no argument since assumes listWords, the first argument
# getKey returns the second elements of the tuple which is the word count
sorted(listWords, key = getKey, reverse=True)[0] # Sort and return the largest

# Breaks down further the line into two steps, create a sorted list, tell me biggest #
s = sorted(listWords, key = getKey, reverse=True) # returns a sorted list of tuples
print s[0]


import os
current_dir = os.getcwd()
print current_dir