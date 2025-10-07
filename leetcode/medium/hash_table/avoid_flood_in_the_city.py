from typing import List


class AvoidFloodInTheCity:
    """
    Leetcode #1488
    Link: https://leetcode.com/problems/avoid-flood-in-the-city
    """

    def avoid_flood(self, rains: List[int]) -> List[int]:
        """
        >>> sut = AvoidFloodInTheCity()
        >>> r = [1, 2, 3, 4]
        >>> expected = [-1, -1, -1, -1]
        >>> actual = sut.avoid_flood(r)
        >>> assert expected == actual, f"expected {expected}; got {actual} for {r}"
        >>> r = [1, 2, 0, 0, 2, 1]
        >>> expected = [-1, -1, 2, 1, -1, -1]
        >>> actual = sut.avoid_flood(r)
        >>> assert expected == actual, f"expected {expected}; got {actual} for {r}"
        >>> r = [1, 2, 0, 1, 2]
        >>> expected = []
        >>> actual = sut.avoid_flood(r)
        >>> assert expected == actual, f"expected {expected}; got {actual} for {r}"
        """
        return []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
