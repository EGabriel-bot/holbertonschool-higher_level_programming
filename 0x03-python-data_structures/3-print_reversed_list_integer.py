#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.sort(reverse=True)
    idx = 0
    for i in my_list:
        print(my_list[idx])
        idx = idx + 1
