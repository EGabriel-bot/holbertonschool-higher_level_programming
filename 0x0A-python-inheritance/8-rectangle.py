#!/usr/bin/python3
"""Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectancle class"""

    def __init__(self, width, height):
        """Initialize instance"""
        self.__width = width
        self.__height = height

        Rectangle.integer_validator(self, "height", self.__height)
        Rectangle.integer_validator(self, "width", self.__width)
