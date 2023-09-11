#!/usr/bin/python3

"""
Module 2-is_same_class
Contains  a function that returns True
if the object is exactly an instance of
the specified class; otherwise False
"""


def is_same_class(obj, a_class):
    """
    Takes two arguments and check if the first is an instance of the second

    Args:
        obj: object argument
        a_class: class argument

    Return:
        True: if object is exactly an instance of the specified class
        False: otherwise
    """

    return type(obj) is a_class
