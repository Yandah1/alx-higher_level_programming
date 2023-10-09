#!/usr/bin/python3
"""Defines class MyList that inherits from list"""


class MyList(list):
    """Custom list class that inherits from the built-in list class."""
    def print_sorted(self):
        """Prints the elements of the list in ascending order."""
        print(sorted(self))
