#!/usr/bin/python3
def inherits_from(obj, a_class):
    if not isinstance(obj, a_class) or type(obj) is a_class:
        return False
    else:
        return True
