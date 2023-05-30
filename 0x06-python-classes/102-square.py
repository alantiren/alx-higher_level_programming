#!/usr/bin/python3

"""
Module: 102-square
Defines the Square class.
"""


class Square:
    """
    Represent a square.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """compare if two squares have equal areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares have different areas."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Compare if one square has a greater area than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if one square has a greater or equal area than the other."""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Compare if one square has a smaller area than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if one square has a smaller or equal area than the other."""
        return self.area() <= other.area()
