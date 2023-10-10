#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self._width = None
        self._height = None
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height
