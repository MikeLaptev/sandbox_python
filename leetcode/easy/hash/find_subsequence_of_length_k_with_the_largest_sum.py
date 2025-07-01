from heapq import heappush, nlargest
from typing import List


class FindSubsequenceOfLengthKWithTheLargestSum:
    """
    Leetcode #2099
    Link: https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum
    """

    def max_subsequence(self, nums: List[int], k: int) -> List[int]:
        """
        >>> sut = FindSubsequenceOfLengthKWithTheLargestSum()
        >>> expected_values = [[-1, 3, 4]]
        >>> actual = sut.max_subsequence([-1, -2, 3, 4], 3)
        >>> assert actual in expected_values, f"expected {expected_values}; got {actual}"
        >>> expected_values = [[4, 3], [3, 4]]
        >>> actual = sut.max_subsequence([3, 4, 3, 3], 2)
        >>> assert actual in expected_values, f"expected one of {expected_values}; got {actual}"
        """
        heap = []
        for i, n in enumerate(nums):
            heappush(heap, (n, i))
        values = nlargest(k, heap)
        values.sort(key=lambda x: x[1])

        return [q[0] for q in values]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
