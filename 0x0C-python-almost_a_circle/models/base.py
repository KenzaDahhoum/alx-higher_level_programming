#!/usr/bin/python3

""" Defines a base model class."""

class Base:
    """ Represent base model

     Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Init Base  

        Args: 
            id (int) : identify of the class Base
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
