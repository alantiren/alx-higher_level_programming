#!/usr/bin/python3
# 1-write_file.py
"""Defines a text file writing function."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written."""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
