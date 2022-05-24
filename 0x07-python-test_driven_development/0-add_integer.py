#!/usr/bin/python3
"""Module to add two integers"""


def add_integer(a, b=98):
    """Function that returns the sum of two integers.
        If the argument is not an integer, raise TypeError.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
