#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    key = list(a_dictionary.keys())[0]
    num = a_dictionary[key]
    for k, v in a_dictionary.items():
        if v > num:
            num = v
            key = k
    return key
