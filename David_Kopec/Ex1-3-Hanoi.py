""" Exercise 3
Powers of Hanoi with N-towers.
Inspired from David Kopec's book Chapter 1.
"""
from Hanoi_tower_class import Stack

def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], num: int) -> None:
    if num == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, num - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, num - 1)


def exercise_3():
    num_disks: int = 10
    tower_a = Stack()
    tower_b = Stack()
    tower_c = Stack()

    # Load the starting tower
    for index in range(1, num_disks + 1):
        tower_a.push(index)

    print(f'\nTower A: {tower_a}')
    print(f'Tower B: {tower_b}')
    print(f'Tower C: {tower_c}')
    print(f'\nSwitch Towers')
    hanoi(tower_a, tower_c, tower_b, num_disks)
    print(f'Tower A: {tower_a}')
    print(f'Tower B: {tower_b}')
    print(f'Tower C: {tower_c}')


if __name__ == '__main__':
    exercise_3()
