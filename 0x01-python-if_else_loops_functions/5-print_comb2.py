#!/usr/bin/python3
for i in range(100):
    num = i % 10
    num2 = i // 10
    
    print("{:d}{:d} ".format(num2, num), end="")
    if i != 99:
      print(",", end= "")
