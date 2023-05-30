#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the square. Defaults to 0.
                Raises:
                    TypeError: If size is not an integer.
                    ValueError: If size is less than 0.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
