#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lastd = number % 10
else:
    lastd = number % -10

if lastd > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, lastd))
elif lastd < 6 and lastd != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, lastd))
else:
    print("Last digit of {:d} is {:d} and is 0"
          .format(number, lastd))
