#!/usr/bin/python3

"""Print the first x elements of a list that are integers."""


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(count, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, IndexError, ValueError):
            pass
    print("")
    return count
