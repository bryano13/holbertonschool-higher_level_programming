#!/usr/bin/python3


def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    suma = 0
    for n in new_list:
        suma = suma + n
    return suma
