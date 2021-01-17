import heapq
import random
from operator import itemgetter


def main():
    numbers = random.sample(range(50), 10)
    print(f"Numbers: {numbers}")
    print(f"Largest: {heapq.nlargest(3, numbers)}")
    print(f"Smallest: {heapq.nsmallest(3, numbers)}")
    heapq.heapify(numbers)
    print(f"Heapify: {numbers}")

    n1 = [10, 17, 37, 39]
    n2 = [4, 6, 13, 27, 30, 42]
    print(f"Merge: {list(heapq.merge(n1, n2))}")

    user_scores = {"bob": 3, "julian": 7, "tim": 10, "sara": 2}
    print(f"user_scores: {user_scores}")

    a = heapq.nsmallest(2, user_scores)  # by lowest name first character
    print(f"a: {a}")
    b = heapq.nsmallest(2, user_scores.items(), key=itemgetter(1))
    print(f"b: {b}")


if __name__ == "__main__":
    main()
