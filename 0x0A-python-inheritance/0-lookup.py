#!/usr/bin/python3
"""Function that returns list of attributes for an object"""


def lookup(obj):
    """Returns the list of attributes for an object"""
    return dir(obj)
