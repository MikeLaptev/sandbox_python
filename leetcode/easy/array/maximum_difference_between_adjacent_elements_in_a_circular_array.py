from typing import List


class MaximumDifferenceBetweenAdjacentElementsInCircularArray:
    """
    Leetcode #3423
    Link: https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/description
    """

    def max_adjacent_distance(self, nums: List[int]) -> int:
        """
        >>> sut = MaximumDifferenceBetweenAdjacentElementsInCircularArray()
        >>> assert 3 == sut.max_adjacent_distance([1, 2, 4])
        >>> assert 5 == sut.max_adjacent_distance([-5, -10, -5])
        """
        maximum = abs(nums[0] - nums[-1])

        for i in range(len(nums) - 1):
            maximum = max(maximum, abs(nums[i] - nums[i + 1]))

        return maximum


if __name__ == '__main__':
    import doctest

    doctest.testmod()
