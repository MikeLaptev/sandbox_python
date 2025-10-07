from typing import List


class FindFirstAndLastPositionOfElementInSortedArray:
    """
    Leetcode #34
    Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
    """

    def search_range(self, nums: List[int], target: int) -> List[int]:
        """
        >>> sut = FindFirstAndLastPositionOfElementInSortedArray()
        >>> n = [5, 7, 7, 8, 8, 10]
        >>> t = 8
        >>> expected = [3, 4]
        >>> actual = sut.search_range(n, t)
        >>> assert expected == actual, f"expected {expected}; got {actual} for {n} and {t}"
        >>> n = [5, 7, 7, 8, 8, 10]
        >>> t = 6
        >>> expected = [-1, -1]
        >>> actual = sut.search_range(n, t)
        >>> assert expected == actual, f"expected {expected}; got {actual} for {n} and {t}"
        >>> n = []
        >>> t = 0
        >>> expected = [-1, -1]
        >>> actual = sut.search_range(n, t)
        >>> assert expected == actual, f"expected {expected}; got {actual} for {n} and {t}"
        """
        if not nums:
            return [-1, -1]
        first_occurrence = self.find_first_occurrence(nums, target)
        if first_occurrence == -1:
            return [-1, -1]

        last_occurrence = self.find_last_occurrence(nums, target)

        return [first_occurrence, last_occurrence]

    def find_first_occurrence(self, nums: List[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1
        result: int = -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return result

    def find_last_occurrence(self, nums: List[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1
        result: int = -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
