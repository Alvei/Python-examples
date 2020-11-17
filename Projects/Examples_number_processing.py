
def sumDigit(n: int) -> int:
    ''' Simple function to add the digits. Takes a number, n, and sums all of its digits '''
    assert (n>0)
    str_n = str(n) # Convert the number into a string
    sum = 0
    for i in str_n:
        sum += int(i)
    return sum


def is_prime(x: int) -> bool:
    ''' Check to see if x is a prime number'''
    assert (n>0)
    n = x
    if (x < 2) :
        return False
    for n in range(2, x-1):
        if x % n == 0:
            return False
        else:
            return True


def divisors(n: int, small: int, large: int) -> bool:
    ''' Check divisibility using recursion.
        Returns True if n has a divisor in the range from small to large.
        Otherwise returns False.'''
    if small > large:
        return False
    elif n % small == 0:    # Is n divisible by small?
        return True
    else:
        return divisors(n, small+1, large)


def isPrime(n: int) -> bool:
    ''' Look for Prime using divisors function
        For any n greater than or equal to 2,
        returns True if n is prime, False if not.'''
    assert (n>0)
    if divisors(n, 2, n-1):
        return False

    # Default
    return True


def listPrimes(n: int, limit: int) -> list:
    ''' Returns a list of prime numbers between n and limit.'''
    if n == limit:
        return[]
    elif isPrime(n):                    # if it is a prime, add to a counter
        return [n] + listPrimes(n+1, limit)
    else:
        return listPrimes(n+1, limit)   # if  not a prime, continue and move fwd to nxt number

def main():
    """ Test harness"""
    numbers = [52, 1246, 123]
    for num in numbers:
        print(f"SumDigit({num}) = {sumDigit(num)}")

if __name__ == "__main__":
    main()