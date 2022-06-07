#!/usr/bin/python3
""" Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class contructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter of x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter of y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area method """
        return self.height * self.width

    def display(self):
        """ display method """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            if self.x == 0:
                print("", end="")
            if self.y == 0:
                print("", end="")
            print("#" * self.width)

    def __str__(self):
        """ str method """
        str = (f"({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")
        return (f"[Rectangle] {str}")

    def update(self, *args, **kwargs):
        """ update method """
        arguments = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, arguments[i], args[i])
        if args is not None:
            for arguments in kwargs:
                setattr(self, arguments, kwargs[arguments])
        else:
            pass

    def to_dictionary(self):
        """ to dictionary method """
        my_dict = {"id": self.id, "width": self.width,
                   "height": self.height, "x": self.x, "y": self.y}

        return my_dict
