"""
Etudes_prime_numbers.py
    Series of functions to help find prime numbers
    divisors(): checks to see if there is a divisor within a range.
    is_prime(): checks to see if a number is a prime.
    list_primes(): creates list of prime numbers within a range with recursion.
    list_primes_loop(): creates list of prime number within a range with loop.
    sieve_primes(): creates a list of prime number with a range using sieve
                    algo which eliminates multiples of any prime found to speed
                    up implementation
    seive_primes_comprehension(): is a cool implementation using comprehension.
    The trick is to remove from the full list from [2,n], all the multiples

    Observations:
    =============
    Uses recursion and function returning a boolean as a IF operator
    list_primes(): for numbers < 500 since recursion limit is exceeded
    list_primes_loop(): for numbers < 995 since recursion is exceeded in divisors

    is_prime_sqrt() and listPrimesSqrt() are version that
    test divisors from 2 to sqrt(limit) to speed.

    sieve_primes(): is more efficient since it removes multiples of prime
    number as soon as it finds a prime. primeSieve also doe not use as many
    recursions therefore can go to limit < 7877.

    sieve_primes_comprehension(): has the most flexibility and can go > 50k

    We can also change the recursion level by importing sys.  """

# import sys
# sys.setrecursionlimit(20000)
from math import sqrt
from typing import List, Set

# Global constants
MAX_RECURSION = 500
MAX_LOOP = 996


def divisors(number: int, small: int, large: int) -> bool:
    """ Returns True if number has a divisor in the range of small to large.
        Otherwise returns False. """

    # Catch wrong entries
    assert number >= 0
    assert small >= 0
    assert large >= 0

    if small > large:
        return False

    if number % small == 0:  # Is number divisible by small?
        return True

    # Default is that it is not divisible and therefore increment and do a recursion
    return divisors(number, small + 1, large)


def is_prime(number: int) -> bool:
    """ For any number greater or equal to 2, return True is number is prime and False if not. """
    assert number >= 2

    # Use divisors function that will iterate over all numbers from 2 to (number-1).
    if divisors(number, 2, number - 1):
        return False

    # Default is that it is a prime number.
    return True


def is_prime_sqrt(number: int) -> bool:
    """ For any number greater or requal to 2, Return True is n is prime, False if not. """

    assert number >= 2

    new_num = int(
        sqrt(number)
    )  # Trick to improve efficiency. Only do half of the numbers

    # Use divisors function that will iterate over all numbers from 2 to (number-1)
    if divisors(number, 2, new_num):
        return False

    # Default case is that it is a prime number.
    return True


def list_primes(beg: int, end: int) -> list:
    """ Returns a list of prime numbers between beg and end. """
    assert beg >= 2 and end < MAX_RECURSION

    if beg == end:
        return []

    if is_prime(beg):
        # print('Found a prime ', beg)

        # Put beg in [] to convert into a list to use concatenation and then do recursion.
        return [beg] + list_primes(beg + 1, end)

    # Default is no prime number was found increment the beg number.
    return list_primes(beg + 1, end)


def list_primes_sqrt(beg: int, end: int) -> List[int]:
    """ Returns a list of prime numbers between beg and end. """

    # assert beg >= 2 and end < 3*MAX_RECURSION

    if beg == end:
        return []

    if is_prime_sqrt(beg):
        # print('Found a prime ', beg)

        # Put beg in [] to convert into a list to use concatenation and then do recursion.
        return [beg] + list_primes_sqrt(beg + 1, end)

    # Default is no prime number was found increment the beg number.
    return list_primes_sqrt(beg + 1, end)


def list_primes_loop(beg: int, end: int) -> list:
    """ Returns a list of prime numbers between beg and end. """

    assert beg >= 2 and end < MAX_LOOP

    my_list: List[int] = []

    if beg == end:
        return []

    for num in range(beg, end):
        if is_prime(num):
            # print( 'Found a prime ', num)
            my_list = my_list + [num]
    return my_list


def sift(number: int, num_list: list) -> List[int]:
    """ Takes a number, and a list of numbers, to
        returns the list of those numbers that are not multiple of n. """

    def my_func(var):
        return var % number != 0

    # Use list() because filter() return an iterator
    return list(filter(my_func, num_list))


def prime_sieve(num_list: list) -> List[int]:
    """ Creates a list of prime number using sieve algo which eliminates multiples
        of any prime found to speed up implementation.
        Assumes the 1st number is a prime so works if start at 2. """

    assert (len(num_list) - 1) < 7878

    if num_list == []:
        return []

    # Make sure 1st number is a prime by default
    assert is_prime(num_list[0])

    # Removing the prime number from numList
    # Then use a sift function to remove the multiple of prime in remaining list
    # This new shorter list is use recursively by primeSieve
    prime = num_list[0]
    return [prime] + prime_sieve(sift(prime, num_list[1:]))


if __name__ == "__main__":
    print(
        f"\nSize of Prime list up to 500: {len(list_primes(2, 499))} => Answer should be 94"
    )
    print(f"Size of Prime list using sqrt trick: {len(list_primes_sqrt(2, 10))}")
    print(f"Prime list using sqrt trick: {list_primes_sqrt(2, 10)}")
    print(len(prime_sieve(range(2, 100))))
