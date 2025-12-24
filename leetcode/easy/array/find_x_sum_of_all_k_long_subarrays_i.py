from operator import itemgetter
from typing import List
from collections import Counter, defaultdict


class FindXSumOfAllKLongSubarraysI:
    """
    Leetcode #3318
    Link: https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i
    """

    def find_x_sum(self, nums: List[int], k: int, x: int) -> List[int]:
        """
        >>> sut = FindXSumOfAllKLongSubarraysI()
        >>> expected = [6, 10, 12]
        >>> actual = sut.find_x_sum([1, 1, 2, 2, 3, 4, 2, 3], 6, 2)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = [11, 15, 15, 15, 12]
        >>> actual = sut.find_x_sum([3, 8, 7, 8, 7, 5], 2, 2)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = [13]
        >>> actual = sut.find_x_sum([9, 2, 2], 3, 3)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        result: List[int] = []
        for i in range(0, len(nums) - k + 1):
            result.append(self.__x_sum(nums[i : i + k], x))
        return result

    def __x_sum(self, nums: List[int], x: int) -> int:
        counter = Counter(nums)
        filtered = sorted(counter.items(), key=itemgetter(1, 0), reverse=True)[:x]
        return sum([pair[1] * pair[0] for pair in filtered])

    def find_x_sum_opt(self, nums: List[int], k: int, x: int) -> List[int]:
        """
        >>> sut = FindXSumOfAllKLongSubarraysI()
        >>> expected = [6, 10, 12]
        >>> actual = sut.find_x_sum_opt([1, 1, 2, 2, 3, 4, 2, 3], 6, 2)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = [11, 15, 15, 15, 12]
        >>> actual = sut.find_x_sum_opt([3, 8, 7, 8, 7, 5], 2, 2)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = [13]
        >>> actual = sut.find_x_sum([9, 2, 2], 3, 3)
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        n: int = len(nums)
        res: List[int] = []

        for i in range(k - 1, n):
            res.append(self.__x_sum_opt(nums, i, k, x))

        return res

    def __x_sum_opt(self, nums: List[int], i: int, k: int, x: int) -> int:
        stats: defaultdict[int, int] = defaultdict(int)
        for j in range(i - (k - 1), i + 1):
            stats[nums[j]] += 1

        arr = list(stats.items())
        arr.sort()
        arr.sort(key=lambda v: v[1])
        return sum([k * v for k, v in arr[max(len(arr) - x, 0) :]])


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
