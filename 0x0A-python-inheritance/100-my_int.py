#!/usr/bin/python3
"""subclassing int """


class MyInt(int):
    """class MyInt"""

    def __eq__(self, other):
        """converting equals to not equals"""
        return super().__ne__(other)

    def __ne__(self, other):
        """converting not equals to equals"""
        return super().__eq__(other)
