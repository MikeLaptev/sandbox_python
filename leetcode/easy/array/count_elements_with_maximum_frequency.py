from collections import Counter
from typing import List


class CountElementsWithMaximumFrequency:

    def max_frequency_elements(self, nums: List[int]) -> int:
        """
        >>> sut = CountElementsWithMaximumFrequency()
        >>> assert 4 == sut.max_frequency_elements([1, 2, 2, 3, 1, 4])
        >>> assert 5 == sut.max_frequency_elements([1, 2, 3, 4, 5])
        """
        c: Counter = Counter(nums)
        s = None
        max_v = None
        for e, v in c.items():
            if max_v is None or max_v < v:
                max_v = v
                s = v
            elif max_v == v:
                s += v
        return s


if __name__ == "__main__":
    import doctest

    doctest.testmod()
