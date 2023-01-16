#!/usr/bin/python3
"""writes an Object to a json file"""
import json


def load_from_json_file(filename):
    """creates and loads an object to a json file"""

    with open(filename, 'r') as f:
        return json.load(f)
