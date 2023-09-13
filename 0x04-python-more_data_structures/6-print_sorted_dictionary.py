#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary.items())
    for key, value in keys:
        print(key, ":", value)
