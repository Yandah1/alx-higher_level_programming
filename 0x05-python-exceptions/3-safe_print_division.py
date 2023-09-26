#!/usr/bin/python3

"""A function that divides 2 integers and prints the result."""


def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError , TypeError):
        result = None
    finally:
        print("Inside Result: {}".format(result))
        return (result)
