from typing import List


class MinimumTimeVisitingAllPoints:
    """
    Leetcode #1266
    Link: https://leetcode.com/problems/minimum-time-visiting-all-points/description
    """

    def min_time_to_visit_all_points(self, points: List[List[int]]) -> int:
        """
        >>> sut = MinimumTimeVisitingAllPoints()
        >>> expected = 7
        >>> actual = sut.min_time_to_visit_all_points([[1,1],[3,4],[-1,0]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 5
        >>> actual = sut.min_time_to_visit_all_points([[3,2],[-2,2]])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        min_time: int = 0

        for pointer in range(len(points) - 1):
            diff_by_x = abs(points[pointer][0] - points[pointer + 1][0])
            diff_by_y = abs(points[pointer][1] - points[pointer + 1][1])

            min_time += max(diff_by_x, diff_by_y)

        return min_time


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
