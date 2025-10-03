class WaterBottles:
    """
    Leetcode #1518
    Link: https://leetcode.com/problems/water-bottles
    """

    def num_water_bottles(self, num_bottles: int, num_exchange: int) -> int:
        """
        >>> sut = WaterBottles()
        >>> num_bottles = 15
        >>> num_exchange = 4
        >>> expected = 19
        >>> actual = sut.num_water_bottles(num_bottles, num_exchange)
        >>> assert actual == expected, f"expected {expected}; got {actual} for num of bottles {num_bottles} and {num_exchange}"
        >>> num_bottles = 9
        >>> num_exchange = 3
        >>> expected = 13
        >>> actual = sut.num_water_bottles(num_bottles, num_exchange)
        >>> assert actual == expected, f"expected {expected}; got {actual} for num of bottles {num_bottles} and {num_exchange}"
        """
        empty: int = 0
        full: int = num_bottles
        result: int = 0

        while empty + full >= num_exchange:
            result += full
            empty += full
            full = empty // num_exchange
            empty = empty % num_exchange

        return result + full


if __name__ == "__main__":
    import doctest

    doctest.testmod()
