#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # this returns value except the intersect, same as set_1 ^ set_2
    return (set_1 | set_2) - (set_1 & set_2)
