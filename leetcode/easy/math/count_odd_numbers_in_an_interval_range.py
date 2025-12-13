class CountOddNumbersInAnIntervalRange:
    """
    Leetcode #1523
    Link: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range
    """

    def count_odds(self, low: int, high: int) -> int:
        """
        >>> sut = CountOddNumbersInAnIntervalRange()
        >>> assert 3 == sut.count_odds(3, 7)
        >>> assert 1 == sut.count_odds(8, 10)
        """
        result: int = 0
        if low & 1 == 1:
            result += 1
            low += 1
        if high & 1 == 1:
            result += 1
            high -= 1
        return result + (high - low) // 2

    def count_odds_opt(self, low: int, high: int) -> int:
        """
        >>> sut = CountOddNumbersInAnIntervalRange()
        >>> assert 3 == sut.count_odds_opt(3, 7)
        >>> assert 1 == sut.count_odds_opt(8, 10)
        """
        return ((high + 1) // 2) - (low // 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
