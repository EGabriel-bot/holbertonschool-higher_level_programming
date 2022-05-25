#!/usr/bin/python3
"""File comment"""


class Rectangle:
    """comment"""

    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            self.perimeter = 0
            return self.perimeter
        return (self.width + self.height) * 2

    def __str__(self):
        sep = ""
        list = []
        if self.width == 0 or self.height == 0:
            return("")
        for i in range(self.height):
            list.append("#" * self.width)
            if i != self.height - 1:
                list.append("\n")
        return sep.join(list)

    def __repr__(self):
        return 'Rectangle(%d, %d)' % (self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
