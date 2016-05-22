# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 16:53:39 2015

@author: Hugo Sarrazin
"""

def findDivisors(n1, n2):
    """ Assumes that n1 and n2 are positive ints
        Returns a tuple containing all common divisors of n1 & n2 """
        
    divisors = ()   #The empty tuple
 
    for i in range(1, min(n1, n2) +1):
        # print "i =", i
        if n1%i == 0 and n2%i == 0:
            # print "found divisor = ", i
            divisors = divisors + (i,)
    return divisors
        
# Test harness
#divisors = findDivisors(20, 100)
#print divisors
#total = 0
#for d in divisors:
#    total += d
#print total

def findExtremeDivisors(n1, n2):
    """ Assumes that n1 and n2 are positive ints
        Returns a tuple containing the smallest commondivisors > 1
        and the largest common divisors of n1 & n2 """
    divisors = ()
    minVal, maxVal = None, None
    
    for i in range(2, min(n1, n2) + 1): 
              # print "i =", i
        if n1%i == 0 and n2%i == 0:
            if minVal == None or i < minVal:
                minVal = i
            if maxVal == None or i > maxVal:
                maxVal = i
                
    return (minVal, maxVal)

# Test harness
minDiv, maxDiv = findExtremeDivisors(100,200)  
print "Min Divisor =", minDiv  
print "Max Divisor =", maxDiv  