from typing import List, Set


class NRepeatedElementInSize2NArray:
    """
    Leetcode #961
    Link: https://leetcode.com/problems/n-repeated-element-in-size-2n-array
    """

    def repeated_n_times(self, nums: List[int]) -> int | None:
        """
        >>> sut = NRepeatedElementInSize2NArray()
        >>> expected = 3
        >>> actual = sut.repeated_n_times(nums = [1,2,3,3])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 2
        >>> actual = sut.repeated_n_times(nums = [2,1,2,5,3,2])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        >>> expected = 5
        >>> actual = sut.repeated_n_times(nums = [5,1,5,2,5,3,5,4])
        >>> assert expected == actual, f"expected: {expected}, actual: {actual}"
        """
        distinct: Set[int] = set()
        for num in nums:
            if num in distinct:
                return num
            distinct.add(num)
        return None


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
