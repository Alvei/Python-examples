"""test_contain_searches.py """
import pytest
import sys, os
# required to allow to find the file to test in directory above the test directory
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from contain_searches import linear_contains, binary_contains

@pytest.fixture
def int_list_not_sorted():
    data = [31, 5, 15, 25, 15, 20] # does NOT need to be sorted
    return data

@pytest.fixture
def str_list_sorted():
    data = list("abcdefgh")
    return data

@pytest.fixture
def int_list_sorted():
    data = [1, 5, 15, 15, 18, 20]
    return data

@pytest.fixture
def str_list_not_sorted():
    data = list("aDciemgh")
    return data

def test_int_linear_contains(int_list_not_sorted):
    """ Basic functional test. Does not check type. """
    assert linear_contains(int_list_not_sorted, 5), "5 should be part of list"
    assert linear_contains(int_list_not_sorted, 15), "15 should be part of list"
    assert not linear_contains(int_list_not_sorted, 19), "19 should be part of list"
    assert not linear_contains(int_list_not_sorted, 26), "25 should NOT be part of list"
    assert not linear_contains(int_list_not_sorted, -5), "-5 should NOT be part of list"

def test_str_linear_contains(str_list_sorted):
    """ Basic functional test. Does not check type. """
    assert linear_contains(str_list_sorted, "a"), "5 should be part of list"
    assert linear_contains(str_list_sorted, "h"), "15 should be part of list"
    assert not linear_contains(str_list_sorted, "A"), "A should be part of list"
    assert not linear_contains(str_list_sorted, 26), "26 should NOT be part of list"
    assert not linear_contains(str_list_sorted, "m"), "m should NOT be part of list"

def test_int_linear_contains_not_sorted(int_list_not_sorted):
    """ Basic functional test. Does not check type. """
    assert linear_contains(int_list_not_sorted, 5), "5 should be part of list"
    assert linear_contains(int_list_not_sorted, 31), "1 should be part of list"
    assert linear_contains(int_list_not_sorted, 15), "15 should be part of list"
    assert not linear_contains(int_list_not_sorted, 30), "30 should be part of list"
    assert not linear_contains(int_list_not_sorted, 35), "25 should NOT be part of list"
    assert not linear_contains(int_list_not_sorted, -5), "-5 should NOT be part of list"

def test_str_linear_contains_not_sorted(str_list_not_sorted):
    """ Basic functional test. Does not check type. """
    assert linear_contains(str_list_not_sorted, "D"), "D should be part of list"
    assert linear_contains(str_list_not_sorted, "m"), "1 should be part of list"
    assert linear_contains(str_list_not_sorted, "g"), "15 should be part of list"
    assert not linear_contains(str_list_not_sorted, "b"), "30 should be part of list"
    assert not linear_contains(str_list_not_sorted, 35), "25 should NOT be part of list"
    assert not linear_contains(str_list_not_sorted, "x"), "-5 should NOT be part of list"

def test_linear_contains_empty():
    assert not linear_contains([], 5)

def test_int_binary_contains(int_list_sorted):
    """ Basic functional test. Does not check type. """
    assert binary_contains(int_list_sorted, 5), "5 should be part of list"
    assert binary_contains(int_list_sorted, 1), "1 should be part of list"
    assert binary_contains(int_list_sorted, 15), "15 should be part of list"
    assert not binary_contains(int_list_sorted, 19), "19 should NOT be part of list"
    assert not binary_contains(int_list_sorted, 25), "25 should NOT be part of list"
    assert not binary_contains(int_list_sorted, -5), "-5 should NOT be part of list"

def test_str_binary_contains(str_list_sorted):
    """ Basic functional test. Does not check type. Only works if everything is of same type."""
    assert binary_contains(str_list_sorted, "a"), "5 should be part of list"
    assert binary_contains(str_list_sorted, "h"), "15 should be part of list"
    assert not binary_contains(str_list_sorted, "A"), "A should be part of list"
    assert not binary_contains(str_list_sorted, "26"), "26 should NOT be part of list"
    assert not binary_contains(str_list_sorted, "m"), "m should NOT be part of list"

def test_int_binary_contains_not_sorted(int_list_not_sorted):
    assert binary_contains(int_list_not_sorted, 5) == -1, "Should return -1 because list is not sorted."

def test_str_binary_contains_not_sorted(str_list_not_sorted):
    assert binary_contains(str_list_not_sorted, 5) == -1, "Should return -1 because list is not sorted."

def test_binary_contains_empty():
    assert not binary_contains([], 5)
