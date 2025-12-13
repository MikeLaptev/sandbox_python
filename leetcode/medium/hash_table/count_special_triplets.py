from collections import defaultdict
from bisect import bisect_left, bisect_right
from typing import List


class CountSpecialTriplets:
    """
    Leetcode #3583
    Link: https://leetcode.com/problems/count-special-triplets/description/
    """

    def special_triplets(self, nums: List[int]) -> int:
        """
        >>> sut = CountSpecialTriplets()
        >>> assert 1 == sut.special_triplets([6, 3, 6])
        >>> assert 1 == sut.special_triplets([0, 1, 0, 0])
        >>> assert 2 == sut.special_triplets([8, 4, 2, 8, 4])
        """
        stats: defaultdict[int, list] = defaultdict(list)
        for i, n in enumerate(nums):
            stats[n].append(i)

        result: int = 0
        for i, positions in stats.items():
            if i * 2 in stats:
                combos = stats[i * 2]
                for p in positions:
                    l = bisect_left(combos, p)
                    r = bisect_right(combos, p)
                    result += l * (len(combos) - r)

        return result % (10**9 + 7)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
