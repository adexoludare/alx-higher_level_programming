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
        self.heigth =hiegth
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

    def area(self):
        '''Calculate the Area of the rectangle'''
        return self.__width * self.__heigth

    def perimeter(self):
        ''' Calculete the perimiter of the rectanglr'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            if i is not self.__height - 1:
                string += "\n"
        return string
