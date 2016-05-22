# -*- coding: utf-8 -*-
"""
miniQuizlet
It is a short program that reads a file called entry.txt to create a dictionary
The program then asks users a question based on the key

Created on Sun Dec 21 12:35:53 2014

@author: Hugo Sarrazin
"""

import random
import os

def cleanString(myString):
    ''' Function that removes leading blanks and EOL character
    Input: string to be cleaned-up
    Output cleaned string'''
    myString = myString.lstrip()
    newString = ""
    
    #remove EOL if found in the second word
    if "\n" in myString:
        newString = myString[0:len(myString)-1]
    else:
        newString = myString
    return newString
    
def getDict(filename): 
    '''Function to read a dictionary from a file
    Input: filename in the current dictionary
    Output: Dictionary'''
    tempDict = {}

    #This is the file that will contain the dictionary data separated by commas
    fobj=open(filename, 'r')

    '''fobj contains a list of strings. Loop over this list having 
    the pointer "line" point to each new string.'''
    for line in fobj:
        x = line.split(",")
        a,b = x[0], cleanString(x[1])
        
        #create the dictionary    
        tempDict[a] = b
    
    fobj.close()
    return tempDict

filename = "C:\Users\Hugo Sarrazin\Documents\Python Scripts\entry.txt"
myDict = getDict(filename)

#create a list of all the keys, myDict.keys() returns the keys
myKeys = list(myDict.keys())

#determine how many time you want to ask questions or how manyr rounds
rounds = int(raw_input("How many rounds do you want to play: "))

score = 0
for index in range(rounds):
    
    #get the starting word by applying random on the list of keys
    question = random.choice(myKeys)
    #get the answer from the dictionary
    answer = myDict[question]
    
    myChoice = raw_input("\n What is the matching word for : "+ question + "\n-> ")
    
    if myChoice == answer:
        score += 1
        print "Congratulation! that is the correct answer. Your score is: "+ str(score)
    else:
        print "Sorry!" + answer + " is the correct answer"
        
print "The final score was: " + str(score)
