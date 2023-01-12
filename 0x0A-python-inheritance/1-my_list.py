#!/usr/bin/python3
""" defines a class that inheritels a lost and retruns yhe sorted list"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """prints a list sorted in ascendinv order"""
        print(sorted(self))
