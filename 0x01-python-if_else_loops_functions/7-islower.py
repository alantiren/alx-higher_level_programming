#!/usr/bin/python3
# 7-islower.py
def islower(c):
    """Checks if a character is lowercase"""
    ascii_value = ord(c)
    if ascii_value >= 97 and ascii_value <= 122:
        return True
    return False
