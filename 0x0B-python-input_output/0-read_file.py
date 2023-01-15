#!/usr/bin/python3
"""function that reads a textfile(UTF8) and prints it out to stdout"""


def read_file(filename=""):
    """prints the contents in UTF8 encoding to stdout"""

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
