from typing import List, Tuple


class ContainerWithMostWater:
    """
    Leetcode #11
    Link: https://leetcode.com/problems/container-with-most-water
    """

    def max_area(self, height: List[int]) -> int:
        """
        >>> sut = ContainerWithMostWater()
        >>> h = [1,8,6,2,5,4,8,3,7]
        >>> expected = 49
        >>> actual = sut.max_area(h)
        >>> assert actual == expected, f"expected {expected}; got {actual}; heights: {h}"
        >>> h = [1,1]
        >>> expected = 1
        >>> actual = sut.max_area(h)
        >>> assert actual == expected, f"expected {expected}; got {actual}; heights: {h}"
        >>> h = [3, 2, 1, 2, 3]
        >>> expected = 12
        >>> actual = sut.max_area(h)
        >>> assert actual == expected, f"expected {expected}; got {actual}; heights: {h}"
        >>> h = [1, 2, 3, 2, 1]
        >>> expected = 4
        >>> actual = sut.max_area(h)
        >>> assert actual == expected, f"expected {expected}; got {actual}; heights: {h}"
        """
        maximum: int = 0
        left: int = 0
        right: int = len(height) - 1
        while left < right:
            maximum = max(maximum, min(height[right], height[left]) * (right - left))
            if height[left] < height[right]:
                t = left
                while left < right:
                    left += 1
                    if height[left] > height[t]:
                        break
            else:
                t = right
                while left < right:
                    right -= 1
                    if height[right] > height[t]:
                        break

        return maximum


if __name__ == "__main__":
    import doctest

    doctest.testmod()
