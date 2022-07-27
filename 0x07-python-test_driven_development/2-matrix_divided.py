#!/usr/bin/python3
# 2-matrix_divided.py
# Adedotun Taiwo
# taiwoadedotunx1@gmail.com

"""Defining function"""


def matrix_divided(matrix, div):
    """function returns a new matrix with which new element is
    equal Matrix[i][j]/div rounded to 2 decimal places
    raise:
        TypeError: if matrix element or div is niether integer or float
        TypeError: if matrix rows is not of thesame type
        ZeroDivisionError: if div is 0
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(elem, int) or isinstance(elem, float))
                for elem in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
