from typing import List, Set, Optional


class MaximumUniqueSubarraySumAfterDeletion:
    """
    Leetcode #3487
    Link: https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion
    """

    def max_sum(self, nums: List[int]) -> int:
        """
        >>> sut = MaximumUniqueSubarraySumAfterDeletion()
        >>> actual = sut.max_sum([1,2,3,4,5])
        >>> assert 15 == actual, f"expected 15; got {actual}"
        >>> actual = sut.max_sum([1,1,0,1,1])
        >>> assert 1 == actual, f"expected 1; got {actual}"
        >>> actual = sut.max_sum([1,2,-1,-2,1,0,-1])
        >>> assert 3 == actual, f"expected 3; got {actual}"
        """
        distinct: Set[int] = set()
        largest_negative: Optional[int] = None
        for num in nums:
            if num >= 0:
                distinct.add(num)
            elif largest_negative is None or largest_negative < num:
                largest_negative = num

        if distinct:
            return sum(distinct)
        return largest_negative


if __name__ == "__main__":
    import doctest

    doctest.testmod()
