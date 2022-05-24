#!/usr/bin/python3
"""Module to print a square"""


def print_square(size):
    """Print a square with the size provided (size).
    if size is not an integer, raise a TypeError 
    and if its less than 0, raise a ValueError"""
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
