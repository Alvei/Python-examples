# -*- coding: utf-8 -*-
"""

Examples of recursions
Created on Fri Dec 26 10:50:21 2014

@author: Hugo Sarrazin
"""
def factorial(n):
    ''' Function using recursion to calculate factorial 
    Input: Asummes n is an int > 0
    Outup: Int'''
    
    assert (n >= 0 )       # Check that n is positive otherwise break
    
    if n == 0: 
        return 1 # Base case
    else:
        return n * factorial(n-1)
        
# Check if a word is a palindrome
# Using list
#######################################
def isPal1(name):
    ''' Requires name to be a list
    returns True is the list is a palindrome, False ortherwise'''
    
    assert type(name) == list # Check that name is a list
    
    temp = name[:]   # Make a copy of the list
    temp.reverse()
    if temp == name:
        return True
    else:
        return False
              
# Second Palindrome function
# Using str
###############################
def isPalindrome(s):
    """ Assumes s is a str
        Returns True if s is a palindrom: False otherwise
        Punctuations marks, blanks, and capitalization ignored."""
    
    def toChars(s):
        """Converts all letters to lowercase and removes all non-letters"""
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
        return letters
    
    def isPal(s):
        """s is a str"""
        print "   isPal called with", s
        if len(s) <= 1:     # Base case
            print "  About to return True from base case"
            return True
        else:
            """ to conditions, 1st one to ensure 1st and last letter the same
            the second, is lunching a recursive call with those 
            two letters removed"""
            answer = s[0] == s[-1] and isPal(s[1:-1])
            print "   About to return", answer, "for", s
            return answer
    
    return isPal(toChars(s))

# Test harness
def testIsPalindrome():
    print "Try dogGod"
    print isPalindrome("dogGod")
    print "Try doGOOD"
    print isPalindrome("doGOOD")
        
# Power of n using recursion
############################################
def recPower(m,n):
    ''' Calculates the power n of a number m using recursion
    Input: m and n are int
    Output: int'''
    assert type(n) == int   # Check that the input are ok

    if n == 0:  # Base case
       return 1 
    else:
       return m * recPower(m,n-1)
       
# Multiplication of m*n using recursion
############################################
def recMult(m,n):
    ''' Calculates multiplication of m * n of a number m using recursion
    Input: m and n are int and positive
    Output: int'''
    assert type(n) == int and type(m) == int  # Check that the input are int
    assert n>=0 and m>=0    # Check that the input are positive

    if n == 0:  # Base case
       return 0 
    else: 
       return m + recMult(m,n-1)

# Hanoi tower example
#################################
def hanoi(height, s, t, b):
    ''' Function to solve hanoi problem recursively
    height is number of ring
    s is source
    t is target
    b is buffer'''
    
    assert height > 0        # Check that n is positive otherwise break
    
    if height == 1:
        print "height: = ", height, " move ", s, " to ", t
    else:
        hanoi(height-1,s,b,t)  # Take all ring except one from Target to  Buffer
        hanoi(1,s,t,b)    # Take the bottom ring in Source to the Target
        hanoi(height-1,b,t,s)  # Take all Buffer back to Target
    
'''for i in range(1,5):
    print "New Hanoi Example: hanoi(", i, " ,source",
    print "------------------------------"
    hanoi(i, "Source", "Target", "Buffer")'''
        
        
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
   print("moving disk from",fp,"to",tp)

#moveTower(3,"A","B","C")

# Recursive Fibonacci with Global Variable
##############################################
def fib(x):
    """ Assumes x an int >= 0
        Returns Fibonacci of x"""
    global numFibCalls
    
    numFibCalls += 1
    
    if x == 0 or x == 1:  #base case
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
def testFib(n):
    for i in range(n+1):
        global numFibCalls
        numFibCalls = 0
        
        print "fib of", i, "=", fib(i)
        print "fib called", numFibCalls, "times."