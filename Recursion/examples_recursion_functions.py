
"""
examples_recursions_functions.py
Examples of recursions:
factorial()
Palindrome with list

Created on Fri Dec 26 10:50:21 2014
for Python 3.5
"""


def factorial(number):
    ''' Function using recursion to calculate factorial.
        Signature (int) -> int.'''

    assert (number >= 0)       # Check that n is positive otherwise break
    assert isinstance(number, int)

    if number == 0:
        return 1  # Base case

    return number * factorial(number - 1)


def is_palindrome_list(name):
    ''' Check if a word is a palindrome
        Signature: (list) -> boolean.'''

    assert type(name) == list  # Check that name is a list

    temp = name[:]   # Make a copy of the list
    temp.reverse()

    if temp == name:
        return True

    return False


def isPalindrome(s):
    """ Check if a word is a palindrome
        Punctuations marks, blanks, and capitalization ignored.
        Signature: (list) -> boolean."""

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
        print("   isPal called with", s)
        if len(s) <= 1:     # Base case
            print("  About to return True from base case")
            return True
        else:
            """ to conditions, 1st one to ensure 1st and last letter the same
            the second, is lunching a recursive call with those
            two letters removed"""
            answer = s[0] == s[-1] and isPal(s[1:-1])
            print("   About to return", answer, "for", s)
            return answer

    return isPal(toChars(s))


def testIsPalindrome():
    print("Try dogGod")
    print(isPalindrome("dogGod"))
    print("Try doGOOD")
    print(isPalindrome("doGOOD"))

# Power of n using recursion
############################################


def recPower(m, n):
    """ Calculates the power n of a number m using recursion
    Signature: (int, int) -> int"""

    # Check that the input are ok
    assert isinstance(n, int) and isinstance(m, int)

    if n == 0:  # Base case
        return 1
    return m * recPower(m, n - 1)


def rec_mult(m, n):
    ''' Calculates multiplication of m * n of a number m using recursion
        Signature: (int, int) -> int'''

    assert type(n) == int and type(m) == int  # Check that the input are int
    assert n >= 0 and m >= 0    # Check that the input are positive

    if n == 0:  # Base case
        return 0
    return m + rec_mult(m, n - 1)

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
        print("height: = ", height, " move ", s, " to ", t)
    else:
        hanoi(height - 1, s, b, t)  # Take all ring except one from Target to  Buffer
        hanoi(1, s, t, b)    # Take the bottom ring in Source to the Target
        hanoi(height - 1, b, t, s)  # Take all Buffer back to Target


'''for i in range(1,5):
    print "New Hanoi Example: hanoi(", i, " ,source",
    print "------------------------------"
    hanoi(i, "Source", "Target", "Buffer")'''


def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)

# moveTower(3,"A","B","C")

# Recursive Fibonacci with Global Variable
##############################################


def fib(x):
    """ Assumes x an int >= 0
        Returns Fibonacci of x"""
    global numFibCalls

    numFibCalls += 1

    if x == 0 or x == 1:  # base case
        return 1

    return fib(x - 1) + fib(x - 2)


def test_fib(n):
    for i in range(n + 1):
        global numFibCalls
        numFibCalls = 0

        print("fib of", i, "=", fib(i))
        print("fib called", numFibCalls, "times.")


print(is_palindrome_list([1, 2, 1]), "should be True")
print(is_palindrome_list([1, 2, 2]), "should be False")
