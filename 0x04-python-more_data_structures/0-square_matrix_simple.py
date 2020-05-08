#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    list1 = []
    for j in matrix:
        list1.append([i**2 for i in j])
    return list1