#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    else:
        max_value = max(a_dictionary, key=a_dictionary.get)
        return max_value
