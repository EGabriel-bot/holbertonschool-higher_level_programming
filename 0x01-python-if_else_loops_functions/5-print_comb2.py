#!/usr/bin/python3
import sys
for i in range(100):
    num = i % 10
    num2 = i // 10

    print("{:d}{:d}".format(num2, num), end="")
    if i != 99:
        print("{:d}{:d}, ".format(num2, num), end="")
    elif i == 99:
        print(i)
