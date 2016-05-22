# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 06:56:45 2014

Basic statistical functions

@author: Hugo Sarrazin
"""

import math

def myCombination(n,r):
    ''' Function that implements the basic combination. Needs math module
    Input: n and r are int
    Output: int
    '''
    assert type(n) == int and type(r) == int # Input should be integers
    assert (n-r)>0                           # myCombination() input test
    
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
    
def myBinomialProb(p, k, n):
    ''' Function that calculates a single Binomial Proabability.
        Needs function myCombination and the math module
        Input:
        n is number of trials, int
        k is number of successes, int
        n-k is the number of failures, int
        p is probability of success of one trial, float
        q is probably of failure of one trial, float
        Output: flot
    '''
    assert (n-k)>0   # myCombination() input test
    q = 1 - p
    prob = myCombination(n,k)*p**k*q**(n-k)
    return prob
    
""" Testing the my implementation of the binomial probability function"""
p = 0.1
k = 1       # number of success
n = 5       # number of trials
ans = []

# Build a list of probabilities if you try n times
for i in range(2,n+1):
    ans.append(myBinomialProb(p,k,i))
    
print ans

# if you want to know the probability of having at least 1 successful trial
# calculate the probabily of having none and substract from it

n = 10           # Maximum num of trials
x = range(1,n+1) # Number of trials

y10 = []
y20 = []
for i in x:
    y10.append(1-myBinomialProb(.1,0,i))
    y20.append(1-myBinomialProb(.2,0,i))
    
print ans

import pylab

pylab.plot(x,y10, x, y20)
pylab.grid()
pylab.xlabel("Number of trials")
pylab.ylabel("Cummulative probability")
