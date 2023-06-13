#!/usr/bin/python3
# 8-class_to_json.py

"""Defines a function that returns the dictionary description
with simple data structures for JSON serialization of an object."""


def class_to_json(obj):
    """Returns the dictionary description of an object
    with simple data structures for JSON serialization."""
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
        for key, value in result.items():
            result[key] = class_to_json(value)
        return result
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {str(key): class_to_json(value) for key, value in obj.items()}
    elif isinstance(obj, (str, int, bool)):
        return obj
    else:
        return str(obj)
