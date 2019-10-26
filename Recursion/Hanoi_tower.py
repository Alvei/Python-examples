""" Hanoi tower example. """


def hanoi(height: int, source: str, target: str, buffer: str) -> None:
    ''' Function to solve hanoi problem recursively height is number of ring. '''
    assert height > 0

    if height == 1:
        print(f"height: = {height} move {source} to {target}")
    else:
        # Take all rings except one from Target to Buffer
        hanoi(height - 1, source, buffer, target)

        # Take the bottom ring in Source to the Target
        hanoi(1, source, target, buffer)

        # Take all Buffer back to Target
        hanoi(height - 1, buffer, target, source)

def move_tower(height: int, from_pole: str, to_pole: str, with_pole: str) -> None:
    """ Function that does all the moving work. """
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(fpole: str, tpole: str) -> None:
    """ Prints the moving action """
    print(f"moving disk from {fpole} to {tpole}")


def main():
    """ Test harness """

    for index in range(4, 5):
        print(f"\nNew Hanoi Example with {index} source")
        print("-"*35)
        hanoi(index, "Source", "Target", "Buffer")


    # size = 3
    # print("Size is ", size)
    # moveTower(size, "A", "B", "C")

if __name__ == "__main__":
    main()
