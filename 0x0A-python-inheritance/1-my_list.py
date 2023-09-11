#!/usr/bin/python3

"""
Module 1-my_list
Contains a class that inherits list
"""


class MyList(list):
    """
    Inherits from list

    methods:
        print_sorted: prints a sorted list
    """
    def print_sorted(self):
        """ prints a list of sorted ints"""
        self.sorted_list = sorted(self)
        print(self.sorted_list)
