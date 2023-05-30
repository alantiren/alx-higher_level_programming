#!/usr/bin/python3
"""Module -MagicClass
MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """
    A class that performs magical calculations.
    """

    def __init__(self, radius: float) -> None:
        """
        Initialize the MagicClass object.

        Args:
            radius (int or float): The radius of the circle.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self) -> float:
        """Return Calculated the area of the circle."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self) -> float:
        """Return Calculated the circumference of the circle."""
        return(2 * math.pi * self.__radius)
