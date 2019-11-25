from Fibonacci import fib, fib_loop, fast_fib, fast_fib2
import pytest

def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(6) == 8
    assert fib(10) == 55

    #while pytest.raises(TypeError):
        #assert fib('a')
    #while pytest.raises(ValueError):
        #assert fib(-1)

def test_fib_loop():
    assert fib_loop(0) == 0
    assert fib_loop(1) == 1
    assert fib_loop(2) == 1
    assert fib_loop(3) == 2
    assert fib_loop(6) == 8
    assert fib_loop(10) == 55

    """while pytest.raises(AssertionError):
        assert fib_loop('a')
        assert fib_loop(-1)"""

def test_fast_fib():
    assert fast_fib(0) == 0
    assert fast_fib(1) == 1
    assert fast_fib(2) == 1
    assert fast_fib(3) == 2
    assert fast_fib(6) == 8
    assert fast_fib(10) == 55

def test_fast_fib2():
    assert fast_fib2(0) == 0
    assert fast_fib2(1) == 1
    assert fast_fib2(2) == 1
    assert fast_fib2(3) == 2
    assert fast_fib2(6) == 8
    assert fast_fib2(10) == 55