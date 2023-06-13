#!/usr/bin/python3
"""
3-is_kind_of_class.py
Defines a class-checking function.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance of
    a class that inherited from, the specified class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True if obj is an instance of or inherited from a_class,
        False otherwise.
    """
    return isinstance(obj, a_class)
