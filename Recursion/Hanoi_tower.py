""" Hanoi tower example
"""


def hanoi(height, s, t, b):
    ''' Function to solve hanoi problem recursively
        height is number of ring
        s is source
        t is target
        b is buffer'''

    assert height > 0        # Check that n is positive otherwise break

    if height == 1:
        print("height: = ", height, " move ", s, " to ", t)
    else:
        hanoi(height - 1, s, b, t)  # Take all ring except one from Target to  Buffer
        hanoi(1, s, t, b)    # Take the bottom ring in Source to the Target
        hanoi(height - 1, b, t, s)  # Take all Buffer back to Target


"""for i in range(1, 5):
    print("New Hanoi Example: hanoi(", i, " ,source")
    print("------------------------------")
    hanoi(i, "Source", "Target", "Buffer")"""
hanoi(3, "Source", "Target", "Buffer")


def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)


# size = 3
# print("Size is ", size)
# moveTower(size, "A", "B", "C")
