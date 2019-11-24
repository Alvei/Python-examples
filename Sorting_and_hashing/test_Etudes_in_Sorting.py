""" Basic unittest. Does not check for bad type input
    or completely out of range. """

import pytest
from Etudes_binary_search import binary_search, b_search, binary_search_while, binary_sort
MY_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_binary_search():
    assert binary_search(1, MY_LIST) == 0
    assert binary_search(5, MY_LIST) == 4
    assert binary_search(10, MY_LIST) == 9
    assert binary_search(15, MY_LIST) == False

    # Check that the second argument is a list
    with pytest.raises(AssertionError):
        assert binary_search(1, 1)
        assert binary_search('a', MY_LIST)

def test_b_search():
    assert b_search(1, MY_LIST) == True
    assert b_search(5, MY_LIST) == True
    assert b_search(10, MY_LIST) == True
    assert b_search(15, MY_LIST) == False
    assert b_search(5, []) == False

    # Check that arguments are a list and integer
    with pytest.raises(AssertionError):
        assert b_search(1, 1)
        assert b_search('a', MY_LIST)

def test_binary_search_while():
    assert binary_search_while(1, MY_LIST) == 0
    assert binary_search_while(5, MY_LIST) == 4
    assert binary_search_while(10, MY_LIST) == 9
    assert binary_search_while(15, MY_LIST) == False
    assert binary_search_while(5, [5, 5]) == 0
    assert binary_search_while(5, [15, 15]) == False

     # Check that arguments are a list and integer
    with pytest.raises(AssertionError):
        assert binary_search_while(1, 1)
        assert binary_search_while('a', MY_LIST)

def test_binary_sort():
    assert binary_sort(1, MY_LIST) == 0
    assert binary_sort(5, MY_LIST) == 4
    assert binary_sort(10, MY_LIST) == 9
    assert binary_sort(15, MY_LIST) == False

    # Check that the second argument is a list
    with pytest.raises(AssertionError):
        assert binary_sort(1, 1)
        assert binary_sort('a', MY_LIST)
