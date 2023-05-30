#!/usr/bin/python3

"""
Module: 101-square
Defines the Square class.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square's side (default is 0).
            position (tuple): The position of the square (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or position is not a tuple.
            ValueError: If size is less than 0.
            TypeError: If position does not contain 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square's side.

        Returns:
            int: The size of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square's side.

        Args:
            value (int): The new size of the square's side.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple.
            TypeError: If value does not contain 2 positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square with the character #.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return self.my_print()
