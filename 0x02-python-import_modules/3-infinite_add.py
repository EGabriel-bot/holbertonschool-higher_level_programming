#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":

    res = 0
    idx = 1
    for i in range(len(argv) - 1):
        res = int(argv[idx]) + res
        idx += 1
    print(f"{res}")
