#!/usr/bin/python3


class Base:
    """ This class will be the “base” of all other classes in this project"""
    """
        args: __nb_object(int): the numbers of instances in base
    """
    __nb_object = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_objects
