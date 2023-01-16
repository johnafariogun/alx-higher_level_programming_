#!/usr/bin/python3
"""creating a function to write an Object to a text file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file"""

    with open(filename, 'w') as f:
        file_ = json.dumps(my_obj)
        f.write(file_)
    f.close()
