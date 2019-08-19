"""
Created on Sat Mar 10 16:11:30 2018

http://stackabuse.com/understanding-pythons-yield-keyword/

The yield keyword in Python is used to create generators.
A generator is a type of collection that produces items on-the-fly
and can only be iterated once. By using generators you can improve
your application's performance and consume less memory as compared
to normal collections, so it provides a nice boost in performance.

"""

# Creating a list using list comprehension
squared_list = [x**2 for x in range(5)]

# Check the type
print( type(squared_list) )

# Iterate over items and print them
for number in squared_list:
    print(number)

"""To create a generator, you start exactly as you would with list comprehension,
   but instead you have to use parentheses instead of square brackets.  """

# Creating a generator
squared_gen = (x**2 for x in range(5))

# Check the type
print( type(squared_gen) )

for number in squared_gen:
    print(number)

""" The yield keyword, unlike the return statement, is used to turn a
    regular Python function in to a generator. This is used as an alternative
    to returning an entire list at once. This will be again explained
    with the help of some simple examples.
"""

def cube_numbers(nums):
    cube_list =[]
    for i in nums:
        cube_list.append(i**3)
    return cube_list

cubes = cube_numbers([1, 2, 3, 4, 5])
print(cubes)

def cube_numbersY(nums):
    for i in nums:
        yield(i**3)

cubes = cube_numbersY([1, 2, 3, 4, 5])
print(cubes)

print(next(cubes))
