#!/usr/bin/python3

"""
Module 4-inherits_from
Contains a function that returns True
if the object is an instance of a class that inherited
(directly or indirectly) the specified class; otherwise False
"""


def inherits_from(obj, a_class):
    """
    Takes two arguments and check if the first was inherited from the second

    Args:
        obj: object argument
        a_class: class argument

    Return:
        True: if object was inherited the specified class
        False: otherwise
    """

    return type(obj) is not a_class and issubclass(type(obj), a_class)
