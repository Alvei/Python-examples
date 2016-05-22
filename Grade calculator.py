# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 19:39:10 2015

@author: Hugo Sarrazin
"""

# Grade calculator
############################

# Dictionary to convert grades
L2G = {"A+":4.3, "A": 4, "A-": 3.7,
       "B+":3.3, "B": 3, "B-": 2.7,
       "C+":2.3, "C": 2}
       
# List of grades unweighted
courses = {"Math": "A-", "BIO": "A-", "English": "A-",
        "Spanish": "B+", "CS": "A-", "APUSH": "B"}
              
# Weighted grades
coursesW = {"Math": "A-", "BIO": "A-", "English": "A",
        "Spanish": "B+", "CS": "A-", "APUSH": "B+"}

def convertGrade(courses, L2G):
    """ Assumes courses and L2G are dictionaries"""
    
    l = []
    for c in courses:
        l.append(L2G[courses[c]])
    return l
    
def average(l):
    """ Assumes l is a non empty list
        Returns the average of the list """
        
    try:   # Check for divide by zero error
        return sum(l)/float(len(l))  
    except ValueError:
        raise ValueError("Unable to calculate average -> list is empty")
    
l = convertGrade(courses, L2G)

GPA = average(l)
print "Unweighted GPA:\t %.2f" % GPA

lW = convertGrade(coursesW, L2G)

GPAW = average(lW)

print "Weighted GPA:\t %.2f" % GPAW