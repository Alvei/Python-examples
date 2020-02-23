""" Run_contain_searches.py
    Different ways of searching. Using generic types not only list
    Linear search with O(n) and binary search with O(nLog(n).
    Binary search requires the list to be ordered.
"""
from __future__ import annotations
from contain_searches import binary_contains, linear_contains, Comparable

if __name__ == "__main__":
    my_list = [1, 5, 15, 15, 15, 20]  # must be sorted list
    key = 5
    print(f"\nkey: {key} is in list: {my_list}? {linear_contains(my_list, key)}")
    print(f"key: {key} is in list {my_list}? {binary_contains(my_list, key)}")

    my_list2 = ["M", "a", "b", "e", "z"] # Uppercase come first
    key2 = "M"
    print(f"\nkey: {key2} is in list: {my_list2}? {linear_contains(my_list2, key2)}")
    print(f"key: {key2} is in list {my_list2}? {binary_contains(my_list2, key2)}")

    my_list3 = ["john", "mark", "ronald", "julie", "sarah"]
    key3 = "sheila"
    print(f"\nkey: {key3} is in list: {my_list3}? {linear_contains(my_list3, key3)}")
    print(f"key: {key3} is in list {my_list3}? {binary_contains(my_list3, key3)}")

    my_list4 = [1, 25, 15, 35, 45, 20]
    key4 = 15
    print(f"\nkey: {key} is in list: {my_list4}? {linear_contains(my_list4, key4)}")
    print(f"key: {key} is in list {my_list4}? {binary_contains(my_list4, key4)}")
