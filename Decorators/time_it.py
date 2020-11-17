"""time_it_decorator.py
    Simple exploration of decorator with the time library.
"""
import time

def time_it(func):
    """ Decorator function that will calculate the time to perform a funtion and print the time."""
    def wrapper(*args, **kwargs):
        start = time.time()
        results = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end-start)*1000:.2f} miliseconds")
        return results
    return wrapper

@time_it
def calc_square(numbers):
    """ Calculates the square of a list."""
    result = []
    for num in numbers:
        result.append(num*num)
    return result

def calc_square2(numbers):
    """ Calculates the square of a list."""
    start = time.time()
    result = []
    for num in numbers:
        result.append(num*num)
    end = time.time()
    print(f"Square2 took {(end-start)*1000:.2f} miliseconds")
    return result

def main():
    temp = range(1,1000000)
    calc_square(temp)   # with the decorator
    calc_square2(temp)  # without the decorator

if __name__ == "__main__":
    main()