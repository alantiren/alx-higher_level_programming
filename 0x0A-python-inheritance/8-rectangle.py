#!/usr/bin/python3
"""
8-rectangle.py
Defines a class Rectangle that inherits from BaseGeometry.
"""


class BaseGeometry:
    """Class BaseGeometry."""

    def area(self):
        """Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.
        Args:
            name (str): The name of the value.
            value (int): The value to be validated.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
            """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
