#!/usr/bin/python3

"""
Module 1-square
Defines a class Square
"""


class Square:
    """
    class Square definition

    Args:
        size : size of square side
    """
    def __init__(self, size):
        """
        Initializes square

        Attributes:
            size: size of square side
        """
        self.__size = size
