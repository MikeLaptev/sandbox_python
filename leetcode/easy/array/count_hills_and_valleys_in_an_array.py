from typing import List


class CountHillsAndValleysInAnArray:
    """
    Leetcode #2210
    Link: https://leetcode.com/problems/count-hills-and-valleys-in-an-array
    """

    def count_hill_valley(self, nums: List[int]) -> int:
        """
        >>> sut = CountHillsAndValleysInAnArray()
        >>> actual = sut.count_hill_valley([85,52,89,81,48,8,18,12,88,20,70,100,67,42,12,95,57,8,41,82,37,44,47,18,46])
        >>> expected = 15
        >>> assert expected == actual, f"expected {expected}; got {actual}"
        >>> actual = sut.count_hill_valley([2,4,1,1,6,5])
        >>> expected = 3
        >>> assert expected == actual, f"expected {expected}; got {actual}"
        >>> actual = sut.count_hill_valley([6,6,5,5,4,1])
        >>> expected = 0
        >>> assert expected == actual, f"expected {expected}; got {actual}"
        """
        left: int = nums[0]
        p: int = self.find_next_non_equal(nums, 0)
        if p == -1:
            return 0

        c = nums[p]
        counter = 0
        while p != -1 and p < len(nums):
            p = self.find_next_non_equal(nums, p)
            if left < c and c > nums[p]:  # hill
                counter += 1
                left = c
            elif left > c and c < nums[p]:  # valley
                counter += 1
                left = c
            c = nums[p]

        return counter


    def find_next_non_equal(self, nums: List[int], s: int) -> int:
        for i in range(s, len(nums)):
            if nums[i] != nums[s]:
                return i
        return -1


if __name__ == '__main__':
    import doctest

    doctest.testmod()
