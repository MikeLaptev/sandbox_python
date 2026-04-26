from typing import List


class MatrixSimilarityAfterCyclicShifts:
    """
    Leetcode #2946
    Link: https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/description/
    """

    def are_similar(self, mat: List[List[int]], k: int) -> bool:
        """
        >>> sut = MatrixSimilarityAfterCyclicShifts()
        >>> mat: List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> actual: bool = sut.are_similar(mat, 4)
        >>> assert False == actual, f"expected False, but got {actual}"
        >>> mat: List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> actual: bool = sut.are_similar(mat, -4)
        >>> assert False == actual, f"expected False, but got {actual}"
        >>> mat: List[List[int]] = [[1 ,2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]]
        >>> actual: bool = sut.are_similar(mat, 2)
        >>> assert True == actual, f"expected True, but got {actual}"
        >>> mat: List[List[int]] = [[2, 2], [2, 2]]
        >>> actual: bool = sut.are_similar(mat, 3)
        >>> assert True == actual, f"expected True, but got {actual}"
        """
        n = len(mat[0])
        shift = k % n
        if shift == 0:
            return True
        for i, row in enumerate(mat):
            m: int = shift if i & 1 == 0 else -shift
            for j, col in enumerate(row):
                if col != row[(j + m) % n]:
                    return False
        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
