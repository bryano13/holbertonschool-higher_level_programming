#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """Function that returns a list of
    the square values of another list"""

    copy = matrix[:]
    index = 0
    for nlist in copy:
        new_list = nlist[:]
        for i in range(len(nlist)):
            new_list[i] = new_list[i] ** 2
        copy[index] = new_list
        index += 1
    return copy
