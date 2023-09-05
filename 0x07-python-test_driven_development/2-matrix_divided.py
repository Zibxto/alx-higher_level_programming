#!/usr/bin/python3

"""
Module 2-matrix_divided.py
Contains a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix

    Args:
        matrix (list): first param to the function
        div (int or float): second param which must be a non zero number

    Returns:
         list: A new matrix in which all elements
               are floated in 2 decimal places

     Raises:
         TypeError: If matrix is not a list of ints and floats
         TypeError: If each rows of the matrix are not equal
         TypeError: If div is not a number
         ZeroDivisionError: If div is equal to 0

    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(message)

    new_matrix = []
    samelen = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(message)
        if len(lists) != samelen:
            raise TypeError("Each row of the matrix must have the same size")
        newlist = []
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError(message)
            newlist.append(round(i/div, 2))
        new_matrix.append(newlist)
    return new_matrix
