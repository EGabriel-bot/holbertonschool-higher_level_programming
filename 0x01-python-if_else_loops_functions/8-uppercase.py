#!/usr/bin/python3
def uppercase(str):
    upper = " "
    for i in (str):
        char = ord(i)
        if char >= ord('a') and char <= ord('z'):
            char = char - 32
            upper = chr(char)
        else:
            upper = i
        print("{:s}".format(upper), end="")
    print("")
