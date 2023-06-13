#!/usr/bin/python3
# 0-lookup.py
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    attributes = []
    for attribute in dir(obj):
        if not attribute.startswith('__'):
            attributes.append(attribute)
    return attributes
