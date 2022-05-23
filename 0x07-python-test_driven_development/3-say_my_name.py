#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))