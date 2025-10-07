from typing import List, Counter


class UniqueNumberOfOccurrences:
    """
    Leetcode #1207
    Link: https://leetcode.com/problems/unique-number-of-occurrences/
    """

    def unique_occurrences(self, arr: List[int]) -> bool:
        """
        >>> sut = UniqueNumberOfOccurrences()
        >>> a = [1, 2, 2, 1, 1, 3]
        >>> assert True == sut.unique_occurrences(a), f"expected true for {a}"
        >>> a = [1, 2]
        >>> assert False == sut.unique_occurrences(a), f"expected false for {a}"
        >>> a = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
        >>> assert True == sut.unique_occurrences(a), f"expected true for {a}"
        """
        counter = Counter(arr)
        return len(counter.keys()) == len(set(counter.values()))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
