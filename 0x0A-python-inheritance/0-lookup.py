#!/usr/bin/python3
# 0-lookup.py
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return [attribute for attribute in dir(obj) if not attribute.startswith('__')]
