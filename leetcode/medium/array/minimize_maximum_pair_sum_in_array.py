from typing import List, Optional


class MinimizeMaximumPairSumInArray:
    """
    Leetcode #1877
    Link: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array
    """

    def min_pair_sum(self, nums: List[int]) -> int:
        """
        >>> sut = MinimizeMaximumPairSumInArray()
        >>> assert 7 == sut.min_pair_sum([3, 5, 2, 3]), "expected 7 for array [3,5,2,3]"
        >>> assert 8 == sut.min_pair_sum([3, 5, 4, 2, 4, 6]), "expected 8 for array [3,5,4,2,4,6]"
        """
        sorted_nums = sorted(nums)
        result: Optional[int] = None
        for i in range(len(sorted_nums) // 2):
            t: int = sorted_nums[i] + sorted_nums[len(sorted_nums) - i - 1]
            if not result or result < t:
                result = t
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
