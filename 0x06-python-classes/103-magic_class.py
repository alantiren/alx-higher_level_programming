#!/usr/bin/python3
"""
Module - MagicClassmatching exactly a bytecode provided by Holberton.
"""

import math

class MagicClass:
    """
    A class that performs magical calculations.
    """

    def __init__(self, radius: float) -> None:
        """
        Initialize the MagicClass object with a given radius.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If the radius is not a number.
        """
        self.__radius = 0

        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self) -> float:
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self) -> float:
        """
        Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
