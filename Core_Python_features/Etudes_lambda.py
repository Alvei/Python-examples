"""
Different functions that explores Lambda and list comprehension

Needs to be tweak for Python 3 b/c of way list are created
for Python 3.5
"""

# Filtering using lambda
# ------------------------


def isNotDivisibleBy2(n):
    """Takes a number as input and returns
       True if the number is not divisible by 2, else returns False."""
    return n % 2 != 0


def test_isNotDivisibleBy2():
    '''Had to add list in front of filter and range for Python 3.5'''
    l1 = list(filter(isNotDivisibleBy2, list(range(1, 10))))
    print('\nList of uneven numbers up to 10:', l1)

    f = list(filter(lambda n: n % 2 != 0, list(range(1, 10))))
    print('List of uneven numbers up to 10:', f)

    def f2(n): return n % 2 != 0
    print('List of uneven numbers up to 10:', list(filter(f2, list(range(1, 10)))))

# Generic list comprehensions
# ---------------------------


def test_listComprehension():
    yy = [x + 1 for x in [10, 20, 30]]  # Simply adding 1 to the list
    print('\nAdd 1 to [10, 20, 30]: ', yy)

    Celsius = [39.2, 36.5, 37.3, 37.8]
    Fahrenheit = [((float(9) / 5) * x + 32) for x in Celsius]
    print('F = ', Fahrenheit, '\n')

    colours = ["red", "green", "yellow", "blue"]
    things = ["house", "car", "tree"]
    coloured_things = [(x, y) for x in colours for y in things]
    for i in coloured_things:  # Shows x is outer loop
        print(i)

# Map equivalent: [f(x) for x in L]
# ---------------------------------


def test_mapEquivalent():
    listOfNames = ['I', 'like', 'spam', 'coconut']
    s = [len(myString) for myString in listOfNames]
    print('\nThe original list of names is:', listOfNames)
    print('Count length of each name in the list:', s)

# Filter equivalent: [x for x in L if (conditions)]
# --------------------------------------------------


def test_filterEquivalent():
    words = ['aardvark', 'darn', 'heck', 'like', 'disco']
    w = [x for x in words if len(x) == 4]
    print('Words are: ', words)
    print('\t => Filter (keep) only the ones with 4 characters: ', w)
    n = 1000
    d = [x for x in range(0, n) if x % 42 == 0]  # Find multiples of 42
    print('\nFind multiple of 42 up to', n, ': \n', d)

# Combo
#------


def test_combo():
    u = [x**2 for x in range(0, 11) if x % 2 == 0]
    print('\nFilter even square numbers after squaring [0:10]:', u)

# The following list comprehension creates the Pythagorean triples
# -----------------------------------------------------------------


def test_combo2():
    # Nice trick to use x and y as argument in the following range
    w1 = [(x, y, z) for x in range(1, 15) for y in range(x, 15) for z in range(y, 15)]
    w = [(x, y, z) for x in range(1, 15) for y in range(x, 15) for z in range(y, 15) if x**2 + y**2 == z**2]
    print('\n(x,y,z) from [1,5] (not filtered) = ')
    print(w1)
    print('\nList filtered to meet pythagorean rule = ')
    for j in w:
        print(j)

# Generator comprehension.
# a generator comprehension returns a generator instead of a list.
# ----------------------------------------------------------------


def test_generator():
    x = (x**2 for x in range(20))
    print('\n The address of the generator is:', x)

    x = list(x)
    print('The list created by the generator of x**2 for [0,20]:\n', x)

# mapReduce examples - simply a combo
#-----------------------------------


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def triple(x):
    return 3 * x


# To implement in Python 3.5 replaced reduce with functools.reduce()
import functools


def mapReduce(mapFunction, reduceFunction, myList):
    """Applied mapFunction to myList to construct a new list
       and then applies reduceFunction to the new list
       and returns that value.
       """
    return functools.reduce(reduceFunction, map(mapFunction, myList))


def test_mapReduce():
    print('Reduce 1 =>', functools.reduce(add, [1, 2, 3, 4]), 'should be 10')
    print('Reduce 2 =>', functools.reduce(multiply, [1, 2, 3, 4]), 'should be 24')
    print('Reduce 3 =>', mapReduce(triple, add, [14, 10, 12, 5]), 'should be 123')


# Testing
# =======
# test_isNotDivisibleBy2()
# test_listComprehension()
# test_mapEquivalent()
# test_filterEquivalent()
# test_combo()
# test_combo2()
# test_generator()

test_mapReduce()
