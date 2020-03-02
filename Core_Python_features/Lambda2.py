"""
Created on Tue Mar  6 18:04:31 2018

for python 3.5
"""


def func():
    step = 1
    point1 = 2
    point2 = point1 + step
    fp1 = point1 ** 3 + 3 * point1 + 3
    fp2 = point2 ** 3 + 3 * point2 + 3
    return (fp2 - fp1) / step
# print(func(), "should be 22.0")


def derivs(f, points, step=1):
    """ f is a function"""
    return [(f(p + step) - f(p)) / step for p in points]


y = derivs(lambda x: x ** 3 + 3 * x + 3, [2, 3, 4, 5], 0.1)
#print( y)


# compute first 20 powers of 2
# ===============================
i = 0
powers = []
while i < 20:
    p = 2 ** i
    powers.append(p)
    i = i + 1


p2 = [(2**n) for n in list(range(0, 20))]

# first 14 k-digit approximations of pi
#======================================
import math
approximations = []
i = 1
while i <= 14:
    approx = round(math.pi, i)
    approximations.append(approx)
    i += 1

# print(approximations)

short_pi = [round(math.pi, n) for n in list(range(1, 15))]
# print(short_pi)


# Generate all (x, y, z) coordinates from three lists
xpoints = [1, 2, -1]
ypoints = [8, 4, 3, 0]
zpoints = [0, -1]
points = []
for x in xpoints:
    for y in ypoints:
        for z in zpoints:
            points.append((x, y, z))

#print ('points = ', points)

pts = [(x, y, z) for x in xpoints for y in ypoints for z in zpoints]
#print('pts = ', pts)


arr1 = [2, 3, 5, 7]
arr2 = arr1  # Pointer assigment, no copying
arr2[2] = 13
# print (arr1[2], arr2[2] )
arr3 = arr1[0:3]  # Same as copying
arr3[0] = 17
# print (arr1[0], arr3[0])


def funct(arr):
    arr.append(2)  # Append changes the definition of the list


my_arr = [1, 2, 3]
#print( len(my_arr) )
funct(my_arr)
#print( len(my_arr) )


dict1 = {'apples': 3, 'oranges': 2}
dict2 = dict1  # Pointer assignment
dict2['bananas'] = 5
if 'bananas' in dict1:
    print('bananas is there!')
else:
    print('no bananas')
