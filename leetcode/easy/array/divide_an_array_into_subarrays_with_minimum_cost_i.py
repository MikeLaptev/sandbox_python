from typing import List


class DivideAnArrayIntoSubarraysWithMinimumCostI:
    """
    Leetcode #3010
    Link: https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/
    """

    def minimum_cost(self, nums: List[int]) -> int:
        f: int = nums[0]
        s: int = nums[1]
        t: int = nums[2]
        for i in range(3, len(nums)):
            a: List[int] = [s, t, nums[i]]
            a.sort()
            s = a[0]
            t = a[1]

        return f + s + t
