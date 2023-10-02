#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Representing a rectangle."""

    def __init__(self, length=0, width=0):
        """Initialize a  Rectangle.

        Args:
            width(int): width of a  rectangle
            hight(int): hieght of a rectangle
        """
        self.length = length
        self.width = width

    @property
    def width(self):
        """Get  width of the rectange"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
