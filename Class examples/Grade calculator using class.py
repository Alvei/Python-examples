# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 21:34:02 2015

@author: Hugo Sarrazin
"""

class Course(object):
    def __init__(self, name, grade = None, honor = False):
        self.name = name
        self.grade = grade
        self.honor = honor
        
    def getName(self):
        return self.name
        
    def setName(self,name):
        self.name = name

    def getGrade(self):
        return self.grade
        
    def setGrade(self,grade):
        self.grade = grade
        
    def getHonor(self):
        return self.honor
        
    def setHonor(self,honor):
        self.honor = honor
        
    def __str__(self):
        if self.honor:    
            ls = self.name + "\t" + "Hon:\t" + str(self.grade) 
        else:
            ls = self.name + "\t" + "Reg:\t" + str(self.grade) 
        return ls
         
# Dictionary to convert grades
L2G = {"A+":4.3, "A": 4, "A-": 3.7,
       "B+":3.3, "B": 3, "B-": 2.7,
       "C+":2.3, "C": 2}    

def getLetterGrades(courseL):
    """Assumes that courseL is a list of object of class Course
        Returns a list containing all the letter grades"""
    letterL = []

    for l in courseL:
        letterL.append(l.getGrade())
    return letterL
    
def convertGrade(letterGrade, L2G):
    """ Assumes letterGrade is a list and L2G are dictionaries
        Returns a list of numerical grades"""
    
    l = []
    for c in letterGrade:
        l.append(L2G[c])
    return l    
         
def average(l):
    """ Assumes l is a non empty list
        Returns the average of the list """
        
    try:   # Check for divide by zero error
        return sum(l)/float(len(l))  
    except ValueError:
        raise ValueError("Unable to calculate average -> list is empty")
        
# def TestGradeAverage():        
mathC = Course("Math", "A-", True)
bioC = Course("BIO", "A-")
englishC = Course("English", "A-", True)
spanishC = Course("Spanish", "B+")
APUSHC = Course("APUSH", "B", True)
CSC = Course("CS", "B+")

courseL = [mathC, bioC, englishC, spanishC, \
            APUSHC, CSC]
for l in courseL:
    print l
    
letterL = getLetterGrades(courseL)
#print letterL
numL = convertGrade(letterL, L2G)
#print numL
print "GPA: ", average(numL)
