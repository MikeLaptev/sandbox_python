from typing import List, Tuple


class MinimumPenaltyForShop:
    """
    Leetcode #2483
    Link: https://leetcode.com/problems/minimum-penalty-for-a-shop
    """

    def best_closing_time(self, customers: str) -> int:
        """
        >>> sut = MinimumPenaltyForShop()
        >>> expected = 1
        >>> actual = sut.best_closing_time("YN")
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 2
        >>> actual = sut.best_closing_time("YYNY")
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 0
        >>> actual = sut.best_closing_time("NNNNN")
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 4
        >>> actual = sut.best_closing_time("YYYY")
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        penalties_for_open: List[List[int]] = [] * (len(customers) + 2)
        penalties_for_open.append([0, 0])
        pos: int = 1
        for customer in customers:
            penalties_for_open.append([0, 0])
            penalties_for_open[pos][1] = penalties_for_open[pos - 1][1]
            if customer == "N":
                penalties_for_open[pos][1] += 1
            pos += 1
        penalties_for_open.append(
            [penalties_for_open[-1][0], penalties_for_open[-1][1]]
        )

        pos: int = len(penalties_for_open) - 2
        for customer in customers[::-1]:
            penalties_for_open[pos][0] = penalties_for_open[pos + 1][0]
            if customer == "Y":
                penalties_for_open[pos][0] = penalties_for_open[pos][0] + 1
            pos -= 1
        penalties_for_open[0][0] = penalties_for_open[1][0]

        m: int = len(customers) + 1
        res: int = 0
        for i in range(len(penalties_for_open) - 1):
            v: int = penalties_for_open[i + 1][0] + penalties_for_open[i][1]
            if m > v:
                res = i
                m = v
            # print(f"{i}: {v}")

        return res

    def best_closing_time_opt(self, customers: str) -> int:
        """
        From the editorial:

        In the previous solution, we used the first traversal to calculate the count of 'Y',
        ensuring that each penalty obtained is accurate.
        However, we don't need the actual penalty values. It is important to note that the problem
        only requires the earliest hour with the lowest penalty. Thus, the only thing that matters
        is the penalty of the hours relative to each other, and our initial
        reference point is not significant.

        For convenience, we can directly set cur_penalty to 0, which is equivalent to shifting
        the curve of the actual penalty vertically. This will not affect the calculation result.
        Note that we could initialize cur_penalty to any value and the algorithm would still
        work since the initial reference point is insignificant.

        >>> sut = MinimumPenaltyForShop()
        >>> expected = 1
        >>> actual = sut.best_closing_time_opt("YN")
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 2
        >>> actual = sut.best_closing_time_opt("YYNY")
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 0
        >>> actual = sut.best_closing_time_opt("NNNNN")
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 4
        >>> actual = sut.best_closing_time_opt("YYYY")
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        cur_penalty = 0
        min_penalty = 0
        earliest_hour = 0

        for i in range(len(customers)):
            if customers[i] == "Y":
                cur_penalty -= 1
                if cur_penalty < min_penalty:
                    min_penalty = cur_penalty
                    earliest_hour = i + 1
            else:
                cur_penalty += 1
        return earliest_hour


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
