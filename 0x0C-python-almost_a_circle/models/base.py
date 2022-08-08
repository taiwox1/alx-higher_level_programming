#!/usr/bin/python3


class Base:
    """ this class manage id in all other classes"""
    __nb_object = 0

    def __init__(self, id=None):
        if id==None:
            self.id = id
        else:
            __nb_object += 1
            self.id = id
