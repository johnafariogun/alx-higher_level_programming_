#!/usr/bin/python3
def uppercase(string):
    for i in string:
        if ord(i) in range(ord('a'), ord('z')+1):
            i = chr(ord(i) - 32)
        print("{:s}".format(i), end='')
    print()
