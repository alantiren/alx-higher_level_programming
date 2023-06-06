#!/usr/bin/python3
"""
Module to multiply two matrices using NumPy
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy

    Args:
        m_a (list): First matrix
        m_b (list): Second matrix

    Returns:
        numpy.ndarray: Resulting matrix
    """
    matrix_a = np.array(m_a)
    matrix_b = np.array(m_b)
    return np.matmul(matrix_a, matrix_b)


if __name__ == '__main__':
    m_a = [[1, 2], [3, 4]]
    m_b = [[1, 2], [3, 4]]
    print(lazy_matrix_mul(m_a, m_b))

    m_a = [[1, 2]]
    m_b = [[3, 4], [5, 6]]
    print(lazy_matrix_mul(m_a, m_b))
