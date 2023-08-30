#!/usr/bin/python3

"""
Module 3-square
Defines a square class with private attribute size, validates size
and calculate the cuurent square area
"""


class Square:
    """
    class Square definition

    Args:
        size (int): size of square side with a default value of 0
    """
    def __init__(self, size=0):
        """
        Initializes square

        Attributes:
            __size (int): size of square side with a default value of 0
        """
        self.__size = size

    @property
    def size(self):
        """"
        Getter

        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter

        Args:
            value: sets size to value, if int and >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and return square area

        Attributes:
            __size: size of square side with a default value of 0
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints the square area in # symbol

        Attributes:
            __size: size of square side with a default value of 0
        """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                print((self.__size) * "#")
