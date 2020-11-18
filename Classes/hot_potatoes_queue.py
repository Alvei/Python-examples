""" hot_potatoes_queue.py
    In this game children line up in a circle and pass an item from
    neighbour to neighbour as fast as they can. At a certain point
    in the game, the action is stopped and the child who has the item
    (potato) is removed from the circle. Play continues until only
    one child is left.
    Inspired: PS with Algo and Data Structure from Miller. Pg 84."""
from typing import List
from Queue import Queue


def hot_potato(name_list: list, num: int) -> List[str]:
    """ Playing the game. """
    circular_queue = Queue()

    for name in name_list:  # Load queue
        circular_queue.enqueue(name)

    while circular_queue.size() > 1:  # Loop until one child is left
        for _ in range(num):
            # Take item at front and move to rear of queue
            # print(_, circular_queue.size())
            circular_queue.enqueue(circular_queue.dequeue())

        # Music stops and remove children. This decrements .size()
        print(f"Remove: {circular_queue.dequeue()}")

    return circular_queue.dequeue()


def main():
    """ Test harness. """
    # Answer Susan
    print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))


if __name__ == "__main__":
    main()
