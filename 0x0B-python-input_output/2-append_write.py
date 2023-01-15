#!/usr/bin/python3
"""function to append some text to a file"""


def append_write(filename="", text=""):
    """appends text to the file with name in argument filename"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
