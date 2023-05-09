#!/usr/bin/python3
# 11-pow.py
def pow(a, b):
    """Compute a to the power of b"""
    result = 1
    if b < 0:
        a = 1/a
        b = -b
    while b > 0:
        if b & 1 == 1:
            result *= a
        a *= a
        b >>= 1
    return (result)
