#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not type(value) is int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not type(value) is int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.height * self.width

    def display(self):
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            if self.x == 0:
                print("", end="")
            if self.y == 0:
                print("", end="")
            print("#" * self.width)

    def __str__(self):
        str = (f"({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")
        return (f"[Rectangle] {str}")

    def update(self, *args, **kwargs):
        arguments = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, arguments[i], args[i])
        if args is not None:
            for arguments in kwargs:
                setattr(self, arguments, kwargs[arguments])
        else:
            pass

    def to_dictionary(self):
        my_dict = {"id": self.id, "width": self.width,
                   "height": self.height, "x": self.x, "y": self.y}

        return my_dict
