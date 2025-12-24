from typing import List


class AppleRedistributionIntoBoxes:
    """
    Leetcode #3074
    Link: https://leetcode.com/problems/apple-redistribution-into-boxes
    """

    def minimum_boxes(self, apple: List[int], capacity: List[int]) -> int:
        """
        >>> sut = AppleRedistributionIntoBoxes()
        >>> expected = 2
        >>> actual = sut.minimum_boxes([1, 3, 2], [4, 3, 1, 5, 2])
        >>> assert expected == actual, f"Expected {expected}, got {actual}"
        >>> expected = 4
        >>> actual = sut.minimum_boxes([5, 5, 5], [2, 4, 2, 7])
        >>> assert expected == actual, f"Expected {expected}, got {actual}"
        """
        capacity.sort(reverse=True)
        all_the_apples = sum(apple)
        for i, c in enumerate(capacity):
            if c >= all_the_apples:
                return i + 1
            else:
                all_the_apples -= c

        return -1


    def minimum_boxes_opt(self, apple: List[int], capacity: List[int]) -> int:
        """
        >>> sut = AppleRedistributionIntoBoxes()
        >>> expected = 2
        >>> actual = sut.minimum_boxes_opt([1, 3, 2], [4, 3, 1, 5, 2])
        >>> assert expected == actual, f"Expected {expected}, got {actual}"
        >>> expected = 4
        >>> actual = sut.minimum_boxes_opt([5, 5, 5], [2, 4, 2, 7])
        >>> assert expected == actual, f"Expected {expected}, got {actual}"
        """
        capacity.sort(reverse=True)
        all_the_apples = sum(apple)
        boxes = 1
        for c in capacity:
            if c >= all_the_apples:
                return boxes
            else:
                all_the_apples -= c
                boxes += 1

        return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
