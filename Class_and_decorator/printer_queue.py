""" printer_queue.py
    Implement 3 classes the simulate a printer queue behaviors.
    PrintQueue Class: class that follows the queue data structure
    Job Class: 
        page attribute - random, 1 to 10
        print_page() - decrements pages
        check_complete() - checks all pages have been printed
    Printer Class:
        get_job() - account for the case where PrintQueue.items is empty
        print_job()
"""
# from __future__ import annotations
from typing import TypeVar, Generic, Optional
from typing import List, Deque


# from typing_extensions import Protocol   # Need to install this module

T = TypeVar("T")  # Create a generic type


class Queue(Generic[T]):
    """ Generic Queue class. """

    def __init__(self) -> None:
        """ Initialize a Special List: Deque as container.
            It gives us access to .popleft(). """
        self._container: Deque[T] = Deque()

    @property
    def empty(self) -> bool:
        """ Returns True for empty container.
            Could have implemented as a function. O(1). """
        return not self._container

    def push(self, item: T) -> None:
        """ Add to the end of the queue item(s). O(1)"""
        self._container.append(item)

    def pop(self) -> T:
        """ Remove the 1st item in the container. FIFO. O(1)
            If we add used a list it would have been in O(n) Linear. """
        if self.empty:
            raise Exception("Queue empty! Cannot use .popleft().")
        return self._container.popleft()

    def size(self):
        """ Return the length of the container. O(1). """
        return len(self._container)

    def peek(self) -> T:
        """ View element at top of the stack. O(1). """
        if self.empty:
            raise Exception("Queue empty! Cannot use .peek().")
        return self._container[0]

    def show(self) -> Deque[T]:
        """ Displays the entire queue as a list. """
        return self._container

    def __repr__(self) -> str:
        """ Use default repr(). """
        return repr(self._container)


class PrinterQueue(Queue):
    """ Inherits the properties from the generic Queue class. """

    pass


class Job:
    """ Job class. """

    def __init__(self) -> None:
        """ Initializer. """
        self.pages = 5

    def print_page(self) -> None:
        """ Print the page of a given job. """
        if self.pages > 0:
            self.pages -= 1

    def check_complete(self) -> bool:
        """ Check if the job is completed. """
        if self.pages == 0:
            print(f"\nCompleted the print job.\n")
            return True
        return False


class Printer:
    """ Class that defines the properties of a printer. """

    def __init__(self) -> None:
        """ Initializer. """
        self.current_job = None

    def get_job(self, print_queue):
        """ Get the next job from the printer queue. """
        try:
            self.current_job = print_queue.pop()
        except IndexError:
            print(f"\n *** No more job to print. ***")

    def print_job(self, job):
        """ Go through the print job. """
        while job.pages > 0:
            job.print_page()
        if job.check_complete():
            return "Printing complete"


def main():
    """ Test Harness. """
    ### Initialize the three classes
    job = Job()
    job2 = Job()
    printer_q = PrinterQueue()
    printer = Printer()

    # Load-up the printer queue with two jobs
    printer_q.push(job)
    printer_q.push(job2)

    # Printer object gets the next job from the printer queue.
    printer.get_job(printer_q)

    # Printer calls the print job method with its  current job.
    printer.print_job(printer.current_job)


if __name__ == "__main__":
    main()
