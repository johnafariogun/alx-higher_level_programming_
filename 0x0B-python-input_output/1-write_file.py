#!/usr/bin/python3
"""writes a textfile(UTF8) and prints out the number of words stdout"""


def write_file(filename="", text=""):
    """prints the contents in UTF8 encoding to stdout"""

    with open(filename, "w", encoding='utf-8') as f:
        lgt = f.write(text)
        f.close()
        return lgt
