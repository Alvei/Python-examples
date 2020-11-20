""" class_printer.py
    Inspired: PS with Algo and Data Structure from Miller. Pg 84. """
import random
from typing import Union
from Queue import Queue


class Task:
    """ Task object. """

    def __init__(self, time: int) -> None:
        """ Initialize Task.
            time in second. It is simply a counter. """
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        """ getter method. """
        return self.timestamp

    def get_pages(self) -> int:
        """ getter method. """
        return self.pages

    def wait_time(self, current_time):
        """ Calculate wait time in sec. """
        return current_time - self.timestamp


class Printer:
    """ Will need to track whether it has a current task. """

    def __init__(self, ppm: int) -> None:
        """ Initialize the printer. """
        self.page_rate = ppm
        self.current_task: Union[None, Task] = None
        self.time_remaining = 0

    def tick(self) -> None:
        """ Decrements the internal timer and
            sets printer to idle if taks is completed. """
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1

        if self.time_remaining <= 0:  # Set printer to idle
            self.current_task = None

    def busy(self) -> bool:
        """ Printer state. """
        if self.current_task is not None:
            return True
        return False

    def start_next(self, new_task: Task) -> None:
        """ Start a new task and calculate time to complete in sec. """
        self.current_task = new_task
        self.time_remaining = int(new_task.get_pages() * 60 / self.page_rate)


def new_print_task() -> bool:
    """ Helper function. Decides whether a new printing task
        has been created. 10 students who each print twice per hour = 20 tasks/hr.
        Which means 1 tasks every 180 sec. """
    num = random.randrange(1, 181)
    if num == 180:
        return True
    return False


def simulation(num_seconds: int, pages_per_minute: int):
    """ Run the printer simulation. """
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):

        # Check if new task was submitted and add to queue
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        # if still task to print and printer is free start new task
        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)  # Calculate new time

        lab_printer.tick()
    task_completed = len(waiting_times)
    average_wait = sum(waiting_times) / task_completed
    print(
        f"{task_completed} tasks, Avg Wait {average_wait:4.0f} sec {print_queue.size()} tasks left."
    )


def main():
    """ Test harness. 10 tests. """
    for _ in range(10):
        simulation(3600, 5)


if __name__ == "__main__":
    main()
