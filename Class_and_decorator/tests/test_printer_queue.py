import pytest
from printer_queue import Job, PrinterQueue, Printer
from typing import Deque


def test_initialize_job():
    job = Job()
    assert job.pages == 5


def test_initialize_printer():
    printer = Printer()
    assert printer.current_job == None


def test_printer_queue_push():
    printer_q = PrinterQueue()
    printer_q.push("Allo")
    printer_q.push("Comment")
    assert printer_q._container == Deque(["Allo", "Comment"])


def test_printer_queue_pop_empty():
    printer_q = PrinterQueue()
    with pytest.raises(Exception):
        printer_q.pop()


def test_printer_queue_pop():
    printer_q = PrinterQueue()
    printer_q.push("Allo")
    printer_q.push("Comment")
    raise printer_q.pop() == "Allo"
