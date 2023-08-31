#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): a list of integers

    Returns:
        int: a peak from the list
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1
    while left < right:
        mid = left + (right - left) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return list_of_integers[left]
