from collections import Counter
from typing import List


class CountTheNumberOfComputerUnlockingPermutations:
    """
    Leetcode #3577
    Link: https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations
    """

    def count_permutations(self, complexity: List[int]) -> int:
        """
        >>> sut = CountTheNumberOfComputerUnlockingPermutations()
        >>> actual = sut.count_permutations([1, 2, 3])
        >>> assert 2 == actual, f"expected 2, got {actual}"
        >>> actual = sut.count_permutations([3, 3, 3, 4, 4, 4])
        >>> assert 0 == actual, f"expected 0, got {actual}"
        >>> actual = sut.count_permutations([58, 283, 52])
        >>> assert 0 == actual, f"expected 0, got {actual}"
        """
        s: int = 0
        for i in complexity:
            if i == complexity[0]:
                s += 1
            if s > 1 or i < complexity[0]:
                return 0

        return self.__factorial(len(complexity) - 1) % (10**9 + 7)

    def __factorial(self, n: int) -> int:
        if n == 1:
            return 1
        return n * self.__factorial(n - 1)

    def count_permutations_opt(self, complexity: List[int]) -> int:
        """
        >>> sut = CountTheNumberOfComputerUnlockingPermutations()
        >>> actual = sut.count_permutations_opt([1, 2, 3])
        >>> assert 2 == actual, f"expected 2, got {actual}"
        >>> actual = sut.count_permutations_opt([3, 3, 3, 4, 4, 4])
        >>> assert 0 == actual, f"expected 0, got {actual}"
        >>> actual = sut.count_permutations_opt([58, 283, 52])
        >>> assert 0 == actual, f"expected 0, got {actual}"
        """
        n, initial, result = len(complexity), complexity[0], 1
        module = 1_000_000_007

        for num in complexity[1:]:
            if num <= initial:
                return 0

        for i in range(2, n):
            result *= i
            result %= module

        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
