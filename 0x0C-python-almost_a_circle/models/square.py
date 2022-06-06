#!/usr/bin/python
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = self.width

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
