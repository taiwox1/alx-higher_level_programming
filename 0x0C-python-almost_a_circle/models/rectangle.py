#!/usr/bin/python3
from base import Base
""" define a Rectangle class"""


class Rectangle(Base):
    """ Rectangle in herits from base, a rrectagle class
        Args:
            width(int): width of rectangle
            height(int): height of rectangle
            x(int): x argment
            y(int): y argument
    """
    def __init__(self, width, heigth, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
