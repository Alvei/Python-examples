"""test_prime_numbers.py
    Did the basic checking but did not cover the bad input cases and the raise conditions. """
import pytest
from prime_numbers import divisors, is_prime, list_primes, prime_sieve, list_primes_sqrt, list_primes_loop
# Global constants
MAX_RECURSION = 500
MAX_LOOP = 996

def test_divisors():
    assert  divisors(10, 2, 5)  == True
    assert  divisors(10, 7, 8)  == False
    with pytest.raises(AssertionError):
        assert divisors(-1, 2, 5)
        assert divisors(10, -2, 5)
        assert divisors(10, 2, -1)

def test_is_prime():
    assert is_prime(7) == True
    assert is_prime(10) == False
    with pytest.raises(AssertionError):
        assert is_prime(-1)

def test_list_primes():
    assert len(list_primes(2, 10)) == 4
    assert len(list_primes(2, 20)) == 8
    assert len(list_primes(2, 100)) == 25

    assert list_primes(5, 5) == []
    #assert len(list_primes(2, 499)) == 94

def test_prime_sieve():
    assert len(prime_sieve(range(2, 10))) == 4
    assert len(prime_sieve(range(2, 20))) == 8
    assert len(prime_sieve(range(2, 100))) == 25
    assert len(prime_sieve(range(2, 499))) == 94

def test_list_primes_sqrt():
    assert len(list_primes_sqrt(2, 10)) == 4
    assert len(list_primes_sqrt(2, 20)) == 8
    assert len(list_primes_sqrt(2, 100)) == 25
    assert len(list_primes_sqrt(2, 499)) == 94

    assert list_primes_sqrt(5, 5) == []

    with pytest.raises(AssertionError):
        assert list_primes_sqrt(-1, 10)
        assert list_primes_sqrt(10, -1)

def test_list_primes_loop():
    assert len(list_primes_loop(2, 10)) == 4
    assert len(list_primes_loop(2, 20)) == 8
    assert len(list_primes_loop(2, 100)) == 25
    assert len(list_primes_loop(2, 499)) == 94

    assert list_primes_loop(5, 5) == []

    with pytest.raises(AssertionError):
        assert list_primes_loop(-1, 10)
        assert list_primes_loop(10, -1)
