#!/usr/bin/python3
""" A module that create a rectangle and initialize its dimensions"""
class Rectangle:
    """Represent a rectangle."""

    def __int__(self, hiegth=0, width=0):
        """ inidialize with the width and height with value checks
        Args:
            width: how wide the rectangle is from side to side
            height: height labels how high (how tall) the rectangle is
        """
        self.heigth = hiegth
        self.width = width

    '''defining a getter'''
    @property
    def width(self):
        return self.__width

    '''defining a setter'''
    @width.setter
    def width(self,value):
        if isinstance(value,int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width=value

    '''defining a getter'''
    @property
    def heigth(self):
        return self.__heigth

    '''defining a setter'''
    @heigth.setter
    def heigth(self, value):
        if isinstance(value, int) is False:
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__heigth = value
