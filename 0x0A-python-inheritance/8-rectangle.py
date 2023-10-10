#!/usr/bin/python3
from 7-base_geometry import iBaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""i

    def __init__(self, width, height):
        self._width = None
        self._height = None
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self._height = height
