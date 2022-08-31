#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = [list(map((lambda x: x**2), elements)) for elements in matrix]
    return squares
