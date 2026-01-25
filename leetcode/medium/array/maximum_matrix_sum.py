from math import inf
from typing import List


class MaximumMatrixSum:
    """
    Leetcode #1975
    Link: https://leetcode.com/problems/maximum-matrix-sum
    """

    def max_matrix_sum(self, matrix: List[List[int]]) -> int:
        """
        >>> sut = MaximumMatrixSum()
        >>> expected = 34
        >>> actual = sut.max_matrix_sum([[2, 9, 3],[5, 4, -4],[1, 7, 1]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 15
        >>> actual = sut.max_matrix_sum([[-1,0,-1],[-2,1,3],[3,2,2]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 21
        >>> actual = sut.max_matrix_sum([[1, -1, 1, 1], [-1, 0, 0, -1],[1, -2, 1, 3], [1, 3, 2, 2]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 4
        >>> actual = sut.max_matrix_sum([[1,-1],[-1,1]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 16
        >>> actual = sut.max_matrix_sum([[1,2,3],[-1,-2,-3],[1,2,3]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        has_zero: bool = False
        sum_positive: int = 0
        sum_negative: int = 0
        count_of_negative: int = 0
        min_abs_positive: int = 0
        max_negative: int = 0
        for row in matrix:
            for e in row:
                if e > 0:
                    sum_positive += e
                    if min_abs_positive == 0 or min_abs_positive > e:
                        min_abs_positive = e
                elif e < 0:
                    sum_negative += e
                    count_of_negative += 1
                    if max_negative == 0 or max_negative < e:
                        max_negative = e
                    if min_abs_positive == 0 or min_abs_positive > abs(e):
                        min_abs_positive = abs(e)
                else:
                    has_zero = True
        return (
            sum_positive
            + (-sum_negative)
            - (
                (2 * min(abs(max_negative), min_abs_positive))
                if (count_of_negative & 1 == 1 and not has_zero)
                else 0
            )
        )

    def max_matrix_sum_opt(self, matrix: List[List[int]]) -> int:
        """
        >>> sut = MaximumMatrixSum()
        >>> expected = 34
        >>> actual = sut.max_matrix_sum_opt([[2, 9, 3],[5, 4, -4],[1, 7, 1]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 15
        >>> actual = sut.max_matrix_sum_opt([[-1,0,-1],[-2,1,3],[3,2,2]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 21
        >>> actual = sut.max_matrix_sum_opt([[1, -1, 1, 1], [-1, 0, 0, -1],[1, -2, 1, 3], [1, 3, 2, 2]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 4
        >>> actual = sut.max_matrix_sum_opt([[1,-1],[-1,1]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 16
        >>> actual = sut.max_matrix_sum_opt([[1,2,3],[-1,-2,-3],[1,2,3]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        pos_sum: int = 0

        num_neg: int = 0
        least_abs: int = inf

        for row in matrix:
            for x in row:
                if x < 0:
                    num_neg += 1
                    x = -x

                if x < least_abs:
                    least_abs = x

                pos_sum += x

        if (num_neg & 1) == 0:
            return pos_sum
        else:
            return pos_sum - least_abs * 2


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
