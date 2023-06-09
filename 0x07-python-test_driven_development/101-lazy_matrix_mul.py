#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines using NumPy matrix multiplication function."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a and m_b must be lists of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float)) for row in m_a for ele in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all((isinstance(ele, int) or isinstance(ele, float)) for row in m_b for ele in row):
        raise TypeError("m_b should contain only integers or floats")

    if len(m_a) == 0 or len(m_b) == 0 or any(len(row) == 0 for row in m_a) or any(len(row) == 0 for row in m_b):
        raise ValueError("m_a and m_b cannot be empty")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b cannot be multiplied")

    return np.matmul(m_a, m_b)
