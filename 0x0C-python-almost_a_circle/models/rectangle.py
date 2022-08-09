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

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the width of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x coordinate of the rectangle"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y coordinate of the rectangle"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError("y must be >= 0")
