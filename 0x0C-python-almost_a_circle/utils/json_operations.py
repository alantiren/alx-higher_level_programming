#!/usr/bin/python3

"""
This module provides JSON-related operations.
"""

import json

def load_json(filename):
    """
    Load JSON data from a file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        dict: The loaded JSON data.
    """
    with open(filename, 'r') as file:
        return json.load(file)

def save_json(filename, data):
    """
    Save JSON data to a file.

    Args:
        filename (str): The name of the file to save JSON data to.
        data (dict): The JSON data to save.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)
