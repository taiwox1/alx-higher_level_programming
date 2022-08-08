#!/usr/bin/python3

"""Defines a base model class"""


class Base:

    """ This class will be the “base” of all other classes in this project
        args: __nb_object(int): the numbers of instances in base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ base initailization
            Args:
                id(int): identity of the new basei
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
