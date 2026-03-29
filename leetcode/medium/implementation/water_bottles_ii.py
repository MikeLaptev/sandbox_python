class WaterBottlesII:
    """
    Leetcode #3100
    Link: https://leetcode.com/problems/water-bottles-ii/
    """

    def max_bottles_drunk(self, num_bottles: int, num_exchange: int) -> int:
        """
        >>> sut = WaterBottlesII()
        >>> expected = 13
        >>> actual = sut.max_bottles_drunk(10, 3)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 15
        >>> actual = sut.max_bottles_drunk(13, 6)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        count: int = 0
        fill_bottles: int = num_bottles
        while fill_bottles >= num_exchange:
            # covers two steps - first to drink the water, and exchange empty bottles with one
            fill_bottles -= num_exchange - 1
            count += num_exchange
            num_exchange += 1

        count += fill_bottles

        return count


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
