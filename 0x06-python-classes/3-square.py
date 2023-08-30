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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates and return square area

        Attributes:
            __size: size of square side with a default value of 0
        """
        return (self.__size ** 2)
