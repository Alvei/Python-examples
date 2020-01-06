"""test_generic_search.py """
import pytest
from generic_search import Stack, Queue, PriorityQueue
from typing import Deque

""" *** STACK TESTS *** """

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

""" *** TESTS QUEUE *** """

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

""" *** TESTS PRIORITY QUEUE *** """

def test_priorityqueue_empty():
    input = PriorityQueue()
    assert input.empty, "Returns True when empty."

    input.push(0)
    assert not input.empty, "Returns False when not empty."

def test_priorityqueue_size():
    input = PriorityQueue()
    assert input.size() == 0, "Size empty stack."

    input.push(0)
    input.push(10)
    assert input.size() == 2, "2 elements in the queue."

def test_priorityqueue():
    input = PriorityQueue()
    input.push(10)
    input.push(2)   # It is now the smallest element at input[0]
    input.push(5)
    assert input.pop() == 2, "pop should be equal to 2."
    assert input.pop() == 5, "pop should be equal to 5."
    assert input.size() == 1, "1 elements in the queue."

    # Because it is a priority queue the order in which items are pushed is not important.
    input2 = PriorityQueue()
    input2.push(5)
    input2.push(10)
    input2.push(11)
    input2.push(2)      # It is now the smallest element at input[0]
    assert input2.pop() == 2, "pop should be equal to 2."
    assert input2.pop() == 5, "pop should be equal to 5."
    assert input2.size() == 2, "2 elements in the queue."
    assert input2.pop() == 10, "pop should be equal to 10."
    assert input2.pop() == 11, "pop should be equal to 11."

    input3 = PriorityQueue()
    input3.push(100)
    input3.push(-50)
    input3.push(10)
    assert input3.pop() == -50, "pop should be equal to -50."
    assert input3.pop() == 10, "pop should be equal to 10."