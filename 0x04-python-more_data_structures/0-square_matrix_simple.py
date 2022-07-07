#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(lambda x: [x[0]**2, x[1]**2, x[2]**2], matrix))
    return (new_matrix)
