from functools import lru_cache
from typing import List


class MinimumScoreTriangulationOfPolygon:
    """
    Leetcode #1039
    Link: https://leetcode.com/problems/minimum-score-triangulation-of-polygon
    """

    def min_score_triangulation(self, values: List[int]) -> int:
        """
        >>> sut = MinimumScoreTriangulationOfPolygon()
        >>> v: List[int] = [1, 2, 3]
        >>> expected: int = 6
        >>> actual: int = sut.min_score_triangulation(v)
        >>> assert expected == actual, f"values: {values}. expected {expected}; got {actual}"
        >>> v: List[int] = [3, 7, 4, 5]
        >>> expected: int = 144
        >>> actual: int = sut.min_score_triangulation(v)
        >>> assert expected == actual, f"values: {values}. expected {expected}; got {actual}"
        >>> v: List[int] = [1, 3, 1, 4, 1, 5]
        >>> expected: int = 13
        >>> actual: int = sut.min_score_triangulation(v)
        >>> assert expected == actual, f"values: {values}. expected {expected}; got {actual}"
        """

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            assert i < j
            if j - i < 2:
                return 0
            if j - i == 2:
                return values[i] * values[i + 1] * values[i + 2]

            return min(
                [
                    values[i] * values[j] * values[k] + dp(i, k) + dp(k, j)
                    for k in range(i + 1, j)
                ]
            )

        return dp(0, len(values) - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
