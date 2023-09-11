#!/usr/bin/python3

"""
Module 3-is_kind_of_class
Contains a function that returns True
if the object is an instance of a class that inherited
from the specified class; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    Takes two arguments and check if the first is an instance of the second

    Args:
        obj: object argument
        a_class: class argument

    Return:
        True: if object is an instance of the specified class
        False: otherwise
    """

    return isinstance(obj, a_class)
