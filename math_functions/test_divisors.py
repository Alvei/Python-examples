import pytest
from divisors import find_divisors, find_extreme_divisors

class TestFindDivisors(object):

    def test_find_divisors_basic(self):
        assert find_divisors(20, 100) == (1, 2, 4, 5, 10, 20)
        assert sum(find_divisors(20, 100)) == 42
        assert find_divisors(5, 30) == (1, 5)
        assert find_divisors(1, 5) == (1, )

    def test_find_divisors_types(self):
        with pytest.raises(AssertionError):
            find_divisors(-5, 30)
            find_divisors(5, -30)
            find_divisors(-5, -30)
            find_divisors('a', 5)
            find_divisors(100, 5.0)
            find_divisors('a', 'b')

class TestFindExtremeDivisors(object):
    def test_find_extreme_divisors_basic(self):
        assert find_extreme_divisors(100, 200) == (2, 100)
        assert find_extreme_divisors(8, 2) == (2, 2)
        assert find_extreme_divisors(50, 200) == (2, 50)
        assert find_extreme_divisors(200, 5) == (5, 5)

    def test_find_extreme_divisors_types(self):
        with pytest.raises(AssertionError):
            assert find_extreme_divisors(1, 1)
            assert find_extreme_divisors(-1, 1)
            assert find_extreme_divisors('a', 1)
            assert find_extreme_divisors(1.2, 1)
            assert find_extreme_divisors(1, 'b')
            assert find_extreme_divisors('d', 'c')

    def test_find_divisors_None(self):
        assert find_extreme_divisors(2, 3) == (None, None)
        assert find_extreme_divisors(11, 45) == (None, None)