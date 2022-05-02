#!/usr/bin/python3
def no_c(my_string):
    replace = {'c': '', 'C': ''}
    my_string = my_string.translate(str.maketrans(replace))
    return my_string
