from typing import List, Set


class KeepMultiplyingFoundValuesByTwo:
    """
    Leetcode #2154
    Link: https://leetcode.com/problems/keep-multiplying-found-values-by-two/
    """

    def find_final_value(self, nums: List[int], original: int) -> int:
        """
        >>> sut = KeepMultiplyingFoundValuesByTwo()
        >>> assert 24 == sut.find_final_value([5, 3, 6, 1, 12], 3)
        >>> assert 4 == sut.find_final_value([2, 7, 9], 4)
        """
        s: Set[int] = set(nums)
        while original in s:
            original <<= 1
        return original


if __name__ == "__main__":
    import doctest

    doctest.testmod()
