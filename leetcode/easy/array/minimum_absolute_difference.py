from typing import List


class MinimumAbsoluteDifference:
    """
    Leetcode #1200
    Link: https://leetcode.com/problems/minimum-absolute-difference
    """

    def minimum_abs_difference(self, arr: List[int]) -> List[List[int]]:
        """
        >>> sut = MinimumAbsoluteDifference()
        >>> actual = sut.minimum_abs_difference([4,2,1,3])
        >>> expected = [[1,2], [2,3], [3,4]]
        >>> assert expected == actual, f"expected {expected}, got {actual}"
        >>> actual = sut.minimum_abs_difference([1,3,6,10,15])
        >>> expected = [[1,3]]
        >>> assert expected == actual, f"expected {expected}, got {actual}"
        >>> actual = sut.minimum_abs_difference([3,8,-10,23,19,-4,-14,27])
        >>> expected = [[-14,-10], [19,23], [23,27]]
        >>> assert expected == actual, f"expected {expected}, got {actual}"
        """
        sorted_arr = sorted(arr)
        result: List[List[int]] = []

        # initial condition
        m: int = sorted_arr[1] - sorted_arr[0]
        result.append([sorted_arr[0], sorted_arr[1]])

        # rest of the items
        for i in range(2, len(sorted_arr)):
            t: int = sorted_arr[i] - sorted_arr[i - 1]
            if t == m:
                result.append([sorted_arr[i - 1], sorted_arr[i]])
            elif t < m:
                result.clear()
                result.append([sorted_arr[i - 1], sorted_arr[i]])
                m = t

        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
