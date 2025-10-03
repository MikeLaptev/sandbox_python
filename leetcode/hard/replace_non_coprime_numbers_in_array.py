from typing import List
import math


class ReplaceNonCoprimeNumbersInArray:
    """
    Leetcode #2197
    Link: https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
    """

    def replace_non_coprimes(self, nums: List[int]) -> List[int]:
        """
        >>> sut = ReplaceNonCoprimeNumbersInArray()
        >>> nums = [287,41,49,287,899,23,23,20677,5,825]
        >>> expected = [2009, 20677, 825]
        >>> actual = sut.replace_non_coprimes(nums)
        >>> assert expected == actual, f"{nums}: expected {expected} got {actual}"
        >>> nums = [6,4,3,2,7,6,2]
        >>> expected = [12, 7, 6]
        >>> actual = sut.replace_non_coprimes(nums)
        >>> assert expected == actual, f"{nums}: expected {expected} got {actual}"
        >>> nums = [2,2,1,1,3,3,3]
        >>> expected = [2, 1, 1, 3]
        >>> actual = sut.replace_non_coprimes(nums)
        >>> assert expected == actual, f"{nums}: expected {expected} got {actual}"
        """
        result: List[int] = [nums[0]]
        for i in range(1, len(nums)):
            g = math.gcd(result[-1], nums[i])
            if g == 1:
                result.append(nums[i])
            else:
                result[-1] = math.lcm(result[-1], nums[i])
                while len(result) > 1:
                    t = math.gcd(result[-1], result[-2])
                    if t == 1:
                        break
                    result[-2] = math.lcm(result[-1], result[-2])
                    result.pop()

        return result

    def replace_non_coprimes_opt(self, nums: List[int]) -> List[int]:
        """
        >>> sut = ReplaceNonCoprimeNumbersInArray()
        >>> nums = [287,41,49,287,899,23,23,20677,5,825]
        >>> expected = [2009, 20677, 825]
        >>> actual = sut.replace_non_coprimes_opt(nums)
        >>> assert expected == actual, f"{nums}: expected {expected} got {actual}"
        >>> nums = [6,4,3,2,7,6,2]
        >>> expected = [12, 7, 6]
        >>> actual = sut.replace_non_coprimes_opt(nums)
        >>> assert expected == actual, f"{nums}: expected {expected} got {actual}"
        >>> nums = [2,2,1,1,3,3,3]
        >>> expected = [2, 1, 1, 3]
        >>> actual = sut.replace_non_coprimes_opt(nums)
        >>> assert expected == actual, f"{nums}: expected {expected} got {actual}"
        """
        ans = []
        curr = nums[0]
        for x in nums[1:]:
            if math.gcd(curr, x) > 1:
                curr = math.lcm(curr, x)

                while ans and math.gcd(curr, ans[-1]) > 1:
                    curr = math.lcm(curr, ans.pop())
            else:
                ans.append(curr)
                curr = x

        ans.append(curr)

        return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
