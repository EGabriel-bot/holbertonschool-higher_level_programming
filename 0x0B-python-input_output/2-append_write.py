#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, 'a+', encoding="utf-8") as f:
        wrote_data = f.write(text)
    return(wrote_data)
