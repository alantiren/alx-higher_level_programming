#!/usr/bin/python3
# 6-load_from_json_file.py
"""Defines a function that creates an object from a JSON file."""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
