#!/usr/bin/python3

"""
Module rectangle
Contain a class called Rectangle which inherits the Base classs
"""


from models.base import Base


class Rectangle(Base):
    """
    A class that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area value of the Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """
        Prints to stdout the Rectangle instance with the character #
        """
        for row in range(self.height):
            for col in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Gets invoked when an instance of the class is printed
        """
        return (f"[{__class__.__name__}] ({self.id}) {self.x}"
                f"/{self.y} - {self.width}/{self.height}")

    def display(self):
        """
        Print in stdout the Rectangle instance with
        character # by taking care of x and y
        """
        print("\n" * self.__y +
              "\n".join(" " * self.__x + "#" * self.__width
                        for i in range(self.__height)))

    def update(self, *args):
        """
        Updates the class by assigning an argument to each attribute
        """
        if args:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.width = v
                elif i == 2:
                    self.height = v
                elif i == 3:
                    self.x = v
                else:
                    self.y = v
