from typing import List


class TrionicArrayI:
    """
    Leetcode #3637
    Link: https://leetcode.com/problems/trionic-array-i/
    """

    def is_trionic(self, nums: List[int]) -> bool:
        """
        >>> sut = TrionicArrayI()
        >>> assert False == sut.is_trionic([9, 4, 6, 8]), f"array [9, 4, 6, 8] is not trionic"
        >>> assert False == sut.is_trionic([1, 2, 3, 4]), f"array [1, 2, 3, 4] is not trionic"
        >>> assert False == sut.is_trionic([1, 2, 3, 2, 1]), f"array [1, 2, 3, 2, 1] is not trionic"
        >>> assert True == sut.is_trionic([1, 2, 3, 2, 1, 2, 3]), f"array [1, 2, 3, 2, 1, 2, 3] is trionic"
        >>> assert False == sut.is_trionic([1, 2, 3, 2, 1, 2, 3, 2]), f"array [1, 2, 3, 2, 1, 2, 3, 2] is not trionic"
        >>> assert True == sut.is_trionic([1,3,5,4,2,6]), f"array [1,3,5,4,2,6] is trionic"
        >>> assert False == sut.is_trionic([2,1,3]), f"array [2,1,3] is not trionic"
        """
        if not nums or len(nums) <= 3:
            return False
        # an additional case, when the first array is already a decreasing one
        if nums[0] >= nums[1]:
            return False

        increasing: bool = True
        decreasing_checked: bool = False
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return False
            if increasing:
                if nums[i - 1] > nums[i]:
                    increasing = False
                    if decreasing_checked:
                        return False
            else:
                decreasing_checked = True
                if nums[i - 1] < nums[i]:
                    increasing = True

        return increasing and decreasing_checked


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
