#!/usr/bin/python3

"""
Module 0-lookup
Contains a that returns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """
    To get a list of available attributes in an object

    Args:
        obj (class): object to check
    Returns:
        list: list of available attributes and methods of an object
    """
    return dir(obj)
