#!/usr/bin/python3
"""converts an input to json else returns a TypeError"""
import json


def to_json_string(my_obj):
    """json stringifies an input"""

    return json.dumps(my_obj)
