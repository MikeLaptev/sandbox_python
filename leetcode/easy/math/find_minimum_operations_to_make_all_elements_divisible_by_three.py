from typing import List


class FindMinimumOperationsToMakeAllElementsDivisibleByThree:
    """
    Leetcode #2169
    Link: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three
    """

    def minimum_operations(self, nums: List[int]) -> int:
        return sum([min(n % 3, 3 - n % 3) for n in nums])
