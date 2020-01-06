"""test_generic_search.py """
import pytest
from generic_search import linear_contains, binary_contains

def test_linear_contains():
    """ Basic functional test. Does not check type. """

    input = [1, 5, 15, 15, 18, 20] # does NOT need to be sorted
    assert linear_contains(input, 5), "5 should be part of list"
    assert linear_contains(input, 1), "1 should be part of list"
    assert linear_contains(input, 15), "15 should be part of list"
    assert not linear_contains(input, 19), "19 should be part of list"
    assert not linear_contains(input, 25), "25 should NOT be part of list"
    assert not linear_contains(input, -5), "-5 should NOT be part of list"

def test_linear_contains_not_sorted():
    """ Basic functional test. Does not check type. """
    input = [31, 5, 15, 25, 15, 20] # does NOT need to be sorted
    assert linear_contains(input, 5), "5 should be part of list"
    assert linear_contains(input, 31), "1 should be part of list"
    assert linear_contains(input, 15), "15 should be part of list"
    assert not linear_contains(input, 30), "30 should be part of list"
    assert not linear_contains(input, 35), "25 should NOT be part of list"
    assert not linear_contains(input, -5), "-5 should NOT be part of list"

def test_linear_contains_empty():
    assert not linear_contains([], 5)

def test_binary_contains():
    """ Basic functional test. Does not check type. """
    input = [1, 5, 10, 15, 18, 22]
    assert binary_contains(input, 5), "5 should be part of list"
    assert binary_contains(input, 1), "1 should be part of list"
    assert binary_contains(input, 15), "15 should be part of list"
    assert not binary_contains(input, 19), "19 should NOT be part of list"
    assert not binary_contains(input, 25), "25 should NOT be part of list"
    assert not binary_contains(input, -5), "-5 should NOT be part of list"

def test_binary_contains_not_sorted():
    assert binary_contains([15, 10, 90], 5) == -1, "Should return -1 because list is not sorted."

def test_binary_contains_empty():
    assert not binary_contains([], 5)
