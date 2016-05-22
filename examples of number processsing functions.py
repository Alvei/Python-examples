#
# Simple function to add the digits
#####################################
def sumDigit(n):
    ''' Takes a number, n, and sums all of its digits '''
    str_n = str(n) # Convert the number into a string
    sum = 0
    for i in str_n:
        sum += int(i)
    return sum

#
# Simple factorial using recursion
######################################
def factorial(n):
    ''' Factorial function '''
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

#
# Simple function to check if a number is prime
##################################################
def is_prime(x):
    ''' Check to see if x is a prime number'''
    n = x
    if (x < 2) :
        return False
    for n in range(2, x-1): 
        if x % n == 0:
            return False
    else:
        return True    

#
# Check divisibility using recursion
#######################################
def divisors(n, small, large):
    ''' Returns True if n has a divisor in the range from small to large.
        Otherwise returns False.'''
    if small > large: return False
    elif n % small == 0:    # Is n divisible by small?
        return True
    else:
        return divisors(n, small+1, large)

#
# Look for Prime using divisors function
#######################################
def isPrime(n):
    ''' For any n greater than or equal to 2,
        returns True if n is prime, False if not.'''
    if divisors(n, 2, n-1):
        return False
    else:
        return True

#
# Create a list of prime numbers
########################################
def listPrimes(n, limit):
    ''' Returns a list of prime numbers between n and limit.'''
    if n == limit:
        return[]
    elif isPrime(n):                    # if it is a prime, add to a counter
        return [n] + listPrimes(n+1, limit)
    else:
        return listPrimes(n+1, limit)   # if  not a prime, continue and move fwd to nxt number
