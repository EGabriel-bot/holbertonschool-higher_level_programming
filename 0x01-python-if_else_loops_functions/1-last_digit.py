#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = int(repr(number)[-1])

if lastd > 5:
    print("Last digit of {0} is {1} and is greater than 5".format(number, lastd))
if lastd == 0:
    print("Last digit of {0} is {1} and is 0".format(number, lastd))
if lastd < 6 and lastd != 0:
    print("Last digit of {0} is {1} and is less than 6 and not 0".format(number, lastd))
    