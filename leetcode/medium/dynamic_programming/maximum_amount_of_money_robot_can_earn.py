from math import inf
from typing import List, Optional


class MaximumAmountOfMoneyRobotCanEarn:
    """
    Leetcode #3418
    Link: https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/description
    """

    def maximum_amount(self, coins: List[List[int]]) -> int:
        """
        >>> sut = MaximumAmountOfMoneyRobotCanEarn()
        >>> actual: int = sut.maximum_amount([[4, -16, 1, -11], [6, 18, -17, 14], [16, -10, 9, 3], [-11, 17, 0, -11]])
        >>> expected: int = 45
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> actual: int = sut.maximum_amount([[-7, 12, 12, 13], [-6, 19, 19, -6], [9, -2, -10, 16], [-4, 14, -10, -9]])
        >>> expected: int = 60
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> actual: int = sut.maximum_amount([[-4]])
        >>> expected: int = 0
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> actual: int = sut.maximum_amount([[0, 1, -1], [1, -2, 3], [2, -3, 4]])
        >>> expected: int = 8
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> actual: int = sut.maximum_amount([[10, 10, 10], [10, 10, 10]])
        >>> expected: int = 40
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        m, n = len(coins), len(coins[0])
        dp = [[[-inf] * 3 for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = coins[0][0]
        for k in range(1, 3):
            dp[0][0][k] = max(coins[0][0], 0)

        for j in range(1, n):
            dp[0][j][0] = dp[0][j - 1][0] + coins[0][j]
            x = max(coins[0][j], 0)
            for k in range(1, 3):
                dp[0][j][k] = max(
                    dp[0][j - 1][k] + coins[0][j], dp[0][j - 1][k - 1] + x
                )

        for i in range(1, m):
            dp[i][0][0] = dp[i - 1][0][0] + coins[i][0]
            x = max(coins[i][0], 0)
            for k in range(1, 3):
                dp[i][0][k] = max(
                    dp[i - 1][0][k] + coins[i][0], dp[i - 1][0][k - 1] + x
                )

        for i in range(1, m):
            for j in range(1, n):
                x = coins[i][j]
                dp[i][j][2] = max(
                    dp[i - 1][j][2] + x,
                    dp[i][j - 1][2] + x,
                    dp[i - 1][j][1],
                    dp[i][j - 1][1],
                )
                dp[i][j][1] = max(
                    dp[i - 1][j][1] + x,
                    dp[i][j - 1][1] + x,
                    dp[i - 1][j][0],
                    dp[i][j - 1][0],
                )
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i][j - 1][0]) + x

        return int(dp[m - 1][n - 1][2])

    def maximum_amount_opt(self, coins: List[List[int]]) -> int:
        """
        >>> sut = MaximumAmountOfMoneyRobotCanEarn()
        >>> actual: int = sut.maximum_amount_opt([[4, -16, 1, -11], [6, 18, -17, 14], [16, -10, 9, 3], [-11, 17, 0, -11]])
        >>> expected: int = 45
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> actual: int = sut.maximum_amount_opt([[-7, 12, 12, 13], [-6, 19, 19, -6], [9, -2, -10, 16], [-4, 14, -10, -9]])
        >>> expected: int = 60
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> actual: int = sut.maximum_amount_opt([[-4]])
        >>> expected: int = 0
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> actual: int = sut.maximum_amount_opt([[0, 1, -1], [1, -2, 3], [2, -3, 4]])
        >>> expected: int = 8
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> actual: int = sut.maximum_amount_opt([[10, 10, 10], [10, 10, 10]])
        >>> expected: int = 40
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        n = len(coins[0])
        dp = [[-inf] * 3 for _ in range(n + 1)]

        dp[1] = [0] * 3
        for row in coins:
            for j, x in enumerate(row):
                dp[j + 1][2] = max(
                    dp[j][2] + x, dp[j + 1][2] + x, dp[j][1], dp[j + 1][1]
                )
                dp[j + 1][1] = max(
                    dp[j][1] + x, dp[j + 1][1] + x, dp[j][0], dp[j + 1][0]
                )
                dp[j + 1][0] = max(dp[j][0], dp[j + 1][0]) + x

        return int(dp[n][2])


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
