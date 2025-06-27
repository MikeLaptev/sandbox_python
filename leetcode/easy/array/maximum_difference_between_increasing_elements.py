from typing import List


class MaximumDifferenceBetweenIncreasingElements:
    """
    Leetcode #2016
    Link: https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/
    """

    def maximum_difference(self, nums: List[int]) -> int:
        """
        >>> sut = MaximumDifferenceBetweenIncreasingElements()
        >>> actual = sut.maximum_difference([7,1,5,4])
        >>> assert actual == 4
        >>> actual = sut.maximum_difference([9,4,3,2])
        >>> assert actual == -1
        >>> actual = sut.maximum_difference([1,5,2,10])
        >>> assert actual == 9, f"expected 9; got {actual}"
        """
        p = len(nums) - 1
        r = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[p] - nums[i] > 0:
                r = max(nums[p] - nums[i], r)
            if nums[p] < nums[i]:
                p = i

        return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
