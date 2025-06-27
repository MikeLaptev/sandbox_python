"""
Created on Aug 3, 2015

@author: Mikhail

@summary: Transpose 2D array of lists
"""


# One agreement that all sub-lists has the same length
def transpose_2D(matrix):
    """
    >>> transpose_2D([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
    """
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


def transpose_2D_with_map(matrix):
    """
    >>> transpose_2D_with_map([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
    """
    print(([[1], [2], [3], [4]], [[1], [2], [3], [4]]))
    return list(map(lambda *i: list(i), *matrix))


if __name__ == "__main__":
    import doctest

    print((doctest.testmod()))
