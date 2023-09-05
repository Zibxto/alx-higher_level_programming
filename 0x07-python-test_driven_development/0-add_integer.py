#!/usr/bin/python3

"""
Module 0-add_integer
The add_integer module has a function that adds 2 integers
"""

def add_integer(a, b=98):
    """
    function that adds 2 integers a, b

    Args:
        a (int or float): first param to the function
        b (int or float): second param with an initializaion of 98

     Returns:
         int: the addition of a and b

     Raises:
         TypeError: If a and be are not ints or floats     
    """
    if isinstance(a, (int)):
        pass
    elif isinstance(a, float):
            a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, int):
        pass
    elif isinstance(b, float):
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    return (a + b)
