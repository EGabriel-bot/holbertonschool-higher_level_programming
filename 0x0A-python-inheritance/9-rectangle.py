#!/usr/bin/python3
"""Full rectangle"""


class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        Rectangle.integer_validator(self, "height", self.__height)

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
