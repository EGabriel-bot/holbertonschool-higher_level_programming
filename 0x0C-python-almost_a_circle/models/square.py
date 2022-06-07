#!/usr/bin/python
"""Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = self.width

    """size getter"""
    @property
    def size(self):
        return self._size

    """size setter"""
    @size.setter
    def size(self, value):
        # self.width = self.height
        # self.height = self.width
        if not type(value) is int:
            raise TypeError("width must be an integer")
        self._size = value

    """str method for square"""

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    """update method for square"""

    def update(self, *args, **kwargs):
        arguments = ["id", "size", "x", "y"]
        for i in range(len(args)):
            setattr(self, arguments[i], args[i])
        if args is not None:
            for arguments in kwargs:
                setattr(self, arguments, kwargs[arguments])
        else:
            pass