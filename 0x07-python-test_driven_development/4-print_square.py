#!/usr/bin/python3

"""
Module 4-print_square.py
Contains a function that prints a square with the character #
The function takes in parameter size which represents the size of the square
"""


def print_square(size):
    """
    Function that prints a square using the character #

    Args:
        size (int): The size length of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
        TypeError: If size is a float
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float):
        raise TypeError("size must be an integer")
    for x in range(size):
        for i in range(size):
            print("#", end="")
        print("")
