from typing import List


class AdjacentIncreasingSubarraysDetectionI:
    """
    Leetcode #3349
    Link: https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i
    """

    def has_increasing_subarrays(self, nums: List[int], k: int) -> bool:
        """
        >>> sut = AdjacentIncreasingSubarraysDetectionI()
        >>> nums = [-15, 19]
        >>> k = 1
        >>> actual = sut.has_increasing_subarrays(nums, k)
        >>> assert True == actual, f"got True; expected False for {nums} and {k}"
        >>> nums = [5, 8, -2, -1]
        >>> k = 2
        >>> actual = sut.has_increasing_subarrays(nums, k)
        >>> assert True == actual, f"got True; expected False for {nums} and {k}"
        >>> nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
        >>> k = 3
        >>> actual = sut.has_increasing_subarrays(nums, k)
        >>> assert True == actual, f"got True; expected False for {nums} and {k}"
        >>> nums = [1,2,3,4,4,4,4,5,6,7]
        >>> k = 3
        >>> actual = sut.has_increasing_subarrays(nums, k)
        >>> assert False == actual, f"got False; expected True for {nums} and {k}"
        """
        for p in range(len(nums)):
            if self.is_strictly_increasing(
                nums, p - k, k
            ) and self.is_strictly_increasing(nums, p, k):
                return True

        return False

    def is_strictly_increasing(self, nums: List[int], q: int, l: int) -> bool:
        if q < 0 or q + l > len(nums):
            return False

        for i in range(q, q + l - 1):
            if nums[i] >= nums[i + 1]:
                return False
        return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
