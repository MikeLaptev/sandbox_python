from typing import List


class FindNumbersWithEvenNumberOfDigits:
    """
    Leetcode #1295
    Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
    """

    def find_numbers(self, nums: List[int]) -> int:
        """
        >>> sut = FindNumbersWithEvenNumberOfDigits()
        >>> expected = 2
        >>> actual = sut.find_numbers([12, 345, 2, 6, 7896])
        >>> assert actual == expected, f"expected {expected}; got {actual}"
        >>> expected = 1
        >>> actual = sut.find_numbers([555, 901, 482, 1771])
        >>> assert actual == expected, f"expected {expected}; got {actual}"
        """
        return len(list([x for x in nums if (len(str(x)) & 1 == 0)]))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
