#!/usr/bin/python3
"""Square #2"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
