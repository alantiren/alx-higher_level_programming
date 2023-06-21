#!/usr/bin/python3

"""
This module provides file input/output operations.
"""

def read_file(filename):
    """
    Read the contents of a file.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The contents of the file.
    """
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    """
    Write content to a file.

    Args:
        filename (str): The name of the file to write to.
        content (str): The content to write to the file.
    """
    with open(filename, 'w') as file:
        file.write(content)
