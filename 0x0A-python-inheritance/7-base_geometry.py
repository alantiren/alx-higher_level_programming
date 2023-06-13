#!/usr/bin/python3
"""
7-base_geometry.py
Defines a class BaseGeometry with area and integer_validator methods.
"""


class BaseGeometry:
    """
    Class BaseGeometry.
    """

    def area(self):
        """
        Raises an Exception with the message area() is not implemented.
        """
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
