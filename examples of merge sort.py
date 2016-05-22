# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 21:06:38 2014

Merge Sort using lamda

@author: Hugo Sarrazin
"""
def mergeList(left, right, lt):
    ''' Assumes left and right are sorted lists.
    lt defines an ordering on the elements of the lists.
    Returns a new sorted (by lt) list containing the same elements
    as (left + right) would contain.'''
    
    assert type(left) == list and type(right) == list  # Check that the input are lists

    result = []
    i,j = 0,0   # Starting at the beginning of each list
    
    # Loop while for the length of the shortest list    
    while i < len(left) and j < len(right):
        
        # print "left %i and right %i" %(i,j)
        if lt(left[i], right[j]):    # Using Lambda, if x < y
            result.append(left[i])   # Save left most element of left list
            i += 1
        else:
            result.append(right[j])  # Save left most element of rigth list
            j += 1
    
    # Check to see if there are still elements not saved in left list
    while (i < len(left)):
        # print "left %i and right %i" %(i,j)
        result.append(left[i])
        i += 1
    
    # Check to see if there are still elements not saved in right list
    while (j < len(right)):
        # print "left %i and right %i" %(i,j)
        result.append(right[j])
        j +=1
        
    return result
    
def mergeSort(L, lt = lambda x,y: x<y):
    '''Returns a new sorted list containing the same elements as L.
    lt is a lambda function left is smaller than right (x<y). 
    Input: L is assumed to be a list list'''
    
    assert type(L) == list      # Check that the input is a list
    
    #print "new list = ", L
    if len(L) <= 1:
        return L[:] # Send back a copy. This is the base case of recursion
    else:
        # start recursion after breaking the list in half
        mid = int(len(L)/2)          
        left = mergeSort(L[:mid], lt)  # provide a list from beginning to mid
        right = mergeSort(L[mid:], lt) # provide a list from mid to end
        
        #print "About to merge", left, " and", right
        return mergeList(left, right, lt)
        
def lastNameFirstName(name1, name2):
    """ Defining a lambda that can be used to sort names starting with Last names
    Input: two strings
    """
    import string
    name1 = string.split(name1, " ")    # Returns a list with each part of name
    name2 = string.split(name2, " ")
    
    if name1[1] != name2[1]:    # Then sort on last name
        return name1[1] < name2[1]
    else:                       # Then Sort on first name
        return name1[0] < name2[0]
        
def firstNameLastName(name1, name2):
    """ Defining a lambda that can be used to sort names starting with first names
    Input: two strings
    """
    import string
    name1 = string.split(name1, " ")    # Returns a list with each part of name
    name2 = string.split(name2, " ")
    
    if name1[0] != name2[0]:        # Then sort on first name
        return name1[0] < name2[0]
    else:                           # then Sort on last name
        return name1[1] < name2[1]
        

 ################ Test harness 
L = [25,4,5,29,17,58,0]

newL = mergeSort(L)    # uses default lambda for int
print(L, "->", newL)
L2 = [2.0, 55.121, 44.01, 44.001, 5]
newL2 = mergeSort(L2, float.__gt__)  # uses the built-in float greater than as lambda
print (L2, "->", newL2)

L3 = ['John Guttag', 'Tom Brady', 'Chancellor Grimson', 'Gisele Brady', 'Big Julie']
newL3 = mergeSort(L3, lastNameFirstName)
print ("sorted by last name: ", newL3)

newL3 = mergeSort(L3, firstNameLastName)
print ("sorted by first name: ", newL3)
