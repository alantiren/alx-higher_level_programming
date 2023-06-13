#!/usr/bin/python3
# 7-add_item.py

"""Script that adds all arguments
to a Python list and saves them to a file."""

import sys
import json
import os.path


def save_to_json_file(my_obj, filename):
    """Write an object to a text file
    using JSON representation."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


filename = "add_item.json"

if os.path.isfile(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)
