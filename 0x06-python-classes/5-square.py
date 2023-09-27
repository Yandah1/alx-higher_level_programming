#!/usr/bin/python3
"""creates class Square with
private instance attribute size and public instance method"""


class Square:
    """defines class that represent a square"""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculates and returns current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the character #."""
        for _ in range(self.__size):
            print("#" * self.__size)

        if self.__size == 0:
            print()
