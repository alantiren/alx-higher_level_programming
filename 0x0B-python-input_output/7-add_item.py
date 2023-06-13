#!/usr/bin/python3
# 7-add_item.py
"""Defines a script that adds arguments
to a Python list and saves it to a file."""


import sys
from os import path
from typing import List
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_item(args: List[str]):
    """Adds arguments to a Python list and saves it to a file."""
    filename = "add_item.json"
    my_list = []
    if path.exists(filename):
        my_list = load_from_json_file(filename)
    my_list.extend(args)
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    add_item(sys.argv[1:])
