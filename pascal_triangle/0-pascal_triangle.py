#!/usr/bin/python3
"""pascal's triangle"""


def pascal_triangle(n):
    """ function to return a list of lists for pascla's triangle
    """
    if n <= 0:
        return []
# first row
    triangle = [[1]]
# start from the second row
    i = 1

    while i < n:
    # every row should start with 1
        row = [1]
        j = 1
        while j < i:
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            j += 1
        row.append(1)
        triangle.append(row)
        i += 1

    return triangle
