from collections import Counter
from typing import List


class FindLuckyIntegerInAnArray:
    """
    Leetcode #1394
    Link: https://leetcode.com/problems/find-lucky-integer-in-an-array
    """

    def find_lucky(self, arr: List[int]) -> int:
        """
        >>> sut = FindLuckyIntegerInAnArray()
        >>> actual = sut.find_lucky([2,2,3,4])
        >>> assert 2 == actual, f"expected 2, got {actual}"
        >>> actual = sut.find_lucky([1,2,2,3,3,3])
        >>> assert 3 == actual, f"expected 3, got {actual}"
        >>> actual = sut.find_lucky([2,2,2,3,3])
        >>> assert -1 == actual, f"expected -1, got {actual}"
        """
        r = -1
        counter = Counter(arr)
        for elem, cnt in counter.items():
            if elem == cnt and r < elem:
                r = elem

        return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
