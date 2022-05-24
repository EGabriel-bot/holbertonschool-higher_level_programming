#!/usr/bin/python3
"""Module to indent a text"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters ".?:"
        If the text is not a string, raise a TypeError"""
    idx = 0

    if type(text) not in [str]:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[idx - 2] == '.':
            print("\n")
        if text[idx - 2] == '?':
            text.replace(' ', '\n')
            print("\n")
        if text[idx - 2] == ':':
            print("\n")

        print(text[idx], end="")
        idx += 1
