from typing import List


class CountPartitionsWithEvenSumDifference:
    """
    Leetcode #3432
    Link: https://leetcode.com/problems/count-partitions-with-even-sum-difference/
    """

    def count_partitions(self, nums: List[int]) -> int:
        to_the_left: List[int] = [0]
        for n in nums:
            to_the_left.append(n + to_the_left[-1])
        to_the_right: int = 0
        result = 0
        for i in range(len(nums) - 1, 0, -1):
            to_the_right += nums[i]
            result += 1 if (abs(to_the_left[i] + to_the_right) & 1) == 0 else 0
        return result
