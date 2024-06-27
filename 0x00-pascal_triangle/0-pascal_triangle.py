#!/usr/bin/python3
"""The pascal triangle interview Challenge"""


def pascal_triangle(n):
    """returns -> list of lists of nbrs
    representing pascal triangle"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for ix in range(n):
        # TO define a row and fill the first and last idx with 1
        nw_row = [0] * (ix+1)
        nw_row[0] = 1
        nw_row[len(nw_row) - 1] = 1

        for ji in range(1, ix):
            if ji > 0 and ji < len(nw_row):
                la = pascal_triangle[ix - 1][ji]
                lb = pascal_triangle[ix - 1][ji - 1]
                nw_row[ji] = la + lb

        pascal_triangle[ix] = nw_row

    return pascal_triangle
