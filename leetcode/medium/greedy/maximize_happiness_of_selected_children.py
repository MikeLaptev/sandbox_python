from typing import List


class MaximizeHappinessOfSelectedChildren:
    """
    Leetcode #3075
    Link: https://leetcode.com/problems/maximize-happiness-of-selected-children
    """

    def maximum_happiness_sum(self, happiness: List[int], k: int) -> int:
        """
        >>> sut = MaximizeHappinessOfSelectedChildren()
        >>> expected = 53
        >>> actual = sut.maximum_happiness_sum([12, 1, 42], 3)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 4
        >>> actual = sut.maximum_happiness_sum([1, 2, 3], 2)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 1
        >>> actual = sut.maximum_happiness_sum([1, 1, 1, 1], 2)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 5
        >>> actual = sut.maximum_happiness_sum([2, 3, 4, 5], 1)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        result: int = 0
        d: int = 0
        happiness.sort(reverse=True)
        for h in happiness[:k]:
            if h <= d:
                break
            result += max(h - d, 0)
            d += 1

        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
