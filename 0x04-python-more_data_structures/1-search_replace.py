#!/usr/bin/bash
def search_replace(my_list, search, replace):
    """function that searches for a number
    on a list and replaces it for another given
    number"""

    new_list = my_list[:]

    for index, n in enumerate(new_list):
        if n == search:
            new_list[index] = replace
    return new_list
