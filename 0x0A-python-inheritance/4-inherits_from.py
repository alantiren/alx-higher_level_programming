#!/usr/bin/python3
"""
4-inherits_from.py
Defines a class inheritance checking function.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that
    inherited (directly or indirectly) from the specified class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True if obj is an instance of a class that inherited from a_class,
        False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
