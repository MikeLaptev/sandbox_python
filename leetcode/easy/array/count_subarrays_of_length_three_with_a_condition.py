from typing import List


class CountSubarraysOfLengthThreeWithCondition:
    """
    Leetcode #3392
    Link: https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition
    """

    def count_subarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums) - 1):
            if 2 * (nums[i + 1] + nums[i - 1]) == nums[i]:
                count = count + 1

        return count
