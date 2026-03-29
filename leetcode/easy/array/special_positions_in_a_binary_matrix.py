from typing import List


class SpecialPositionsInBinaryMatrix:
    """
    Leetcode #1582
    Link: https://leetcode.com/problems/special-positions-in-a-binary-matrix
    """

    def num_special(self, mat: List[List[int]]) -> int:
        """
        >>> sut = SpecialPositionsInBinaryMatrix()
        >>> actual = sut.num_special([[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0],[1,0,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]])
        >>> assert 1 == actual, f"expected 1, got {actual}"
        >>> actual = sut.num_special([[1,0,0],[0,0,1],[1,0,0]])
        >>> assert 1 == actual, f"expected 1, got {actual}"
        >>> actual = sut.num_special([[1,0,0],[0,1,0],[0,0,1]])
        >>> assert 3 == actual, f"expected 3, got {actual}"
        """
        n: int = len(mat)
        m: int = len(mat[0])
        by_rows: List[int] = [sum(mat[i]) for i in range(n)]
        by_cols: List[int] = [sum(mat[j][i] for j in range(n)) for i in range(m)]
        result: int = 0
        for i in range(len(by_rows)):
            if by_rows[i] == 1:
                for j in range(len(by_cols)):
                    if by_cols[j] == 1 and mat[i][j] == 1:
                        result += 1

        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
