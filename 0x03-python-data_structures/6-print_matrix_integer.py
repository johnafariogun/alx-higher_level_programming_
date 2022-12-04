#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(len(i)):
            if j + 1 != len(i):
                end = " "
            else:
                end = ''
            print("{:d}".format(i[j]), end=end)

        print()
