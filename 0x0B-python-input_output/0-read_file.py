#!/usr/bin/python3

"""
Module 0-read_file
Contains function that reads a text file(utf-8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Takes a file, reads and outputs its content

    Args:
        filename(str): param to pass
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
