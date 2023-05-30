#!/usr/bin/python3
"""
Module -MagicClass
MagicClass matching exactly a bytecode provided by Holberton.
"""
import math


class MagicClass:
    """A class that performs calculations."""


    def __init__(self, radius=0):
        """Initialize a MagicClass project.

        Arg:
            radius (float or int): The radius of the MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the calculated area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the calculated circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
