#!/usr/bin/python3
def text_indentation(text):
    idx = 0

    if type(text) not in [str]:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[idx - 2] == '.':
            print("\n")
        if text[idx - 2] == '?':
            text.replace(' ', '\n')
            print("\n")
        if text[idx - 2] == ':':
            print("\n")

        print(text[idx], end="")
        idx += 1
