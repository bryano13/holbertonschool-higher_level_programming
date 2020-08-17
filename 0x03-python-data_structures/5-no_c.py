#!/usr/bin/python3
def no_c(my_string):
    str_l = len(my_string)
    s1 = my_string[:]
    idx = 0
    while idx < len(s1):
        if s1[idx] == 'C' or s1[idx] == 'c':
            s1 = my_string[:idx] + s1[idx + 1:]
        else:
            idx = idx + 1
    return s1
