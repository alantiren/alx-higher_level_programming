#!/usr/bin/python3
# 5-save_to_json_file.py
"""Defines a function that writes an object
to a text file using JSON representation."""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file
    using JSON representation."""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
