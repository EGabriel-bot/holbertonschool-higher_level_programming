#!/usr/bin/python3
"""Function to check if is the same class"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly
    of the same class otherwise return False"""

    if not type(obj) is a_class:
        return False
    else:
        return True
