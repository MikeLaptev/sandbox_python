from typing import List
import bisect


class CountNegativeNumbersInSortedMatrix:
    """
    Leetcode #1351
    Link: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix
    """

    def count_negatives(self, grid: List[List[int]]) -> int:
        """
        >>> sut = CountNegativeNumbersInSortedMatrix()
        >>> expected = 8
        >>> actual = sut.count_negatives([[4,3,2,-1], [3,2,1,-1], [1,1,-1,-2], [-1,-1,-2,-3]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 0
        >>> actual = sut.count_negatives([[3,2], [1,0]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        count: int = 0
        for row in grid[::-1]:
            if row[-1] >= 0:
                break
            count += len(row)
            if row[0] >= 0:
                i = bisect.bisect_right(row, 0, key=lambda x: -x)
                count -= i

        return count


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
