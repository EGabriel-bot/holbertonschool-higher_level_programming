#!/usr/bin/python
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = self.width

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        #self.width = self.height
        #self.height = self.width
        if not type(value) is int:
            raise TypeError("width must be an integer")
        self._size = value

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
