#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, 'w+', encoding="utf-8") as f:
        wrote_data = f.write(text)
    return(wrote_data)
