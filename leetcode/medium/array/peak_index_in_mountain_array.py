from typing import List


class PeakIndexInMountainArray:

    def peak_index_in_mountain_array(self, arr: List[int]) -> int:
        """
        >>> sut = PeakIndexInMountainArray()
        >>> a = [0, 1, 0]
        >>> expected = 1
        >>> actual = sut.peak_index_in_mountain_array(a)
        >>> assert expected == actual, f"expected {expected}; got {actual} for array {a}"
        >>> a = [0, 2, 1, 0]
        >>> expected = 1
        >>> actual = sut.peak_index_in_mountain_array(a)
        >>> assert expected == actual, f"expected {expected}; got {actual} for array {a}"
        >>> a = [0, 1, 5, 7, 10, 5, 2]
        >>> expected = 4
        >>> actual = sut.peak_index_in_mountain_array(a)
        >>> assert expected == actual, f"expected {expected}; got {actual} for array {a}"
        """
        left: int = 0
        right: int = len(arr) - 1
        peak = -1

        while left <= right:
            mid = left + (right - left) // 2
            if (
                0 < mid < len(arr) - 1
                and arr[mid - 1] <= arr[mid]
                and arr[mid] >= arr[mid + 1]
                or mid == 0
                and arr[mid + 1] < arr[mid]
                or mid == len(arr) - 1
                and arr[mid - 1] < arr[mid]
            ):
                return mid
            elif (
                0 < mid < len(arr) - 1
                and arr[mid - 1] <= arr[mid] <= arr[mid + 1]
                or mid == 0
            ):
                left = mid + 1
            else:
                right = mid - 1
        return peak

    def peak_index_in_mountain_array_opt(self, arr: List[int]) -> int:
        """
        >>> sut = PeakIndexInMountainArray()
        >>> a = [0, 1, 0]
        >>> expected = 1
        >>> actual = sut.peak_index_in_mountain_array_opt(a)
        >>> assert expected == actual, f"expected {expected}; got {actual} for array {a}"
        >>> a = [0, 2, 1, 0]
        >>> expected = 1
        >>> actual = sut.peak_index_in_mountain_array_opt(a)
        >>> assert expected == actual, f"expected {expected}; got {actual} for array {a}"
        >>> a = [0, 1, 5, 7, 10, 5, 2]
        >>> expected = 4
        >>> actual = sut.peak_index_in_mountain_array_opt(a)
        >>> assert expected == actual, f"expected {expected}; got {actual} for array {a}"
        """
        low, high = 0, len(arr) - 1

        while low < high:
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return low


if __name__ == "__main__":
    import doctest

    doctest.testmod()
