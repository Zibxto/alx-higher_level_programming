#!/usr/bin/python3

"""
Module 0-lookup
Contains a that returns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """
    Args:
        obj: object to check
    Returns:
        The list of available attributes and methods of an object
    """
    return dir(obj)
