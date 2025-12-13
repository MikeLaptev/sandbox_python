class CalculateMoneyInLeetcodeBank:
    """
    Leetcode #1716
    Link: https://leetcode.com/problems/calculate-money-in-leetcode-bank
    """

    def total_money(self, n: int) -> int:
        """
        >>> sut = CalculateMoneyInLeetcodeBank()
        >>> assert 10 == sut.total_money(4), f"expected 4; got {sut.total_money(4)}"
        >>> assert 37 == sut.total_money(10), f"expected 37; got {sut.total_money(10)}"
        >>> assert 96 == sut.total_money(20), f"expected 96; got {sut.total_money(20)}"
        """
        monday_before: int = 0
        full_weeks: int = n // 7
        days: int = n % 7

        per_week: int = 28
        total = 0
        for i in range(0, full_weeks):
            total += monday_before * 7
            monday_before += 1
            total += per_week

        for i in range(0, days):
            total += monday_before + i + 1

        return total


if __name__ == "__main__":
    import doctest

    doctest.testmod()
