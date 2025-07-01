from typing import List


class BuildArrayFromPermutation:
    """
    Leetcode #1920
    Link: https://leetcode.com/problems/build-array-from-permutation/
    """

    def build_array(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        for i in range(0, len(nums)):
            result[i] = nums[nums[i]]

        return result
