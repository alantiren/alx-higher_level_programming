#!/usr/bin/python3
# 0-lookup.py
"""Defines a function to lookup attributes and methods of an object"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    return [attribute for attribute in dir(obj) if not attribute.startswith('__')]
