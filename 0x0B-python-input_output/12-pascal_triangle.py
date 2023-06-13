#!/usr/bin/python3
# 12-pascal_triangle.py


def pascal_triangle(n):
    """
    Generates the Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists representing the Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
