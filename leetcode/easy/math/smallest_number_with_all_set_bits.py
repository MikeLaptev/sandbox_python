class SmallestNumberWithAllSetBits:
    """
    Leetcode #3370
    Link: https://leetcode.com/problems/smallest-number-with-all-set-bits
    """

    def smallest_number(self, n: int) -> int:
        """
        >>> sut = SmallestNumberWithAllSetBits()
        >>> assert 7 == sut.smallest_number(5), f"expected 7, got {sut.smallest_number(5)}"
        >>> assert 15 == sut.smallest_number(10), f"expected 15, got {sut.smallest_number(10)}"
        >>> assert 3 == sut.smallest_number(3), f"expected 3, got {sut.smallest_number(3)}"
        """
        result: int = 1

        while n != 0:
            result <<= 1
            n >>= 1

        return result - 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
