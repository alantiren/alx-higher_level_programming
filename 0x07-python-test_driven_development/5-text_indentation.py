#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a function of  text-indentation."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    special_chars = [".", "?", ":"]
    for char in text:
        result += char
        if char in special_chars:
            result += "\n\n"

    lines = result.splitlines()
    for line in lines:
        print(line.strip())
