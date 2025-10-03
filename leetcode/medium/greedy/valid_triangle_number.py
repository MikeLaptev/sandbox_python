import bisect
from typing import List


class ValidTriangleNumber:
    """
    Leetcode #611
    Link: https://leetcode.com/problems/valid-triangle-number
    """

    def triangle_number(self, nums: List[int]) -> int:
        """
        >>> sut = ValidTriangleNumber()
        >>> n = [0, 0, 0]
        >>> expected = 0
        >>> actual = sut.triangle_number(n)
        >>> n = [2, 2, 2]
        >>> assert expected == actual, f"expected {expected}; got {actual}; arguments: {n}"
        >>> expected = 1
        >>> actual = sut.triangle_number(n)
        >>> assert expected == actual, f"expected {expected}; got {actual}; arguments: {n}"
        >>> n = [4, 2, 3, 2]
        >>> expected = 3
        >>> actual = sut.triangle_number(n)
        >>> assert expected == actual, f"expected {expected}; got {actual}; arguments: {n}"
        >>> n = [2, 2, 3, 4]
        >>> expected = 3
        >>> actual = sut.triangle_number(n)
        >>> assert expected == actual, f"expected {expected}; got {actual}; arguments: {n}"
        >>> n = [4, 2, 3, 4]
        >>> expected = 4
        >>> actual = sut.triangle_number(n)
        >>> assert expected == actual, f"expected {expected}; got {actual}; arguments: {n}"
        """
        s = [*filter(lambda n: n > 0, nums)]
        if len(s) < 3:
            return 0
        s = sorted(s)
        total = 0
        for i in range(len(s) - 2):
            for j in range(i + 1, len(s) - 1):
                m = s[i] + s[j]
                p = bisect.bisect_left(s, m)
                total += p - j - 1

        return total

    def triangle_number_opt(self, nums: List[int]) -> int:
        """
        >>> sut = ValidTriangleNumber()
        >>> n = [0, 0, 0]
        >>> expected = 0
        >>> actual = sut.triangle_number_opt(n)
        >>> n = [2, 2, 2]
        >>> assert expected == actual, f"expected {expected}; got {actual}; arguments: {n}"
        >>> expected = 1
        >>> actual = sut.triangle_number_opt(n)
        >>> assert expected == actual, f"expected {expected}; got {actual}; arguments: {n}"
        >>> n = [4, 2, 3, 2]
        >>> expected = 3
        >>> actual = sut.triangle_number_opt(n)
        >>> assert expected == actual, f"expected {expected}; got {actual}; arguments: {n}"
        >>> n = [2, 2, 3, 4]
        >>> expected = 3
        >>> actual = sut.triangle_number_opt(n)
        >>> assert expected == actual, f"expected {expected}; got {actual}; arguments: {n}"
        >>> n = [4, 2, 3, 4]
        >>> expected = 4
        >>> actual = sut.triangle_number_opt(n)
        >>> assert expected == actual, f"expected {expected}; got {actual}; arguments: {n}"
        """
        nums.sort()
        if len(nums) < 3:
            return 0
        count = 0
        for k in range(2, len(nums)):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1
        return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
