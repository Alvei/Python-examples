"""test_generic_search.py """
import pytest
from generic_search import linear_contains, binary_contains
from generic_search import Stack, Queue, PriorityQueue
from typing import Deque

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

def test_linear_containst_empty():
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

def test_binary_containst_empty():
    assert not binary_contains([], 5)

def test_stack_empty():
    input = Stack()
    assert input.empty, "Returns True when empty."

    input.push(0)
    assert not input.empty, "Returns False when not empty."

def test_stack_size():
    input = Stack()
    assert input.size() == 0, "Size empty stack."

    input.push(0)
    input.push(10)
    assert input.size() == 2, "2 elements in the stack."

def test_stack():
    input = Stack()
    input.push(10)
    input.push(2)
    input.push('five')
    assert input.pop() == 'five', "pop should be equal to 5."
    assert input.size() == 2, "2 elements in the stack."

def test_stack_pop_empty():
    input = Stack()
    with pytest.raises(IndexError):
        input.pop()

def test_stack_peek():
    input = Stack()
    input.push(10)
    input.push('Two')
    input.push(5)
    assert input.peek() == 5,"Looking at the last Stack value == 5."

    input.pop()
    input.pop()
    input.pop()
    with pytest.raises(Exception):
        input.peek()

def test_stack_show():
    input = Stack()
    input.push(10)
    input.push('Two')
    input.push(5)
    assert input.show() == [10, 'Two', 5]

def test_queue_empty():
    input = Queue()
    assert input.empty, "Returns True when empty."

    input.push(0)
    assert not input.empty, "Returns False when not empty."

def test_queue_size():
    input = Queue()
    assert input.size() == 0, "Size empty stack."

    input.push(0)
    input.push(10)
    assert input.size() == 2, "2 elements in the stack."

def test_queue():
    input = Queue()
    input.push(10)
    input.push(2)
    input.push('five')
    assert input.pop() == 10, "pop should be equal to 10."
    assert input.size() == 2, "2 elements in the stack."

def test_queue_pop_empty():
    input = Queue()
    with pytest.raises(IndexError):
        input.pop()

def test_queue_peek():
    input = Queue()
    input.push(10)
    input.push('Two')
    input.push(5)
    assert input.peek() == 10,"Looking at the 1st Queue value == 10."

    input.pop()
    input.pop()
    input.pop()
    with pytest.raises(Exception):
        input.peek()

def test_queue_show():
    input = Queue()
    input.push(10)
    input.push('Two')
    input.push(5)
    assert input.show() == Deque([10, 'Two', 5])
