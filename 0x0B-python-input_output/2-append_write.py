#!/usr/bin/python3

"""
Module 2-append_write
Contains function that appends to a text file(utf-8)
"""


def append_write(filename="", text=""):
    """
    Returns the number of character appended to a file

    Args:
        filename(str): name of file
        text(str): string wriiten to file
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
