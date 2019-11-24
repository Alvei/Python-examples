""" Basic unittest. Does not check for bad type input
    or completely out of range. """

import pytest
from Etudes_binary_search import  binary_search, b_search_helper
from Etudes_binary_search import binary_search_while, binary_sort
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

def test_b_search_helper():
    assert b_search_helper(MY_LIST, 1, 0, 10) == True
    assert b_search_helper(MY_LIST, 1, 0, 5) == True
    assert b_search_helper(MY_LIST, 1, 5, 5) == False
    #assert b_search_helper(MY_LIST, 15, 0, 10) == False

def test_bbinary_search_while():
    assert binary_search_while(1, MY_LIST) == 0
    assert binary_search_while(5, MY_LIST) == 4
    assert binary_search_while(10, MY_LIST) == 9
    assert binary_search_while(15, MY_LIST) == False

def test_binary_sort():
    assert binary_sort(1, MY_LIST) == 0
    assert binary_sort(5, MY_LIST) == 4
    assert binary_sort(10, MY_LIST) == 9
    assert binary_sort(15, MY_LIST) == False
