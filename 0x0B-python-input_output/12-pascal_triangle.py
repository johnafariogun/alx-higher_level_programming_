#!/usr/bin/python3
""" creates a function to create a pscal triangle"""


def pascal_triangle(n):
    """function that returns a list of numbers represernting
    a pascal triangle
    args:
        n: integer which is the length of pascal
    """

    if n <= 0:
        return []

    tri = [[1]]

    for i in range(1, n):
        line = [1]
        for j in range(1, i):
            line.append(tri[i-1][j-1] + tri[i-1][j])
        line.append(1)
        tri.append(line)
    return tri
