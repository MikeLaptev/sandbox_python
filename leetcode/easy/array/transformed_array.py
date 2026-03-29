from typing import List


class TransformedArray:
    """
    Leetcode #3379
    Link: https://leetcode.com/problems/transformed-array
    """

    def construct_transformed_array(self, nums: List[int]) -> List[int]:
        """
        >>> sut = TransformedArray()
        >>> assert [1,1,1,3] == sut.construct_transformed_array([3,-2,1,1]),\
                f"expected [1, 1, 1, 3], but got {sut.construct_transformed_array([3,-2,1,1])}"
        >>> assert [-1,-1,4] == sut.construct_transformed_array([-1,4,-1]),\
                f"expected [-1,-1, 4], but got {sut.construct_transformed_array([-1,4,-1])}"
        """
        result = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                result[i] = 0
            else:
                result[i] = nums[(i + nums[i]) % len(nums)]

        return result

    def construct_transformed_array_opt(self, nums: List[int]) -> List[int]:
        """
        >>> sut = TransformedArray()
        >>> assert [1,1,1,3] == sut.construct_transformed_array_opt([3,-2,1,1]),\
                f"expected [1, 1, 1, 3], but got {sut.construct_transformed_array_opt([3,-2,1,1])}"
        >>> assert [-1,-1,4] == sut.construct_transformed_array_opt([-1,4,-1]),\
                f"expected [-1,-1, 4], but got {sut.construct_transformed_array_opt([-1,4,-1])}"
        """
        return [nums[(i + v) % len(nums)] for i, v in enumerate(nums)]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
