#!/usr/bin/python3
"""Rectangle"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        """Area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator method"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectancle class"""

    def __init__(self, width, height):
        """Initialize instance"""
        self.__width = width
        self.__height = height

        Rectangle.integer_validator(self, "height", self.__height)
