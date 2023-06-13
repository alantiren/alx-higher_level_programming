#!/usr/bin/python3
"""
100-my_int.py
Defines a class MyInt that inherits from int.
"""


class MyInt(int):
    """
    Class MyInt that inherits from int.
    """

    def __eq__(self, other):
        """
        Overrides the == operator.
        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator.
        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
