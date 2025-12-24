from typing import List


class MakeArrayElementsEqualToZero:
    """
    Leetcode #3354
    Link: https://leetcode.com/problems/make-array-elements-equal-to-zero/
    """

    def count_valid_selections(self, nums: List[int]) -> int:
        """
        >>> sut = MakeArrayElementsEqualToZero()
        >>> nums = [16, 13, 10, 0, 0, 0, 10, 6, 7, 8, 7]
        >>> actual = sut.count_valid_selections(nums)
        >>> expected = 3
        >>> assert expected == actual, f"expected: {expected}, got: {actual}"
        >>> nums = [2, 3, 4, 0, 4, 1, 0]
        >>> actual = sut.count_valid_selections(nums)
        >>> expected = 0
        >>> assert expected == actual, f"expected: {expected}, got: {actual}"
        >>> nums = [1, 0, 2, 0, 3]
        >>> actual = sut.count_valid_selections(nums)
        >>> expected = 2
        >>> assert expected == actual, f"expected: {expected}, got: {actual}"
        """
        count: int = 0
        prefix_sum: List[int] = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            prefix_sum[i + 1] = prefix_sum[i]
            if num != 0:
                prefix_sum[i + 1] += num

        running_sum: int = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != 0:
                running_sum += nums[i]
            elif running_sum == prefix_sum[i + 1]:
                count += 2
            elif abs(running_sum - prefix_sum[i + 1]) == 1:
                count += 1

        return count


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
