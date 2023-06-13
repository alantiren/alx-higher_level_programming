#!/usr/bin/python3
# 1-my_list.py
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Custom list class that inherits from the built-in list class."""


    def print_sorted(self):
        """
        Public instance method that prints the list in sorted order (ascending).
        """
        sorted_list = sorted(self)
        print(sorted_list)
