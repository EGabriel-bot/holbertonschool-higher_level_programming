#!/usr/bin/python3
def multiple_returns(sentence):
    tup = (len(sentence), sentence[0])
    first = tup[1]
    if sentence:
        return tup
    else:
        first = None
