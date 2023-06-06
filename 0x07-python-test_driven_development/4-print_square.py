#!/usr/bin/python3

def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or a float.
        ValueError: If size is less than 0 or a float less than 0.

    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
