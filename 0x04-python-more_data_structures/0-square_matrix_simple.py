#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Function that returns a list of
    the square values of another list"""

    copy = matrix[:]

    for index, nlist in enumerate(copy):
        new_list = nlist[:]
        for i in range(len(nlist)):
            new_list[i] = new_list[i] ** 2
        copy[index] = new_list
    return copy
