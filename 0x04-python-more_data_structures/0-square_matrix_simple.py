#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    for i in matrix:
        res1 = []
        for x in i:
            res1.append(x**2)
        res.append(res1)
    return (res)
