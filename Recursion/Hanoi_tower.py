""" Hanoi tower example.
"""


def hanoi(height, s, t, b):
    ''' Function to solve hanoi problem recursively
        height is number of ring
        s is source
        t is target
        b is buffer'''

    assert height > 0

    if height == 1:
        print("height: = ", height, " move ", s, " to ", t)
    else:
        # Take all rings except one from Target to Buffer
        hanoi(height - 1, s, b, t)

        # Take the bottom ring in Source to the Target
        hanoi(1, s, t, b)

        # Take all Buffer back to Target
        hanoi(height - 1, b, t, s)


"""for i in range(1, 5):
    print("New Hanoi Example: hanoi(", i, " ,source")
    print("------------------------------")
    hanoi(i, "Source", "Target", "Buffer")"""
hanoi(3, "Source", "Target", "Buffer")


def move_tower(height, fromPole, toPole, withPole):
    if height >= 1:
        move_tower(height - 1, fromPole, withPole, toPole)
        move_disk(fromPole, toPole)
        move_tower(height - 1, withPole, toPole, fromPole)


def move_disk(fp, tp):
    print("moving disk from", fp, "to", tp)


# size = 3
# print("Size is ", size)
# moveTower(size, "A", "B", "C")
