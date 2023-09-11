#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for i, numbers in enumerate(row):
            if i < len(row) - 1:
                print("{:d} ".format(numbers), end="")
            else:
                print("{:d}".format(numbers), end="")
        print()
