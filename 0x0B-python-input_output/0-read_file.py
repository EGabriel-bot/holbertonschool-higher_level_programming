#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """reads a text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print(read_data)
