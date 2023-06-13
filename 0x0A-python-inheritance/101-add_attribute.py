#!/usr/bin/python3
"""
101-add_attribute.py
Defines a function that adds a new attribute to an object if possible.
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible.
    Args:
        obj (object): The object to which the attribute is to be added.
        attribute (str): The name of the attribute.
        value (any): The value of the attribute.
    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
