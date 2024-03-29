#!/usr/bin/python3
""" accepts sys arguments loads them in a list,
loads and saves them in a json file"""
import sys
from os import path


save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

lists = []
try:
    items = load_json('add_item.json')
except FileNotFoundError:
    items = []
items.extend(sys.argv[1:])
save_json(items, 'add_item.json')
