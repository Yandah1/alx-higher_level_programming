#!/usr/bin/python3
"""Write the first class  Base"""


class Base:
    """Base Class forobject"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base object.

        Args:
            id (int): The ID of the object.
        """

        if id  is not None:
            self.id =  id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
