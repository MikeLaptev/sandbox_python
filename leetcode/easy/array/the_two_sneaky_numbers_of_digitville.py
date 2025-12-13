from collections import Counter
from typing import List


class TheTwoSneakyNumbersOfDigitville:
    """
    Leetcode #3289
    Link: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
    """

    def get_sneaky_numbers(self, nums: List[int]) -> List[int]:
        """
        >>> sut = TheTwoSneakyNumbersOfDigitville()
        >>> actual = sut.get_sneaky_numbers([0, 1, 1, 0])
        >>> assert actual in [[0, 1]], f"got {actual}"
        >>> actual = sut.get_sneaky_numbers([0, 3, 2, 1, 3, 2])
        >>> assert actual in [[2, 3], [3, 2]], f"got {actual}"
        >>> actual = sut.get_sneaky_numbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2])
        >>> assert actual in [[4, 5], [5, 4]], f"got {actual}"
        """
        return [e for e, cnt in Counter(nums).items() if cnt > 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
