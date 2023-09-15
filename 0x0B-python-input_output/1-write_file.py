#!/usr/bin/python3

"""
Module 1-write_file
Contains function that writes to a text file(utf-8)
"""


def write_file(filename="", text=""):
    """
    Returns the number of character written to a file

    Args:
        filename(str): name of file
        text(str): string wriiten to file
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
