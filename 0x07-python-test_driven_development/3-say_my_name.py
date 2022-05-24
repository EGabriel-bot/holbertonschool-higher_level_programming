#!/usr/bin/python3
"""Module to print first and last name"""


def say_my_name(first_name, last_name=""):
    """Print first and last name. If first or last name
        are not of type string, raise a TypeError."""
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
