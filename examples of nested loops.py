# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 19:53:30 2014

@author: Hugo Sarrazin
"""

#List comprehensions form new lists by manipulating old ones
vals = [1, 2, 3, 5, 7, 9, 10]
double_vals = [2 * v for v in vals]

# Only include doubles for values dibisible by 5
double_vals5 = [2 * v for v in vals if v % 5 == 0]

x_pts = [-1, 0, 2]
y_pts = [2, 4]
xy_pts = [[x, y] for x in x_pts for y in y_pts]
# [[-1, 2], [-1, 4], [0, 2], [0, 4], [2, 2], [2, 4]]

#Parsing a vector
vec = '[12.4, 3, 4, 7.22]'
# strip away the brackets
vec = vec.lstrip('[')
vec = vec.rstrip(']')
# form an array by splitting on comma
nums = vec.split(',')
# go from string to floating point
nums = [float(n) for n in nums]

#parsing a vector in one line
vec = '[12.4, 3, 4, 7.22]'
nums = [float(n) for n in vec.strip('[]').split(',')]

#intro to dict
import math
p = (1.2, -40.0, 2*math.pi)
point = {} # form an empty dictionary
point['x'] = p[0]
point['y'] = p[1]
point['z'] = p[2]
point['r'] = math.sqrt(sum([v ** 2 for v in p]))
point['theta'] = math.acos(point['z'] / point['r'])
point['phi'] = math.atan(point['y'] / point['x'])

# print all keys
for key in point:
    print key
# check if a key is there
if 'theta' not in point:
    print 'missing theta!'